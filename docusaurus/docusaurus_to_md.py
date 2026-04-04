#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import mimetypes
import os
import posixpath
import re
import sys
import time
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlsplit, urlunsplit, urldefrag, unquote

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import markdownify as md

TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (compatible; DocusaurusToMarkdown/1.5)"

ARTICLE_SELECTORS = [
    "main article",
    "article.theme-doc-markdown",
    "article",
    "main [class*='docMarkdown']",
    "main [class*='markdown']",
    "main",
]

SIDEBAR_SELECTORS = [
    "aside[class*='docSidebar']",
    "aside.theme-doc-sidebar-container",
    "nav[aria-label*='Docs sidebar']",
    "aside nav.menu",
    "aside",
    "nav.menu",
]

NOISE_SELECTORS = [
    "script",
    "style",
    "noscript",
    "a.hash-link",
    "button[aria-label*='Copy']",
    "button[title*='Copy']",
    "button[class*='copyButton']",
    "button[class*='clean-btn']",
    "[class*='codeBlockContainer'] button",
    "[class*='breadcrumbs']",
    "nav[aria-label*='breadcrumb']",
    "nav.pagination-nav",
    "[class*='pagination-nav']",
    "[class*='theme-edit-this-page']",
    "[class*='editThisPage']",
    "[class*='lastUpdated']",
]

DOC_PAGE_EXTENSIONS = {"", ".html", ".htm"}
ASSET_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".bmp",
    ".ico",
    ".pdf",
    ".zip",
    ".gz",
    ".tgz",
    ".bz2",
    ".xz",
    ".jar",
    ".war",
    ".ear",
    ".tar",
    ".txt",
    ".csv",
    ".json",
    ".yaml",
    ".yml",
    ".xml",
}


@dataclass
class NavNode:
    title: str
    href: Optional[str] = None
    children: List["NavNode"] = field(default_factory=list)
    kind: str = "link"


@dataclass
class PageRecord:
    url: str
    final_url: str
    title: str
    html_text: str
    sidebar_tree: List[NavNode] = field(default_factory=list)
    virtual_path: Optional[Path] = None
    page_anchor: Optional[str] = None
    markdown_body: str = ""


def build_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    return session


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
    return urlunsplit(
        (
            (parts.scheme or "https").lower(),
            parts.netloc.lower(),
            norm,
            "",
            "",
        )
    )


def absolutize(base_url: str, href: str) -> str:
    return urljoin(base_url, href)


def split_and_normalize(base_url: str, href: str) -> Tuple[str, str]:
    abs_url = absolutize(base_url, href)
    abs_url, frag = urldefrag(abs_url)
    return normalize_url(abs_url), unquote(frag or "")


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


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


def compose_heading_anchor(page_anchor: str, fragment: str) -> str:
    return f"{page_anchor}--{slugify_anchor(fragment)}"


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


def select_article(soup: BeautifulSoup) -> Optional[Tag]:
    best: Tuple[int, int, Optional[Tag]] = (-1, -1, None)
    for rank, selector in enumerate(ARTICLE_SELECTORS):
        for node in soup.select(selector):
            score = len(node.get_text(" ", strip=True))
            if node.find(re.compile(r"^h[1-6]$")):
                score += 1000
            if score > best[0] or (score == best[0] and -rank > best[1]):
                best = (score, -rank, node)
    return best[2]


def select_sidebar(soup: BeautifulSoup, current_domain: str, base_url: Optional[str] = None) -> Optional[Tag]:
    candidates: List[Tuple[int, Tag]] = []
    seen: Set[int] = set()

    for selector in SIDEBAR_SELECTORS:
        for node in soup.select(selector):
            if id(node) in seen:
                continue
            seen.add(id(node))
            links = []
            for a in node.select("a[href]"):
                href = (a.get("href") or "").strip()
                if not href or href.startswith("#"):
                    continue
                abs_url = normalize_url(absolutize(base_url or ("https://" + current_domain), href))
                if urlsplit(abs_url).netloc != current_domain:
                    continue
                links.append(abs_url)
            unique_links = len(set(links))
            if unique_links:
                score = unique_links * 100 + len(node.find_all("ul"))
                candidates.append((score, node))

    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def extract_title(soup: BeautifulSoup, article: Optional[Tag]) -> str:
    if article is not None:
        h1 = article.find(re.compile(r"^h1$"))
        if h1 is not None:
            text = clean_text(h1.get_text(" ", strip=True))
            if text:
                return text
    if soup.title and soup.title.string:
        return clean_text(soup.title.string)
    return "Untitled"


def extract_nav_label(li: Tag, current_domain: str, base_url: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
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
        if child.name == "ul":
            continue

        link = child if child.name == "a" else child.find("a", href=True)
        if link is not None:
            label = clean_text(link.get_text(" ", strip=True))
            if label and not title:
                title = label
            if link.get("href"):
                abs_url = normalize_url(absolutize(base_url or ("https://" + current_domain), link["href"]))
                if urlsplit(abs_url).netloc == current_domain and not link["href"].startswith("#"):
                    href = abs_url
            if title and href:
                break

        if not title:
            for tag_name in ["button", "span", "div", "strong", "p"]:
                label_tag = child if child.name == tag_name else child.find(tag_name)
                if label_tag is not None:
                    label = clean_text(label_tag.get_text(" ", strip=True))
                    if label:
                        title = label
                        break

    return title, href


def parse_nav_list(ul: Tag, current_domain: str, base_url: Optional[str] = None) -> List[NavNode]:
    nodes: List[NavNode] = []
    for li in ul.find_all("li", recursive=False):
        child_ul = li.find("ul", recursive=False)
        title, href = extract_nav_label(li, current_domain=current_domain, base_url=base_url)
        if child_ul is not None:
            children = parse_nav_list(child_ul, current_domain=current_domain, base_url=base_url)
            if title or children:
                nodes.append(
                    NavNode(
                        title=title or (children[0].title if children else "Section"),
                        href=href,
                        children=children,
                        kind="category",
                    )
                )
        elif href and title:
            nodes.append(NavNode(title=title, href=href, kind="link"))
        elif title:
            nodes.append(NavNode(title=title, kind="category"))
    return dedupe_nav(nodes)


def extract_sidebar_tree(sidebar: Optional[Tag], current_domain: str, base_url: Optional[str] = None) -> List[NavNode]:
    if sidebar is None:
        return []

    ul_candidates = list(sidebar.find_all("ul"))
    if not ul_candidates:
        return []

    scored: List[Tuple[int, Tag]] = []
    for ul in ul_candidates:
        links = [
            normalize_url(absolutize(base_url or ("https://" + current_domain), a.get("href", "")))
            for a in ul.select("a[href]")
            if a.get("href") and not a.get("href", "").startswith("#")
        ]
        links = [u for u in links if urlsplit(u).netloc == current_domain]
        scored.append((len(set(links)), ul))

    scored.sort(key=lambda item: item[0], reverse=True)
    root_ul = scored[0][1]
    return parse_nav_list(root_ul, current_domain=current_domain, base_url=base_url)


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


def flatten_nav_urls(nodes: List[NavNode]) -> List[str]:
    urls: List[str] = []
    for node in nodes:
        if node.href:
            urls.append(node.href)
        if node.children:
            urls.extend(flatten_nav_urls(node.children))
    return urls


def extract_candidate_links(
    soup: BeautifulSoup,
    domain: str,
    docs_prefix: str,
    base_url: Optional[str] = None,
) -> Set[str]:
    containers: List[Tag] = []
    sidebar = select_sidebar(soup, domain, base_url=base_url)
    article = select_article(soup)
    if sidebar is not None:
        containers.append(sidebar)
    if article is not None:
        containers.append(article)
    for node in soup.select("nav.pagination-nav"):
        containers.append(node)
    if not containers:
        main = soup.find("main")
        if main is not None:
            containers.append(main)

    links: Set[str] = set()
    for container in containers:
        for a in container.select("a[href]"):
            href = (a.get("href") or "").strip()
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            abs_url = normalize_url(absolutize(base_url or ("https://" + domain), href))
            parts = urlsplit(abs_url)
            if parts.netloc != domain:
                continue
            if not parts.path.startswith(docs_prefix):
                continue
            ext = Path(parts.path).suffix.lower()
            if ext not in DOC_PAGE_EXTENSIONS:
                continue
            links.add(abs_url)
    return links


def common_path_prefix(paths: List[str]) -> str:
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


def guess_docs_prefix(entry_url: str, soup: BeautifulSoup) -> str:
    parts = urlsplit(entry_url)
    path = parts.path or "/"
    sidebar = select_sidebar(soup, parts.netloc, base_url=entry_url)
    sidebar_links: List[str] = []
    if sidebar is not None:
        sidebar_links = [
            normalize_url(absolutize(entry_url, a.get("href", "")))
            for a in sidebar.select("a[href]")
            if a.get("href") and not a.get("href", "").startswith("#")
        ]
        sidebar_links = [u for u in sidebar_links if urlsplit(u).netloc == parts.netloc]

    common = common_path_prefix([urlsplit(u).path for u in sidebar_links] + [path])
    if common and common not in {"/", path}:
        return common if common.endswith("/") else common + "/"

    segs = [seg for seg in path.strip("/").split("/") if seg]
    if not segs:
        return "/"
    if segs[0] == "docs":
        return "/docs/"
    return "/" + segs[0] + "/"


def url_to_rel_output(url: str, docs_prefix: str) -> Path:
    path = urlsplit(url).path
    rel = path[len(docs_prefix):] if path.startswith(docs_prefix) else path.lstrip("/")
    rel = rel.lstrip("/")

    if not rel or rel.endswith("/"):
        rel = rel.rstrip("/")
        if rel:
            return Path(rel) / "index.md"
        return Path("index.md")

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


def path_relative_to(current_output: Path, target: Path) -> str:
    rel = os.path.relpath(target, start=current_output.parent)
    return Path(rel).as_posix()


def fetch_text(session: requests.Session, url: str, delay: float) -> Tuple[str, str]:
    resp = session.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    if delay:
        time.sleep(delay)
    if not resp.encoding:
        resp.encoding = resp.apparent_encoding or "utf-8"
    return resp.text, normalize_url(resp.url)


def fetch_binary(session: requests.Session, url: str, delay: float) -> Tuple[bytes, str, Optional[str]]:
    resp = session.get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    if delay:
        time.sleep(delay)
    content_type = resp.headers.get("content-type", "").split(";", 1)[0].strip()
    return resp.content, normalize_url(resp.url), content_type or None


def assign_virtual_paths(pages: Dict[str, PageRecord], docs_prefix: str) -> Dict[str, Path]:
    taken: Set[Path] = set()
    out: Dict[str, Path] = {}
    for url, record in sorted(pages.items()):
        rel = url_to_rel_output(url, docs_prefix)
        virtual_path = Path("docs") / rel
        virtual_path = uniquify_path(virtual_path, taken)
        taken.add(virtual_path)
        record.virtual_path = virtual_path
        out[url] = virtual_path
        out[record.url] = virtual_path
    return out


def assign_page_anchors(pages: Dict[str, PageRecord]) -> Dict[str, str]:
    taken: Set[str] = set()
    out: Dict[str, str] = {}
    for url, record in sorted(pages.items()):
        assert record.virtual_path is not None
        anchor = virtual_path_to_page_anchor(record.virtual_path)
        base_anchor = anchor
        counter = 2
        while anchor in taken:
            anchor = f"{base_anchor}-{counter}"
            counter += 1
        taken.add(anchor)
        record.page_anchor = anchor
        out[url] = anchor
        out[record.url] = anchor
    return out


def download_asset(
    session: requests.Session,
    asset_cache: Dict[str, Path],
    asset_url: str,
    site_dir: Path,
    delay: float,
) -> Path:
    asset_url = normalize_url(asset_url)
    if asset_url in asset_cache:
        return asset_cache[asset_url]

    payload, final_url, content_type = fetch_binary(session, asset_url, delay)
    ext = extension_for_asset(final_url, content_type)
    stem = safe_stem(Path(urlsplit(final_url).path).stem or "asset")
    digest = hashlib.sha1(final_url.encode("utf-8")).hexdigest()[:16]
    subdir = "images" if (content_type or "").startswith("image/") else "files"
    rel_path = Path("assets") / subdir / f"{stem}_{digest}{ext}"
    abs_path = site_dir / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    abs_path.write_bytes(payload)

    asset_cache[asset_url] = rel_path
    if final_url != asset_url:
        asset_cache[final_url] = rel_path
    return rel_path


def render_code_block(pre: Tag) -> str:
    code = pre.find("code")
    if code is not None:
        text = code.get_text("\n", strip=False)
        language = ""
        for cls in code.get("class", []):
            if cls.startswith("language-"):
                language = cls.split("language-", 1)[1]
                break
    else:
        text = pre.get_text("\n", strip=False)
        language = ""

    text = text.replace("\r\n", "\n").rstrip("\n")
    fence = "```"
    while fence in text:
        fence += "`"
    return f"\n{fence}{language}\n{text}\n{fence}\n"


def render_complex_block(node: Tag) -> str:
    if node.name == "pre":
        return render_code_block(node)
    return str(node)


def postprocess_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip() + "\n"


def starts_with_markdown_heading(text: str) -> bool:
    probe = text.lstrip()
    probe = re.sub(r'^(?:<a\s+id="[^"]+"></a>\s*)+', "", probe)
    probe = probe.lstrip()
    return bool(re.match(r"^#{1,6}\s+", probe))


def prepare_content(
    root: Tag,
    current_url: str,
    page_anchor: str,
    combined_output_path: Path,
    site_dir: Path,
    session: requests.Session,
    delay: float,
    asset_cache: Dict[str, Path],
    url_to_anchor: Dict[str, str],
    domain: str,
    docs_prefix: str,
) -> str:
    placeholders: Dict[str, str] = {}
    idx = 0

    for selector in NOISE_SELECTORS:
        for tag in list(root.select(selector)):
            tag.decompose()

    for heading in list(root.find_all(re.compile(r"^h[1-6]$"))):
        heading_id = heading.get("id")
        for a in list(heading.select("a.hash-link")):
            a.decompose()
        if heading_id:
            unique_id = compose_heading_anchor(page_anchor, heading_id)
            token = f"DOC2MDTOKEN{idx}END"
            idx += 1
            placeholders[token] = f'<a id="{unique_id}"></a>\n\n'
            heading.insert_before(NavigableString(token))

    for img in list(root.find_all("img")):
        src = (img.get("src") or "").strip()
        if not src or src.startswith("data:"):
            continue
        abs_url = absolutize(current_url, src)
        try:
            local_path = download_asset(
                session=session,
                asset_cache=asset_cache,
                asset_url=abs_url,
                site_dir=site_dir,
                delay=delay,
            )
            img["src"] = path_relative_to(combined_output_path, site_dir / local_path)
            if img.has_attr("srcset"):
                del img["srcset"]
        except Exception:
            pass

    for a in list(root.find_all("a", href=True)):
        href = a.get("href", "").strip()
        if not href or href.startswith("javascript:"):
            continue

        if href.startswith("#"):
            frag = href[1:]
            a["href"] = "#" + (compose_heading_anchor(page_anchor, frag) if frag else page_anchor)
            continue

        abs_url, frag = split_and_normalize(current_url, href)

        if abs_url in url_to_anchor:
            target_anchor = url_to_anchor[abs_url]
            if frag:
                target_anchor = compose_heading_anchor(target_anchor, frag)
            a["href"] = "#" + target_anchor
            continue

        if is_probably_asset(abs_url):
            try:
                local_path = download_asset(
                    session=session,
                    asset_cache=asset_cache,
                    asset_url=abs_url,
                    site_dir=site_dir,
                    delay=delay,
                )
                a["href"] = path_relative_to(combined_output_path, site_dir / local_path)
                continue
            except Exception:
                pass

        parts = urlsplit(abs_url)
        if parts.netloc == domain and parts.path.startswith(docs_prefix):
            a["href"] = abs_url + (f"#{frag}" if frag else "")
            continue

        if parts.netloc == domain:
            a["href"] = abs_url + (f"#{frag}" if frag else "")

    complex_nodes: List[Tag] = []
    for tag in list(root.find_all(True)):
        if tag.name in {"table", "iframe", "video", "audio", "svg", "details", "pre"}:
            complex_nodes.append(tag)
            continue
        classes = " ".join(tag.get("class", []))
        if "tabs-container" in classes or tag.get("role") == "tablist":
            complex_nodes.append(tag)
            continue
        if "admonition" in classes or "alert--" in classes:
            complex_nodes.append(tag)
            continue

    processed: Set[int] = set()
    for node in complex_nodes:
        if id(node) in processed:
            continue
        if any(id(parent) in processed for parent in node.parents if isinstance(parent, Tag)):
            continue
        token = f"DOC2MDTOKEN{idx}END"
        idx += 1
        placeholders[token] = render_complex_block(node)
        processed.add(id(node))
        node.replace_with(NavigableString(f"\n\n{token}\n\n"))

    markdown = md(str(root), heading_style="ATX", bullets="-", strong_em_symbol="*")
    for token, replacement in placeholders.items():
        markdown = markdown.replace(token, replacement)

    markdown = postprocess_markdown(markdown)
    if not starts_with_markdown_heading(markdown):
        markdown = f"# {page_anchor}\n\n" + markdown.lstrip()
    return markdown


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
            lines.append(f"{prefix}{node.title} ({node.href})")
        else:
            lines.append(f"{prefix}{node.title}")
        if node.children:
            lines.extend(render_singlefile_navigation(node.children, url_to_anchor, indent + 1))
    return lines


def ordered_page_urls(pages: Dict[str, PageRecord], nav: List[NavNode]) -> List[str]:
    ordered: List[str] = []
    seen: Set[str] = set()

    for url in flatten_nav_urls(nav):
        if url in pages and url not in seen:
            ordered.append(url)
            seen.add(url)

    for url in sorted(pages.keys()):
        if url not in seen:
            ordered.append(url)
            seen.add(url)

    return ordered


def crawl_site(
    entry_url: str,
    out_dir: Path,
    delay: float,
    max_pages: Optional[int],
) -> None:
    session = build_session()
    entry_url = normalize_url(entry_url)

    entry_html, entry_final_url = fetch_text(session, entry_url, delay)
    entry_soup = BeautifulSoup(entry_html, "html.parser")

    docs_prefix = guess_docs_prefix(entry_final_url, entry_soup)
    domain = urlsplit(entry_final_url).netloc
    site_slug = slugify(domain.split(".")[0] + "_" + docs_prefix.strip("/").replace("/", "_"))
    site_dir = out_dir / site_slug
    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "assets" / "images").mkdir(parents=True, exist_ok=True)
    (site_dir / "assets" / "files").mkdir(parents=True, exist_ok=True)

    combined_output_path = site_dir / "combined.md"

    queue: deque[str] = deque([entry_final_url])
    seen: Set[str] = set()
    pages: Dict[str, PageRecord] = {}
    url_alias_to_canonical: Dict[str, str] = {}
    sidebar_tree: List[NavNode] = []
    asset_cache: Dict[str, Path] = {}

    while queue:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        if max_pages is not None and len(pages) >= max_pages:
            break

        try:
            if url == entry_final_url:
                html_text = entry_html
                final_url = entry_final_url
            else:
                html_text, final_url = fetch_text(session, url, delay)
        except Exception as exc:
            print(f"[warn] failed to fetch {url}: {exc}")
            continue

        soup = BeautifulSoup(html_text, "html.parser")
        article = select_article(soup)
        sidebar = select_sidebar(soup, domain, base_url=final_url)
        title = extract_title(soup, article)
        nav = extract_sidebar_tree(sidebar, current_domain=domain, base_url=final_url)
        if nav:
            merge_nav_lists(sidebar_tree, nav)

        pages[final_url] = PageRecord(
            url=url,
            final_url=final_url,
            title=title,
            html_text=html_text,
            sidebar_tree=nav,
        )
        url_alias_to_canonical[url] = final_url
        url_alias_to_canonical[final_url] = final_url

        for link in sorted(extract_candidate_links(soup, domain, docs_prefix, base_url=final_url)):
            if link not in seen:
                queue.append(link)

    url_to_virtual_path = assign_virtual_paths(pages, docs_prefix)
    url_to_anchor = assign_page_anchors(pages)

    for url, record in sorted(pages.items()):
        soup = BeautifulSoup(record.html_text, "html.parser")
        article = select_article(soup)
        if article is None:
            main = soup.find("main")
            article = main or soup.body or soup

        article_copy = BeautifulSoup(str(article), "html.parser")
        root = article_copy.find() or article_copy

        assert record.page_anchor is not None
        markdown_body = prepare_content(
            root=root,
            current_url=url,
            page_anchor=record.page_anchor,
            combined_output_path=combined_output_path,
            site_dir=site_dir,
            session=session,
            delay=delay,
            asset_cache=asset_cache,
            url_to_anchor=url_to_anchor,
            domain=domain,
            docs_prefix=docs_prefix,
        )
        if not starts_with_markdown_heading(markdown_body):
            markdown_body = f"# {record.title}\n\n" + markdown_body.lstrip()
        record.markdown_body = markdown_body.strip() + "\n"

    nav_lines = render_singlefile_navigation(sidebar_tree, url_to_anchor)
    ordered_urls = ordered_page_urls(pages, sidebar_tree)

    parts: List[str] = []
    parts.append(f"# {site_slug.replace('_', ' ').title()}\n\n")
    parts.append("## Navigation\n\n")
    if nav_lines:
        parts.append("\n".join(nav_lines) + "\n")
    else:
        parts.append("- No navigation extracted\n")
    parts.append("\n## Content\n")

    for index, url in enumerate(ordered_urls, start=1):
        record = pages[url]
        assert record.page_anchor is not None
        body = record.markdown_body.strip()
        if not body:
            body = f"# {record.title}\n"

        parts.append(f'\n<a id="{record.page_anchor}"></a>\n')
        parts.append(f"\n<!-- source_url: {url} -->\n")
        parts.append(f"\n<!-- page_index: {index} -->\n\n")
        parts.append(body)
        parts.append("\n\n---\n")

    combined_output_path.write_text("".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"done: {combined_output_path}")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawl Docusaurus docs and convert them into a single Markdown bundle."
    )
    parser.add_argument("url", help="Docs entry URL")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("./converted_docs"),
        help="Output directory",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.15,
        help="Delay between HTTP requests",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Maximum number of pages",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    try:
        crawl_site(
            entry_url=args.url,
            out_dir=args.out_dir,
            delay=args.delay,
            max_pages=args.max_pages,
        )
    except KeyboardInterrupt:
        raise
    except Exception as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
