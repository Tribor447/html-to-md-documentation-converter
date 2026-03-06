#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md

DEFAULT_URL = "https://opennlp.apache.org/docs/2.5.7/manual/opennlp.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Apache OpenNLP documentation HTML to Markdown."
    )
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--html-file")
    parser.add_argument("--output", default="opennlp_manual.md")
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def download_html(url: str, timeout: int) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def read_html_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def absolutize_links(soup: BeautifulSoup, base_url: str) -> None:
    for tag in soup.find_all(href=True):
        href = str(tag.get("href") or "").strip()
        if not href or href.startswith("#"):
            continue
        tag["href"] = urljoin(base_url, href)

    for tag in soup.find_all(src=True):
        src = str(tag.get("src") or "").strip()
        if not src:
            continue
        tag["src"] = urljoin(base_url, src)


def remove_unwanted_elements(soup: BeautifulSoup) -> None:
    for tag in soup(["script", "style", "noscript", "iframe", "form"]):
        tag.decompose()

    for selector in [
        ".navheader",
        ".navfooter",
        ".headerlink",
        ".breadcrumbs",
        ".toc",
        ".lot",
        ".list-of-tables",
    ]:
        for tag in soup.select(selector):
            tag.decompose()


def pick_root(soup: BeautifulSoup) -> Tag:
    for selector in ["div.book", "main", "article", "body"]:
        node = soup.select_one(selector)
        if node is not None:
            return node
    return soup.body if soup.body is not None else soup  # type: ignore[return-value]


def html_to_markdown(html_text: str, base_url: str) -> str:
    soup = BeautifulSoup(html_text, "lxml")
    remove_unwanted_elements(soup)
    absolutize_links(soup, base_url)
    root = pick_root(soup)

    markdown = md(
        str(root),
        heading_style="ATX",
        bullets="-",
        strip=["span"],
    )

    markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    return markdown.strip() + "\n"


def main() -> int:
    args = parse_args()

    try:
        if args.html_file:
            html_text = read_html_file(args.html_file)
        else:
            html_text = download_html(args.url, args.timeout)

        markdown = html_to_markdown(html_text, args.url)
    except requests.RequestException as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Conversion error: {exc}", file=sys.stderr)
        return 1

    Path(args.output).write_text(markdown, encoding="utf-8")
    print(f"Saved to: {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
