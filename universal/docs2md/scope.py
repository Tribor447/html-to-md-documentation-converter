#documentation-site prefix detection and project scoping

from __future__ import annotations

from bs4 import BeautifulSoup
from bs4 import Tag
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from urllib.parse import unquote
from urllib.parse import urlsplit
import posixpath

from .constants import (
    DOC_LIKE_KEYWORDS,
    DOC_PAGE_EXTENSIONS,
)
from .html_analysis import (
    is_inside_global_chrome,
    link_visible_text,
    select_content_root,
    select_nav_root,
)
from .urls import (
    clamp_prefix_to_version_scope,
    common_path_prefix,
    ensure_trailing_slash,
    looks_versionish,
    path_similarity,
    query_looks_search_like,
    should_skip_crawl_url,
    slugify,
    split_and_normalize,
    spring_docs_scope_prefix_from_entry_url,
)


def prefix_from_doc_link_clusters(entry_path: str, candidate_links: List[str]) -> Optional[str]:



    if not candidate_links:
        return None

    counts: Dict[str, int] = {}
    path_samples: Dict[str, List[str]] = {}

    for url in candidate_links:
        path = urlsplit(url).path or "/"
        segs = [unquote(seg).lower() for seg in path.strip("/").split("/") if seg]
        if not segs:
            continue

        prefixes: List[str] = []
        first = segs[0]
        if first in DOC_LIKE_KEYWORDS or first in {"documentation", "manuals", "learn", "help"}:
            prefixes.append("/" + first + "/")
            if len(segs) > 1 and looks_versionish(segs[1]):
                prefixes.append("/" + first + "/" + segs[1] + "/")

       
        for i, seg in enumerate(segs[:3]):
            if seg in DOC_LIKE_KEYWORDS or seg in {"documentation", "manuals", "learn", "help"}:
                prefixes.append("/" + "/".join(segs[: i + 1]) + "/")
                if i + 1 < len(segs) and looks_versionish(segs[i + 1]):
                    prefixes.append("/" + "/".join(segs[: i + 2]) + "/")
                break

        for prefix in prefixes:
            counts[prefix] = counts.get(prefix, 0) + 1
            path_samples.setdefault(prefix, []).append(path)

    if not counts:
        return None

    best_prefix, best_count = max(counts.items(), key=lambda item: (item[1], len(item[0])))
    if best_count < 3:
        return None

   
   
    samples = path_samples.get(best_prefix, [])
    if len(samples) >= 3:
        common = common_path_prefix(samples)
        if common and common != "/" and common.startswith(best_prefix):
            return clamp_prefix_to_version_scope(entry_path, common)
    return clamp_prefix_to_version_scope(entry_path, best_prefix)


def broad_docs_prefix_from_nav(entry_url: str, nav_root: Optional[Tag]) -> Optional[str]:
    if nav_root is None or is_inside_global_chrome(nav_root):
        return None
    parts = urlsplit(entry_url)
    urls: List[str] = []
    for a in nav_root.select("a[href]"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        abs_url, _frag = split_and_normalize(entry_url, href)
        target = urlsplit(abs_url)
        if target.netloc != parts.netloc:
            continue
        if Path(target.path).suffix.lower() not in DOC_PAGE_EXTENSIONS:
            continue
        if query_looks_search_like(abs_url):
            continue
        if should_skip_crawl_url(abs_url, link_text=link_visible_text(a), profile="generic"):
            continue
        urls.append(abs_url)
    unique = sorted(set(urls))
    if len(unique) < 12:
        return None
    paths = [urlsplit(url).path for url in unique]
    common = common_path_prefix(paths + [parts.path or "/"])
    first_segments: Dict[str, int] = {}
    for path in paths:
        rel = path[len(common):].lstrip("/") if common != "/" and path.startswith(common) else path.lstrip("/")
        first = rel.split("/", 1)[0]
        if first:
            first_segments[first] = first_segments.get(first, 0) + 1
    if len(first_segments) < 2:
        return None
    largest = max(first_segments.values())
    if largest / max(len(unique), 1) > 0.86:
        return None
    if common == "/":
        return "/"
    return ensure_trailing_slash(common)


def apache_project_scope_prefix_from_entry_path(path: str, profile: str = "generic") -> Optional[str]:
    """Return a tight per-project prefix for Apache Maven/Commons-style sites.

    Apache Commons pages often live under /proper/<component>/ or
    /dormant/<component>/, while the site navigation and sitemap contain many
    sibling components.  If we let a broad nav/sidebar decide the prefix first,
    a single commons-email entry can expand to commons-bcel, commons-codec, etc.
    """
    segs = [unquote(seg) for seg in (path or "/").strip("/").split("/") if seg]
    if len(segs) >= 2 and segs[0].lower() in {"proper", "dormant", "sandbox"}:
        return "/" + "/".join(segs[:2]) + "/"

    leaf = segs[-1].lower() if segs else ""
    maven_report_leaves = {
        "project-info.html", "index.html", "summary.html",
        "dependencies.html", "dependency-info.html", "dependency-management.html",
        "dependency-convergence.html", "distribution-management.html",
        "issue-management.html", "mail-lists.html", "plugin-management.html",
        "plugins.html", "project-modules.html", "scm-usage.html",
        "source-repository.html", "team-list.html", "license.html", "licenses.html",
        "changes.html", "changes-report.html", "jira-changes.html", "rat-report.html",
        "checkstyle.html", "pmd.html", "cpd.html", "spotbugs.html", "japicmp.html",
    }
    if profile == "maven" and (leaf in maven_report_leaves or leaf.endswith("-report.html")):
        parent = posixpath.dirname(path or "/") or "/"
        return ensure_trailing_slash(parent)

    return None


def guess_site_prefix(entry_url: str, soup: BeautifulSoup, profile: str = "generic") -> str:
    parts = urlsplit(entry_url)
    path = parts.path or "/"

    spring_prefix = spring_docs_scope_prefix_from_entry_url(entry_url, profile=profile)
    if spring_prefix:
        return clamp_prefix_to_version_scope(path, spring_prefix)

    tight_project_prefix = apache_project_scope_prefix_from_entry_path(path, profile=profile)
    if tight_project_prefix:
        return clamp_prefix_to_version_scope(path, tight_project_prefix)

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
            if should_skip_crawl_url(abs_url, link_text=link_visible_text(a), profile=profile):
                continue
            candidate_links.append(abs_url)

   
   
    broad_nav_prefix = broad_docs_prefix_from_nav(entry_url, nav_root)
    path_segs_for_broad = [seg.lower() for seg in path.strip("/").split("/") if seg]
    broad_prefix_allowed = profile != "maven" and not (
        len(path_segs_for_broad) >= 2 and path_segs_for_broad[0] in {"proper", "dormant", "sandbox"}
    )
    if broad_nav_prefix and broad_prefix_allowed:
        return clamp_prefix_to_version_scope(path, broad_nav_prefix)

    cluster_prefix = prefix_from_doc_link_clusters(path, candidate_links)
    if cluster_prefix and (profile == "generic" or path == "/" or path.endswith("/index.html")):
        return cluster_prefix

   
   
   
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

