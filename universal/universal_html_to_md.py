#!/usr/bin/env python3
"""Convert scoped HTML documentation pages into Markdown."""
from __future__ import annotations

import argparse
import posixpath
from pathlib import Path
from urllib.parse import SplitResult, urljoin, urlsplit, urlunsplit, urldefrag

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

USER_AGENT = "Mozilla/5.0 (compatible; docs2md/0.2)"
DOC_EXTENSIONS = {"", ".html", ".htm", ".xhtml"}


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


def convert_page(url: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    root = soup.find("main") or soup.find("article") or soup.body or soup
    markdown = markdownify(str(root), heading_style="ATX")
    output = out_dir / "combined.md"
    output.write_text(markdown.strip() + "\n", encoding="utf-8")
    return output


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out-dir", type=Path, default=Path("converted_docs"))
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    print(convert_page(args.url, args.out_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
