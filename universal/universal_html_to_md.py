#!/usr/bin/env python3
"""Convert one HTML page into Markdown."""
from __future__ import annotations

import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

USER_AGENT = "Mozilla/5.0 (compatible; docs2md/0.1)"


def fetch_html(url: str) -> str:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding
    return response.text


def page_title(soup: BeautifulSoup) -> str:
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        return h1.get_text(" ", strip=True)
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "Documentation"


def convert_page(url: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    root = soup.find("main") or soup.find("article") or soup.body or soup
    markdown = markdownify(str(root), heading_style="ATX")
    output = out_dir / "combined.md"
    output.write_text(f"# {page_title(soup)}\n\n{markdown.strip()}\n", encoding="utf-8")
    return output


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out-dir", type=Path, default=Path("converted_docs"))
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    output = convert_page(args.url, args.out_dir)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
