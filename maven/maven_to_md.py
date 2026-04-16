#!/usr/bin/env python3
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
import time
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Set, Tuple
from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit, urldefrag, unquote

import requests
import yaml
from bs4 import BeautifulSoup, Comment, NavigableString, Tag, UnicodeDammit
from markdownify import markdownify as md
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USER_AGENT = "Mozilla/5.0 (compatible; MavenSiteToMarkdown/1.0; +https://example.invalid/bot)"
TIMEOUT = 30

CONTENT_SELECTORS = [
    "#bodyColumn",
    "td#bodyColumn",
    "div#bodyColumn",
    "div#contentBox",
    "td#contentBox",
    "main article",
    "main",
    "article",
    "#content",
    "#contentBox",
    "div.content",
    "div.section",
    "body",
]

NAV_SELECTORS = [
    "#leftColumn #navcolumn",
    "#navcolumn",
    "td#leftColumn",
    "div#leftColumn",
    "div.leftColumn",
    "aside nav",
    "nav[aria-label*='Navigation']",
    "nav",
]

CONTENT_NOISE_SELECTORS = [
    "script",
    "style",
    "noscript",
    "wbr",
    "#leftColumn",
    "#navcolumn",
    "#searchbox",
    "#searchBox",
    "#breadcrumbs",
    ".breadcrumbs",
    ".breadcrumb",
    "nav.breadcrumbs",
    "#banner",
    "#bannerLeft",
    "#bannerRight",
    "#poweredBy",
    ".clear",
    "hr",
    "form[action*='search']",
    "button[aria-label*='Copy']",
    "button[title*='Copy']",
]

RAW_HTML_BLOCK_TAGS = {"table", "iframe", "video", "audio", "svg", "details"}
DOC_PAGE_EXTENSIONS = {"", ".html", ".htm"}
ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico",
    ".pdf", ".zip", ".gz", ".tgz", ".bz2", ".xz", ".jar", ".war", ".ear",
    ".tar", ".txt", ".csv", ".json", ".yaml", ".yml", ".xml", ".asc", ".sha1",
    ".sha256", ".sha512", ".md5", ".pom", ".apk", ".deb", ".rpm",
}

SKIP_URL_PATTERNS = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"/apidocs(?:/|$)",
        r"/api-release(?:/|$)",
        r"/api(?:/|$)",
        r"/testapidocs(?:/|$)",
        r"/xref(?:/|$)",
        r"/xref-test(?:/|$)",
        r"/jacoco(?:/|$)",
        r"/cobertura(?:/|$)",
        r"/surefire-report(?:\.html)?$",
        r"/checkstyle(?:-[^.]+)?\.html$",
        r"/pmd(?:-[^.]+)?\.html$",
        r"/cpd\.html$",
        r"/jdepend\.html$",
        r"/jxr(?:/|$)",
        r"/taglist(?:\.html)?$",
        r"/changes-report\.html$",
        r"/dependencies-report\.html$",
        r"/dependency-convergence\.html$",
        r"/plugin-management\.html$",
        r"/project-reports\.html$",
        r"/index-all\.html$",
        r"/allclasses(?:-index)?\.html$",
        r"/overview-tree\.html$",
        r"/deprecated-list\.html$",
        r"/serialized-form\.html$",
        r"/package-summary\.html$",
        r"/package-tree\.html$",
        r"/package-use\.html$",
        r"/class-use(?:/|$)",
    ]
]

INLINE_BREAK_PARENT_TAGS = {"p", "li", "td", "th", "span", "div", "a", "strong", "em"}
SKIP_TEXT_NORMALIZATION_TAGS = {"pre", "code", "textarea", "script", "style"}
SANITIZED_HTML_ATTRS = {"href", "src", "alt", "title", "colspan", "rowspan", "align", "width", "height", "name", "id"}
ZERO_WIDTH_RE = re.compile(r"[\u200b\u200c\u200d\ufeff]")
SOFT_SPACE_RE = re.compile(r"[\u00a0\u2007\u202f]")
MOJIBAKE_HINT_RE = re.compile(r"(?:ï¼|Ã.|Â.|â€|â€™|â€œ|â€”|â€“)")
CALL_OUT_KIND_MAP = {
    "note": "NOTE",
    "info": "NOTE",
    "tip": "TIP",
    "warning": "WARNING",
    "danger": "CAUTION",
    "caution": "CAUTION",
    "important": "IMPORTANT",
}


@dataclass
class NavNode:
    title: str
    href: Optional[str] = None
    children: List["NavNode"] = field(default_factory=list)
    kind: str = "link"  # link | category

    def to_dict(self, url_to_anchor: Dict[str, str], url_to_virtual_path: Dict[str, Path]) -> Dict[str, object]:
        payload: Dict[str, object] = {"title": self.title, "kind": self.kind}
        if self.href:
            payload["source_url"] = self.href
            if self.href in url_to_anchor:
                payload["anchor"] = url_to_anchor[self.href]
            if self.href in url_to_virtual_path:
                payload["virtual_path"] = url_to_virtual_path[self.href].as_posix()
        if self.children:
            payload["children"] = [child.to_dict(url_to_anchor, url_to_virtual_path) for child in self.children]
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


class MavenSiteConverter:
    def __init__(
        self,
        entry_url: str,
        out_dir: Path,
        delay: float = 0.15,
        max_pages: Optional[int] = None,
        save_html: bool = False,
        use_sitemap: bool = False,
        site_prefix_override: Optional[str] = None,
        combined_filename: str = "combined.md",
    ) -> None:
        self.entry_url = normalize_url(entry_url)
        self.entry_parts = urlsplit(self.entry_url)
        self.domain = self.entry_parts.netloc
        self.out_root = out_dir
        self.delay = delay
        self.max_pages = max_pages
        self.save_html = save_html
        self.use_sitemap = use_sitemap
        self.site_prefix_override = site_prefix_override
        self.combined_filename = combined_filename

        self.session = build_session()
        self.asset_cache: Dict[str, Path] = {}
        self.url_to_virtual_path: Dict[str, Path] = {}
        self.url_to_anchor: Dict[str, str] = {}
        self.url_alias_to_canonical: Dict[str, str] = {}
        self.pages: Dict[str, PageRecord] = {}
        self.nav_tree: List[NavNode] = []
        self.site_prefix: Optional[str] = None
        self.site_slug: Optional[str] = None
        self.site_dir: Optional[Path] = None
        self.combined_output_path: Optional[Path] = None
        self.entry_final_url: Optional[str] = None

    def run(self) -> None:
        print(f"\n=== {self.entry_url} ===")
        entry_html, entry_final_url = self.fetch_text(self.entry_url)
        self.entry_final_url = entry_final_url
        entry_soup = BeautifulSoup(entry_html, "html.parser")

        self.site_prefix = self.site_prefix_override or guess_site_prefix(entry_final_url, entry_soup)
        self.site_slug = build_site_slug(entry_final_url, self.site_prefix)
        self.site_dir = self.out_root / self.site_slug
        self.combined_output_path = self.site_dir / self.combined_filename
        assets_dir = self.site_dir / "assets"
        self.site_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)
        if self.save_html:
            (self.site_dir / "html_cache").mkdir(parents=True, exist_ok=True)

        print(f"site prefix: {self.site_prefix}")
        print(f"output dir : {self.site_dir}")
        print(f"single file: {self.combined_output_path.name}")

        self.crawl(entry_html=entry_html, entry_final_url=entry_final_url)
        self.assign_virtual_paths()
        self.assign_page_anchors()
        self.convert_pages_to_fragments()
        self.write_navigation_sidecars()
        self.write_combined_markdown()
        self.write_manifests()
        print(f"done: {len(self.pages)} pages, {len(self.asset_cache)} assets")

    # -------------------- Fetching --------------------
    def fetch_text(self, url: str) -> Tuple[str, str]:
        resp = self.session.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        if self.delay:
            time.sleep(self.delay)
        return decode_response_text(resp), normalize_url(resp.url)

    def fetch_binary(self, url: str) -> Tuple[bytes, str, Optional[str]]:
        resp = self.session.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        if self.delay:
            time.sleep(self.delay)
        content_type = resp.headers.get("content-type", "").split(";", 1)[0].strip()
        return resp.content, normalize_url(resp.url), content_type or None

    # -------------------- Crawl -----------------------
    def crawl(self, entry_html: str, entry_final_url: str) -> None:
        assert self.site_prefix is not None
        queue: deque[str] = deque([entry_final_url])
        if self.use_sitemap:
            seeds = self.discover_from_sitemap()
            for seed in sorted(seeds):
                if seed not in queue:
                    queue.append(seed)
        seen: Set[str] = set()

        while queue:
            url = queue.popleft()
            if url in seen:
                continue
            seen.add(url)

            if self.max_pages is not None and len(self.pages) >= self.max_pages:
                print("max-pages reached; stopping crawl")
                break

            try:
                if url == entry_final_url:
                    html_text = entry_html
                    final_url = entry_final_url
                else:
                    html_text, final_url = self.fetch_text(url)
            except Exception as exc:
                print(f"[warn] failed to fetch {url}: {exc}")
                continue

            soup = BeautifulSoup(html_text, "html.parser")
            content = select_content(soup)
            nav_root = select_nav(soup, current_domain=self.domain, base_url=final_url)
            title = extract_title(soup, content)
            nav_tree = extract_maven_nav_tree(nav_root, current_domain=self.domain, base_url=final_url, site_prefix=self.site_prefix)
            if not nav_tree and content is not None:
                nav_tree = extract_content_nav_tree(content, current_domain=self.domain, base_url=final_url, site_prefix=self.site_prefix)
            if nav_tree:
                merge_nav_lists(self.nav_tree, nav_tree)

            if content is None and not nav_tree:
                print(f"[skip] no content/nav in {final_url}")
                continue

            if final_url not in self.pages:
                self.pages[final_url] = PageRecord(
                    url=url,
                    final_url=final_url,
                    title=title,
                    html_text=html_text,
                    nav_tree=nav_tree,
                )
            self.url_alias_to_canonical[url] = final_url
            self.url_alias_to_canonical[final_url] = final_url
            print(f"[page] {final_url}")

            candidate_links = extract_candidate_links(
                soup=soup,
                current_domain=self.domain,
                site_prefix=self.site_prefix,
                base_url=final_url,
            )
            for link in sorted(candidate_links):
                if link not in seen:
                    queue.append(link)

    def discover_from_sitemap(self) -> Set[str]:
        assert self.site_prefix is not None
        site_root = f"{self.entry_parts.scheme}://{self.entry_parts.netloc}"
        sitemap_urls = [
            f"{site_root}/sitemap.xml",
            urljoin(site_root, self.site_prefix.lstrip("/") + "/sitemap.xml"),
        ]
        discovered: Set[str] = set()
        for sitemap_url in dedupe_preserve_order(sitemap_urls):
            try:
                xml_text, _ = self.fetch_text(sitemap_url)
            except Exception:
                continue
            locs = re.findall(r"<loc>(.*?)</loc>", xml_text, flags=re.IGNORECASE | re.DOTALL)
            for loc in locs:
                norm = normalize_url(html.unescape(loc.strip()))
                if self.is_allowed_page(norm):
                    discovered.add(norm)
        return discovered

    # ------------------- Filters ----------------------
    def is_allowed_page(self, url: str) -> bool:
        assert self.site_prefix is not None
        parts = urlsplit(url)
        if parts.netloc != self.domain:
            return False
        if not parts.path.startswith(self.site_prefix):
            return False
        if should_skip_path(parts.path):
            return False
        ext = Path(parts.path).suffix.lower()
        if ext not in DOC_PAGE_EXTENSIONS:
            return False
        return True

    # ------------------- Mapping ----------------------
    def assign_virtual_paths(self) -> None:
        assert self.site_prefix is not None
        taken: Set[Path] = set()
        for url, record in sorted(self.pages.items()):
            rel = url_to_rel_output(url, self.site_prefix)
            virtual_path = Path("docs") / rel
            virtual_path = uniquify_path(virtual_path, taken)
            taken.add(virtual_path)
            record.virtual_path = virtual_path
            self.url_to_virtual_path[url] = virtual_path
            if record.url:
                self.url_to_virtual_path[record.url] = virtual_path

    def assign_page_anchors(self) -> None:
        taken: Set[str] = set()
        for url, record in sorted(self.pages.items()):
            assert record.virtual_path is not None
            anchor = virtual_path_to_page_anchor(record.virtual_path)
            base_anchor = anchor
            counter = 2
            while anchor in taken:
                anchor = f"{base_anchor}-{counter}"
                counter += 1
            taken.add(anchor)
            record.page_anchor = anchor
            self.url_to_anchor[url] = anchor
            if record.url:
                self.url_to_anchor[record.url] = anchor

    # ---------------- Conversion ----------------------
    def convert_pages_to_fragments(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        for url, record in sorted(self.pages.items()):
            soup = BeautifulSoup(record.html_text, "html.parser")
            content = select_content(soup)
            if content is None:
                content = soup.body or soup

            content_html = BeautifulSoup(str(content), "html.parser")
            root = content_html.find() or content_html
            assert record.page_anchor is not None
            markdown_body = self.prepare_content(
                root=root,
                current_url=url,
                page_anchor=record.page_anchor,
                current_output=self.combined_output_path,
            )
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
    ) -> str:
        assert self.site_dir is not None
        placeholders: Dict[str, str] = {}
        idx = 0

        for comment in list(root.find_all(string=lambda text: isinstance(text, Comment))):
            comment.extract()

        for selector in CONTENT_NOISE_SELECTORS:
            for tag in list(root.select(selector)):
                tag.decompose()

        for anchor in list(root.find_all("a")):
            if anchor.get("name") and not anchor.get("id") and not anchor.get("href"):
                anchor["id"] = clean_anchor_name(anchor.get("name", ""))

        normalize_dom_text_nodes(root)
        replace_inline_breaks(root)

        unwrap_selector(root, ".source")
        unwrap_selector(root, ".code")

        for heading in list(root.find_all(re.compile(r"^h[1-6]$"))):
            heading_id = heading.get("id")
            if not heading_id:
                named_anchor = heading.find_previous_sibling("a")
                if isinstance(named_anchor, Tag) and named_anchor.get("id"):
                    heading_id = named_anchor.get("id")
            if heading_id:
                unique_id = compose_heading_anchor(page_anchor, heading_id)
                token = f"MAVEN2MDTOKEN{idx}END"
                idx += 1
                placeholders[token] = f'<a id="{html.escape(unique_id, quote=True)}"></a>\n\n'
                heading.insert_before(NavigableString(token))

        for img in list(root.find_all("img")):
            src = (img.get("src") or "").strip()
            if not src or src.startswith("data:"):
                continue
            abs_url = absolutize(current_url, src)
            try:
                local_path = self.download_asset(abs_url)
                rel = path_relative_to(current_output, self.site_dir / local_path)
                img["src"] = rel
                if img.has_attr("srcset"):
                    del img["srcset"]
            except Exception as exc:
                print(f"[warn] asset fetch failed {abs_url}: {exc}")

        for a in list(root.find_all("a", href=True)):
            href = (a.get("href") or "").strip()
            if not href or href.startswith("javascript:"):
                continue
            if href.startswith("#"):
                frag = clean_anchor_name(href[1:])
                a["href"] = "#" + (compose_heading_anchor(page_anchor, frag) if frag else page_anchor)
                continue

            abs_url, frag = split_and_normalize(current_url, href)
            if abs_url in self.url_to_anchor:
                target_anchor = self.url_to_anchor[abs_url]
                if frag:
                    target_anchor = compose_heading_anchor(target_anchor, frag)
                a["href"] = "#" + target_anchor
                continue

            if is_probably_asset(abs_url):
                try:
                    local_path = self.download_asset(abs_url)
                    target = self.site_dir / local_path
                    a["href"] = path_relative_to(current_output, target)
                    continue
                except Exception:
                    pass

            if self.is_allowed_page(abs_url):
                a["href"] = abs_url + (f"#{frag}" if frag else "")
                continue

            if urlsplit(abs_url).netloc == self.domain:
                a["href"] = abs_url + (f"#{frag}" if frag else "")

        complex_nodes: List[Tag] = []
        for tag in list(root.find_all(True)):
            if tag.name in RAW_HTML_BLOCK_TAGS:
                complex_nodes.append(tag)
                continue
            classes = {cls.lower() for cls in tag.get("class", [])}
            if tag.name == "pre" or (tag.name == "div" and ("source" in classes or "code" in classes) and tag.find("pre")):
                complex_nodes.append(tag)
                continue
            if classes & {"note", "info", "tip", "warning", "danger", "caution", "important"}:
                complex_nodes.append(tag)
                continue
            if tag.name == "blockquote" and len(clean_text(tag.get_text(" ", strip=True))) > 20:
                complex_nodes.append(tag)
                continue
            if tag.name == "code" and tag.parent and tag.parent.name == "pre":
                continue

        processed: Set[int] = set()
        for node in complex_nodes:
            if id(node) in processed:
                continue
            if any(id(parent) in processed for parent in node.parents if isinstance(parent, Tag)):
                continue
            token = f"MAVEN2MDTOKEN{idx}END"
            idx += 1
            placeholders[token] = render_complex_block(node)
            processed.add(id(node))
            node.replace_with(NavigableString(f"\n\n{token}\n\n"))

        html_text = str(root)
        markdown = md(html_text, heading_style="ATX", bullets="-", strong_em_symbol="*")
        for token, replacement in placeholders.items():
            markdown = markdown.replace(token, replacement)
        return markdown

    # ---------------- Assets --------------------------
    def download_asset(self, asset_url: str) -> Path:
        assert self.site_dir is not None
        asset_url = normalize_url(asset_url)
        if asset_url in self.asset_cache:
            return self.asset_cache[asset_url]

        payload, final_url, content_type = self.fetch_binary(asset_url)
        ext = extension_for_asset(final_url, content_type)
        stem = safe_stem(Path(urlsplit(final_url).path).stem or "asset")
        digest = hashlib.sha1(final_url.encode("utf-8")).hexdigest()[:16]
        subdir = "images" if (content_type or "").startswith("image/") else "files"
        rel_path = Path("assets") / subdir / f"{stem}_{digest}{ext}"
        abs_path = self.site_dir / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_bytes(payload)
        self.asset_cache[asset_url] = rel_path
        if final_url != asset_url:
            self.asset_cache[final_url] = rel_path
        return rel_path

    # ---------------- Navigation ----------------------
    def canonicalize_page_url(self, url: str) -> str:
        return self.url_alias_to_canonical.get(url, url)

    def effective_nav_tree(self) -> List[NavNode]:
        nav = prune_duplicate_nav(copy.deepcopy(self.nav_tree))
        if not nav:
            nav = build_url_tree(self.pages, self.url_to_virtual_path)

        nav_urls = {self.canonicalize_page_url(url) for url in flatten_nav_urls(nav)}
        missing_urls = [url for url in self.ordered_page_urls_from_nav(nav) if url not in nav_urls]
        if missing_urls:
            nav.append(NavNode(
                title="Other pages",
                children=[NavNode(title=self.pages[url].title, href=url, kind="link") for url in missing_urls],
                kind="category",
            ))
        return prune_duplicate_nav(nav)

    def ordered_page_urls(self) -> List[str]:
        return self.ordered_page_urls_from_nav(self.effective_nav_tree())

    def ordered_page_urls_from_nav(self, nav: List[NavNode]) -> List[str]:
        ordered: List[str] = []
        seen: Set[str] = set()
        for url in flatten_nav_urls(nav):
            canon = self.canonicalize_page_url(url)
            if canon in self.pages and canon not in seen:
                ordered.append(canon)
                seen.add(canon)
        for url in sorted(self.pages.keys(), key=lambda u: self.url_to_virtual_path.get(u, Path(u)).as_posix()):
            if url not in seen:
                ordered.append(url)
                seen.add(url)
        return ordered

    def write_navigation_sidecars(self) -> None:
        assert self.site_dir is not None
        nav = self.effective_nav_tree()
        payload = [node.to_dict(self.url_to_anchor, self.url_to_virtual_path) for node in nav]
        (self.site_dir / "navigation.yml").write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        (self.site_dir / "navigation.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def write_combined_markdown(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None
        nav = self.effective_nav_tree()
        ordered_urls = self.ordered_page_urls_from_nav(nav)
        site_title = derive_bundle_title(
            entry_url=self.entry_final_url or self.entry_url,
            entry_title=self.pages.get(self.entry_final_url or self.entry_url, PageRecord("", "", "", "")).title,
            site_slug=self.site_slug or "site",
        )

        parts: List[str] = []
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

        self.combined_output_path.write_text("".join(parts).rstrip() + "\n", encoding="utf-8")

    def write_manifests(self) -> None:
        assert self.site_dir is not None
        assert self.site_prefix is not None
        assert self.combined_output_path is not None
        manifest = {
            "entry_url": self.entry_url,
            "site_prefix": self.site_prefix,
            "site_slug": self.site_slug,
            "combined_markdown": self.combined_output_path.name,
            "page_count": len(self.pages),
            "asset_count": len(self.asset_cache),
            "pages": [
                {
                    "source_url": url,
                    "title": record.title,
                    "anchor": record.page_anchor,
                    "virtual_path": self.url_to_virtual_path[url].as_posix(),
                }
                for url, record in sorted(self.pages.items(), key=lambda item: self.url_to_virtual_path[item[0]].as_posix())
            ],
        }
        (self.site_dir / "site_manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
        )


# -------------------------- Helper functions --------------------------

def build_session() -> requests.Session:
    session = requests.Session()
    retries = Retry(
        total=5,
        connect=5,
        read=5,
        backoff_factor=1.0,
        allowed_methods=frozenset(["GET", "HEAD"]),
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retries, pool_connections=20, pool_maxsize=20)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": USER_AGENT})
    return session


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
            "utf-8",
            "utf-8-sig",
            "cp1252",
            "latin-1",
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


def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
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
        query="",
        fragment="",
    )
    return urlunsplit(clean)


def split_and_normalize(base_url: str, href: str) -> Tuple[str, str]:
    abs_url = absolutize(base_url, href)
    abs_url, frag = urldefrag(abs_url)
    return normalize_url(abs_url), clean_anchor_name(unquote(frag or ""))


def absolutize(base_url: str, href: str) -> str:
    return urljoin(base_url, href)


def clean_text(text: str) -> str:
    text = maybe_fix_mojibake(text or "")
    return re.sub(r"\s+", " ", text).strip()


def clean_anchor_name(text: str) -> str:
    text = normalize_unicode_text(unquote(text or "")).strip()
    text = text.replace(" ", "-")
    return re.sub(r"[^A-Za-z0-9._:-]+", "-", text).strip("-")


def dirname_prefix(path: str) -> str:
    if not path or path == "/":
        return "/"
    if path.endswith("/"):
        return path
    return path.rsplit("/", 1)[0] + "/"


def common_path_prefix(paths: Iterable[str]) -> str:
    split_paths: List[List[str]] = []
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


def normalize_site_prefix(prefix: str, entry_path: str) -> str:
    prefix = prefix or "/"
    if prefix.endswith((".html", ".htm")):
        prefix = dirname_prefix(prefix)
    if not prefix.startswith("/"):
        prefix = "/" + prefix
    if not prefix.endswith("/"):
        prefix += "/"
    if prefix == "//":
        prefix = "/"
    if prefix == "/" and entry_path not in {"", "/"}:
        # Keep root only for true root-level sites.
        if entry_path.count("/") > 1:
            prefix = dirname_prefix(entry_path)
    return prefix


def guess_site_prefix(entry_url: str, soup: BeautifulSoup) -> str:
    parts = urlsplit(entry_url)
    entry_path = parts.path or "/"
    nav_root = select_nav(soup, current_domain=parts.netloc, base_url=entry_url)
    candidates: List[str] = [entry_path]
    if nav_root is not None:
        for a in nav_root.select("a[href]"):
            href = (a.get("href") or "").strip()
            if not href or href.startswith("#"):
                continue
            abs_url = normalize_url(absolutize(entry_url, href))
            abs_parts = urlsplit(abs_url)
            if abs_parts.netloc != parts.netloc:
                continue
            if should_skip_path(abs_parts.path):
                continue
            candidates.append(abs_parts.path)
    if len(candidates) <= 1:
        content = select_content(soup)
        if content is not None:
            content_links = extract_candidate_links(soup, current_domain=parts.netloc, site_prefix="/", base_url=entry_url)
            for link in list(content_links)[:50]:
                candidates.append(urlsplit(link).path)
    prefix = common_path_prefix(candidates)
    prefix = normalize_site_prefix(prefix, entry_path)
    return prefix


def build_site_slug(entry_url: str, site_prefix: str) -> str:
    host = urlsplit(entry_url).netloc.split(".")[0]
    parts = [p for p in site_prefix.strip("/").split("/") if p]
    if parts:
        return slugify("_".join([host] + parts))
    return slugify(host)


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
    return site_slug.replace("_", " ").title() or urlsplit(entry_url).netloc


def score_content_candidate(node: Tag) -> int:
    text_len = len(node.get_text(" ", strip=True))
    score = text_len
    if node.get("id") == "bodyColumn":
        score += 5000
    if node.find(["h1", "h2"]):
        score += 500
    if node.find("table"):
        score += 100
    if node.select_one("#navcolumn, #leftColumn"):
        score -= 2000
    return score


def select_content(soup: BeautifulSoup) -> Optional[Tag]:
    best: Tuple[int, int, Optional[Tag]] = (-1, -1, None)
    for rank, selector in enumerate(CONTENT_SELECTORS):
        for node in soup.select(selector):
            score = score_content_candidate(node)
            if score > best[0] or (score == best[0] and -rank > best[1]):
                best = (score, -rank, node)
    return best[2]


def score_nav_candidate(node: Tag, current_domain: str, base_url: Optional[str]) -> int:
    links: List[str] = []
    for a in node.select("a[href]"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith("#"):
            continue
        abs_url = normalize_url(absolutize(base_url or ("https://" + current_domain), href))
        if urlsplit(abs_url).netloc != current_domain:
            continue
        if should_skip_path(urlsplit(abs_url).path):
            continue
        links.append(abs_url)
    score = len(set(links)) * 100 + len(node.find_all(["ul", "ol"])) * 10
    text = node.get_text(" ", strip=True).lower()
    if "on this page" in text:
        score -= 1000
    if node.get("id") == "navcolumn":
        score += 500
    return score


def select_nav(soup: BeautifulSoup, current_domain: str, base_url: Optional[str] = None) -> Optional[Tag]:
    candidates: List[Tuple[int, Tag]] = []
    seen: Set[int] = set()
    for selector in NAV_SELECTORS:
        for node in soup.select(selector):
            if id(node) in seen:
                continue
            seen.add(id(node))
            score = score_nav_candidate(node, current_domain=current_domain, base_url=base_url)
            if score > 0:
                candidates.append((score, node))
    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def extract_title(soup: BeautifulSoup, content: Optional[Tag]) -> str:
    if content is not None:
        for tag_name in ["h1", "h2", "h3"]:
            heading = content.find(tag_name)
            if heading is not None:
                text = clean_text(heading.get_text(" ", strip=True))
                if text:
                    return strip_site_title_suffix(text)
    if soup.title and soup.title.string:
        return strip_site_title_suffix(clean_text(soup.title.string))
    return "Untitled"


def strip_site_title_suffix(text: str) -> str:
    text = re.sub(r"\s*[\-|–—]\s*apache\b.*$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*[-|–—]\s*overview$", "", text, flags=re.IGNORECASE)
    return clean_text(text)


def is_heading_like(tag: Tag) -> bool:
    return tag.name in {"h1", "h2", "h3", "h4", "h5", "h6"}


def is_allowed_nav_link(url: str, current_domain: str, site_prefix: str) -> bool:
    parts = urlsplit(url)
    if parts.netloc != current_domain:
        return False
    if not parts.path.startswith(site_prefix):
        return False
    if should_skip_path(parts.path):
        return False
    return Path(parts.path).suffix.lower() in DOC_PAGE_EXTENSIONS


def extract_maven_nav_tree(nav_root: Optional[Tag], current_domain: str, base_url: Optional[str], site_prefix: str) -> List[NavNode]:
    if nav_root is None:
        return []

    nodes: List[NavNode] = []
    section_title: Optional[str] = None
    section_children: List[NavNode] = []

    def flush_section() -> None:
        nonlocal section_title, section_children, nodes
        if section_title or section_children:
            if section_title:
                nodes.append(NavNode(title=section_title, children=section_children, kind="category"))
            else:
                nodes.extend(section_children)
        section_title = None
        section_children = []

    for child in nav_root.children:
        if isinstance(child, NavigableString):
            continue
        if not isinstance(child, Tag):
            continue
        if child.name in {"script", "style"}:
            continue
        if is_heading_like(child):
            flush_section()
            section_title = clean_text(child.get_text(" ", strip=True))
            continue

        direct_list = child if child.name in {"ul", "ol"} else child.find(["ul", "ol"], recursive=False)
        if direct_list is not None:
            items = parse_nav_list(direct_list, current_domain=current_domain, base_url=base_url, site_prefix=site_prefix)
            if items:
                if section_title is not None:
                    section_children.extend(items)
                else:
                    nodes.extend(items)
                continue

        if child.name == "a" and child.get("href"):
            href = normalize_url(absolutize(base_url or ("https://" + current_domain), child["href"]))
            if is_allowed_nav_link(href, current_domain=current_domain, site_prefix=site_prefix):
                nodes.append(NavNode(title=clean_text(child.get_text(" ", strip=True)) or href, href=href, kind="link"))
                continue

    flush_section()

    if nodes:
        return dedupe_nav(nodes)

    lists = list(nav_root.find_all(["ul", "ol"]))
    if not lists:
        return []
    scored: List[Tuple[int, Tag]] = []
    for lst in lists:
        links = [
            normalize_url(absolutize(base_url or ("https://" + current_domain), a.get("href", "")))
            for a in lst.select("a[href]")
            if a.get("href")
        ]
        links = [u for u in links if is_allowed_nav_link(u, current_domain=current_domain, site_prefix=site_prefix)]
        scored.append((len(set(links)), lst))
    scored.sort(key=lambda item: item[0], reverse=True)
    if not scored or scored[0][0] == 0:
        return []
    return parse_nav_list(scored[0][1], current_domain=current_domain, base_url=base_url, site_prefix=site_prefix)


def extract_content_nav_tree(content: Tag, current_domain: str, base_url: Optional[str], site_prefix: str) -> List[NavNode]:
    list_candidates: List[Tuple[int, Tag]] = []
    for lst in content.find_all(["ul", "ol"], recursive=True):
        if lst.find_parent(["table", "nav"]) is not None:
            continue
        links = [
            normalize_url(absolutize(base_url or ("https://" + current_domain), a.get("href", "")))
            for a in lst.select("a[href]")
            if a.get("href")
        ]
        allowed = [u for u in links if is_allowed_nav_link(u, current_domain=current_domain, site_prefix=site_prefix)]
        if len(set(allowed)) >= 4:
            list_candidates.append((len(set(allowed)), lst))
    if not list_candidates:
        return []
    list_candidates.sort(key=lambda item: item[0], reverse=True)
    return parse_nav_list(list_candidates[0][1], current_domain=current_domain, base_url=base_url, site_prefix=site_prefix)


def parse_nav_list(ul: Tag, current_domain: str, base_url: Optional[str], site_prefix: str) -> List[NavNode]:
    nodes: List[NavNode] = []
    for li in ul.find_all("li", recursive=False):
        child_ul = li.find(["ul", "ol"], recursive=False)
        title, href = extract_nav_label(li, current_domain=current_domain, base_url=base_url, site_prefix=site_prefix)
        if child_ul is not None:
            children = parse_nav_list(child_ul, current_domain=current_domain, base_url=base_url, site_prefix=site_prefix)
            if title or children:
                nodes.append(NavNode(title=title or (children[0].title if children else "Section"), href=href, children=children, kind="category"))
        elif href and title:
            nodes.append(NavNode(title=title, href=href, kind="link"))
        elif title:
            nodes.append(NavNode(title=title, kind="category"))
    return dedupe_nav(nodes)


def extract_nav_label(li: Tag, current_domain: str, base_url: Optional[str], site_prefix: str) -> Tuple[Optional[str], Optional[str]]:
    title: Optional[str] = None
    href: Optional[str] = None
    for child in li.children:
        if isinstance(child, NavigableString):
            raw = clean_text(str(child))
            if raw and not title:
                title = raw
            continue
        if not isinstance(child, Tag):
            continue
        if child.name in {"ul", "ol"}:
            continue

        link = child if child.name == "a" else child.find("a", href=True)
        if link is not None:
            label = clean_text(link.get_text(" ", strip=True))
            if label and not title:
                title = label
            abs_url = normalize_url(absolutize(base_url or ("https://" + current_domain), link.get("href", "")))
            if is_allowed_nav_link(abs_url, current_domain=current_domain, site_prefix=site_prefix):
                href = abs_url
            if title and href:
                break

        if not title:
            label = clean_text(child.get_text(" ", strip=True))
            if label:
                title = label
    return title, href


def nav_key(node: NavNode) -> Tuple[str, str]:
    if node.href:
        return ("href", node.href.rstrip("/"))
    return ("title", node.title.lower())


def merge_nav_lists(dst: List[NavNode], src: List[NavNode]) -> None:
    index = {nav_key(node): node for node in dst}
    for src_node in src:
        key = nav_key(src_node)
        if key not in index:
            cloned = copy.deepcopy(src_node)
            dst.append(cloned)
            index[key] = cloned
            continue
        dst_node = index[key]
        if not dst_node.href and src_node.href:
            dst_node.href = src_node.href
        if src_node.children:
            merge_nav_lists(dst_node.children, src_node.children)


def dedupe_nav(nodes: List[NavNode]) -> List[NavNode]:
    out: List[NavNode] = []
    seen: Set[Tuple[str, str]] = set()
    for node in nodes:
        key = nav_key(node)
        if key in seen:
            continue
        seen.add(key)
        out.append(node)
    return out




def prune_duplicate_nav(nodes: List[NavNode], seen_urls: Optional[Set[str]] = None) -> List[NavNode]:
    seen = seen_urls if seen_urls is not None else set()
    out: List[NavNode] = []
    for node in nodes:
        if node.href:
            canon = node.href.rstrip("/")
            if canon in seen:
                continue
            seen.add(canon)
        children = prune_duplicate_nav(node.children, seen) if node.children else []
        cloned = NavNode(title=node.title, href=node.href, children=children, kind=node.kind)
        if cloned.href or cloned.children or cloned.kind == "category":
            if cloned.kind == "category" and not cloned.children and not cloned.href:
                continue
            out.append(cloned)
    return out


def flatten_nav_urls(nodes: List[NavNode]) -> List[str]:
    urls: List[str] = []
    for node in nodes:
        if node.href:
            urls.append(node.href)
        if node.children:
            urls.extend(flatten_nav_urls(node.children))
    return urls


def should_skip_path(path: str) -> bool:
    for pattern in SKIP_URL_PATTERNS:
        if pattern.search(path):
            return True
    return False


def extract_candidate_links(soup: BeautifulSoup, current_domain: str, site_prefix: str, base_url: Optional[str]) -> Set[str]:
    containers: List[Tag] = []
    nav_root = select_nav(soup, current_domain=current_domain, base_url=base_url)
    content = select_content(soup)
    if nav_root is not None:
        containers.append(nav_root)
    if content is not None:
        containers.append(content)
    if not containers and soup.body is not None:
        containers.append(soup.body)

    links: Set[str] = set()
    for container in containers:
        for a in container.select("a[href]"):
            href = (a.get("href") or "").strip()
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            abs_url = normalize_url(absolutize(base_url or ("https://" + current_domain), href))
            parts = urlsplit(abs_url)
            if parts.netloc != current_domain:
                continue
            if not parts.path.startswith(site_prefix):
                continue
            if should_skip_path(parts.path):
                continue
            ext = Path(parts.path).suffix.lower()
            if ext not in DOC_PAGE_EXTENSIONS:
                continue
            links.add(abs_url)
    return links


def url_to_rel_output(url: str, site_prefix: str) -> Path:
    path = urlsplit(url).path
    rel = path[len(site_prefix):] if path.startswith(site_prefix) else path.lstrip("/")
    rel = rel.lstrip("/")
    if not rel or rel.endswith("/"):
        rel = rel.rstrip("/")
        return Path(rel) / "index.md" if rel else Path("index.md")

    suffix = Path(rel).suffix.lower()
    if suffix in {".html", ".htm"}:
        rel = str(Path(rel).with_suffix(".md"))
    elif suffix:
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


def path_relative_to(current_output: Optional[Path], target: Path) -> str:
    if current_output is None:
        return target.as_posix()
    rel = os.path.relpath(target, start=current_output.parent)
    return Path(rel).as_posix()


def safe_stem(text: str) -> str:
    text = slugify(text).replace("_", "-")
    return text or "asset"


def extension_for_asset(final_url: str, content_type: Optional[str]) -> str:
    ext = Path(urlsplit(final_url).path).suffix
    if ext:
        return ext
    if content_type:
        guessed = mimetypes.guess_extension(content_type, strict=False)
        if guessed:
            return guessed
    return ".bin"


def is_probably_asset(url: str) -> bool:
    return Path(urlsplit(url).path).suffix.lower() in ASSET_EXTENSIONS


def clone_tag(node: Tag) -> Tag:
    soup = BeautifulSoup(str(node), "html.parser")
    cloned = soup.find()
    assert cloned is not None
    return cloned


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
        cleaned = normalize_unicode_text(maybe_fix_mojibake(original))
        if cleaned != original:
            node.replace_with(NavigableString(cleaned))


def has_block_descendants(parent: Tag) -> bool:
    for child in parent.find_all(True, recursive=False):
        if child.name in {"table", "ul", "ol", "dl", "pre", "code", "blockquote", "section", "article", "aside", "nav", "header", "footer", "div", "p"} and child.name != "br":
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


def unwrap_selector(root: Tag, selector: str) -> None:
    for tag in list(root.select(selector)):
        if tag.find(["pre", "table", "blockquote"]) is None:
            tag.unwrap()


def render_complex_block(node: Tag) -> str:
    classes = {cls.lower() for cls in node.get("class", [])}
    if node.name == "pre":
        return render_code_block(node)
    if node.name == "div" and ("source" in classes or "code" in classes) and node.find("pre") is not None:
        return render_code_block(node.find("pre"))
    if classes & {"note", "info", "tip", "warning", "danger", "caution", "important"}:
        return render_callout_block(node)
    if node.name == "blockquote":
        return render_blockquote(node)
    sanitize_raw_html_tree(node)
    return str(node)


def sanitize_raw_html_tree(root: Tag) -> None:
    for tag in root.find_all(True):
        attrs: Dict[str, object] = {}
        for key, value in list(tag.attrs.items()):
            if key in SANITIZED_HTML_ATTRS:
                attrs[key] = value
        tag.attrs = attrs


def render_blockquote(node: Tag) -> str:
    clone = clone_tag(node)
    sanitize_raw_html_tree(clone)
    body_md = md(str(clone), heading_style="ATX", bullets="-", strong_em_symbol="*")
    body_md = postprocess_markdown(body_md).strip()
    lines = ["> " + line if line else ">" for line in body_md.splitlines()]
    return "\n" + "\n".join(lines) + "\n"


def detect_callout_kind(node: Tag) -> str:
    classes = {cls.lower() for cls in node.get("class", [])}
    for key in ["important", "warning", "danger", "caution", "tip", "info", "note"]:
        if key in classes:
            return key
    text = clean_text(node.get_text(" ", strip=True)).lower()
    for key in ["important", "warning", "danger", "caution", "tip", "info", "note"]:
        if text.startswith(key + ":") or text.startswith(key + " "):
            return key
    return "note"


def render_callout_block(node: Tag) -> str:
    clone = clone_tag(node)
    kind = detect_callout_kind(clone)
    label = CALL_OUT_KIND_MAP.get(kind, "NOTE")

    title_text = ""
    title_candidate = None
    for child in clone.find_all(["strong", "b", "h3", "h4", "h5", "p"], recursive=False):
        text = clean_text(child.get_text(" ", strip=True))
        if text and len(text) <= 120:
            title_candidate = child
            title_text = text
            break
    if title_candidate is not None:
        title_candidate.decompose()

    sanitize_raw_html_tree(clone)
    body_md = md(str(clone), heading_style="ATX", bullets="-", strong_em_symbol="*")
    body_md = postprocess_markdown(body_md).strip()

    lines: List[str] = [f"> [!{label}]"]
    if title_text and title_text.lower() not in {kind, label.lower()}:
        lines.append(f"> **{title_text}**")
        if body_md:
            lines.append(">")
    if body_md:
        for line in body_md.splitlines():
            lines.append("> " + line if line else ">")
    return "\n" + "\n".join(lines) + "\n"


def render_code_block(pre: Tag) -> str:
    text, language = extract_preformatted_text(pre)
    text = text.replace("\r\n", "\n").rstrip("\n")
    fence = "```"
    while fence in text:
        fence += "`"
    return f"\n{fence}{language}\n{text}\n{fence}\n"


def detect_code_language(node: Optional[Tag]) -> str:
    if node is None:
        return ""
    classes = node.get("class", [])
    for cls in classes:
        if cls.startswith("language-"):
            return cls.split("language-", 1)[1]
        if cls.startswith("lang-"):
            return cls.split("lang-", 1)[1]
    return ""


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


def find_code_line_nodes(root: Tag) -> List[Tag]:
    selectors = [
        ".token-line", ".line", ".cl", "[class*=tokenLine]", "[class*=codeLine]",
        ".code-line", "[class*=lineContent]", "[class~=line]", "[class~=cl]", "[data-code-line]",
        'span[style*="display:block"]',
    ]
    for selector in selectors:
        matches = list(root.select(selector))
        if not matches:
            continue
        filtered = [
            node for node in matches
            if not any(isinstance(parent, Tag) and parent is not root and parent in matches for parent in node.parents)
        ]
        if filtered:
            return filtered
    direct_tag_children = [child for child in root.children if isinstance(child, Tag)]
    if direct_tag_children and not any(isinstance(child, NavigableString) and clean_text(str(child)) for child in root.children):
        if all(child.name in {"div", "p", "span"} for child in direct_tag_children):
            return direct_tag_children
    return []


def looks_like_command_output(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith(("error", "warning", "info", "[INFO]", "[ERROR]", "[WARN]")):
        return True
    if stripped.endswith(("%", ":")):
        return True
    if re.match(r"^[A-Za-z]:\\", stripped):
        return True
    if re.match(r"^/[^^\s]+", stripped):
        return True
    return False


def normalize_shell_fragments(parts: List[str]) -> str:
    prompt = parts[0]
    rest = [frag.strip() for frag in parts[1:] if frag.strip()]
    if not rest:
        return prompt
    merged = prompt.rstrip()
    for frag in rest:
        if merged.endswith(("=", ":", ",", "(", "[", "{", "/")):
            merged += frag
        elif frag.startswith(("=", ":", ",", ".", ")", "]", "}", "/", ";")):
            merged += frag
        else:
            merged += " " + frag
    return re.sub(r"\s+", " ", merged).strip()


def repair_shell_command_wrapping(text: str, language: str) -> str:
    shell_like = {"", "bash", "shell", "sh", "console", "terminal", "shell-session"}
    if language.lower() not in shell_like:
        return text
    blocks = text.split("\n\n")
    repaired_blocks: List[str] = []
    for block in blocks:
        lines = [line.rstrip() for line in block.split("\n")]
        if not lines:
            repaired_blocks.append(block)
            continue
        merged: List[str] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if re.match(r"^\s*[$#>]\s", line):
                parts = [line]
                j = i + 1
                while j < len(lines):
                    nxt = lines[j]
                    if not nxt.strip():
                        break
                    if re.match(r"^\s*[$#>]\s", nxt):
                        break
                    if looks_like_command_output(nxt) and len(parts) == 1:
                        break
                    parts.append(nxt)
                    j += 1
                merged.append(normalize_shell_fragments(parts))
                i = j
            else:
                merged.append(line)
                i += 1
        repaired_blocks.append("\n".join(merged))
    return "\n\n".join(repaired_blocks)


def extract_preformatted_text(pre: Tag) -> Tuple[str, str]:
    working = clone_tag(pre)
    for selector in [
        ".line-number", ".line-numbers-rows", "[class*=lineNumber]", "[class*=line-number]",
        "[class*=linenumber]", "[class*=codeLineNumber]", "[class*=gutter]",
    ]:
        for tag in list(working.select(selector)):
            tag.decompose()

    code = working.find("code")
    root = code or working
    language = detect_code_language(code) or detect_code_language(working)
    line_nodes = find_code_line_nodes(root)
    if line_nodes:
        lines = [extract_inline_text(line).rstrip("\n") for line in line_nodes]
        text = "\n".join(lines)
    else:
        text = extract_inline_text(root)

    text = normalize_unicode_text(maybe_fix_mojibake(text))
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = repair_shell_command_wrapping(text, language)
    return text.strip("\n"), language


def protect_fenced_code_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    placeholders: Dict[str, str] = {}
    pattern = re.compile(r"(?ms)^(?P<fence>`{3,})(?P<info>[^\n]*)\n.*?^\1[ \t]*$")
    def repl(match: re.Match[str]) -> str:
        token = f"MAVEN2MDCODETOKEN{len(placeholders)}END"
        placeholders[token] = match.group(0)
        return token
    return pattern.sub(repl, text), placeholders


def restore_placeholders(text: str, placeholders: Dict[str, str]) -> str:
    for token, block in placeholders.items():
        text = text.replace(token, block)
    return text


def collapse_accidental_hardbreaks(text: str) -> str:
    text = re.sub(r"(?<=\S) {2,}\n(?=(?:\[[^\]]+\]\([^)]+\)|<a\b|[A-Za-z0-9_(@`]))", " ", text)
    text = re.sub(r"(?<=,)\n(?=(?:\[[^\]]+\]\([^)]+\)|<a\b|[A-Za-z0-9_(@`]))", " ", text)
    return text


def postprocess_markdown(text: str) -> str:
    text = normalize_unicode_text(maybe_fix_mojibake(text))
    protected, placeholders = protect_fenced_code_blocks(text)
    protected = collapse_accidental_hardbreaks(protected)
    protected = re.sub(r"\n{3,}", "\n\n", protected)
    protected = re.sub(r"[ \t]+\n", "\n", protected)
    protected = re.sub(r"\n([*-] )\n", r"\n\1", protected)
    return restore_placeholders(protected, placeholders).strip() + "\n"


def starts_with_markdown_heading(text: str) -> bool:
    probe = text.lstrip()
    probe = re.sub(r'^(?:<a\s+id="[^"]+"></a>\s*)+', '', probe)
    probe = probe.lstrip()
    return bool(re.match(r'^#{1,6}\s+', probe))


def render_singlefile_navigation(nodes: List[NavNode], url_to_anchor: Dict[str, str], indent: int = 0) -> List[str]:
    lines: List[str] = []
    for node in nodes:
        prefix = "  " * indent + "- "
        if node.href and node.href in url_to_anchor:
            lines.append(f"{prefix}[{node.title}](#{url_to_anchor[node.href]})")
        elif node.href:
            lines.append(f"{prefix}{node.title} ({node.href})")
        else:
            lines.append(f"{prefix}{node.title}")
        if node.children:
            lines.extend(render_singlefile_navigation(node.children, url_to_anchor, indent + 1))
    return lines


def build_url_tree(pages: Dict[str, PageRecord], url_to_virtual_path: Dict[str, Path]) -> List[NavNode]:
    root = NavNode(title="root", kind="category")
    folder_nodes: Dict[Tuple[str, ...], NavNode] = {(): root}
    for url, record in sorted(pages.items(), key=lambda item: url_to_virtual_path[item[0]].as_posix()):
        rel = url_to_virtual_path[url]
        parts = list(rel.parts)
        folder_parts = tuple(parts[:-1])
        parent_key = ()
        for i in range(len(folder_parts)):
            key = tuple(folder_parts[: i + 1])
            if key not in folder_nodes:
                title = key[-1].replace("_", " ").replace("-", " ").title()
                node = NavNode(title=title, kind="category")
                folder_nodes[parent_key].children.append(node)
                folder_nodes[key] = node
            parent_key = key
        folder_nodes[parent_key].children.append(NavNode(title=record.title, href=url, kind="link"))
    return root.children


def load_targets(targets_file: Optional[Path], urls: Sequence[str]) -> List[str]:
    out = [normalize_url(u) for u in urls if u.strip()]
    if targets_file is not None:
        for line in targets_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(normalize_url(line))
    return dedupe_preserve_order(out)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Crawl Maven Site / project-info docs and convert them to one Markdown bundle per site.")
    parser.add_argument("urls", nargs="*", help="One or more entry URLs.")
    parser.add_argument("--targets-file", type=Path, help="Text file with one URL per line.")
    parser.add_argument("--out-dir", type=Path, default=Path("./converted_maven_docs"), help="Output directory (default: ./converted_maven_docs).")
    parser.add_argument("--delay", type=float, default=0.15, help="Delay between HTTP requests in seconds (default: 0.15).")
    parser.add_argument("--max-pages", type=int, default=None, help="Maximum number of pages per site.")
    parser.add_argument("--save-html", action="store_true", help="Save original HTML files for debugging.")
    parser.add_argument("--use-sitemap", action="store_true", help="Use sitemap.xml as extra crawl seeds when available.")
    parser.add_argument("--site-prefix", default=None, help="Override auto-detected site prefix for all targets, e.g. /proper/commons-cli/.")
    parser.add_argument("--combined-filename", default="combined.md", help="Name of the single combined Markdown file (default: combined.md).")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    targets = load_targets(args.targets_file, args.urls)
    if not targets:
        parser.error("Provide at least one URL or --targets-file.")

    out_dir: Path = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    for target in targets:
        converter = MavenSiteConverter(
            entry_url=target,
            out_dir=out_dir,
            delay=args.delay,
            max_pages=args.max_pages,
            save_html=args.save_html,
            use_sitemap=args.use_sitemap,
            site_prefix_override=args.site_prefix,
            combined_filename=args.combined_filename,
        )
        try:
            converter.run()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"[error] site failed {target}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

