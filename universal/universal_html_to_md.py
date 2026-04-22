#!/usr/bin/env python3
"""Convert HTML documentation sites into a Markdown bundle."""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import mimetypes
import os
import posixpath
import re
import sys
import threading
import time
import urllib.robotparser
from collections import deque, OrderedDict
from concurrent.futures import Future, ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Set, Tuple
from urllib.parse import SplitResult, parse_qsl, urlencode, urljoin, urlsplit, urlunsplit, urldefrag, unquote

import requests
import yaml
from bs4 import BeautifulSoup, Comment, NavigableString, Tag, UnicodeDammit
from markdownify import markdownify as md
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

try:
    from playwright.sync_api import Browser, sync_playwright                
    PLAYWRIGHT_AVAILABLE = True
except Exception:
    Browser = None                
    sync_playwright = None                
    PLAYWRIGHT_AVAILABLE = False


                                                                         
                                                                         
                                                                         

USER_AGENT = (
    "Mozilla/5.0 (compatible; docs2md/2.0; +https://example.invalid/bot)"
)
HTTP_TIMEOUT = 30
BROWSER_TIMEOUT_MS = 45000
DEFAULT_MAX_ASSET_BYTES = 25 * 1024 * 1024         
DEFAULT_CONCURRENCY = 6
DEFAULT_MAX_DEPTH = 20
CACHE_SCHEMA_VERSION = 5

                                               
ADMONITION_STYLE = "callout"

                                                                          

GENERIC_CONTENT_SELECTORS = [
    "main article",
    "article[role='main']",
    "div[role='main'] article",
    "article.theme-doc-markdown",
    ".theme-doc-markdown",
    ".vp-doc",
    ".VPDoc .content",
    ".VPDoc",
    ".md-content__inner",
    ".rst-content",
    ".documentwrapper .body",
    ".document",
    ".content",
    ".page-inner",
    ".page-content",
    ".book-page",
    ".book-post",
    ".markdown",
    ".markdown-body",
    ".prose",
    "#bodyColumn",
    "td#bodyColumn",
    "#content",
    "#contentBox",
    "td#contentBox",
    "main",
    "article",
    "body",
]

GENERIC_NAV_SELECTORS = [
    "aside nav",
    "aside[class*='sidebar']",
    "aside[class*='Sidebar']",
    "nav[aria-label*='sidebar' i]",
    "nav[aria-label*='navigation' i]",
    "nav[class*='sidebar']",
    "nav[class*='Sidebar']",
    "div[class*='sidebar']",
    "div[class*='Sidebar']",
    ".theme-doc-sidebar-container",
    ".menu.menu__list",
    ".VPSidebar",
    ".md-sidebar",
    "nav[data-md-level]",
    ".wy-menu.wy-menu-vertical",
    ".sphinxsidebar",
    ".toctree-wrapper",
    "#leftColumn",
    "#navcolumn",
    ".book-menu",
    ".book-menu-content",
    "aside",
    "nav",
]

                                                               
PROFILE_HINTS = {
    "docusaurus": {
        "content": ["article.theme-doc-markdown", ".theme-doc-markdown", "main article"],
        "nav": [".theme-doc-sidebar-container", "aside[class*='docSidebar']", "nav.menu"],
    },
    "vitepress": {
        "content": [".vp-doc", ".VPDoc", "main article"],
        "nav": [".VPSidebar", "aside nav"],
    },
    "sphinx": {
        "content": ["div[role='main']", ".rst-content", ".documentwrapper .body", ".document"],
        "nav": [".wy-menu.wy-menu-vertical", ".sphinxsidebar", "nav[aria-label*='Navigation' i]"],
    },
    "mkdocs": {
        "content": [".md-content__inner", "main article"],
        "nav": [".md-sidebar--primary", ".md-sidebar", "nav[data-md-level]"],
    },
    "maven": {
        "content": ["#bodyColumn", "#contentBox", "main article"],
        "nav": ["#navcolumn", "#leftColumn"],
    },
    "book": {
        "content": [".book-page", ".book-post", "main article"],
        "nav": [".book-menu", ".book-menu-content", "aside nav"],
    },
}

                                                                          

NOISE_SELECTORS = [
    "script", "style", "noscript", "wbr", "template",
    "svg[class*='icon']",
    "form[role='search']",
    "form[action*='search' i]",
    "input[type='search']",
    "a.hash-link", "a.headerlink",
    "button[aria-label*='copy' i]",
    "button[title*='copy' i]",
    "button[class*='copy']",
    "button[class*='Copy']",
    "button[class*='clean-btn']",
    "[class*='breadcrumbs']",
    "[class*='breadcrumb']",
    "nav[aria-label*='breadcrumb' i]",
    "nav.pagination-nav",
    "[class*='pagination-nav']",
    "[class*='theme-edit-this-page']",
    "[class*='editThisPage']",
    "[class*='lastUpdated']",
    "[class*='tocCollapsible']",
    "[class*='tableOfContents']",
    "[class*='OnThisPage']",
    "[class*='on-this-page']",
    "[class*='page-tools']",
    "[class*='pageTools']",
    "[class*='feedback']",
    "[class*='Feedback']",
    "#searchbox", "#searchBox",
    "#poweredBy",
    "#banner", "#bannerLeft", "#bannerRight",
    ".clear",
]

                                                            
RAW_HTML_BLOCK_TAGS = {"iframe", "video", "audio", "svg", "details", "math"}

DOC_PAGE_EXTENSIONS = {
    "", ".html", ".htm", ".xhtml", ".php", ".asp", ".aspx",
    ".jsp", ".jspx", ".shtml",
}

ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico",
    ".pdf", ".zip", ".gz", ".tgz", ".bz2", ".xz", ".jar", ".war", ".ear",
    ".tar", ".txt", ".csv", ".json", ".yaml", ".yml", ".xml", ".asc", ".sha1",
    ".sha256", ".sha512", ".md5", ".pom", ".apk", ".deb", ".rpm", ".mp4",
    ".mp3", ".ogg", ".wav", ".woff", ".woff2", ".ttf", ".eot", ".otf",
}

                                                                      
                                                                                
                           
SKIP_URL_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in [
        r"/search(?:/|\.html)?$",
        r"/genindex\.html$",
        r"/py-modindex\.html$",
        r"/objects\.inv$",
        r"/sitemap(?:\.xml)?$",
        r"/feed(?:\.xml)?$",
        r"/rss(?:\.xml)?$",
        r"/atom(?:\.xml)?$",
        r"/404(?:\.html)?$",
        r"/print(?:/|\.html)?$",
        r"/tag(?:s)?(?:/|\.html)?$",
        r"/categor(?:y|ies)(?:/|\.html)?$",
        r"/blog(?:/|\.html?|$)",
        r"/news(?:/|\.html?|$)",
        r"/changelog(?:/|\.html?|$)",
        r"/release(?:s|_notes|-notes)?(?:/|\.html?|$)",
        r"/apidocs(?:/|\.html?|$)",
        r"/api-release(?:/|\.html?|$)",
        r"/testapidocs(?:/|\.html?|$)",
        r"/xref(?:/|\.html?|$)",
        r"/xref-test(?:/|\.html?|$)",
        r"/jacoco(?:/|\.html?|$)",
        r"/cobertura(?:/|\.html?|$)",
        r"/jxr(?:/|\.html?|$)",
        r"/class-use(?:/|$)",
        r"/allclasses(?:-index)?\.html$",
        r"/index-all\.html$",
        r"/overview-tree\.html$",
        r"/deprecated-list\.html$",
        r"/serialized-form\.html$",
        r"/package-summary\.html$",
        r"/package-tree\.html$",
        r"/package-use\.html$",
        r"/help-doc\.html$",
        r"/constant-values\.html$",
    ]
]

                                                                        
                                                                          
                                                        
SOFT_NOISE_PATH_TOKENS = {
    "javadoc", "apidocs", "api-docs", "reference-api", "api-reference",
    "coverage", "reports", "report",
}

                                                                          

ZERO_WIDTH_RE = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff]")
SOFT_SPACE_RE = re.compile(r"[\u00a0\u202f\u2007\u2009\u200a]")
MOJIBAKE_HINT_RE = re.compile(r"(?:Ã.|Â.|â.|ï¼|ï½|ï»¿|ðŸ|â€|â€™|â€œ|â€“|â€”|�)")
SKIP_TEXT_NORMALIZATION_TAGS = {"pre", "code", "script", "style", "textarea"}
INLINE_BREAK_PARENT_TAGS = {"p", "td", "th", "li", "dd", "dt", "span", "div", "a", "strong", "em"}

                                                                          

ADMONITION_KIND_MAP = {
    "note": "note", "info": "info", "tip": "tip", "success": "tip",
    "hint": "tip", "important": "important", "warning": "warning",
    "caution": "warning", "danger": "danger", "error": "danger",
}

CALL_OUT_KIND_MAP = {
    "note": "NOTE", "info": "NOTE", "tip": "TIP",
    "important": "IMPORTANT", "warning": "WARNING", "danger": "CAUTION",
}

SANITIZED_HTML_ATTRS = {
    "href", "src", "alt", "title", "rowspan", "colspan", "width", "height",
    "target", "rel", "id", "name", "open", "start", "type", "align",
    "scope", "headers",
}

DOC_LIKE_KEYWORDS = {
    "docs", "doc", "documentation", "manual", "guide", "guides", "reference",
    "references", "tutorial", "tutorials", "learn", "book", "books",
    "user-guide", "getting-started", "how-to", "concepts", "design",
    "handbook", "cookbook",
}

                                                                             
                                                                           
                                            
TRACKING_QUERY_PARAMS = {
    "fbclid", "gclid", "dclid", "msclkid", "yclid", "mc_cid", "mc_eid",
    "igshid", "spm", "ref_src", "ref_url", "source", "from", "campaign",
}
TRACKING_QUERY_PREFIXES = ("utm_",)

                                                                              
                                                                             
                                                
VERSION_QUERY_PARAMS = {
    "version", "ver", "v", "docs_version", "doc_version", "release",
    "branch", "tag", "rev", "revision", "ref", "lang", "language",
    "locale", "hl",
}

SEARCH_QUERY_PARAMS = {"q", "query", "search", "keyword", "keywords", "term", "terms"}

                                                                             
                                                                          
                                                                
SIDEBAR_CONTEXT_RE = re.compile(
    r"(?:^|[-_\s])(?:sidebar|side-nav|sidenav|docs-sidebar|doc-sidebar|"
    r"docsidebar|toc-tree|toctree|navcolumn|leftcolumn|book-menu|wy-menu|"
    r"md-sidebar|vpsidebar|theme-doc-sidebar|menu)(?:$|[-_\s])",
    re.I,
)
GLOBAL_CHROME_RE = re.compile(
    r"(?:^|[-_\s])(?:navbar|nav-bar|topbar|top-bar|masthead|header|"
    r"site-header|global-nav|main-nav|footer|site-footer|dropdown|"
    r"version|versions|language|locale|social|foundation)(?:$|[-_\s])",
    re.I,
)
TOC_CONTEXT_RE = re.compile(
    r"(?:on-this-page|table-of-contents|toccollapsible|toc-collapsible|"
    r"page-toc|toc-list|right-sidebar|contents)",
    re.I,
)

CONTENT_CHROME_SELECTORS = [
    "header", "footer", "[role='banner']", "[role='contentinfo']",
    "#leftColumn", "#navcolumn", "#sidebar", "#sideNav", "#sidenav",
    ".theme-doc-sidebar-container", ".docSidebar", "[class*='docSidebar']",
    ".VPSidebar", ".vp-sidebar", ".md-sidebar", ".wy-nav-side",
    ".sphinxsidebar", ".book-menu", ".book-menu-content",
    "aside[class*='sidebar' i]", "div[class*='sidebar' i]",
    "nav[class*='sidebar' i]", "nav[aria-label*='sidebar' i]",
    "nav[aria-label*='navigation' i]",
    "aside[class*='side-nav' i]", "nav[class*='side-nav' i]",
    "div[class*='side-nav' i]", "aside[class*='sidenav' i]",
    "nav[class*='sidenav' i]", "div[class*='sidenav' i]",
    ".navbar", "[class*='navbar' i]",
    "[class*='topbar' i]", "[class*='site-header' i]", "[class*='site-footer' i]",
]

GLOBAL_NAV_TITLE_HINTS = {
    "blog", "blogs", "community", "communities", "download", "downloads",
    "foundation", "apache", "asf", "github", "license", "events",
    "security", "sponsorship", "thanks", "privacy", "code of conduct",
    "resources", "others", "benchmark",
}


                                                                         
                                                                         
                                                                         

@dataclass
class NavNode:
    title: str
    href: Optional[str] = None
    children: List["NavNode"] = field(default_factory=list)
    kind: str = "link"                   

    def to_dict(
        self,
        url_to_anchor: Dict[str, str],
        url_to_virtual_path: Dict[str, Path],
    ) -> Dict[str, object]:
        payload: Dict[str, object] = {"title": self.title, "kind": self.kind}
        if self.href:
            payload["source_url"] = self.href
            if self.href in url_to_anchor:
                payload["anchor"] = url_to_anchor[self.href]
            if self.href in url_to_virtual_path:
                payload["virtual_path"] = url_to_virtual_path[self.href].as_posix()
        if self.children:
            payload["children"] = [
                child.to_dict(url_to_anchor, url_to_virtual_path)
                for child in self.children
            ]
        return payload


@dataclass
class PageRecord:
    url: str
    final_url: str
    title: str
    html_text: str
    nav_tree: List[NavNode] = field(default_factory=list)
    virtual_path: Optional[Path] = None
    page_anchor: Optional[str] = None
    markdown_body: str = ""
    profile: str = "generic"
    content_score: int = 0
    depth: int = 0


@dataclass
class FetchResult:
    text: str
    final_url: str
    from_cache: bool = False


                                                                         
                                                                         
                                                                         

def dedupe_preserve_order(items: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen: Set[str] = set()
    for item in items:
        if not item or item in seen:
            continue
        out.append(item)
        seen.add(item)
    return out


def normalize_unicode_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = ZERO_WIDTH_RE.sub("", text)
    text = text.replace("\u00ad", "")
    text = SOFT_SPACE_RE.sub(" ", text)
    text = text.replace("\u2028", "\n").replace("\u2029", "\n")
    return text


def mojibake_badness(text: str) -> int:
    score = 0
    score += len(MOJIBAKE_HINT_RE.findall(text)) * 10
    score += text.count("�") * 20
    score += text.count("\x00") * 50
    return score


def maybe_fix_mojibake(text: str) -> str:
    text = normalize_unicode_text(text)
    best = text
    best_score = mojibake_badness(text)
    for enc in ("latin-1", "cp1252"):
        try:
            repaired = text.encode(enc).decode("utf-8")
        except Exception:
            continue
        repaired = normalize_unicode_text(repaired)
        score = mojibake_badness(repaired)
        if score < best_score:
            best = repaired
            best_score = score
    return best


def decode_response_text(resp: requests.Response) -> str:
    payload = resp.content
    text: Optional[str] = None

    dammit = UnicodeDammit(payload, is_html=True, smart_quotes_to=None)
    if dammit.unicode_markup:
        text = dammit.unicode_markup

    if text is None:
        candidates = dedupe_preserve_order([
            getattr(resp, "apparent_encoding", None) or "",
            getattr(resp, "encoding", None) or "",
            "utf-8", "utf-8-sig", "cp1252", "latin-1",
        ])
        for enc in candidates:
            try:
                text = payload.decode(enc)
                break
            except Exception:
                continue

    if text is None:
        text = payload.decode("utf-8", errors="replace")
    return normalize_unicode_text(maybe_fix_mojibake(text))


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def normalize_query_string(query: str) -> str:
    if not query:
        return ""
    normalized: List[Tuple[str, str]] = []
    for key, value in parse_qsl(query, keep_blank_values=True):
        if not key:
            continue
        low = key.lower()
        if low in TRACKING_QUERY_PARAMS or any(low.startswith(prefix) for prefix in TRACKING_QUERY_PREFIXES):
            continue
        normalized.append((key, value))
    if not normalized:
        return ""
    normalized.sort(key=lambda item: (item[0].lower(), item[1]))
    return urlencode(normalized, doseq=True)


def normalize_url(url: str, *, keep_query: bool = True) -> str:
    url, _frag = urldefrag(url)
    parts = urlsplit(url)
    path = parts.path or "/"
    trailing = path.endswith("/")
    norm = posixpath.normpath(path)
    if not norm.startswith("/"):
        norm = "/" + norm
    if trailing and not norm.endswith("/"):
        norm += "/"
    if norm == "/.":
        norm = "/"
    clean = SplitResult(
        scheme=(parts.scheme or "https").lower(),
        netloc=parts.netloc.lower(),
        path=norm,
        query=normalize_query_string(parts.query) if keep_query else "",
        fragment="",
    )
    return urlunsplit(clean)


def scoped_query_params_from_url(url: str) -> List[Tuple[str, str]]:
    parts = urlsplit(url)
    scoped: List[Tuple[str, str]] = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        low = key.lower()
        if low in VERSION_QUERY_PARAMS or looks_versionish(value):
            scoped.append((key, value))
    return scoped


def inherit_scoped_query(base_url: str, candidate_url: str) -> str:
    base = urlsplit(base_url)
    candidate = urlsplit(candidate_url)
    if candidate.query or base.netloc.lower() != candidate.netloc.lower():
        return candidate_url
    scoped = scoped_query_params_from_url(base_url)
    if not scoped:
        return candidate_url
    return urlunsplit(SplitResult(
        scheme=candidate.scheme,
        netloc=candidate.netloc,
        path=candidate.path,
        query=urlencode(scoped, doseq=True),
        fragment=candidate.fragment,
    ))


def split_and_normalize(base_url: str, href: str) -> Tuple[str, str]:
    abs_url = urljoin(base_url, href)
    abs_url, frag = urldefrag(abs_url)
    abs_url = inherit_scoped_query(base_url, abs_url)
    return normalize_url(abs_url), unquote(frag or "")


def absolutize(base_url: str, href: str) -> str:
    return urljoin(base_url, href)


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "site"


def slugify_anchor(text: str) -> str:
    text = unquote(text or "").strip().lower()
    text = text.replace("/", "-")
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9._:-]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-") or "section"


def safe_stem(text: str) -> str:
    text = slugify(text).replace("_", "-")
    return text or "asset"


def looks_versionish(segment: str) -> bool:
    if not segment:
        return False
    segment = unquote(str(segment)).strip().strip("/")
    if not segment:
        return False
                                                                  
    if Path(segment).suffix.lower() in DOC_PAGE_EXTENSIONS:
        segment = Path(segment).stem
    return bool(re.match(
        r"^(?:latest|next|stable|main|master|current|snapshot|"
        r"v?(?:\d+|x)(?:(?:\.|-)(?:\d+|x)){0,5}"
        r"(?:[-._]?(?:alpha|beta|rc|m|milestone|final|snapshot|ga)\d*)?"
        r"(?:[-._][A-Za-z0-9]+)*)$",
        segment, re.I,
    ))


def is_probably_asset(url: str) -> bool:
    return Path(urlsplit(url).path).suffix.lower() in ASSET_EXTENSIONS


def ensure_trailing_slash(path: str) -> str:
    return path if path.endswith("/") else path + "/"


def common_path_prefix(paths: Iterable[str]) -> str:
    split_paths = []
    for path in paths:
        segments = [seg for seg in path.split("/") if seg]
        if segments:
            split_paths.append(segments)
    if not split_paths:
        return "/"
    prefix: List[str] = []
    for bundle in zip(*split_paths):
        first = bundle[0]
        if all(seg == first for seg in bundle):
            prefix.append(first)
        else:
            break
    return "/" + "/".join(prefix) + ("/" if prefix else "")


def path_similarity(path_a: str, path_b: str) -> float:
    segs_a = [seg for seg in path_a.strip("/").split("/") if seg]
    segs_b = [seg for seg in path_b.strip("/").split("/") if seg]
    if not segs_a or not segs_b:
        return 0.0
    common = 0
    for a, b in zip(segs_a, segs_b):
        if a == b:
            common += 1
        else:
            break
    return common / max(len(segs_a), len(segs_b), 1)


def path_segments_for_scope(path: str) -> List[str]:
    segs = [unquote(seg) for seg in path.strip("/").split("/") if seg]
    if segs and Path(segs[-1]).suffix.lower() in DOC_PAGE_EXTENSIONS:
        segs = segs[:-1]
    return segs


def infer_version_scope_prefix(path: str, base_prefix: Optional[str] = None) -> Optional[str]:
    segs = path_segments_for_scope(path)
    if not segs:
        return None

    version_indices = [i for i, seg in enumerate(segs) if looks_versionish(seg)]
    if not version_indices:
        return None

                                                                    
                                                                       
    strong_markers = DOC_LIKE_KEYWORDS | {"version", "versions", "release", "releases"}
    for i in version_indices:
        prev = segs[i - 1].lower() if i > 0 else ""
        if prev in strong_markers:
            return "/" + "/".join(segs[: i + 1]) + "/"

                                                                               
                                        
    base_parts = [p for p in (base_prefix or "").strip("/").split("/") if p]
    for i in reversed(version_indices):
        if base_parts and i < len(base_parts):
            return "/" + "/".join(segs[: i + 1]) + "/"

                                                                              
    i = version_indices[-1]
    return "/" + "/".join(segs[: i + 1]) + "/"


def clamp_prefix_to_version_scope(path: str, prefix: str) -> str:
    version_prefix = infer_version_scope_prefix(path, prefix)
    if not version_prefix:
        return ensure_trailing_slash(prefix)
    prefix = ensure_trailing_slash(prefix)
                                                                              
                                                                         
    if prefix == "/" or version_prefix.startswith(prefix):
        return version_prefix
    if prefix.startswith(version_prefix):
        return prefix
    return version_prefix


def query_scope_from_url(url: str) -> Tuple[Tuple[str, str], ...]:
    return tuple(scoped_query_params_from_url(url))


def url_matches_query_scope(url: str, scope: Tuple[Tuple[str, str], ...]) -> bool:
    if not scope:
        return True
    params = parse_qsl(urlsplit(url).query, keep_blank_values=True)
    for wanted_key, wanted_value in scope:
        if (wanted_key, wanted_value) not in params:
            return False
    return True


def query_looks_search_like(url: str) -> bool:
    for key, _value in parse_qsl(urlsplit(url).query, keep_blank_values=True):
        if key.lower() in SEARCH_QUERY_PARAMS:
            return True
    return False


                                                                         
                                                                         
                                                                         

class RateLimiter:

    def __init__(self, min_interval: float) -> None:
        self.min_interval = max(0.0, min_interval)
        self._last: Dict[str, float] = {}
        self._lock = threading.Lock()

    def wait(self, domain: str) -> None:
        if self.min_interval <= 0:
            return
        while True:
            with self._lock:
                now = time.monotonic()
                last = self._last.get(domain, 0.0)
                wait_for = self.min_interval - (now - last)
                if wait_for <= 0:
                    self._last[domain] = now
                    return
            time.sleep(wait_for)


class HttpCache:

    def __init__(self, root: Path, enabled: bool = True) -> None:
        self.root = root
        self.enabled = enabled
        self.root.mkdir(parents=True, exist_ok=True)
        self._index_path = root / "index.json"
        self._index: Dict[str, Dict[str, str]] = {}
        self._lock = threading.Lock()
        if enabled and self._index_path.exists():
            try:
                self._index = json.loads(self._index_path.read_text(encoding="utf-8"))
            except Exception:
                self._index = {}
        schema = self._index.get("__schema__", {}) if isinstance(self._index, dict) else {}
        if not isinstance(schema, dict) or schema.get("version") != CACHE_SCHEMA_VERSION:
            self._index = {"__schema__": {"version": CACHE_SCHEMA_VERSION}}

    def _key(self, url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()[:24]

    def _path_for(self, key: str) -> Path:
        return self.root / f"{key}.html"

    def get(self, url: str) -> Optional[Tuple[str, str]]:
        if not self.enabled:
            return None
        key = self._key(url)
        with self._lock:
            entry = self._index.get(key)
        if not entry:
            return None
        path = self._path_for(key)
        if not path.exists():
            return None
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            return None
        return text, entry.get("final_url", url)

    def put(self, url: str, text: str, final_url: str) -> None:
        if not self.enabled:
            return
        key = self._key(url)
        path = self._path_for(key)
        try:
            path.write_text(text, encoding="utf-8")
        except Exception:
            return
        with self._lock:
            self._index[key] = {"url": url, "final_url": final_url}
            self._flush_locked()

    def _flush_locked(self) -> None:
        try:
            self._index_path.write_text(
                json.dumps(self._index, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except Exception:
            pass


class BrowserPool:

    def __init__(self, timeout_ms: int) -> None:
        self.timeout_ms = timeout_ms
        self._pw = None
        self._browser: Optional["Browser"] = None
        self._lock = threading.Lock()

    def _ensure(self) -> None:
        if self._browser is not None:
            return
        if not PLAYWRIGHT_AVAILABLE:
            raise RuntimeError("Playwright is not installed")
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=True)

    def render(self, url: str) -> Tuple[str, str]:
        with self._lock:
            self._ensure()
            assert self._browser is not None
            context = self._browser.new_context(user_agent=USER_AGENT)
            page = context.new_page()
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=self.timeout_ms)
                try:
                    page.wait_for_load_state("networkidle", timeout=self.timeout_ms)
                except Exception:
                    pass
                page.wait_for_timeout(250)
                html_text = page.content()
                final_url = normalize_url(page.url)
            finally:
                page.close()
                context.close()
        html_text = maybe_fix_mojibake(normalize_unicode_text(html_text))
        return html_text, final_url

    def close(self) -> None:
        with self._lock:
            try:
                if self._browser is not None:
                    self._browser.close()
            finally:
                self._browser = None
            try:
                if self._pw is not None:
                    self._pw.stop()
            finally:
                self._pw = None


def build_session() -> requests.Session:
    session = requests.Session()
    retries = Retry(
        total=5, connect=5, read=5, backoff_factor=1.0,
        allowed_methods=frozenset(["GET", "HEAD"]),
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retries, pool_connections=32, pool_maxsize=32)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": USER_AGENT})
    return session


class Fetcher:

    def __init__(
        self,
        session: requests.Session,
        cache: HttpCache,
        rate_limiter: RateLimiter,
        browser_pool: Optional[BrowserPool],
        browser_mode: str = "never",
        respect_robots: bool = True,
        max_asset_bytes: int = DEFAULT_MAX_ASSET_BYTES,
    ) -> None:
        self.session = session
        self.cache = cache
        self.rate_limiter = rate_limiter
        self.browser_pool = browser_pool
        self.browser_mode = browser_mode
        self.respect_robots = respect_robots
        self.max_asset_bytes = max_asset_bytes
        self._robots: Dict[str, urllib.robotparser.RobotFileParser] = {}
        self._robots_lock = threading.Lock()

                                                                          

    def _robots_for(self, url: str) -> Optional[urllib.robotparser.RobotFileParser]:
        if not self.respect_robots:
            return None
        parts = urlsplit(url)
        base = f"{parts.scheme}://{parts.netloc}"
        with self._robots_lock:
            if base in self._robots:
                return self._robots[base]
        rp = urllib.robotparser.RobotFileParser()
        try:
            resp = self.session.get(base + "/robots.txt", timeout=HTTP_TIMEOUT)
            if resp.status_code < 400 and resp.text:
                rp.parse(resp.text.splitlines())
            else:
                rp.parse([])
        except Exception:
            rp.parse([])
        with self._robots_lock:
            self._robots[base] = rp
        return rp

    def allowed_by_robots(self, url: str) -> bool:
        rp = self._robots_for(url)
        if rp is None:
            return True
        try:
            return rp.can_fetch(USER_AGENT, url)
        except Exception:
            return True

                                                                         

    def fetch_text(self, url: str) -> FetchResult:
        url = normalize_url(url)
        cached = self.cache.get(url)
        if cached is not None:
            text, final_url = cached
            return FetchResult(text=text, final_url=final_url, from_cache=True)

        if self.browser_mode == "always" and self.browser_pool is not None:
            self.rate_limiter.wait(urlsplit(url).netloc)
            text, final_url = self.browser_pool.render(url)
            self.cache.put(url, text, final_url)
            return FetchResult(text=text, final_url=final_url)

        self.rate_limiter.wait(urlsplit(url).netloc)
        resp = self.session.get(url, timeout=HTTP_TIMEOUT)
        resp.raise_for_status()
        text = decode_response_text(resp)
        final_url = normalize_url(resp.url)

        if (
            self.browser_mode == "auto"
            and self.browser_pool is not None
            and should_try_browser_render(text, url)
        ):
            try:
                b_text, b_final = self.browser_pool.render(url)
                if b_text and browser_quality_score(b_text) > browser_quality_score(text):
                    text, final_url = b_text, b_final
            except Exception as exc:
                print(f"[warn] browser render failed for {url}: {exc}")

        self.cache.put(url, text, final_url)
        return FetchResult(text=text, final_url=final_url)

                                                                         

    def fetch_binary(self, url: str) -> Tuple[bytes, str, Optional[str]]:
        self.rate_limiter.wait(urlsplit(url).netloc)
        with self.session.get(url, timeout=HTTP_TIMEOUT, stream=True) as resp:
            resp.raise_for_status()
            content_length = resp.headers.get("content-length")
            if content_length and content_length.isdigit():
                if int(content_length) > self.max_asset_bytes:
                    raise ValueError(
                        f"asset too large: {content_length} bytes > "
                        f"{self.max_asset_bytes}"
                    )
            content_type = resp.headers.get("content-type", "").split(";", 1)[0].strip()
            chunks: List[bytes] = []
            total = 0
            for chunk in resp.iter_content(chunk_size=65536):
                if not chunk:
                    continue
                total += len(chunk)
                if total > self.max_asset_bytes:
                    raise ValueError(
                        f"asset exceeded size limit of {self.max_asset_bytes} bytes"
                    )
                chunks.append(chunk)
            payload = b"".join(chunks)
            final_url = normalize_url(resp.url)
        return payload, final_url, content_type or None


def should_try_browser_render(text: str, url: Optional[str] = None) -> bool:
    if not PLAYWRIGHT_AVAILABLE:
        return False
    soup = BeautifulSoup(text, "html.parser")
    script_count = len(soup.find_all("script"))
    body_text = clean_text(soup.get_text(" ", strip=True))

    if len(body_text) < 250:
        shell_ids = {"app", "root", "__docusaurus", "__next", "vitepress", "content"}
        for node in soup.select("[id]"):
            if node.get("id", "") in shell_ids:
                return True
        if script_count >= 5:
            return True

    if soup.find(string=re.compile(r"enable javascript|requires javascript", re.I)):
        return True

    root = select_content_root(soup)
    if root is None or len(clean_text(root.get_text(" ", strip=True))) < 180:
        if script_count >= 6:
            return True

                                                                           
                                                                         
                                                                             
                         
    if url and script_count >= 5:
        parts = urlsplit(url)
        if parts.netloc:
            profile = detect_profile(soup, url)
            nav_root = select_nav_root(
                soup,
                current_domain=parts.netloc.lower(),
                base_url=url,
                content_root=root,
                profile=profile,
                current_url=url,
                site_prefix=None,
            )
            nav_links = 0
            if nav_root is not None:
                for a in nav_root.select("a[href]"):
                    href = (a.get("href") or "").strip()
                    if href and not href.startswith(("#", "javascript:", "mailto:", "tel:")):
                        nav_links += 1
            if nav_root is None or nav_links < 3:
                if soup.select_one("#__docusaurus, #app, #root, [data-vitepress], [data-reactroot]"):
                    return True

    return False



def browser_quality_score(text: str) -> int:
    soup = BeautifulSoup(text, "html.parser")
    root = select_content_root(soup)
    if root is None:
        return len(clean_text(soup.get_text(" ", strip=True)))
    return compute_content_score(root)


                                                                         
                                                                         
                                                                         

def detect_profile(soup: BeautifulSoup, url: str, hint: Optional[str] = None) -> str:
    if hint and hint != "generic":
        hard = detect_profile(soup, url, hint=None)
        if hard != "generic":
            return hard
        return hint

    html_tag = soup.find("html")
    html_classes = {cls.lower() for cls in (html_tag.get("class", []) if html_tag else [])}
    html_attrs = html_tag.attrs if html_tag else {}
    body_text = (soup.get_text(" ", strip=True)[:1000] if soup else "").lower()

    if soup.select_one("#__docusaurus, .theme-doc-markdown, .theme-doc-sidebar-container"):
        return "docusaurus"
    if (
        html_attrs.get("data-readthedocs-tool") == "sphinx"
        or "writer-html5" in html_classes
        or soup.select_one(".wy-menu.wy-menu-vertical, .rst-content")
    ):
        return "sphinx"
    if soup.select_one(".md-content__inner, nav[data-md-level], [data-md-component]"):
        return "mkdocs"
    if soup.select_one(".vp-doc, .VPSidebar, .VPDoc"):
        return "vitepress"
    if soup.select_one("#bodyColumn, #navcolumn, #leftColumn") or "built by maven" in body_text:
        return "maven"
    if soup.select_one(".book-menu, .book-page, .gitbook-navigation, .gitbook-page"):
        return "book"
    return "generic"


def profile_selectors(profile: str, kind: str) -> List[str]:
    hints = PROFILE_HINTS.get(profile, {})
    selectors = list(hints.get(kind, []))
    selectors.extend(GENERIC_CONTENT_SELECTORS if kind == "content" else GENERIC_NAV_SELECTORS)
    return dedupe_preserve_order(selectors)


def select_content_root(soup: BeautifulSoup, profile: str = "generic") -> Optional[Tag]:
    best: Tuple[int, int, Optional[Tag]] = (-10**9, -10**9, None)
    seen: Set[int] = set()

                                                                          
                                                                           
                                                                
    preferred_selectors = PROFILE_HINTS.get(profile, {}).get("content", [])
    preferred: List[Tuple[int, int, Tag]] = []
    for rank, selector in enumerate(preferred_selectors):
        for node in soup.select(selector):
            if id(node) in seen:
                continue
            seen.add(id(node))
            score = compute_content_score(node)
            if score > -1500:
                preferred.append((score, -rank, node))
    if preferred:
        preferred.sort(key=lambda item: (item[0], item[1]), reverse=True)
        return preferred[0][2]

    selectors = profile_selectors(profile, "content")
    for rank, selector in enumerate(selectors):
        for node in soup.select(selector):
            if id(node) in seen:
                continue
            seen.add(id(node))
            score = compute_content_score(node)
            tie = -rank
            if score > best[0] or (score == best[0] and tie > best[1]):
                best = (score, tie, node)
    return best[2]



def compute_content_score(node: Tag) -> int:
    text_len = len(clean_text(node.get_text(" ", strip=True)))
    headings = len(node.find_all(re.compile(r"^h[1-6]$")))
    paragraphs = len(node.find_all("p"))
    code_blocks = len(node.find_all("pre"))
    tables = len(node.find_all("table"))
    lists = len(node.find_all(["ul", "ol", "dl"]))
    links = node.find_all("a", href=True)
    link_count = len(links)
    link_text_len = sum(len(clean_text(a.get_text(" ", strip=True))) for a in links)
    link_density = link_text_len / max(text_len, 1)

    attrs = " ".join([
        node.get("id", ""),
        *node.get("class", []),
        node.name or "",
    ]).lower()

    score = text_len
    score += headings * 300
    score += paragraphs * 70
    score += code_blocks * 180
    score += tables * 90
    score += lists * 25
    if node.name in {"main", "article"}:
        score += 400
    if re.search(
        r"content|article|main|markdown|doc|document|bodycolumn|page|prose|"
        r"rst-content|md-content|vp-doc|theme-doc",
        attrs,
    ):
        score += 1200
    if re.search(r"nav|sidebar|menu|header|footer|breadcrumb|toc|search|toolbar|topbar", attrs):
        score -= 1600
    score -= int(link_density * 900)

                                                                          
                      
    if link_count > 40 and paragraphs < 3 and code_blocks == 0 and tables < 2:
        score -= 3000
    if text_len < 120:
        score -= 1200
    return score


def tag_attr_signature(tag: Tag) -> str:
    attrs: List[str] = [tag.name or ""]
    for attr in ("id", "class", "role", "aria-label", "data-testid", "data-md-component"):
        value = tag.get(attr)
        if isinstance(value, list):
            attrs.extend(str(v) for v in value)
        elif value:
            attrs.append(str(value))
    return " ".join(attrs).lower()


def tag_context_signature(tag: Tag, max_ancestors: int = 5) -> str:
    pieces: List[str] = []
    current = tag
    steps = 0
    while isinstance(current, Tag) and steps <= max_ancestors:
        pieces.append(tag_attr_signature(current))
        parent = current.parent
        if not isinstance(parent, Tag):
            break
        current = parent
        steps += 1
    return " ".join(pieces).lower()


def is_inside_global_chrome(tag: Tag) -> bool:
    current = tag
    while isinstance(current, Tag):
        if current.name in {"header", "footer"}:
            return True
        role = str(current.get("role", "")).lower()
        if role in {"banner", "contentinfo"}:
            return True
        sig = tag_attr_signature(current)
        if GLOBAL_CHROME_RE.search(sig) and not SIDEBAR_CONTEXT_RE.search(sig):
            return True
        parent = current.parent
        if not isinstance(parent, Tag):
            break
        current = parent
    return False


def is_sidebarish_tag(tag: Tag) -> bool:
    if tag.name == "aside" and not is_inside_global_chrome(tag):
        return True
    sig = tag_context_signature(tag)
    return bool(SIDEBAR_CONTEXT_RE.search(sig)) and not is_inside_global_chrome(tag)


def is_toc_like_tag(tag: Tag) -> bool:
    sig = tag_context_signature(tag, max_ancestors=2)
    text = clean_text(tag.get_text(" ", strip=True)).lower()
    if TOC_CONTEXT_RE.search(sig):
        return True
    if "on this page" in text or "table of contents" in text or "page contents" in text:
        normal_links = 0
        fragment_links = 0
        for a in tag.select("a[href]"):
            href = (a.get("href") or "").strip()
            if href.startswith("#"):
                fragment_links += 1
            elif href:
                normal_links += 1
        return fragment_links >= max(3, normal_links * 2)
    return False


def has_structured_nav_headings(tag: Tag) -> bool:
    direct_lists = [child for child in tag.children if isinstance(child, Tag) and child.name in {"ul", "ol"}]
    direct_headings = [
        child for child in tag.children
        if isinstance(child, Tag) and (
            child.name in {"h1", "h2", "h3", "h4", "h5", "h6"}
            or is_nav_heading_tag(child)
        )
    ]
    if direct_headings:
        return True
    if len(direct_lists) >= 2:
        return True
                                                          
    shallow_headings = 0
    for child in tag.find_all(True, recursive=False):
        if child.name in {"ul", "ol"}:
            continue
        if child.find(["h1", "h2", "h3", "h4", "h5", "h6"], recursive=False):
            shallow_headings += 1
    return shallow_headings > 0


def url_path_in_prefix(url: str, site_prefix: Optional[str]) -> bool:
    if not site_prefix:
        return True
    prefix = ensure_trailing_slash(site_prefix)
    if prefix == "/":
        return True
    return urlsplit(url).path.startswith(prefix)


def select_nav_root(
    soup: BeautifulSoup,
    current_domain: str,
    base_url: Optional[str] = None,
    content_root: Optional[Tag] = None,
    profile: str = "generic",
    current_url: Optional[str] = None,
    site_prefix: Optional[str] = None,
) -> Optional[Tag]:
    candidates: List[Tuple[int, int, int, int, Tag]] = []
    seen: Set[int] = set()
    selectors = profile_selectors(profile, "nav")

                                                                             
                                                                            
                                                                        
    broad_selectors = [
        "aside", "nav", "ul", "ol",
        "[id*='sidebar' i]", "[class*='sidebar' i]",
        "[id*='sidenav' i]", "[class*='sidenav' i]",
        "[id*='side-nav' i]", "[class*='side-nav' i]",
        "[id*='navcolumn' i]", "[id*='leftColumn' i]",
        "[class*='toc-tree' i]", "[class*='toctree' i]",
        "[class*='book-menu' i]", "[class*='wy-menu' i]",
        "[class*='md-sidebar' i]", "[class*='VPSidebar' i]",
        "[class*='menu__list' i]", "[class*='menu-list' i]",
    ]

    def consider(node: Tag) -> None:
        if id(node) in seen:
            return
        seen.add(id(node))
        score = compute_nav_score(
            node,
            current_domain=current_domain,
            base_url=base_url,
            content_root=content_root,
            current_url=normalize_url(current_url) if current_url else None,
            site_prefix=site_prefix,
        )
        if score <= 0:
            return
        sidebar_bonus = 1 if is_sidebarish_tag(node) else 0
        global_penalty = 1 if is_inside_global_chrome(node) else 0
        text_len = len(clean_text(node.get_text(" ", strip=True)))
        candidates.append((score, sidebar_bonus, -global_penalty, -text_len, node))

    for selector in selectors:
        for node in soup.select(selector):
            consider(node)

                                                                           
                                                                            
                                             
    for selector in broad_selectors:
        for node in soup.select(selector):
            consider(node)

    if not candidates:
        return None

    candidates.sort(key=lambda item: (item[0], item[1], item[2], item[3]), reverse=True)

    best = candidates[0]
    best_node = best[4]
    best_score = best[0]

                                                                              
                                                                              
                                                                        
                                                                            
    if best_node.name in {"ul", "ol"}:
        for parent in best_node.parents:
            if not isinstance(parent, Tag) or parent.name in {"body", "html"}:
                break
            if not is_sidebarish_tag(parent):
                continue
            if not has_structured_nav_headings(parent):
                continue
            parent_score = compute_nav_score(
                parent,
                current_domain=current_domain,
                base_url=base_url,
                content_root=content_root,
                current_url=normalize_url(current_url) if current_url else None,
                site_prefix=site_prefix,
            )
            if parent_score > 0 and parent_score >= int(best_score * 0.35):
                return parent

    if is_sidebarish_tag(best_node) and has_structured_nav_headings(best_node):
        return best_node

                                                                              
                                                                               
                                                                                 
                                 
    if site_prefix and site_prefix != "/":
        best_scoped = 0
        best_depth = 0
        for a in best_node.select("a[href]"):
            href = (a.get("href") or "").strip()
            if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
                continue
            abs_url = split_and_normalize(base_url or ("https://" + current_domain), href)[0]
            if url_path_in_prefix(abs_url, site_prefix):
                best_scoped += 1
        best_depth = len(best_node.find_all(["ul", "ol"]))
        for score, sidebar_bonus, global_penalty, _neg_text_len, node in candidates[1:]:
            scoped = 0
            for a in node.select("a[href]"):
                href = (a.get("href") or "").strip()
                if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
                    continue
                abs_url = split_and_normalize(base_url or ("https://" + current_domain), href)[0]
                if url_path_in_prefix(abs_url, site_prefix):
                    scoped += 1
            depth = len(node.find_all(["ul", "ol"]))
            if scoped >= max(6, best_scoped + 4) and depth >= best_depth and not is_inside_global_chrome(node):
                return node

                                                                             
                                                                             
                                                              
    for score, sidebar_bonus, global_penalty, _neg_text_len, node in candidates[1:]:
        try:
            is_descendant = node in best_node.descendants
        except Exception:
            is_descendant = False
        if not is_descendant:
            continue
        if score >= int(best_score * 0.72) and (sidebar_bonus or not global_penalty):
            return node

    return best_node


def compute_nav_score(
    node: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
    content_root: Optional[Tag] = None,
    current_url: Optional[str] = None,
    site_prefix: Optional[str] = None,
) -> int:
    internal_links: List[str] = []
    scoped_links: List[str] = []
    fragment_links = 0
    contains_current = False
    base = base_url or ("https://" + current_domain)

    for a in node.select("a[href]"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith(("javascript:", "mailto:", "tel:")):
            continue
        if href.startswith("#"):
            fragment_links += 1
            continue
        abs_url = split_and_normalize(base, href)[0]
        parts = urlsplit(abs_url)
        if parts.netloc != current_domain:
            continue
        ext = Path(parts.path).suffix.lower()
        if ext and ext not in DOC_PAGE_EXTENSIONS:
            continue
        if query_looks_search_like(abs_url):
            continue
        internal_links.append(abs_url)
        if url_path_in_prefix(abs_url, site_prefix):
            scoped_links.append(abs_url)
        if current_url is not None and abs_url == current_url:
            contains_current = True

    unique_internal = set(internal_links)
    unique_scoped = set(scoped_links)
    unique_links = len(unique_internal)
    scoped_count = len(unique_scoped)
    offscope_count = max(0, unique_links - scoped_count)

    if unique_links == 0 and fragment_links == 0:
        return -1

    text = clean_text(node.get_text(" ", strip=True)).lower()
    attrs = tag_attr_signature(node)
    context = tag_context_signature(node)
    nested_lists = len(node.find_all(["ul", "ol"]))
    global_chrome = is_inside_global_chrome(node)
    sidebarish = is_sidebarish_tag(node)
    toc_like = is_toc_like_tag(node)

                                                   
    if unique_links < 2 and fragment_links >= 3:
        return -1

    score = scoped_count * 230
    score += offscope_count * 25
    score += nested_lists * 45
    score += min(fragment_links, 12) * 3

    if sidebarish:
        score += 1800
    elif SIDEBAR_CONTEXT_RE.search(attrs):
        score += 1000

    if contains_current:
        score += 3200

    if site_prefix and site_prefix != "/":
        if scoped_count:
            score += int(1000 * (scoped_count / max(unique_links, 1)))
        if offscope_count > scoped_count:
            score -= (offscope_count - scoped_count) * 140
        if scoped_count < 2 and offscope_count >= 3:
            score -= 1200

    if re.search(r"sidebar|nav|menu|toctree|book-menu|wy-menu|leftcolumn|navcolumn|toc-tree", attrs):
        score += 450

    if toc_like:
        score -= 2500

    if "on this page" in text or "table of contents" in text or "page contents" in text:
        score -= 1200

    if GLOBAL_CHROME_RE.search(attrs) or global_chrome:
        score -= 3200

                                                                            
                                                                                
    if re.search(r"footer|mega-?menu|site-?map|global-?nav|navbar|topbar", context):
        score -= 1600

    if content_root is not None:
        try:
                                                                                
                                                                               
                                                    
            if getattr(content_root, "name", None) != "body":
                if node is content_root or node in content_root.descendants:
                    score -= 1500
        except Exception:
            pass

                                                                         
    text_len = len(text)
    if text_len > 6000 and site_prefix and site_prefix != "/" and scoped_count < max(3, unique_links // 2):
        score -= 1000

                                                                                
                          
    title_words = {clean_text(child.get_text(" ", strip=True)).lower() for child in node.find_all(["h1", "h2", "h3", "h4", "h5", "strong"], recursive=False)}
    if title_words & GLOBAL_NAV_TITLE_HINTS and not sidebarish:
        score -= 700

    return score



def extract_title(soup: BeautifulSoup, root: Optional[Tag]) -> str:
    if root is not None:
        h1 = root.find(re.compile(r"^h1$"))
        if h1:
            text = clean_text(h1.get_text(" ", strip=True))
            if text:
                return text
    meta = soup.find("meta", attrs={"property": "og:title"})
    if meta and meta.get("content"):
        return clean_text(meta["content"])
    if soup.title and soup.title.string:
        return clean_text(soup.title.string)
    return "Untitled"


def is_doc_like_page(content_root: Optional[Tag], nav_root: Optional[Tag], score: int) -> bool:
    if content_root is None:
        return False
    if score >= 400:
        return True
    if nav_root is None:
        return False
    text_len = len(clean_text(content_root.get_text(" ", strip=True)))
    return text_len >= 200


def first_nonempty_attr(tag: Tag, names: Sequence[str]) -> str:
    for name in names:
        value = (tag.get(name) or "").strip()
        if value:
            if name == "srcset":
                first = value.split(",", 1)[0].strip().split(" ", 1)[0].strip()
                if first:
                    return first
            return value
    return ""


                                                                         

def nav_link_count(nodes: List[NavNode]) -> int:
    total = 0
    for node in nodes:
        if node.href:
            total += 1
        total += nav_link_count(node.children)
    return total


def nav_has_categories(nodes: List[NavNode]) -> bool:
    return any((not node.href) or node.children or nav_has_categories(node.children) for node in nodes)


def nav_tree_depth_basic(nodes: List[NavNode]) -> int:
    if not nodes:
        return 0
    return 1 + max((nav_tree_depth_basic(node.children) for node in nodes), default=0)


def nav_tree_basic_score(nodes: List[NavNode]) -> int:
    if not nodes:
        return 0
    links = nav_link_count(nodes)
    cats = sum(1 for node in nodes if node.children or not node.href)
    depth = nav_tree_depth_basic(nodes)
    return links * 100 + cats * 55 + depth * 180 + len(nodes) * 8


def is_nav_heading_tag(tag: Tag) -> bool:
    classes = " ".join(tag.get("class", [])).lower()
    role = str(tag.get("role", "")).lower()
    if tag.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return True
    if "nav-header" in classes or "nav_header" in classes:
        return True
    if "sidebar-heading" in classes or "sidebar-title" in classes or "menu-heading" in classes:
        return True
    if role in {"heading", "separator"} and clean_text(tag.get_text(" ", strip=True)):
        return True
                                                                           
    if tag.name in {"strong", "b"} and not tag.find("a", href=True):
        text = clean_text(tag.get_text(" ", strip=True))
        return bool(text and len(text) <= 140)
    return False


def is_nav_header_item(item: Tag) -> bool:
    classes = " ".join(item.get("class", [])).lower()
    if "nav-header" in classes or "nav_header" in classes or "sidebar-heading" in classes:
        return True
    if item.find(["ul", "ol"], recursive=False) is not None:
        return False
    if item.find("a", href=True) is not None:
        return False
    text = clean_text(item.get_text(" ", strip=True))
    if not text or len(text) > 140:
        return False
                                                                              
    return item.name in {"li", "dt", "dd"}


def clean_nav_title_value(title: str) -> str:
    title = clean_text(title)
    title = re.sub(r"^(?:expand|collapse)\s+sidebar\s+category\s+", "", title, flags=re.I)
    title = re.sub(r"^(?:open|close)\s+", "", title, flags=re.I)
    title = re.sub(r"^[•›»·\-\s]+", "", title)
    title = re.sub(r"\s+", " ", title).strip()
                                                                           
                                                                             
    if "_" in title and " " not in title:
        title = title.replace("_", " ")
    return title[:180].strip()


def direct_label_text(tag: Tag) -> str:
    pieces: List[str] = []
    for child in tag.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
        elif isinstance(child, Tag):
            if child.name in {"ul", "ol", "script", "style", "svg", "button"}:
                continue
            if child.find(["ul", "ol"]):
                pieces.append(direct_label_text(child))
            else:
                pieces.append(child.get_text(" ", strip=True))
    return clean_nav_title_value(" ".join(pieces))


def best_anchor_text(link: Tag) -> str:
    text = clean_nav_title_value(link.get_text(" ", strip=True))
    if text:
        return text
    for attr in ("aria-label", "title"):
        value = link.get(attr)
        if value:
            text = clean_nav_title_value(str(value))
            if text:
                return text
    return ""


def is_explicit_nav_header_item(item: Tag) -> bool:
    classes = " ".join(item.get("class", [])).lower()
    role = str(item.get("role", "")).lower()
    return (
        "nav-header" in classes
        or "nav_header" in classes
        or "sidebar-heading" in classes
        or "menu-heading" in classes
        or (role in {"heading", "separator"} and item.find("a", href=True) is None)
    )


def extract_heading_title(tag: Tag) -> str:
                                                                          
    title = direct_label_text(tag) or clean_nav_title_value(tag.get_text(" ", strip=True))
    return title[:140].strip()


def parse_nav_container_sequence(
    container: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
    depth: int = 0,
) -> List[NavNode]:
    nodes: List[NavNode] = []
    current_heading: Optional[NavNode] = None

    def append_parsed(parsed: List[NavNode]) -> None:
        nonlocal current_heading
        if not parsed:
            return
        if current_heading is not None:
            current_heading.children.extend(parsed)
            current_heading = None
        else:
            nodes.extend(parsed)

    for child in container.children:
        if isinstance(child, NavigableString):
            if clean_text(str(child)):
                                                                              
                                                      
                continue
            continue
        if not isinstance(child, Tag):
            continue

        if child.name in {"script", "style", "noscript", "template"}:
            continue

        if is_nav_heading_tag(child):
            title = extract_heading_title(child)
            if title:
                current_heading = NavNode(title=title, kind="category")
                nodes.append(current_heading)
            continue

        if child.name in {"ul", "ol"}:
            parsed = parse_nav_list(child, current_domain=current_domain, base_url=base_url)
            append_parsed(parsed)
            continue

        if child.name == "a" and child.get("href"):
            title = best_anchor_text(child)
            href = str(child.get("href") or "").strip()
            if title and href and not href.startswith("#"):
                abs_url = split_and_normalize(base_url or ("https://" + current_domain), href)[0]
                if urlsplit(abs_url).netloc == current_domain:
                    append_parsed([NavNode(title=title, href=abs_url, kind="link")])
            continue

                                                                            
                                                                        
                     
        if depth < 4 and child.name in {"div", "section", "nav", "aside", "td", "li"}:
            parsed = parse_nav_container_sequence(
                child,
                current_domain=current_domain,
                base_url=base_url,
                depth=depth + 1,
            )
            if nav_link_count(parsed) or nav_has_categories(parsed):
                append_parsed(parsed)

                                                                     
    nodes = [node for node in nodes if node.href or node.children or node.kind == "category"]
    return dedupe_nav(nodes)


def extract_nav_tree(
    sidebar: Optional[Tag],
    current_domain: str,
    base_url: Optional[str] = None,
) -> List[NavNode]:
    if sidebar is None:
        return []

                                                                            
                                                                   
    if sidebar.name in {"ul", "ol"}:
        listed = parse_nav_list(sidebar, current_domain=current_domain, base_url=base_url)
        if listed:
            return listed

    structured = parse_nav_container_sequence(
        sidebar,
        current_domain=current_domain,
        base_url=base_url,
    )

                                                                               
                                                                                
                                                                               
                                                                         
                                                                              
    best_list_nodes: List[NavNode] = []
    best_list_score = 0
    list_candidates = list(sidebar.find_all(["ul", "ol"]))
    if list_candidates:
        top_level = [
            lst for lst in list_candidates
            if not any(
                isinstance(parent, Tag) and parent.name in {"ul", "ol"}
                and parent is not lst
                for parent in lst.parents
            )
        ]
                                                                            
                                                               
        ordered_lists: List[Tag] = []
        seen_list_ids: Set[int] = set()
        for lst in [*top_level, *list_candidates]:
            if id(lst) in seen_list_ids:
                continue
            seen_list_ids.add(id(lst))
            ordered_lists.append(lst)
        for lst in ordered_lists:
            parsed = parse_nav_list(lst, current_domain=current_domain, base_url=base_url)
            if not parsed:
                continue
            links = [u for u in flatten_nav_urls(parsed) if urlsplit(u).netloc == current_domain]
            scoped_bonus = len(set(links)) * 20
            score = nav_tree_basic_score(parsed) + scoped_bonus
            if score > best_list_score:
                best_list_score = score
                best_list_nodes = parsed

    structured_score = nav_tree_basic_score(structured)
    if best_list_nodes:
                                                                            
                                                                              
                                                                          
        if (
            not structured
            or best_list_score >= int(structured_score * 1.25)
            or (
                nav_link_count(best_list_nodes) >= nav_link_count(structured) + 4
                and nav_tree_depth_basic(best_list_nodes) >= nav_tree_depth_basic(structured)
            )
        ):
            return dedupe_nav(best_list_nodes)

    if nav_link_count(structured) >= 2 or nav_has_categories(structured):
        return structured

                                                                   
    nodes: List[NavNode] = []
    seen: Set[str] = set()
    for a in sidebar.select("a[href]"):
        href = (a.get("href") or "").strip()
        title = best_anchor_text(a)
        if not href or not title or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        abs_url = split_and_normalize(base_url or ("https://" + current_domain), href)[0]
        if abs_url in seen:
            continue
        seen.add(abs_url)
        nodes.append(NavNode(title=title, href=abs_url, kind="link"))
    return dedupe_nav(nodes)

def first_direct_child_list(item: Tag) -> Optional[Tag]:
    for child in item.children:
        if isinstance(child, Tag) and child.name in {"ul", "ol"}:
            return child
    for child in item.find_all(True, recursive=False):
        found = child.find(["ul", "ol"], recursive=False)
        if found is not None:
            return found
    return None


def parse_single_nav_item(
    item: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> Optional[NavNode]:
    child_list = first_direct_child_list(item)
    title, href = extract_nav_label(item, current_domain=current_domain, base_url=base_url)
    if child_list is not None:
        children = parse_nav_list(child_list, current_domain=current_domain, base_url=base_url)
        if title or children:
            return NavNode(
                title=title or (children[0].title if children else "Section"),
                href=href,
                children=children,
                kind="category",
            )
    elif href and title:
        return NavNode(title=title, href=href, kind="link")
    elif title:
        return NavNode(title=title, kind="category")
    return None


def parse_nav_list(
    ul: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> List[NavNode]:
    nodes: List[NavNode] = []
    item_tags = [child for child in ul.find_all(["li", "dt", "dd"], recursive=False)]
    if not item_tags and ul.name in {"li", "dt", "dd"}:
        item_tags = [ul]

                                                                          
                                                                            
    has_inline_headers = any(is_explicit_nav_header_item(item) for item in item_tags)
    current_group: Optional[NavNode] = None

    for item in item_tags:
        if has_inline_headers and is_explicit_nav_header_item(item):
            title = extract_heading_title(item)
            if title:
                current_group = NavNode(title=title, kind="category")
                nodes.append(current_group)
            continue

        parsed = parse_single_nav_item(item, current_domain=current_domain, base_url=base_url)
        if parsed is None:
            continue
        if current_group is not None:
            current_group.children.append(parsed)
        else:
            nodes.append(parsed)

    return dedupe_nav(nodes)


def first_direct_nav_link(tag: Tag) -> Optional[Tag]:
                                                                               
                                                                              
                                                                              
                       
    if tag.name == "a":
        return tag
    for child in tag.children:
        if isinstance(child, Tag):
            if child.name in {"ul", "ol"}:
                continue
            if child.name == "a":
                return child
                                                                                         
            for grand in child.children:
                if isinstance(grand, Tag):
                    if grand.name in {"ul", "ol"}:
                        continue
                    if grand.name == "a":
                        return grand
    return None


def extract_nav_label(
    li: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> Tuple[Optional[str], Optional[str]]:
    title: Optional[str] = None
    href: Optional[str] = None

    for child in li.children:
        if isinstance(child, NavigableString):
            raw = clean_nav_title_value(str(child))
            if raw and not title:
                title = raw
            continue
        if not isinstance(child, Tag):
            continue
        if child.name in {"ul", "ol"}:
            continue

        link = first_direct_nav_link(child)
        if link is not None:
            label = best_anchor_text(link)
            if label and not title:
                title = label
            if link.get("href"):
                raw_href = str(link.get("href") or "").strip()
                if raw_href and not raw_href.startswith(("#", "javascript:", "mailto:", "tel:")):
                                                                             
                                                                                 
                                                                                  
                    href = split_and_normalize(
                        base_url or ("https://" + current_domain),
                        raw_href,
                    )[0]
            if title and href:
                break

        if not title:
            for tag_name in ["a", "button", "span", "div", "strong", "p"]:
                label_tag = child if child.name == tag_name else child.find(tag_name)
                if label_tag is not None:
                    label = direct_label_text(label_tag) or clean_nav_title_value(label_tag.get_text(" ", strip=True))
                    if label:
                        title = label
                        break
    return title, href


def normalize_nav_title_key(title: str) -> str:
    title = clean_nav_title_value(title).casefold()
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def normalize_nav_href_key(href: Optional[str]) -> Optional[str]:
    if not href:
        return None
    return normalize_url(href).rstrip("/") or None


def nav_key(node: NavNode) -> Tuple[str, str]:
    href_key = normalize_nav_href_key(node.href)
    if href_key:
        return ("href", href_key)
    return ("title", normalize_nav_title_key(node.title))


def nav_identity_keys(node: NavNode) -> Set[Tuple[str, str]]:
    keys: Set[Tuple[str, str]] = set()
    href_key = normalize_nav_href_key(node.href)
    if href_key:
        keys.add(("href", href_key))
    title_key = normalize_nav_title_key(node.title)
    if title_key:
        keys.add(("title", title_key))
    return keys


def _collect_nav_href_keys(nodes: List[NavNode], out: Set[str]) -> None:
    for node in nodes:
        href_key = normalize_nav_href_key(node.href)
        if href_key:
            out.add(href_key)
        if node.children:
            _collect_nav_href_keys(node.children, out)



def _collect_nav_href_title_keys(nodes: List[NavNode], out: Set[Tuple[str, str]]) -> None:
    for node in nodes:
        href_key = normalize_nav_href_key(node.href)
        title_key = normalize_nav_title_key(node.title)
        if href_key:
            out.add((href_key, title_key))
        if node.children:
            _collect_nav_href_title_keys(node.children, out)

def _collect_nav_keys(nodes: List[NavNode], out: Set[Tuple[str, str]]) -> None:
    for node in nodes:
        out.update(nav_identity_keys(node))
        if node.children:
            _collect_nav_keys(node.children, out)


def find_matching_sibling(index: Dict[Tuple[str, str], NavNode], node: NavNode) -> Optional[NavNode]:
    href_key = normalize_nav_href_key(node.href)
    title_key = normalize_nav_title_key(node.title)
    if href_key:
        match = index.get(("href", href_key))
        if match is not None:
            match_title_key = normalize_nav_title_key(match.title)
                                                                              
                                                                              
                                                                          
            if not title_key or not match_title_key or title_key == match_title_key:
                return match
    if title_key:
        return index.get(("title", title_key))
    return None


def index_sibling(node: NavNode, index: Dict[Tuple[str, str], NavNode]) -> None:
    for key in nav_identity_keys(node):
        index.setdefault(key, node)


def merge_nav_lists(dst: List[NavNode], src: List[NavNode]) -> None:
    sibling_index: Dict[Tuple[str, str], NavNode] = {}
    for node in dst:
        index_sibling(node, sibling_index)

    existing_href_titles: Set[Tuple[str, str]] = set()
    _collect_nav_href_title_keys(dst, existing_href_titles)

    for src_node in src:
        dst_node = find_matching_sibling(sibling_index, src_node)
        if dst_node is not None:
            if not dst_node.href and src_node.href:
                dst_node.href = src_node.href
                index_sibling(dst_node, sibling_index)
                href_key = normalize_nav_href_key(src_node.href)
                title_key = normalize_nav_title_key(src_node.title)
                if href_key:
                    existing_href_titles.add((href_key, title_key))
            if dst_node.title and src_node.title:
                dst_sluggy = "_" in dst_node.title or "-" in dst_node.title
                src_cleaner = "_" not in src_node.title and len(src_node.title) >= len(dst_node.title.replace("_", " "))
                if dst_sluggy and src_cleaner:
                    dst_node.title = src_node.title
            if src_node.children:
                merge_nav_lists(dst_node.children, src_node.children)
            continue

        href_key = normalize_nav_href_key(src_node.href)
        title_key = normalize_nav_title_key(src_node.title)
        if href_key and (href_key, title_key) in existing_href_titles:
            continue

        cloned = copy.deepcopy(src_node)
        dst.append(cloned)
        index_sibling(cloned, sibling_index)
        _collect_nav_href_title_keys([cloned], existing_href_titles)


def dedupe_nav(nodes: List[NavNode]) -> List[NavNode]:
    out: List[NavNode] = []
    sibling_index: Dict[Tuple[str, str], NavNode] = {}
    for node in nodes:
        match = find_matching_sibling(sibling_index, node)
        if match is not None:
            if not match.href and node.href:
                match.href = node.href
                index_sibling(match, sibling_index)
            if node.children:
                merge_nav_lists(match.children, node.children)
            continue
        out.append(node)
        index_sibling(node, sibling_index)
    return out

def flatten_nav_urls(nodes: List[NavNode]) -> List[str]:
    urls: List[str] = []
    for node in nodes:
        if node.href:
            urls.append(node.href)
        if node.children:
            urls.extend(flatten_nav_urls(node.children))
    return urls


def mark_active_nav_item(
    nodes: List[NavNode],
    current_url: str,
    current_title: str,
) -> None:
    page_slug = slugify_anchor(current_title)
    for node in nodes:
        if not node.href:
            node_slug = slugify_anchor(node.title)
            exact = node_slug == page_slug
            leaf_suffix = (not node.children) and page_slug.endswith("-" + node_slug)
            if exact or leaf_suffix:
                node.href = current_url
        if node.children:
            mark_active_nav_item(node.children, current_url, current_title)


def nav_category_count(nodes: List[NavNode]) -> int:
    total = 0
    for node in nodes:
        if node.children or not node.href:
            total += 1
        total += nav_category_count(node.children)
    return total


def nav_max_depth(nodes: List[NavNode], depth: int = 0) -> int:
    if not nodes:
        return depth
    return max(nav_max_depth(node.children, depth + 1) for node in nodes)


def nav_tree_quality(
    nodes: List[NavNode],
    site_prefix: Optional[str] = None,
    domain: Optional[str] = None,
) -> int:
    links = flatten_nav_urls(nodes)
    unique_links = set(links)
    scoped = 0
    offscope = 0
    for url in unique_links:
        parts = urlsplit(url)
        if domain and parts.netloc and parts.netloc != domain:
            offscope += 1
            continue
        if url_path_in_prefix(url, site_prefix):
            scoped += 1
        else:
            offscope += 1

    categories = nav_category_count(nodes)
    depth = nav_max_depth(nodes)
    top_titles = {clean_text(node.title).lower() for node in nodes[:8]}

    score = scoped * 140
    score += categories * 90
    score += depth * 220
    score -= offscope * 80

                                                                            
                                                                            
    noisy = len(top_titles & GLOBAL_NAV_TITLE_HINTS)
    score -= noisy * 260

                                                                          
    if depth < 2 and scoped < 4:
        score -= 400

    return score


def merged_nav_from_snapshots(
    snapshots: List[List[NavNode]],
    site_prefix: Optional[str] = None,
    domain: Optional[str] = None,
) -> List[NavNode]:
    if not snapshots:
        return []
    ranked = [
        (nav_tree_quality(snapshot, site_prefix=site_prefix, domain=domain), idx, snapshot)
        for idx, snapshot in enumerate(snapshots)
        if snapshot
    ]
    if not ranked:
        return []
    ranked.sort(key=lambda item: (item[0], -item[1]), reverse=True)

    merged = copy.deepcopy(ranked[0][2])
    for _quality, _idx, snapshot in ranked[1:]:
        merge_nav_lists(merged, copy.deepcopy(snapshot))
    return merged


                                                                         

def extract_crawl_links(
    soup: BeautifulSoup,
    domain: str,
    site_prefix: str,
    base_url: str,
    profile: str,
    follow_content_links: bool = False,
    current_url: Optional[str] = None,
) -> List[str]:
    content_root = select_content_root(soup, profile=profile)
    nav_root = select_nav_root(
        soup,
        current_domain=domain,
        base_url=base_url,
        content_root=content_root,
        profile=profile,
        current_url=current_url,
        site_prefix=site_prefix,
    )

    containers: List[Tag] = []
    if nav_root is not None:
        containers.append(nav_root)

                                                               
    for selector in [
        "nav.pagination-nav",
        "[rel='next']",
        "[rel='prev']",
        "a[aria-label*='next' i]",
        "a[aria-label*='previous' i]",
        ".prev-next", ".pagination", ".pager",
    ]:
        for node in soup.select(selector):
            containers.append(node)

    if follow_content_links and content_root is not None:
        containers.append(content_root)

                                                                            
                                            
    if not containers:
        if content_root is not None:
            containers.append(content_root)
        elif soup.body is not None:
            containers.append(soup.body)
        else:
            containers.append(soup)

    out: List[str] = []
    seen: Set[str] = set()
    for container in containers:
        for a in container.select("a[href]"):
            href = (a.get("href") or "").strip()
            if not href:
                continue
            if href.startswith(("#", "javascript:", "mailto:", "tel:")):
                continue
            abs_url, _frag = split_and_normalize(base_url, href)
            parts = urlsplit(abs_url)
            if parts.netloc != domain:
                continue
            if not parts.path.startswith(site_prefix):
                continue
            ext = Path(parts.path).suffix.lower()
            if ext not in DOC_PAGE_EXTENSIONS:
                continue
            if query_looks_search_like(abs_url):
                continue
            if any(pattern.search(parts.path) for pattern in SKIP_URL_PATTERNS):
                continue
            if abs_url in seen:
                continue
            seen.add(abs_url)
            out.append(abs_url)
    return out


                                                                         
                                                                         
                                                                         

def is_inside_tags(node: NavigableString, tag_names: Set[str]) -> bool:
    parent = node.parent
    while isinstance(parent, Tag):
        if parent.name in tag_names:
            return True
        parent = parent.parent
    return False


def normalize_dom_text_nodes(root: Tag) -> None:
    for node in list(root.find_all(string=True)):
        if not isinstance(node, NavigableString):
            continue
        if is_inside_tags(node, SKIP_TEXT_NORMALIZATION_TAGS):
            continue
        original = str(node)
        cleaned = maybe_fix_mojibake(original)
        cleaned = normalize_unicode_text(cleaned)
        if cleaned != original:
            node.replace_with(NavigableString(cleaned))


def has_block_descendants(parent: Tag) -> bool:
    for child in parent.find_all(True, recursive=False):
        if child.name in {
            "table", "ul", "ol", "dl", "pre", "code", "blockquote",
            "section", "article", "aside", "nav", "header", "footer",
            "div", "p",
        } and child.name != "br":
            return True
    return False


def replace_inline_breaks(root: Tag) -> None:
    for br in list(root.find_all("br")):
        parent = br.parent
        if not isinstance(parent, Tag):
            br.replace_with(NavigableString(" "))
            continue
        if parent.name in SKIP_TEXT_NORMALIZATION_TAGS:
            br.replace_with(NavigableString("\n"))
            continue
        if parent.name in INLINE_BREAK_PARENT_TAGS and not has_block_descendants(parent):
            br.replace_with(NavigableString(" "))
        else:
            br.replace_with(NavigableString("\n"))


def collapse_accidental_hardbreaks(text: str) -> str:
    text = re.sub(
        r"(?<=\S) {2,}\n(?=(?:\[[^\]]+\]\([^)]+\)|<a\b|[A-Za-z0-9_(@`]))",
        " ", text,
    )
    text = re.sub(
        r"(?<=,)\n(?=(?:\[[^\]]+\]\([^)]+\)|<a\b|[A-Za-z0-9_(@`]))",
        " ", text,
    )
    return text


def clone_tag(node: Tag) -> Tag:
    soup = BeautifulSoup(str(node), "html.parser")
    cloned = soup.find()
    assert cloned is not None
    return cloned


def sanitize_raw_html_tree(root: Tag) -> None:
    for tag in root.find_all(True):
        attrs_to_drop = [name for name in list(tag.attrs) if name not in SANITIZED_HTML_ATTRS]
        for name in attrs_to_drop:
            del tag.attrs[name]
        if tag.has_attr("href"):
            tag["href"] = str(tag["href"])
        if tag.has_attr("src"):
            tag["src"] = str(tag["src"])


def extract_preformatted_text(pre: Tag) -> Tuple[str, str]:
    language = detect_code_language(pre) or detect_code_language(pre.find("code"))

    line_nodes = find_code_line_nodes(pre)
    if line_nodes:
        lines = [extract_inline_text(node).replace("\xa0", " ") for node in line_nodes]
        text = "\n".join(line.rstrip("\n") for line in lines)
        return repair_shell_command_wrapping(text, language), language

    code = pre.find("code")
    if code is not None:
        if not language:
            language = detect_code_language(code)
        text = code.get_text("", strip=False)
    else:
        text = pre.get_text("", strip=False)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = maybe_fix_mojibake(text)
    return repair_shell_command_wrapping(text, language), language


def detect_code_language(node: Optional[Tag]) -> str:
    if node is None:
        return ""
    classes = node.get("class", [])
    for cls in classes:
        if cls.startswith("language-"):
            return cls.split("language-", 1)[1]
        if cls.startswith("lang-"):
            return cls.split("lang-", 1)[1]
        if cls.startswith("highlight-"):
            return cls.split("highlight-", 1)[1]
    if node.has_attr("data-lang"):
        return str(node["data-lang"])
    if node.has_attr("data-language"):
        return str(node["data-language"])
    return ""


def find_code_line_nodes(root: Tag) -> List[Tag]:
    selectors = [
        ".token-line", ".line", ".cl",
        "[class*=tokenLine]", "[class*=codeLine]",
        ".code-line", "[class*=lineContent]",
        "[class~=line]", "[class~=cl]",
        "[data-code-line]",
        'span[style*="display:block"]',
    ]
    for selector in selectors:
        matches = list(root.select(selector))
        if not matches:
            continue
        filtered = [
            node for node in matches
            if not any(
                isinstance(parent, Tag) and parent is not root and parent in matches
                for parent in node.parents
            )
        ]
        if filtered:
            return filtered

    direct_tag_children = [child for child in root.children if isinstance(child, Tag)]
    if direct_tag_children and not any(
        isinstance(child, NavigableString) and clean_text(str(child))
        for child in root.children
    ):
        if all(child.name in {"div", "p", "span"} for child in direct_tag_children):
            return direct_tag_children
    return []


def extract_inline_text(node) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    pieces: List[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
        elif isinstance(child, Tag):
            if child.name == "br":
                pieces.append("\n")
            else:
                pieces.append(extract_inline_text(child))
    return "".join(pieces)


def repair_shell_command_wrapping(text: str, language: str) -> str:
    lang = (language or "").lower()
    if lang not in {"", "bash", "shell", "sh", "zsh", "console", "terminal", "shell-session"}:
        return text

    lines = text.splitlines()
    out: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        if re.match(r"^\s*(?:\$|#|>|%|PS>)(?:\s.*)?$", stripped):
            parts = [stripped]
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if not nxt:
                    break
                if re.match(r"^(?:\$|#|>|%|PS>)\s", nxt):
                    break
                if looks_like_command_output(nxt):
                    break
                parts.append(nxt)
                j += 1
            out.append(normalize_shell_fragments(parts))
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def looks_like_command_output(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if re.match(r"^[A-Za-z0-9_.-]+\s*=\s*.+$", stripped):
        return True
    if re.match(r"^[A-Za-z]:\\", stripped):
        return True
    if re.match(r"^/[A-Za-z0-9_.-]+", stripped):
        return True
    if re.match(r"^(?:Error|Warning|Note|INFO|DEBUG|TRACE)\b", stripped, re.I):
        return True
    return False


def normalize_shell_fragments(parts: List[str]) -> str:
    prompt = parts[0]
    rest = [frag.strip() for frag in parts[1:] if frag.strip()]
    if not rest:
        return prompt
    merged = prompt.rstrip()
    for frag in rest:
        if merged.endswith(("=", ":", ",", "(", "[", "{", "/", "-")):
            merged += frag
        elif frag.startswith(("=", ":", ",", ".", ")", "]", "}", "/", ";")):
            merged += frag
        else:
            merged += " " + frag
    return re.sub(r"\s+", " ", merged).strip()


                                                                         

def looks_like_admonition(node: Tag) -> bool:
    attrs = " ".join([node.get("id", ""), *node.get("class", []), node.name]).lower()
    if any(word in attrs for word in ["admonition", "alert", "callout", "notice", "hint"]):
        return True
    heading = find_admonition_heading(node)
    heading_text = clean_text(heading.get_text(" ", strip=True)).lower() if heading else ""
    if heading_text in ADMONITION_KIND_MAP:
        return True
    return False


def looks_like_tab_container(node: Tag) -> bool:
    classes = " ".join(node.get("class", []))
    if "tabs-container" in classes:
        return True
    if "tabs" in classes and node.get("role") == "tablist":
        return True
    return False


def table_is_simple(node: Tag) -> bool:
    if node.find("table") is not node:
                                       
        pass
    for nested in node.find_all("table"):
        if nested is not node:
            return False
    for cell in node.find_all(["td", "th"]):
        if cell.get("rowspan") and str(cell["rowspan"]).strip() not in {"", "1"}:
            return False
        if cell.get("colspan") and str(cell["colspan"]).strip() not in {"", "1"}:
            return False
        for block in cell.find_all(["ul", "ol", "pre", "table", "blockquote", "dl"]):
            return False
    return True


def render_complex_block(node: Tag) -> str:
    if node.name == "pre":
        return render_code_block(node)
    if looks_like_admonition(node):
        return render_admonition_block(node)
    if node.name == "table":
        if table_is_simple(node):
                                                   
            return "\n" + md(str(clone_tag(node)), heading_style="ATX") + "\n"
        clone = clone_tag(node)
        sanitize_raw_html_tree(clone)
        return "\n" + str(clone) + "\n"
    clone = clone_tag(node)
    sanitize_raw_html_tree(clone)
    return "\n" + str(clone) + "\n"


def render_code_block(pre: Tag) -> str:
    text, language = extract_preformatted_text(pre)
    text = text.replace("\r\n", "\n").rstrip("\n")
    fence = "```"
    while fence in text:
        fence += "`"
    return f"\n{fence}{language}\n{text}\n{fence}\n"


def render_admonition_block(node: Tag) -> str:
    clone = clone_tag(node)
    for icon in list(clone.select("[class*=admonitionIcon], [class*=alertIcon], i.fa, i.icon")):
        icon.decompose()
    for svg in list(clone.select("svg")):
        svg.decompose()

    kind = detect_admonition_kind(clone)
    label = CALL_OUT_KIND_MAP.get(kind, "NOTE")
    heading = find_admonition_heading(clone)
    title = clean_text(heading.get_text(" ", strip=True)) if heading is not None else label.title()

    content = find_admonition_content(clone)
    if heading is not None:
        heading.decompose()
        if content is None:
            content = clone
    if content is None:
        content = clone

    content = clone_tag(content)
    admon_md = markdownify_fragment(content)

    if ADMONITION_STYLE == "html":
        border_map = {
            "NOTE": "#2563eb", "TIP": "#16a34a", "IMPORTANT": "#7c3aed",
            "WARNING": "#d97706", "CAUTION": "#dc2626",
        }
        border = border_map.get(label, "#2563eb")
        body_html = markdown_to_safe_html(admon_md)
        return (
            "\n"
            f"<div style=\"border-left:4px solid {border}; padding:0.75rem 1rem; "
            f"margin:1rem 0; background:rgba(127,127,127,0.08);\">"
            f"<p><strong>{html.escape(title or label)}</strong></p>"
            f"{body_html}</div>\n"
        )

    lines: List[str] = [f"> [!{label}]"]
    normalized_title = clean_text(title).upper()
    if normalized_title and normalized_title != label:
        lines.append(f"> **{escape_markdown_text(title)}**")

    body_lines = admon_md.splitlines() or [title]
    prev_blank = False
    for line in body_lines:
        stripped = line.rstrip()
        if not stripped:
            if not prev_blank:
                lines.append(">")
            prev_blank = True
            continue
        lines.append(f"> {stripped}")
        prev_blank = False
    return "\n" + "\n".join(lines).rstrip() + "\n"


def markdown_to_safe_html(text: str) -> str:
    safe = html.escape(text)
    safe = safe.replace("\n\n", "</p><p>").replace("\n", "<br>")
    return f"<p>{safe}</p>"


def escape_markdown_text(text: str) -> str:
    return re.sub(r"([*_`\[\]\\])", r"\\\1", text)


def detect_admonition_kind(node: Tag) -> str:
    classes = [cls.lower() for cls in node.get("class", [])]
    for cls in classes:
        for prefix in ["theme-admonition-", "admonition-", "alert--", "callout-", "notice-"]:
            if cls.startswith(prefix):
                key = cls.split(prefix, 1)[1]
                if key in ADMONITION_KIND_MAP:
                    return ADMONITION_KIND_MAP[key]
        if cls in ADMONITION_KIND_MAP:
            return ADMONITION_KIND_MAP[cls]

    heading = find_admonition_heading(node)
    heading_text = clean_text(heading.get_text(" ", strip=True)).lower() if heading else ""
    for key, mapped in ADMONITION_KIND_MAP.items():
        if heading_text == key or heading_text.startswith(key + " "):
            return mapped
    return "note"


def find_admonition_heading(node: Tag) -> Optional[Tag]:
    selectors = [
        "[class*=admonitionHeading]",
        "[class*=admonitionTitle]",
        "[class*=alertHeading]",
        "[class*=alertTitle]",
        "[class*=callout-title]",
        ".admonition-title",
        ".markdown-alert-title",
        "summary",
    ]
    for selector in selectors:
        match = node.select_one(selector)
        if match is not None:
            return match
    for child in node.find_all(["p", "div", "strong", "summary"], recursive=False):
        text = clean_text(child.get_text(" ", strip=True))
        if text and len(text) <= 140:
            return child
    return None


def find_admonition_content(node: Tag) -> Optional[Tag]:
    selectors = [
        "[class*=admonitionContent]",
        "[class*=alertContent]",
        "[class*=callout-content]",
        ".admonition-content",
        ".markdown-alert-content",
    ]
    for selector in selectors:
        match = node.select_one(selector)
        if match is not None:
            return match
    return None


def markdownify_fragment(root: Tag) -> str:
    fragment = clone_tag(root)
    placeholders: Dict[str, str] = {}
    idx = 0

    complex_nodes: List[Tag] = []
    for tag in list(fragment.find_all(True)):
        if tag.name in RAW_HTML_BLOCK_TAGS:
            complex_nodes.append(tag)
            continue
        if tag.name == "pre":
            complex_nodes.append(tag)
            continue
        if tag.name == "code" and tag.parent and tag.parent.name == "pre":
            continue
        if looks_like_tab_container(tag):
            complex_nodes.append(tag)
            continue
        if looks_like_admonition(tag):
            complex_nodes.append(tag)
            continue

    processed: Set[int] = set()
    for node in complex_nodes:
        if id(node) in processed:
            continue
        if any(id(parent) in processed for parent in node.parents if isinstance(parent, Tag)):
            continue
        token = f"DOC2MDFRAGMENTTOKEN{idx}END"
        idx += 1
        placeholders[token] = render_complex_block(node)
        processed.add(id(node))
        node.replace_with(NavigableString(f"\n\n{token}\n\n"))

    html_text = str(fragment)
    markdown = md(html_text, heading_style="ATX", bullets="-", strong_em_symbol="*")
    for token, replacement in placeholders.items():
        markdown = markdown.replace(token, replacement)
    return postprocess_markdown(markdown)


def html_fragment_to_markdown(root: Tag) -> str:
    return root.get_text("", strip=False)


def protect_fenced_code_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    placeholders: Dict[str, str] = {}
    pattern = re.compile(r"(?ms)^(?P<fence>`{3,})(?P<info>[^\n]*)\n.*?^(?P=fence)[ \t]*$")

    def repl(match: re.Match[str]) -> str:
        token = f"DOC2MDCODEBLOCKTOKEN{len(placeholders)}END"
        placeholders[token] = match.group(0)
        return token

    return pattern.sub(repl, text), placeholders


def restore_placeholders(text: str, placeholders: Dict[str, str]) -> str:
    for token, block in placeholders.items():
        text = text.replace(token, block)
    return text


def postprocess_markdown(text: str) -> str:
    text = maybe_fix_mojibake(text)
    text = normalize_unicode_text(text)
    text = text.replace("\r\n", "\n")
    protected, placeholders = protect_fenced_code_blocks(text)
    protected = collapse_accidental_hardbreaks(protected)
    protected = re.sub(r"\n{3,}", "\n\n", protected)
    protected = re.sub(r"[ \t]+\n", "\n", protected)
    protected = re.sub(r"\n([*-] )\n", r"\n\1", protected)
    text = restore_placeholders(protected, placeholders)
    return text.strip() + "\n"


def starts_with_markdown_heading(text: str) -> bool:
    probe = text.lstrip()
    probe = re.sub(r'^(?:<a\s+id="[^"]+"></a>\s*)+', "", probe)
    probe = probe.lstrip()
    return bool(re.match(r"^#{1,6}\s+", probe))


                                                                         
                                                                         
                                                                         

def guess_site_prefix(entry_url: str, soup: BeautifulSoup, profile: str = "generic") -> str:
    parts = urlsplit(entry_url)
    path = parts.path or "/"
    nav_root = select_nav_root(soup, parts.netloc, base_url=entry_url, profile=profile)
    content_root = select_content_root(soup, profile=profile)

    candidate_links: List[str] = []
    for container in [nav_root, content_root]:
        if container is None:
            continue
        for a in container.select("a[href]"):
            href = (a.get("href") or "").strip()
            if not href or href.startswith(("#", "javascript:")):
                continue
            abs_url, _frag = split_and_normalize(entry_url, href)
            if urlsplit(abs_url).netloc != parts.netloc:
                continue
            ext = Path(urlsplit(abs_url).path).suffix.lower()
            if ext not in DOC_PAGE_EXTENSIONS:
                continue
            if query_looks_search_like(abs_url):
                continue
            candidate_links.append(abs_url)

                                                                               
                                                                                
                                                           
    docish = [u for u in candidate_links if path_similarity(urlsplit(u).path, path) >= 0.2]
    if len(docish) >= 3:
        common = common_path_prefix([urlsplit(u).path for u in docish] + [path])
        common_parts = [p for p in common.strip("/").split("/") if p]
        entry_parts = [p for p in path.strip("/").split("/") if p]
        if (
            len(entry_parts) >= 2
            and entry_parts[0].lower() in {"proper", "dormant", "sandbox"}
            and (not common_parts or common_parts == [entry_parts[0]])
        ):
            return clamp_prefix_to_version_scope(path, "/" + "/".join(entry_parts[:2]) + "/")
        if common and common != "/":
            return clamp_prefix_to_version_scope(path, common)

    segs = [seg for seg in path.strip("/").split("/") if seg]
    if not segs:
        return "/"
    for i, seg in enumerate(segs):
        if seg.lower() in DOC_LIKE_KEYWORDS:
            prefix_parts = segs[: i + 1]
            if i + 1 < len(segs) and looks_versionish(segs[i + 1]):
                prefix_parts.append(segs[i + 1])
            return clamp_prefix_to_version_scope(path, "/" + "/".join(prefix_parts) + "/")

                                                          
                                                                            
                                                                         
                       
    if len(segs) >= 2 and segs[0].lower() in {"proper", "dormant", "sandbox"}:
        return clamp_prefix_to_version_scope(path, "/" + "/".join(segs[:2]) + "/")

    suffix = Path(path).suffix.lower()
    if suffix:
        parent = posixpath.dirname(path) or "/"
        return clamp_prefix_to_version_scope(path, ensure_trailing_slash(parent))
    return clamp_prefix_to_version_scope(path, "/" + segs[0] + "/")


def build_site_slug(entry_url: str, site_prefix: str) -> str:
    host = urlsplit(entry_url).netloc.split(".")[0]
    parts = [p for p in site_prefix.strip("/").split("/") if p]
    if parts:
        return slugify("_".join([host] + parts))
    return slugify(host)


def url_to_rel_output(url: str, site_prefix: str) -> Path:
    path = urlsplit(url).path
    rel = path[len(site_prefix):] if path.startswith(site_prefix) else path.lstrip("/")
    rel = rel.lstrip("/")
    if not rel or rel.endswith("/"):
        rel = rel.rstrip("/")
        if rel:
            return Path(rel) / "index.md"
        return Path("index.md")
    suffix = Path(rel).suffix.lower()
    if suffix:
        rel = str(Path(rel).with_suffix(".md"))
    else:
        rel = rel + ".md"
    return Path(rel)


def uniquify_path(path: Path, taken: Set[Path]) -> Path:
    if path not in taken:
        return path
    counter = 2
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if candidate not in taken:
            return candidate
        counter += 1


def virtual_path_to_page_anchor(path: Path) -> str:
    rel = path
    if rel.parts and rel.parts[0] == "docs":
        rel = Path(*rel.parts[1:]) if len(rel.parts) > 1 else Path("index.md")
    parts = list(rel.parts)
    if parts and parts[-1] == "index.md":
        parts = parts[:-1] or ["index"]
    elif parts:
        parts[-1] = Path(parts[-1]).stem
    return slugify_anchor("-".join(parts) or "index")


def compose_heading_anchor(page_anchor: str, fragment: str) -> str:
    frag = slugify_anchor(fragment)
    return f"{page_anchor}--{frag}"


def derive_bundle_title(entry_url: str, entry_title: str, site_slug: str) -> str:
    if entry_title:
        clean = clean_text(entry_title)
        if clean:
            return clean
    host = urlsplit(entry_url).netloc
    return site_slug.replace("_", " ").title() or host


def path_relative_to(current_output: Optional[Path], target: Path) -> str:
    if current_output is None:
        return target.as_posix()
    rel = os.path.relpath(target, start=current_output.parent)
    return Path(rel).as_posix()


def extension_for_asset(final_url: str, content_type: Optional[str]) -> str:
    ext = Path(urlsplit(final_url).path).suffix
    if ext:
        return ext
    if content_type:
        guessed = mimetypes.guess_extension(content_type, strict=False)
        if guessed:
            return guessed
    return ".bin"


def load_targets(targets_file: Optional[Path], urls: List[str]) -> List[str]:
    out = [normalize_url(u) for u in urls if u.strip()]
    if targets_file is not None:
        for line in targets_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(normalize_url(line))
    return dedupe_preserve_order(out)


def render_singlefile_navigation(
    nodes: List[NavNode],
    url_to_anchor: Dict[str, str],
    indent: int = 0,
) -> List[str]:
    lines: List[str] = []
    for node in nodes:
        prefix = "  " * indent + "- "
        if node.href and node.href in url_to_anchor:
            lines.append(f"{prefix}[{node.title}](#{url_to_anchor[node.href]})")
        elif node.href:
            lines.append(f"{prefix}[{node.title}]({node.href})")
        else:
            lines.append(f"{prefix}{node.title}")
        if node.children:
            lines.extend(render_singlefile_navigation(node.children, url_to_anchor, indent + 1))
    return lines


def build_url_tree(
    pages: Dict[str, PageRecord],
    url_to_virtual_path: Dict[str, Path],
) -> List[NavNode]:
    root = NavNode(title="root", kind="category")
    folder_nodes: Dict[Tuple[str, ...], NavNode] = {(): root}

    for url, record in sorted(pages.items(), key=lambda item: url_to_virtual_path[item[0]].as_posix()):
        rel = url_to_virtual_path[url]
        parts = list(rel.parts)
        folder_parts = tuple(parts[:-1])
        parent_key: Tuple[str, ...] = ()
        for i in range(len(folder_parts)):
            key = tuple(folder_parts[: i + 1])
            if key not in folder_nodes:
                title = key[-1].replace("_", " ").replace("-", " ").title()
                node = NavNode(title=title, kind="category")
                folder_nodes[parent_key].children.append(node)
                folder_nodes[key] = node
            parent_key = key
        folder_nodes[parent_key].children.append(
            NavNode(title=record.title, href=url, kind="link")
        )
    return root.children


                                                                         
                                                                         
                                                                         

class UniversalDocsConverter:
    def __init__(
        self,
        entry_url: str,
        out_dir: Path,
        delay: float = 0.15,
        max_pages: Optional[int] = None,
        max_depth: int = DEFAULT_MAX_DEPTH,
        save_html: bool = False,
        use_sitemap: bool = False,
        site_prefix_override: Optional[str] = None,
        combined_filename: str = "combined.md",
        browser_mode: str = "auto",
        browser_timeout_ms: int = BROWSER_TIMEOUT_MS,
        front_matter: bool = False,
        profile_override: Optional[str] = None,
        concurrency: int = DEFAULT_CONCURRENCY,
        follow_content_links: bool = False,
        respect_robots: bool = True,
        max_asset_bytes: int = DEFAULT_MAX_ASSET_BYTES,
        cache_dir: Optional[Path] = None,
        use_cache: bool = True,
        download_external_assets: bool = False,
        strict_version_scope: bool = True,
    ) -> None:
        self.entry_url = normalize_url(entry_url)
        self.entry_parts = urlsplit(self.entry_url)
        self.domain = self.entry_parts.netloc
        self.out_root = out_dir
        self.delay = delay
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.save_html = save_html
        self.use_sitemap = use_sitemap
        self.site_prefix_override = site_prefix_override
        self.combined_filename = combined_filename
        self.browser_mode = browser_mode
        self.browser_timeout_ms = browser_timeout_ms
        self.front_matter = front_matter
        self.profile_override = profile_override
        self.concurrency = max(1, concurrency)
        self.follow_content_links = follow_content_links
        self.respect_robots = respect_robots
        self.download_external_assets = download_external_assets
        self.strict_version_scope = strict_version_scope

        self.session = build_session()
        self.rate_limiter = RateLimiter(delay)

        cache_root = cache_dir or (out_dir / ".cache")
        self.cache = HttpCache(cache_root, enabled=use_cache)

        self.browser_pool: Optional[BrowserPool] = None
        if browser_mode != "never" and PLAYWRIGHT_AVAILABLE:
            self.browser_pool = BrowserPool(timeout_ms=browser_timeout_ms)

        self.fetcher = Fetcher(
            session=self.session,
            cache=self.cache,
            rate_limiter=self.rate_limiter,
            browser_pool=self.browser_pool,
            browser_mode=browser_mode,
            respect_robots=respect_robots,
            max_asset_bytes=max_asset_bytes,
        )

        self.asset_cache: Dict[str, Path] = {}
        self.asset_cache_lock = threading.Lock()
        self.url_to_virtual_path: Dict[str, Path] = {}
        self.url_to_anchor: Dict[str, str] = {}
        self.url_alias_to_canonical: Dict[str, str] = {}
        self.pages: Dict[str, PageRecord] = {}
        self.nav_tree: List[NavNode] = []
        self.nav_snapshots: List[List[NavNode]] = []
        self.site_prefix: Optional[str] = None
        self.site_slug: Optional[str] = None
        self.site_dir: Optional[Path] = None
        self.combined_output_path: Optional[Path] = None
        self.entry_final_url: Optional[str] = None
        self.profile: str = "generic"
        self.version_scope_prefix: Optional[str] = None
        self.version_query_scope: Tuple[Tuple[str, str], ...] = ()
        self._pages_lock = threading.Lock()
        self._nav_lock = threading.Lock()

                                                                      
    def run(self) -> None:
        print(f"\n=== {self.entry_url} ===")
        try:
            entry_result = self.fetcher.fetch_text(self.entry_url)
        except Exception as exc:
            print(f"[error] cannot fetch entry URL: {exc}")
            return
        entry_html = entry_result.text
        entry_final_url = entry_result.final_url
        self.entry_final_url = entry_final_url
        entry_soup = BeautifulSoup(entry_html, "html.parser")

        self.profile = self.profile_override or detect_profile(entry_soup, entry_final_url)
        self.site_prefix = self.site_prefix_override or guess_site_prefix(
            entry_final_url, entry_soup, self.profile,
        )
        if self.strict_version_scope:
            self.version_scope_prefix = infer_version_scope_prefix(
                urlsplit(entry_final_url).path,
                self.site_prefix,
            )
            self.version_query_scope = query_scope_from_url(entry_final_url)
            if self.version_scope_prefix and not self.site_prefix_override:
                self.site_prefix = clamp_prefix_to_version_scope(
                    urlsplit(entry_final_url).path,
                    self.site_prefix,
                )
        self.site_slug = build_site_slug(entry_final_url, self.site_prefix)
        self.site_dir = self.out_root / self.site_slug
        self.combined_output_path = self.site_dir / self.combined_filename
        assets_dir = self.site_dir / "assets"
        self.site_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)
        if self.save_html:
            (self.site_dir / "html_cache").mkdir(parents=True, exist_ok=True)

        print(f"profile    : {self.profile}")
        print(f"site prefix: {self.site_prefix}")
        if self.version_scope_prefix or self.version_query_scope:
            print(f"version pin: {self.version_scope_prefix or '-'} {dict(self.version_query_scope) if self.version_query_scope else ''}")
        print(f"output dir : {self.site_dir}")
        print(f"concurrency: {self.concurrency}")
        if self.browser_mode != "never":
            browser_note = "available" if PLAYWRIGHT_AVAILABLE else "not installed"
            print(f"browser    : {self.browser_mode} ({browser_note})")

        try:
            self.crawl(entry_html=entry_html, entry_final_url=entry_final_url)
            self.assign_virtual_paths()
            self.assign_page_anchors()
            self.convert_pages_to_fragments()
            self.write_navigation_sidecars()
            self.write_combined_markdown()
            self.write_manifests()
        finally:
            if self.browser_pool is not None:
                self.browser_pool.close()
        print(f"done: {len(self.pages)} pages, {len(self.asset_cache)} assets")

                                                                     
    def crawl(self, entry_html: str, entry_final_url: str) -> None:
        assert self.site_prefix is not None
        start_urls: List[Tuple[str, int]] = [(entry_final_url, 0)]
        if self.use_sitemap:
            sitemap_urls = self.discover_from_sitemap()
            if sitemap_urls:
                print(f"sitemap seeds: {len(sitemap_urls)}")
                for url in sorted(sitemap_urls):
                    if url != entry_final_url:
                        start_urls.append((url, 0))

        queued: Set[str] = set(url for url, _ in start_urls)
        seen_done: Set[str] = set()

                                                                             
        self._preloaded_entry = (entry_final_url, entry_html)

        executor = ThreadPoolExecutor(max_workers=self.concurrency)
        in_flight: Dict[Future, Tuple[str, int]] = {}
        pending: deque[Tuple[str, int]] = deque(start_urls)
        reached_max = False

        try:
            while pending or in_flight:
                                
                while pending and len(in_flight) < self.concurrency:
                    if self.max_pages is not None and len(self.pages) + len(in_flight) >= self.max_pages:
                        break
                    url, depth = pending.popleft()
                    if url in seen_done:
                        continue
                    future = executor.submit(self._fetch_and_parse, url, depth)
                    in_flight[future] = (url, depth)

                if not in_flight:
                    break

                                               
                done = next(as_completed(in_flight))
                url, depth = in_flight.pop(done)
                seen_done.add(url)

                try:
                    result = done.result()
                except Exception as exc:
                    print(f"[warn] failed to process {url}: {exc}")
                    continue

                if result is None:
                    continue

                record, new_links = result
                with self._pages_lock:
                    if record.final_url not in self.pages:
                        self.pages[record.final_url] = record

                if self.max_pages is not None and len(self.pages) >= self.max_pages:
                    if not reached_max:
                        print("max-pages reached; stopping dispatch")
                        reached_max = True

                if reached_max:
                    continue

                                   
                next_depth = depth + 1
                if next_depth > self.max_depth:
                    continue
                for link in new_links:
                    if link in seen_done or link in queued:
                        continue
                    if not self.is_allowed_page(link):
                        continue
                    queued.add(link)
                    pending.append((link, next_depth))
        finally:
            executor.shutdown(wait=True)

    def _fetch_and_parse(
        self,
        url: str,
        depth: int,
    ) -> Optional[Tuple[PageRecord, List[str]]]:
        if self.respect_robots and not self.fetcher.allowed_by_robots(url):
            print(f"[skip] blocked by robots.txt: {url}")
            return None

                                                                
        if (
            getattr(self, "_preloaded_entry", None) is not None
            and self._preloaded_entry[0] == url
        ):
            html_text, final_url = self._preloaded_entry[1], url
        else:
            try:
                result = self.fetcher.fetch_text(url)
            except Exception as exc:
                print(f"[warn] fetch failed {url}: {exc}")
                return None
            html_text, final_url = result.text, result.final_url

        if final_url != url and not self.is_allowed_page(final_url):
            return None

        soup = BeautifulSoup(html_text, "html.parser")
        profile = detect_profile(soup, final_url, hint=self.profile)
        content_root = select_content_root(soup, profile=profile)
        nav_root = select_nav_root(
            soup,
            current_domain=self.domain,
            base_url=final_url,
            content_root=content_root,
            profile=profile,
            current_url=final_url,
            site_prefix=self.site_prefix,
        )

        score = compute_content_score(content_root) if content_root is not None else 0
        if not is_doc_like_page(content_root, nav_root, score):
            print(f"[skip] weak/non-doc page {final_url}")
            return None

                                                           
        path_parts = [seg.lower() for seg in urlsplit(final_url).path.strip("/").split("/")]
        if any(p in SOFT_NOISE_PATH_TOKENS for p in path_parts) and score < 1200:
            print(f"[skip] soft-noise path {final_url}")
            return None

        title = extract_title(soup, content_root)
        nav_tree = extract_nav_tree(
            nav_root,
            current_domain=self.domain,
            base_url=final_url,
        )
        if nav_tree:
            mark_active_nav_item(nav_tree, final_url, title)
            with self._nav_lock:
                                                                                
                                                                              
                                                                                 
                self.nav_snapshots.append(copy.deepcopy(nav_tree))

        print(f"[page] {final_url}")
        record = PageRecord(
            url=url,
            final_url=final_url,
            title=title,
            html_text=html_text,
            nav_tree=nav_tree,
            profile=profile,
            content_score=score,
            depth=depth,
        )
        with self._pages_lock:
            self.url_alias_to_canonical[url] = final_url
            self.url_alias_to_canonical[final_url] = final_url

        assert self.site_prefix is not None
        candidate_links = extract_crawl_links(
            soup=soup,
            domain=self.domain,
            site_prefix=self.site_prefix,
            base_url=final_url,
            profile=profile,
            follow_content_links=self.follow_content_links,
            current_url=final_url,
        )
        return record, candidate_links

    def discover_from_sitemap(self) -> Set[str]:
        assert self.site_prefix is not None
        site_root = f"{self.entry_parts.scheme}://{self.entry_parts.netloc}"
        sitemap_urls = [f"{site_root}/sitemap.xml"]
        discovered: Set[str] = set()
        for sitemap_url in sitemap_urls:
            try:
                resp = self.session.get(sitemap_url, timeout=HTTP_TIMEOUT)
                if resp.status_code >= 400:
                    continue
                xml = decode_response_text(resp)
                for loc in re.findall(r"<loc>(.*?)</loc>", xml):
                    loc = html.unescape(loc.strip())
                    url = normalize_url(loc)
                    if self.is_allowed_page(url):
                        discovered.add(url)
            except Exception as exc:
                print(f"[warn] sitemap fetch failed {sitemap_url}: {exc}")
        return discovered

                                                                     
    def assign_virtual_paths(self) -> None:
        assert self.site_prefix is not None
        taken: Set[Path] = set()
        for url in sorted(self.pages.keys()):
            rel = url_to_rel_output(url, self.site_prefix)
            virtual = Path("docs") / rel
            if virtual in taken:
                virtual = uniquify_path(virtual, taken)
            taken.add(virtual)
            self.url_to_virtual_path[url] = virtual
            self.pages[url].virtual_path = virtual

    def assign_page_anchors(self) -> None:
        seen: Set[str] = set()
        for url, record in sorted(
            self.pages.items(),
            key=lambda item: self.url_to_virtual_path[item[0]].as_posix(),
        ):
            assert record.virtual_path is not None
            anchor = virtual_path_to_page_anchor(record.virtual_path)
            if anchor in seen:
                base = anchor
                idx = 2
                while f"{base}-{idx}" in seen:
                    idx += 1
                anchor = f"{base}-{idx}"
            seen.add(anchor)
            record.page_anchor = anchor
            self.url_to_anchor[url] = anchor
            alias_url = normalize_url(record.url)
            self.url_to_anchor[alias_url] = anchor
            if record.final_url != url:
                self.url_to_anchor[record.final_url] = anchor

                                                                     
    def convert_pages_to_fragments(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        for url, record in sorted(self.pages.items()):
            soup = BeautifulSoup(record.html_text, "html.parser")
            root = select_content_root(soup, profile=record.profile)
            if root is None:
                root = soup.find("main") or soup.body or soup

            root = copy.copy(root)
            root = BeautifulSoup(str(root), "html.parser")
            content = root.find() or root
            if isinstance(content, Tag) and content.name in {"td", "th"}:
                wrapper_soup = BeautifulSoup("<div></div>", "html.parser")
                wrapper = wrapper_soup.div
                assert wrapper is not None
                for child in list(content.children):
                    wrapper.append(copy.copy(child))
                content = wrapper

            assert record.page_anchor is not None
            self.prepare_content(
                content,
                current_url=url,
                page_anchor=record.page_anchor,
                current_output=self.combined_output_path,
            )
            markdown_body = html_fragment_to_markdown(content)
            markdown_body = postprocess_markdown(markdown_body)
            if not starts_with_markdown_heading(markdown_body):
                markdown_body = f"# {record.title}\n\n" + markdown_body.lstrip()
            record.markdown_body = markdown_body.strip() + "\n"

            if self.save_html:
                assert record.virtual_path is not None
                cache_path = self.site_dir / "html_cache" / record.virtual_path.relative_to("docs")
                cache_path = cache_path.with_suffix(".html")
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(record.html_text, encoding="utf-8")

    def prepare_content(
        self,
        root: Tag,
        current_url: str,
        page_anchor: str,
        current_output: Optional[Path],
    ) -> None:
        assert self.site_dir is not None
        placeholders: Dict[str, str] = {}
        idx = 0

        for selector in NOISE_SELECTORS:
            for tag in list(root.select(selector)):
                tag.decompose()

                                                                           
                                                                             
                                                                             
                                                               
        for selector in CONTENT_CHROME_SELECTORS:
            for tag in list(root.select(selector)):
                if tag is not root:
                    tag.decompose()

        if getattr(root, "name", None) == "body" or root.select_one("#navcolumn, #leftColumn, .theme-doc-sidebar-container, .VPSidebar, .md-sidebar, .sphinxsidebar"):
            nav_in_content = select_nav_root(
                root,
                current_domain=self.domain,
                base_url=current_url,
                content_root=None,
                profile=self.profile,
                current_url=current_url,
                site_prefix=self.site_prefix,
            )
            if nav_in_content is not None and nav_in_content is not root:
                try:
                    nav_in_content.decompose()
                except Exception:
                    pass

        for comment in list(root.find_all(string=lambda x: isinstance(x, Comment))):
            comment.extract()

        replace_inline_breaks(root)
        normalize_dom_text_nodes(root)

                                                     
        for heading in list(root.find_all(re.compile(r"^h[1-6]$"))):
            heading_id = heading.get("id") or heading.get("name")
            for a in list(heading.select("a.hash-link, a.headerlink")):
                a.decompose()
            if heading_id:
                unique_id = compose_heading_anchor(page_anchor, heading_id)
                token = f"DOC2MDPLACEHOLDERTOKEN{idx}END"
                idx += 1
                placeholders[token] = f'<a id="{html.escape(unique_id, quote=True)}"></a>\n\n'
                heading.insert_before(NavigableString(token))

                         
        for img in list(root.find_all("img")):
            src = first_nonempty_attr(img, [
                "src", "data-src", "data-original",
                "data-lazy-src", "data-src-retina",
            ])
            if not src or src.startswith("data:"):
                continue
            abs_url = absolutize(current_url, src)
            if not self.should_download_asset(abs_url):
                                                                    
                                                                             
                                                                             
                img["src"] = abs_url
                for attr in ["srcset", "data-src", "data-original", "data-lazy-src", "data-src-retina"]:
                    if img.has_attr(attr) and attr != "src":
                        del img[attr]
                continue
            try:
                local_path = self.download_asset(abs_url)
                rel = path_relative_to(current_output, self.site_dir / local_path)
                img["src"] = rel
                for attr in ["srcset", "data-src", "data-original", "data-lazy-src", "data-src-retina"]:
                    if img.has_attr(attr) and attr != "src":
                        del img[attr]
            except Exception as exc:
                print(f"[warn] asset fetch failed {abs_url}: {exc}")

                        
        for a in list(root.find_all("a", href=True)):
            href = (a.get("href") or "").strip()
            if not href or href.startswith(("javascript:", "mailto:", "tel:")):
                continue

            if href.startswith("#"):
                frag = href[1:]
                a["href"] = "#" + (
                    compose_heading_anchor(page_anchor, frag) if frag else page_anchor
                )
                continue

            abs_url, frag = split_and_normalize(current_url, href)
            canon = self.url_alias_to_canonical.get(abs_url, abs_url)
            if canon in self.url_to_anchor:
                target_anchor = self.url_to_anchor[canon]
                if frag:
                    target_anchor = compose_heading_anchor(target_anchor, frag)
                a["href"] = "#" + target_anchor
                continue

            if is_probably_asset(abs_url):
                if not self.should_download_asset(abs_url):
                    a["href"] = abs_url + (f"#{frag}" if frag else "")
                    continue
                try:
                    local_path = self.download_asset(abs_url)
                    target = self.site_dir / local_path
                    a["href"] = path_relative_to(current_output, target)
                    continue
                except Exception:
                    pass

            if urlsplit(abs_url).netloc == self.domain:
                a["href"] = abs_url + (f"#{frag}" if frag else "")

                                                               
        complex_nodes: List[Tag] = []
        for tag in list(root.find_all(True)):
            if tag.name in RAW_HTML_BLOCK_TAGS:
                complex_nodes.append(tag)
                continue
            if tag.name == "pre":
                complex_nodes.append(tag)
                continue
            if tag.name == "code" and tag.parent and tag.parent.name == "pre":
                continue
            if tag.name == "table":
                complex_nodes.append(tag)
                continue
            if looks_like_tab_container(tag):
                complex_nodes.append(tag)
                continue
            if looks_like_admonition(tag):
                complex_nodes.append(tag)
                continue
            if tag.name == "figure" and tag.find("table"):
                complex_nodes.append(tag)
                continue

        processed: Set[int] = set()
        for node in complex_nodes:
            if id(node) in processed:
                continue
            if any(id(parent) in processed for parent in node.parents if isinstance(parent, Tag)):
                continue
            token = f"DOC2MDPLACEHOLDERTOKEN{idx}END"
            idx += 1
            placeholders[token] = render_complex_block(node)
            processed.add(id(node))
            node.replace_with(NavigableString(f"\n\n{token}\n\n"))

        html_text = str(root)
        markdown = md(
            html_text,
            heading_style="ATX",
            bullets="-",
            strong_em_symbol="*",
        )
        for token, replacement in placeholders.items():
            markdown = markdown.replace(token, replacement)
        root.clear()
        root.append(NavigableString(markdown))

                                                                     
    def should_download_asset(self, asset_url: str) -> bool:
        if self.download_external_assets:
            return True
        try:
            parts = urlsplit(normalize_url(asset_url))
        except Exception:
            return False
        return parts.netloc == self.domain

    def download_asset(self, asset_url: str) -> Path:
        assert self.site_dir is not None
        asset_url = normalize_url(asset_url)
        if not self.should_download_asset(asset_url):
            raise ValueError(f"external asset download disabled: {asset_url}")
        with self.asset_cache_lock:
            if asset_url in self.asset_cache:
                return self.asset_cache[asset_url]

        payload, final_url, content_type = self.fetcher.fetch_binary(asset_url)
        if not self.download_external_assets and urlsplit(final_url).netloc != self.domain:
            raise ValueError(f"asset redirected to external host: {final_url}")
        ext = extension_for_asset(final_url, content_type)
        stem = safe_stem(Path(urlsplit(final_url).path).stem or "asset")
        digest = hashlib.sha1(final_url.encode("utf-8")).hexdigest()[:16]
        subdir = "images" if (content_type or "").startswith("image/") else "files"
        rel_path = Path("assets") / subdir / f"{stem}_{digest}{ext}"
        abs_path = self.site_dir / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_bytes(payload)
        with self.asset_cache_lock:
            self.asset_cache[asset_url] = rel_path
            if final_url != asset_url:
                self.asset_cache[final_url] = rel_path
        return rel_path

                                                                    
    def canonicalize_page_url(self, url: str) -> str:
        return self.url_alias_to_canonical.get(url, url)

    def effective_nav_tree(self) -> List[NavNode]:
                                                                                
                                                                              
                                                              
        nav = merged_nav_from_snapshots(
            self.nav_snapshots,
            site_prefix=self.site_prefix,
            domain=self.domain,
        )
        if not nav:
            nav = copy.deepcopy(self.nav_tree)

                                                                       
        nav = filter_nav_to_known_urls(nav, set(self.pages.keys()), self.url_alias_to_canonical)
        if not nav:
            nav = build_url_tree(self.pages, self.url_to_virtual_path)

        nav_urls = {self.canonicalize_page_url(url) for url in flatten_nav_urls(nav)}
        missing_urls = [
            url for url in self.pages.keys()
            if self.canonicalize_page_url(url) not in nav_urls
        ]
        if missing_urls:
                                                            
            missing_urls.sort(key=lambda u: self.url_to_virtual_path[u].as_posix())
            other_children = [
                NavNode(title=self.pages[url].title, href=url, kind="link")
                for url in missing_urls
            ]
            nav.append(NavNode(title="Other pages", children=other_children, kind="category"))
        return nav

    def ordered_page_urls_from_nav(self, nav: List[NavNode]) -> List[str]:
        ordered: List[str] = []
        seen: Set[str] = set()
        for url in flatten_nav_urls(nav):
            canon = self.canonicalize_page_url(url)
            if canon in self.pages and canon not in seen:
                ordered.append(canon)
                seen.add(canon)
        for url in sorted(self.pages.keys(), key=lambda u: self.url_to_virtual_path[u].as_posix()):
            canon = self.canonicalize_page_url(url)
            if canon not in seen:
                ordered.append(canon)
                seen.add(canon)
        return ordered

    def write_navigation_sidecars(self) -> None:
        assert self.site_dir is not None
        nav = self.effective_nav_tree()
        nav_dict = [node.to_dict(self.url_to_anchor, self.url_to_virtual_path) for node in nav]
        (self.site_dir / "navigation.json").write_text(
            json.dumps(nav_dict, ensure_ascii=False, indent=2), encoding="utf-8",
        )
        (self.site_dir / "navigation.yml").write_text(
            yaml.safe_dump(nav_dict, sort_keys=False, allow_unicode=True), encoding="utf-8",
        )
        summary_lines = ["# Summary", ""]
        summary_lines.extend(render_singlefile_navigation(nav, self.url_to_anchor))
        (self.site_dir / "SUMMARY.md").write_text(
            "\n".join(summary_lines).rstrip() + "\n", encoding="utf-8",
        )

    def write_combined_markdown(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        nav = self.effective_nav_tree()
        ordered_urls = self.ordered_page_urls_from_nav(nav)
        entry_record = self.pages.get(
            self.entry_final_url or self.entry_url,
            PageRecord("", "", "", ""),
        )
        site_title = derive_bundle_title(
            entry_url=self.entry_final_url or self.entry_url,
            entry_title=entry_record.title,
            site_slug=self.site_slug or "site",
        )

        parts: List[str] = []
        if self.front_matter:
            front_matter = {
                "entry_url": self.entry_url,
                "page_count": len(self.pages),
                "asset_count": len(self.asset_cache),
                "profile": self.profile,
            }
            parts.append(
                "---\n"
                + yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True).strip()
                + "\n---\n\n"
            )

        parts.append(f"# {site_title}\n\n")
        parts.append("## Navigation\n\n")
        nav_lines = render_singlefile_navigation(nav, self.url_to_anchor)
        if nav_lines:
            parts.append("\n".join(nav_lines) + "\n")
        else:
            parts.append("- No navigation extracted\n")

        parts.append("\n## Content\n")
        for index, url in enumerate(ordered_urls, start=1):
            record = self.pages[url]
            assert record.page_anchor is not None
            body = record.markdown_body.strip() or f"# {record.title}\n"
            parts.append(f'\n<a id="{record.page_anchor}"></a>\n')
            parts.append(f"\n<!-- source_url: {url} -->\n")
            parts.append(f"\n<!-- page_index: {index} -->\n\n")
            parts.append(body)
            parts.append("\n\n---\n")

        combined_text = "".join(parts).rstrip() + "\n"
        self.combined_output_path.write_text(combined_text, encoding="utf-8")

    def write_manifests(self) -> None:
        assert self.site_dir is not None
        assert self.site_prefix is not None
        assert self.combined_output_path is not None

        manifest = {
            "entry_url": self.entry_url,
            "site_prefix": self.site_prefix,
            "site_slug": self.site_slug,
            "profile": self.profile,
            "combined_markdown": self.combined_output_path.name,
            "page_count": len(self.pages),
            "asset_count": len(self.asset_cache),
            "pages": [
                {
                    "source_url": url,
                    "title": record.title,
                    "anchor": record.page_anchor,
                    "virtual_path": self.url_to_virtual_path[url].as_posix(),
                    "profile": record.profile,
                    "score": record.content_score,
                    "depth": record.depth,
                }
                for url, record in sorted(
                    self.pages.items(),
                    key=lambda item: self.url_to_virtual_path[item[0]].as_posix(),
                )
            ],
        }
        (self.site_dir / "site_manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8",
        )

                                                                    
    def is_allowed_page(self, url: str) -> bool:
        assert self.site_prefix is not None
        url = normalize_url(url)
        parts = urlsplit(url)
        if parts.netloc != self.domain:
            return False
        if query_looks_search_like(url):
            return False
        if any(pattern.search(parts.path) for pattern in SKIP_URL_PATTERNS):
            return False
        ext = Path(parts.path).suffix.lower()
        if ext not in DOC_PAGE_EXTENSIONS:
            return False
        if not parts.path.startswith(self.site_prefix):
            return False

                                                                             
                                                                                
                                                 
        if self.strict_version_scope:
            if self.version_scope_prefix and not parts.path.startswith(self.version_scope_prefix):
                return False
            if self.version_query_scope and not url_matches_query_scope(url, self.version_query_scope):
                return False

                                                                               
                                                                               
                                                        
            if not self.version_scope_prefix:
                rel = parts.path[len(self.site_prefix):].lstrip("/") if parts.path.startswith(self.site_prefix) else ""
                first = rel.split("/", 1)[0] if rel else ""
                if first and "/" in rel and looks_versionish(first):
                    return False
        return True


def filter_nav_to_known_urls(
    nodes: List[NavNode],
    known_urls: Set[str],
    alias: Dict[str, str],
) -> List[NavNode]:
    out: List[NavNode] = []
    for node in nodes:
        children = filter_nav_to_known_urls(node.children, known_urls, alias) if node.children else []
        if node.href:
            canon = alias.get(node.href, node.href)
            if canon in known_urls:
                node.href = canon
        node.children = children
        if node.href or node.children:
            out.append(node)
    return dedupe_nav(out)


                                                                         
                                                                         
                                                                         

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawl an HTML documentation site and convert it into a single Markdown file.",
    )
    parser.add_argument("urls", nargs="*", help="One or more docs entry URLs.")
    parser.add_argument("--targets-file", type=Path, help="Text file with one URL per line.")
    parser.add_argument("--out-dir", type=Path, default=Path("./converted_docs"),
                        help="Output directory (default: ./converted_docs).")
    parser.add_argument("--delay", type=float, default=0.15,
                        help="Minimum interval between requests to the same host (default: 0.15s).")
    parser.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY,
                        help=f"Number of concurrent fetches (default: {DEFAULT_CONCURRENCY}).")
    parser.add_argument("--max-pages", type=int, default=None,
                        help="Maximum number of pages per site.")
    parser.add_argument("--max-depth", type=int, default=DEFAULT_MAX_DEPTH,
                        help=f"Maximum link-depth from entry URL (default: {DEFAULT_MAX_DEPTH}).")
    parser.add_argument("--save-html", action="store_true",
                        help="Save original HTML files next to the output for debugging.")
    parser.add_argument("--use-sitemap", action="store_true",
                        help="Use sitemap.xml as extra crawl seeds.")
    parser.add_argument("--site-prefix", default=None,
                        help="Force the crawl path prefix, e.g. /docs/ or /manual/.")
    parser.add_argument("--combined-filename", default="combined.md",
                        help="Name of the single combined Markdown file.")
    parser.add_argument("--browser", choices=["auto", "always", "never"], default="auto",
                        help="Whether to use Playwright rendering for JS-heavy docs.")
    parser.add_argument("--browser-timeout-ms", type=int, default=BROWSER_TIMEOUT_MS,
                        help=f"Playwright timeout in ms (default: {BROWSER_TIMEOUT_MS}).")
    parser.add_argument("--admonition-style", choices=["callout", "html"], default="callout",
                        help="How to render note/tip/warning blocks.")
    parser.add_argument("--front-matter", action="store_true",
                        help="Include a YAML front matter block at the top of combined.md.")
    parser.add_argument("--profile",
                        choices=["generic", "docusaurus", "sphinx", "mkdocs", "vitepress", "maven", "book"],
                        default=None,
                        help="Force a site profile if auto-detection gets it wrong.")
    parser.add_argument("--follow-content-links", action="store_true",
                        help="Also follow links found in page content (default: only sidebar+pagination).")
    parser.add_argument("--no-robots", action="store_true", help="Ignore robots.txt.")
    parser.add_argument("--max-asset-mb", type=float,
                        default=DEFAULT_MAX_ASSET_BYTES / (1024 * 1024),
                        help="Maximum size of any single downloaded asset (default: 25 MB).")
    parser.add_argument("--download-external-assets", action="store_true",
                        help="Download images/files from external hosts. Default: keep external URLs unchanged.")
    parser.add_argument("--loose-version-scope", action="store_true",
                        help="Allow crawling sibling documentation versions. Default: stay pinned to the entry URL's version.")
    parser.add_argument("--cache-dir", type=Path, default=None,
                        help="HTTP cache directory (default: <out-dir>/.cache).")
    parser.add_argument("--no-cache", action="store_true", help="Disable the HTTP cache.")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    global ADMONITION_STYLE
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    ADMONITION_STYLE = args.admonition_style
    targets = load_targets(args.targets_file, args.urls)
    if not targets:
        parser.error("Provide at least one URL or --targets-file.")

    max_asset_bytes = int(args.max_asset_mb * 1024 * 1024)

    for entry_url in targets:
        converter = UniversalDocsConverter(
            entry_url=entry_url,
            out_dir=args.out_dir,
            delay=args.delay,
            max_pages=args.max_pages,
            max_depth=args.max_depth,
            save_html=args.save_html,
            use_sitemap=args.use_sitemap,
            site_prefix_override=args.site_prefix,
            combined_filename=args.combined_filename,
            browser_mode=args.browser,
            browser_timeout_ms=args.browser_timeout_ms,
            front_matter=args.front_matter,
            profile_override=args.profile,
            concurrency=args.concurrency,
            follow_content_links=args.follow_content_links,
            respect_robots=not args.no_robots,
            max_asset_bytes=max_asset_bytes,
            cache_dir=args.cache_dir,
            use_cache=not args.no_cache,
            download_external_assets=args.download_external_assets,
            strict_version_scope=not args.loose_version_scope,
        )
        try:
            converter.run()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"[error] {entry_url}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
