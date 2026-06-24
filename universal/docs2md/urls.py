#URL normalization, language filtering, and crawl-scope rules

from __future__ import annotations

from bs4 import BeautifulSoup
from pathlib import Path
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from urllib.parse import SplitResult
from urllib.parse import parse_qsl
from urllib.parse import unquote
from urllib.parse import urldefrag
from urllib.parse import urlencode
from urllib.parse import urljoin
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
import posixpath
import re

from .constants import (
    ASSET_EXTENSIONS,
    DOC_LIKE_KEYWORDS,
    DOC_PAGE_EXTENSIONS,
    ENGLISH_LANGUAGE_CODES,
    KNOWN_LANGUAGE_CODES,
    LANGUAGE_QUERY_PARAMS,
    LANGUAGE_SEGMENT_RE,
    PREFERRED_LANGUAGE_DEFAULT,
    SEARCH_QUERY_PARAMS,
    SKIP_URL_PATTERNS,
    TRACKING_QUERY_PARAMS,
    TRACKING_QUERY_PREFIXES,
    VERSION_QUERY_PARAMS,
)
from .text import clean_text


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


def normalize_language_code(value: str) -> str:
    value = unquote(str(value or "")).strip().lower().replace("_", "-")
    value = value.split(".", 1)[0]
    value = re.sub(r"[^a-z0-9-]", "", value)
    return value


def preferred_language_key(value: Optional[str]) -> str:
    value = normalize_language_code(value or PREFERRED_LANGUAGE_DEFAULT)
    if value in {"", "any", "all", "none", "off"}:
        return "any"
    return value


def is_english_language_code(value: str) -> bool:
    value = normalize_language_code(value)
    return value in ENGLISH_LANGUAGE_CODES or value.startswith("en-")


def language_matches_preference(value: str, preferred: str) -> bool:
    preferred = preferred_language_key(preferred)
    if preferred == "any":
        return True
    value = normalize_language_code(value)
    if not value:
        return True
    if preferred == "en":
        return is_english_language_code(value)
    return value == preferred or value.startswith(preferred + "-")


def url_language_code(url: str) -> str:
    parts = urlsplit(url)
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        if key.lower() in LANGUAGE_QUERY_PARAMS:
            lang = normalize_language_code(value)
            if lang:
                return lang
    segments = [unquote(seg).strip() for seg in parts.path.split("/") if seg.strip()]
    for idx, seg in enumerate(segments[:5]):
        lang = normalize_language_code(seg)
        if not lang or not LANGUAGE_SEGMENT_RE.match(lang):
            continue
        base = lang.split("-", 1)[0]
        if lang not in KNOWN_LANGUAGE_CODES and base not in KNOWN_LANGUAGE_CODES:
            continue
        prev = normalize_language_code(segments[idx - 1]) if idx > 0 else ""
        next_seg = normalize_language_code(segments[idx + 1]) if idx + 1 < len(segments) else ""
        docish_prev = prev in DOC_LIKE_KEYWORDS or "doc" in prev or "manual" in prev or "guide" in prev
        near_docs_marker = idx == 0 or docish_prev
        looks_like_locale_prefix = (
            idx <= 3
            and not looks_versionish(prev)
            and (next_seg in DOC_LIKE_KEYWORDS or looks_versionish(next_seg) or (docish_prev and len(segments) > idx + 2))
        )
        if near_docs_marker or looks_like_locale_prefix:
            return lang
    return ""


def url_allowed_for_language(url: str, preferred_language: str) -> bool:
    preferred = preferred_language_key(preferred_language)
    if preferred == "any":
        return True
    lang = url_language_code(url)
    if not lang:
        return True
    return language_matches_preference(lang, preferred)


def soup_declared_language(soup: BeautifulSoup) -> str:
    html_tag = soup.find("html")
    if html_tag is not None:
        for attr in ("lang", "xml:lang"):
            value = html_tag.get(attr)
            if value:
                return normalize_language_code(str(value))
    for meta in soup.find_all("meta"):
        http_equiv = str(meta.get("http-equiv") or "").lower()
        name = str(meta.get("name") or meta.get("property") or "").lower()
        if http_equiv == "content-language" or name in {"language", "og:locale"}:
            content = str(meta.get("content") or "").split(",", 1)[0]
            lang = normalize_language_code(content)
            if lang:
                return lang
    return ""


def soup_allowed_for_language(soup: BeautifulSoup, preferred_language: str) -> bool:
    preferred = preferred_language_key(preferred_language)
    if preferred == "any":
        return True
    declared = soup_declared_language(soup)
    if not declared:
        return True
    return language_matches_preference(declared, preferred)


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


def url_with_fragment(url: str, fragment: str = "") -> str:

    url = normalize_url(url)
    fragment = unquote(fragment or "").strip()
    if not fragment:
        return url
    return f"{url}#{fragment}"


def split_stored_href(href: Optional[str]) -> Tuple[Optional[str], str]:



    if not href:
        return None, ""
    base, frag = urldefrag(str(href))
    if not base:
        return None, unquote(frag or "")
    return normalize_url(base), unquote(frag or "")


def nav_href_base(href: Optional[str]) -> Optional[str]:
    return split_stored_href(href)[0]


def url_equivalence_variants(url: str) -> Set[str]:



    base, _frag = urldefrag(url)
    try:
        normalized = normalize_url(base)
    except Exception:
        return {base} if base else set()

    parts = urlsplit(normalized)
    scheme, netloc, query = parts.scheme, parts.netloc, parts.query
    path = parts.path or "/"
    variants: Set[str] = set()

    def add(path_value: str) -> None:
        if not path_value.startswith("/"):
            path_value = "/" + path_value
        variants.add(urlunsplit(SplitResult(
            scheme=scheme, netloc=netloc, path=path_value or "/",
            query=query, fragment="",
        )))

    add(path)

    if path.endswith("/"):
        stripped = path.rstrip("/") or "/"
        add(stripped)
        if path != "/":
            add(path + "index.html")
            add(path + "index.htm")
    else:
        suffix = Path(path).suffix.lower()
        if path.endswith("/index.html") or path.endswith("/index.htm"):
            parent = path.rsplit("/", 1)[0] + "/"
            add(parent)
            add(parent.rstrip("/") or "/")
        elif suffix in {".html", ".htm"}:
            stem = path[: -len(suffix)]
            add(stem)
            add(stem + "/")
        elif suffix == "":
            add(path + "/")
            add(path + ".html")
            add(path + ".htm")
    

    return variants


def urls_equivalent(url_a: str, url_b: str) -> bool:
    if not url_a or not url_b:
        return False
    a_base, _ = split_stored_href(url_a)
    b_base, _ = split_stored_href(url_b)
    if not a_base or not b_base:
        return False
    return bool(url_equivalence_variants(a_base) & url_equivalence_variants(b_base))


def absolutize(base_url: str, href: str) -> str:
    return urljoin(base_url, href)


def repair_legacy_maven_javadoc_url(url: str, title: str = "") -> str:



    if not url:
        return url
    title_l = (title or "").casefold()
    if "javadoc" not in title_l and "javadocs" not in title_l:
        return url
    parts = urlsplit(url)
    path = parts.path
    if "/api-release/" not in path:
        return url
    fixed_path = path.replace("/api-release/", "/apidocs/")
    return urlunsplit(SplitResult(
        scheme=parts.scheme,
        netloc=parts.netloc,
        path=fixed_path,
        query=parts.query,
        fragment=parts.fragment,
    ))


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


RELEASE_NOTES_PATH_RE = re.compile(
    r"(?:^|/|[-_])(?:release[-_]?notes?|releasenotes|change[-_]?log|changelog|changes)(?:/|[-_.]|$)",
    re.I,
)


RELEASE_NOTES_TEXT_RE = re.compile(
    r"\b(?:release\s+notes?|releasenotes|change\s*log|changelog|changes)\b",
    re.I,
)


RELEASE_ARCHIVE_TEXT_RE = re.compile(
    r"\b(?:all\s+releases?|download(?:\s+apache)?(?:\s+[\w.®+-]+)?\s+releases?|releases?\s+archive)\b",
    re.I,
)


RELEASE_ARCHIVE_SEGMENTS = {"release", "releases", "download", "downloads"}


DOCISH_RELEASE_ESCAPE_SEGMENTS = {
    "docs", "doc", "documentation", "manual", "guide", "guides",
    "reference", "tutorial", "tutorials", "user-guide", "admin-guide",
}


JAVADOC_SCOPE_RE = re.compile(r"/(?:javadoc-api|api/java|apidocs|api-release)(?:/|$)", re.I)


JAVADOC_SKIP_PAGE_RE = re.compile(
    r"/(?:class-use(?:/|$)|allclasses(?:-index)?\.html$|index-all\.html$|"
    r"overview-tree\.html$|deprecated-list\.html$|serialized-form\.html$|"
    r"package-tree\.html$|package-use\.html$|help-doc\.html$|constant-values\.html$)",
    re.I,
)


MAVEN_REPORT_PAGE_RE = re.compile(
    r"/(?:changes|changes-report|jira-changes|rat-report|checkstyle|pmd|cpd|"
    r"spotbugs|findbugs|japicmp|clirr|taglist|surefire-report|failsafe-report|"
    r"jdepend|jdeps|junit-report|test-results|project-reports|"
    r"dependencies|dependency-convergence|dependency-info|dependency-management|"
    r"distribution-management|issue-management|license|licenses|mail-lists|"
    r"plugin-management|plugins|project-info|project-modules|scm-usage|"
    r"source-repository|team-list)\.html$",
    re.I,
)


def is_javadoc_url(url: str) -> bool:
    path = urlsplit(url).path or "/"
    return bool(JAVADOC_SCOPE_RE.search(path))


def is_release_archive_url(url: str, link_text: str = "") -> bool:
    parts = urlsplit(url)
    path = parts.path or "/"
    low_text = clean_text(link_text).casefold()
    if RELEASE_NOTES_PATH_RE.search(path) or RELEASE_NOTES_TEXT_RE.search(low_text):
        return True

    segments = [unquote(seg).strip().lower() for seg in path.split("/") if seg.strip()]
    release_indices = [
        idx for idx, seg in enumerate(segments)
        if seg in RELEASE_ARCHIVE_SEGMENTS or seg in {"release-notes", "releasenotes", "changelog"}
    ]
    if not release_indices and not RELEASE_ARCHIVE_TEXT_RE.search(low_text):
        return False

    for idx in release_indices:
        tail = set(segments[idx + 1:])
        if tail & DOCISH_RELEASE_ESCAPE_SEGMENTS:
            return False

    return True


def should_skip_crawl_url(
    url: str,
    link_text: str = "",
    profile: str = "generic",
    allow_javadoc: bool = False,
) -> bool:
    try:
        normalized = normalize_url(url)
    except Exception:
        normalized = url
    parts = urlsplit(normalized)
    path = parts.path or "/"

    if query_looks_search_like(normalized):
        return True
    if is_release_archive_url(normalized, link_text=link_text):
        return True

    javadoc = is_javadoc_url(normalized)
    if javadoc:
        if not allow_javadoc and profile != "javadoc":
            return True
        return bool(JAVADOC_SKIP_PAGE_RE.search(path))

    if MAVEN_REPORT_PAGE_RE.search(path):
        return profile == "maven"

    for pattern in SKIP_URL_PATTERNS:
        if not pattern.search(path):
            continue
        if MAVEN_REPORT_PAGE_RE.search(path) and profile != "maven":
            continue
        if path.endswith("/package-summary.html") and (allow_javadoc or profile == "javadoc"):
            continue
        return True

    return False


def spring_docs_scope_prefix_from_entry_url(entry_url: str, profile: str = "generic") -> Optional[str]:
    parts = urlsplit(entry_url)
    host = parts.netloc.lower()
    path = parts.path or "/"
    segs = [unquote(seg) for seg in path.strip("/").split("/") if seg]
    low = [seg.lower() for seg in segs]

    def prefix_through(index: int) -> str:
        return "/" + "/".join(segs[: index + 1]) + "/"

    if host == "projectreactor.io":
        if low[:4] == ["docs", "core", "release", "reference"]:
            return "/docs/core/release/reference/"
        if low and low[0] == "docs":
            for idx, seg in enumerate(low):
                if seg in {"reference", "api"}:
                    return prefix_through(idx)
            return "/docs/"

    if host.endswith("docs.micrometer.io"):
        if "reference" in low:
            return prefix_through(low.index("reference"))
        if segs:
            return "/" + segs[0] + "/"

    if host == "docs.spring.io":
        if is_javadoc_url(entry_url) or profile == "javadoc":
            for marker in ("javadoc-api", "api", "apidocs", "api-release"):
                if marker in low:
                    idx = low.index(marker)
                    if marker == "api" and idx + 1 < len(low) and low[idx + 1] == "java":
                        idx += 1
                    return prefix_through(idx)
        if "reference" in low:
            idx = low.index("reference")
            if idx + 1 < len(low) and low[idx + 1] in {"html", "htmlsingle"}:
                idx += 1
            return prefix_through(idx)
        if segs:
            return "/" + segs[0] + "/"

    return None


def javadoc_allowed_for_entry(entry_url: str, profile: str = "generic") -> bool:
    return profile == "javadoc" or is_javadoc_url(entry_url)

