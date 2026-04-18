#!/usr/bin/env python3
"""Convert scoped HTML documentation pages into Markdown."""
from __future__ import annotations

import argparse
import posixpath
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit, urldefrag

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

USER_AGENT = "Mozilla/5.0 (compatible; docs2md/0.2)"
DOC_EXTENSIONS = {"", ".html", ".htm", ".xhtml"}


@dataclass
class NavNode:
    title: str
    href: str | None = None
    children: list["NavNode"] = field(default_factory=list)



def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
    parts = urlsplit(url)
    path = parts.path or "/"
    keep_slash = path.endswith("/")
    path = posixpath.normpath(path)
    if not path.startswith("/"):
        path = "/" + path
    if keep_slash and not path.endswith("/"):
        path += "/"
    return urlunsplit(SplitResult((parts.scheme or "https").lower(), parts.netloc.lower(), path, parts.query, ""))


def same_site(url: str, root: str) -> bool:
    a = urlsplit(normalize_url(url))
    b = urlsplit(normalize_url(root))
    return a.netloc == b.netloc and a.path.startswith(b.path.rsplit("/", 1)[0] + "/")


def fetch_html(url: str) -> str:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    return response.text


def extract_links(soup: BeautifulSoup, base_url: str) -> list[str]:
    links: list[str] = []
    seen: set[str] = set()
    for anchor in soup.select("a[href]"):
        href = anchor.get("href", "").strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        url = normalize_url(urljoin(base_url, href))
        if Path(urlsplit(url).path).suffix.lower() not in DOC_EXTENSIONS:
            continue
        if same_site(url, base_url) and url not in seen:
            links.append(url)
            seen.add(url)
    return links


def extract_navigation(soup: BeautifulSoup, base_url: str) -> list[NavNode]:
    sidebar = soup.select_one("aside nav, nav[aria-label*=sidebar i], .sidebar, #navcolumn, #leftColumn")
    if sidebar is None:
        return []
    nodes: list[NavNode] = []
    seen: set[str] = set()
    for anchor in sidebar.select("a[href]"):
        title = anchor.get_text(" ", strip=True)
        href = anchor.get("href", "").strip()
        if not title or not href.startswith(("/", ".", "http")):
            continue
        target = normalize_url(urljoin(base_url, href))
        if target in seen:
            continue
        seen.add(target)
        nodes.append(NavNode(title=title, href=target))
    return nodes


def crawl(entry_url: str, max_pages: int = 50) -> list[tuple[str, BeautifulSoup]]:
    queue = deque([normalize_url(entry_url)])
    seen: set[str] = set()
    pages: list[tuple[str, BeautifulSoup]] = []
    while queue and len(pages) < max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        soup = BeautifulSoup(fetch_html(url), "html.parser")
        pages.append((url, soup))
        for link in extract_links(soup, url):
            if link not in seen:
                queue.append(link)
    return pages


def convert_page(url: str, out_dir: Path, max_pages: int = 50) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    pages = crawl(url, max_pages=max_pages)
    nav = extract_navigation(pages[0][1], pages[0][0]) if pages else []
    nav_md = "\n".join(f"- [{n.title}](#{i + 1})" for i, n in enumerate(nav))
    chunks = ["# Navigation", "", nav_md, "", "# Content"]
    for index, (page_url, soup) in enumerate(pages, start=1):
        root = soup.find("main") or soup.find("article") or soup.body or soup
        chunks.append(f"\n<a id=\"{index}\"></a>\n")
        chunks.append(markdownify(str(root), heading_style="ATX").strip())
    output = out_dir / "combined.md"
    output.write_text("\n".join(chunks).strip() + "\n", encoding="utf-8")
    return output


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out-dir", type=Path, default=Path("converted_docs"))
    parser.add_argument("--max-pages", type=int, default=50)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    print(convert_page(args.url, args.out_dir, max_pages=args.max_pages))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
