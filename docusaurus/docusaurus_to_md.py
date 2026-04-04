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
from typing import Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit, urldefrag, unquote

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import markdownify as md


USER_AGENT = "Mozilla/5.0 (compatible; DocusaurusToMarkdown/2.0)"
TIMEOUT = 30

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

RAW_HTML_BLOCK_TAGS = {"table", "iframe", "video", "audio", "svg", "details"}

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

VERSION_LIKE_RE = re.compile(
    r"^(?:latest|next|stable|main|master|current|v?\d+(?:\.\d+){0,3}(?:[-._][A-Za-z0-9]+)*)$",
    re.IGNORECASE,
)


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


class DocusaurusConverter:
    def __init__(
        self,
        entry_url: str,
        out_dir: Path,
        delay: float = 0.15,
        max_pages: Optional[int] = None,
        combined_filename: str = "combined.md",
    ) -> None:
        self.entry_url = normalize_url(entry_url)
        self.entry_parts = urlsplit(self.entry_url)
        self.domain = self.entry_parts.netloc
        self.out_root = out_dir
        self.delay = delay
        self.max_pages = max_pages
        self.combined_filename = combined_filename

        self.session = build_session()
        self.asset_cache: Dict[str, Path] = {}
        self.url_to_virtual_path: Dict[str, Path] = {}
        self.url_to_anchor: Dict[str, str] = {}
        self.url_alias_to_canonical: Dict[str, str] = {}
        self.pages: Dict[str, PageRecord] = {}
        self.sidebar_tree: List[NavNode] = []
        self.docs_prefix: Optional[str] = None
        self.site_slug: Optional[str] = None
        self.site_dir: Optional[Path] = None
        self.combined_output_path: Optional[Path] = None
        self.entry_final_url: Optional[str] = None

    def run(self) -> None:
        print(f"\n=== {self.entry_url} ===")
        entry_html, entry_final_url = self.fetch_text(self.entry_url)
        self.entry_final_url = entry_final_url
        entry_soup = BeautifulSoup(entry_html, "html.parser")

        self.docs_prefix = guess_docs_prefix(entry_final_url, entry_soup)
        self.site_slug = build_site_slug(entry_final_url, self.docs_prefix)
        self.site_dir = self.out_root / self.site_slug
        self.combined_output_path = self.site_dir / self.combined_filename

        assets_dir = self.site_dir / "assets"
        self.site_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)

        print(f"docs prefix : {self.docs_prefix}")
        print(f"output dir  : {self.site_dir}")
        print(f"single file : {self.combined_output_path.name}")

        self.crawl(entry_html=entry_html, entry_final_url=entry_final_url)
        self.assign_virtual_paths()
        self.assign_page_anchors()
        self.convert_pages_to_fragments()
        self.write_combined_markdown()
        print(f"done: {len(self.pages)} pages, {len(self.asset_cache)} assets")

    def fetch_text(self, url: str) -> Tuple[str, str]:
        resp = self.session.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        if self.delay:
            time.sleep(self.delay)
        if not resp.encoding:
            resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text, normalize_url(resp.url)

    def fetch_binary(self, url: str) -> Tuple[bytes, str, Optional[str]]:
        resp = self.session.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        if self.delay:
            time.sleep(self.delay)
        content_type = resp.headers.get("content-type", "").split(";", 1)[0].strip()
        return resp.content, normalize_url(resp.url), content_type or None

    def crawl(self, entry_html: str, entry_final_url: str) -> None:
        assert self.docs_prefix is not None

        queue: deque[str] = deque([entry_final_url])
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
            article = select_article(soup)
            sidebar = select_sidebar(soup, self.domain, base_url=final_url)
            title = extract_title(soup, article)
            sidebar_tree = extract_sidebar_tree(
                sidebar,
                current_domain=self.domain,
                base_url=final_url,
            )
            if sidebar_tree:
                merge_nav_lists(self.sidebar_tree, sidebar_tree)

            if article is None:
                main = soup.find("main")
                if main is None and not sidebar_tree:
                    print(f"[skip] no article/main/sidebar in {final_url}")
                    continue

            if final_url not in self.pages:
                self.pages[final_url] = PageRecord(
                    url=url,
                    final_url=final_url,
                    title=title,
                    html_text=html_text,
                    sidebar_tree=sidebar_tree,
                )

            self.url_alias_to_canonical[url] = final_url
            self.url_alias_to_canonical[final_url] = final_url
            print(f"[page] {final_url}")

            candidate_links = extract_candidate_links(
                soup=soup,
                domain=self.domain,
                docs_prefix=self.docs_prefix,
                base_url=final_url,
            )
            for link in sorted(candidate_links):
                if link not in seen:
                    queue.append(link)

    def assign_virtual_paths(self) -> None:
        assert self.docs_prefix is not None
        taken: Set[Path] = set()

        for url, record in sorted(self.pages.items()):
            rel = url_to_rel_output(url, self.docs_prefix)
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

    def convert_pages_to_fragments(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        for url, record in sorted(self.pages.items()):
            soup = BeautifulSoup(record.html_text, "html.parser")
            article = select_article(soup)
            if article is None:
                main = soup.find("main")
                article = main or soup.body or soup

            article = copy.copy(article)
            article = BeautifulSoup(str(article), "html.parser")
            root = article.find() or article

            assert record.page_anchor is not None
            self.prepare_content(
                root,
                current_url=url,
                page_anchor=record.page_anchor,
                current_output=self.combined_output_path,
            )

            markdown_body = html_fragment_to_markdown(root)
            markdown_body = postprocess_markdown(markdown_body)
            if not starts_with_markdown_heading(markdown_body):
                markdown_body = f"# {record.title}\n\n" + markdown_body.lstrip()
            record.markdown_body = markdown_body.strip() + "\n"

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

        for heading in list(root.find_all(re.compile(r"^h[1-6]$"))):
            heading_id = heading.get("id")
            for a in list(heading.select("a.hash-link")):
                a.decompose()
            if heading_id:
                unique_id = compose_heading_anchor(page_anchor, heading_id)
                token = f"DOC2MDPLACEHOLDERTOKEN{idx}END"
                idx += 1
                placeholders[token] = f'<a id="{unique_id}"></a>\n\n'
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
            href = a.get("href", "").strip()
            if not href or href.startswith("javascript:"):
                continue

            if href.startswith("#"):
                frag = href[1:]
                a["href"] = "#" + (
                    compose_heading_anchor(page_anchor, frag) if frag else page_anchor
                )
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
            classes = " ".join(tag.get("class", []))
            if "tabs-container" in classes or tag.get("role") == "tablist":
                complex_nodes.append(tag)
                continue
            if "admonition" in classes or "alert--" in classes:
                complex_nodes.append(tag)
                continue
            if tag.name == "pre":
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

    def canonicalize_page_url(self, url: str) -> str:
        return self.url_alias_to_canonical.get(url, url)

    def effective_nav_tree(self) -> List[NavNode]:
        nav = copy.deepcopy(self.sidebar_tree)
        if not nav:
            nav = build_url_tree(self.pages, self.url_to_virtual_path)
        return nav

    def ordered_page_urls(self) -> List[str]:
        nav = self.effective_nav_tree()
        ordered = []
        seen = set()
        for url in flatten_nav_urls(nav):
            canon = self.canonicalize_page_url(url)
            if canon in self.pages and canon not in seen:
                ordered.append(canon)
                seen.add(canon)
        for url in sorted(
            self.pages.keys(),
            key=lambda u: self.url_to_virtual_path.get(u, Path(u)).as_posix(),
        ):
            if url not in seen:
                ordered.append(url)
                seen.add(url)
        return ordered

    def write_combined_markdown(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        nav = self.effective_nav_tree()
        ordered_urls = self.ordered_page_urls()
        site_title = derive_bundle_title(
            entry_url=self.entry_final_url or self.entry_url,
            entry_title=self.pages.get(
                self.entry_final_url or self.entry_url,
                PageRecord("", "", "", "")
            ).title,
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
            body = record.markdown_body.strip()
            if not body:
                body = f"# {record.title}\n"

            parts.append(f'\n<a id="{record.page_anchor}"></a>\n')
            parts.append(f"\n<!-- source_url: {url} -->\n")
            parts.append(f"\n<!-- page_index: {index} -->\n\n")
            parts.append(body)
            parts.append("\n\n---\n")

        combined_text = "".join(parts).rstrip() + "\n"
        self.combined_output_path.write_text(combined_text, encoding="utf-8")

    def is_allowed_page(self, url: str) -> bool:
        assert self.docs_prefix is not None

        parts = urlsplit(url)
        if parts.netloc != self.domain:
            return False
        if not parts.path.startswith(self.docs_prefix):
            return False
        if parts.path.endswith("/search") or parts.path.endswith("/search/"):
            return False
        ext = Path(parts.path).suffix.lower()
        return ext in DOC_PAGE_EXTENSIONS


def build_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    return session


def normalize_url(url: str) -> str:
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
        query="",
        fragment="",
    )
    return urlunsplit(clean)


def split_and_normalize(base_url: str, href: str) -> Tuple[str, str]:
    abs_url = absolutize(base_url, href)
    abs_url, frag = urldefrag(abs_url)
    return normalize_url(abs_url), unquote(frag or "")


def absolutize(base_url: str, href: str) -> str:
    return urljoin(base_url, href)


def looks_versionish(segment: str) -> bool:
    return bool(VERSION_LIKE_RE.match(segment or ""))


def guess_docs_prefix(entry_url: str, soup: BeautifulSoup) -> str:
    parts = urlsplit(entry_url)
    path = parts.path or "/"
    sidebar = select_sidebar(soup, parts.netloc, base_url=entry_url)
    sidebar_links = []
    if sidebar is not None:
        sidebar_links = [
            normalize_url(absolutize(entry_url, a.get("href", "")))
            for a in sidebar.select("a[href]")
            if a.get("href") and not a.get("href", "").startswith("#")
        ]
        sidebar_links = [u for u in sidebar_links if urlsplit(u).netloc == parts.netloc]

    common = common_path_prefix([urlsplit(u).path for u in sidebar_links] + [path])
    if common and common not in {"/", path}:
        return ensure_trailing_slash(common)

    segs = [seg for seg in path.strip("/").split("/") if seg]
    if not segs:
        return "/"
    if segs[0] != "docs":
        return "/" + segs[0] + "/"

    if len(segs) >= 3 and looks_versionish(segs[2]):
        return f"/docs/{segs[1]}/{segs[2]}/"
    if len(segs) >= 2 and looks_versionish(segs[1]):
        return f"/docs/{segs[1]}/"
    return "/docs/"


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


def ensure_trailing_slash(path: str) -> str:
    return path if path.endswith("/") else path + "/"


def build_site_slug(entry_url: str, docs_prefix: str) -> str:
    host = urlsplit(entry_url).netloc.split(".")[0]
    parts = [p for p in docs_prefix.strip("/").split("/") if p and p != "docs"]
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
    host = urlsplit(entry_url).netloc
    return site_slug.replace("_", " ").title() or host


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


def select_sidebar(
    soup: BeautifulSoup,
    current_domain: str,
    base_url: Optional[str] = None,
) -> Optional[Tag]:
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
                abs_url = normalize_url(
                    absolutize(base_url or ("https://" + current_domain), href)
                )
                if urlsplit(abs_url).netloc != current_domain:
                    continue
                links.append(abs_url)
            unique_links = len(set(links))
            text = node.get_text(" ", strip=True).lower()
            if "on this page" in text and unique_links < 3:
                continue
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
        if h1:
            text = clean_text(h1.get_text(" ", strip=True))
            if text:
                return text
    if soup.title and soup.title.string:
        return clean_text(soup.title.string)
    return "Untitled"


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def extract_sidebar_tree(
    sidebar: Optional[Tag],
    current_domain: str,
    base_url: Optional[str] = None,
) -> List[NavNode]:
    if sidebar is None:
        return []

    ul_candidates = list(sidebar.find_all("ul"))
    if not ul_candidates:
        return []

    scored: List[Tuple[int, Tag]] = []
    for ul in ul_candidates:
        links = [
            normalize_url(
                absolutize(base_url or ("https://" + current_domain), a.get("href", ""))
            )
            for a in ul.select("a[href]")
            if a.get("href") and not a.get("href", "").startswith("#")
        ]
        links = [u for u in links if urlsplit(u).netloc == current_domain]
        scored.append((len(set(links)), ul))
    scored.sort(key=lambda item: item[0], reverse=True)
    root_ul = scored[0][1]
    return parse_nav_list(root_ul, current_domain=current_domain, base_url=base_url)


def parse_nav_list(
    ul: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> List[NavNode]:
    nodes: List[NavNode] = []
    for li in ul.find_all("li", recursive=False):
        child_ul = li.find("ul", recursive=False)
        title, href = extract_nav_label(
            li,
            current_domain=current_domain,
            base_url=base_url,
        )
        if child_ul is not None:
            children = parse_nav_list(
                child_ul,
                current_domain=current_domain,
                base_url=base_url,
            )
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


def extract_nav_label(
    li: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> Tuple[Optional[str], Optional[str]]:
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
                abs_url = normalize_url(
                    absolutize(base_url or ("https://" + current_domain), link["href"])
                )
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


def render_complex_block(node: Tag) -> str:
    if node.name == "pre":
        return render_code_block(node)
    return str(node)


def render_code_block(pre: Tag) -> str:
    code = pre.find("code")
    if code is not None:
        text = code.get_text("\n", strip=False)
        language = detect_code_language(code) or detect_code_language(pre)
    else:
        text = pre.get_text("\n", strip=False)
        language = detect_code_language(pre)

    text = text.replace("\r\n", "\n").rstrip("\n")
    fence = "```"
    while fence in text:
        fence += "`"
    return f"\n{fence}{language}\n{text}\n{fence}\n"


def detect_code_language(node: Tag) -> str:
    classes = node.get("class", [])
    for cls in classes:
        if cls.startswith("language-"):
            return cls.split("language-", 1)[1]
        if cls.startswith("lang-"):
            return cls.split("lang-", 1)[1]
    return ""


def html_fragment_to_markdown(root: Tag) -> str:
    return root.get_text("", strip=False)


def postprocess_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n([*-] )\n", r"\n\1", text)
    return text.strip() + "\n"


def starts_with_markdown_heading(text: str) -> bool:
    probe = text.lstrip()
    probe = re.sub(r'^(?:<a\s+id="[^"]+"></a>\s*)+', "", probe)
    probe = probe.lstrip()
    return bool(re.match(r"^#{1,6}\s+", probe))


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


def load_targets(targets_file: Optional[Path], urls: List[str]) -> List[str]:
    out = [normalize_url(u) for u in urls if u.strip()]
    if targets_file is not None:
        for line in targets_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(normalize_url(line))
    deduped = []
    seen = set()
    for item in out:
        if item not in seen:
            deduped.append(item)
            seen.add(item)
    return deduped


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawl Docusaurus docs and convert them into a single Markdown file per site."
    )
    parser.add_argument("urls", nargs="*", help="One or more docs entry URLs.")
    parser.add_argument(
        "--targets-file",
        type=Path,
        help="Text file with one URL per line.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("./converted_docs"),
        help="Output directory (default: ./converted_docs).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.15,
        help="Delay between HTTP requests in seconds (default: 0.15).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Maximum number of pages per site.",
    )
    parser.add_argument(
        "--combined-filename",
        default="combined.md",
        help="Name of the single combined Markdown file (default: combined.md).",
    )
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
        converter = DocusaurusConverter(
            entry_url=target,
            out_dir=out_dir,
            delay=args.delay,
            max_pages=args.max_pages,
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
