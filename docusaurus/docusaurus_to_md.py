#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, List

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (compatible; DocusaurusToMarkdown/1.0)"


def fetch_text(url: str) -> str:
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=TIMEOUT)
    resp.raise_for_status()
    if not resp.encoding:
        resp.encoding = resp.apparent_encoding or "utf-8"
    return resp.text


def extract_article(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    if article is None:
        main = soup.find("main")
        if main is not None:
            article = main
        else:
            article = soup.body or soup
    return str(article)


def extract_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if h1 is not None:
        text = h1.get_text(" ", strip=True)
        if text:
            return text
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "Untitled"


def convert_to_markdown(html_fragment: str) -> str:
    return md(html_fragment, heading_style="ATX")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out", type=Path, default=Path("output.md"))
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    html = fetch_text(args.url)
    title = extract_title(html)
    article_html = extract_article(html)
    markdown = convert_to_markdown(article_html)

    result = f"# {title}\n\n" + markdown.strip() + "\n"
    args.out.write_text(result, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
