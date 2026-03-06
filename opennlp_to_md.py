#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import markdownify as md

DEFAULT_URL = "https://opennlp.apache.org/docs/2.5.7/manual/opennlp.html"
FENCE_RE = re.compile(r"^(```+|~~~+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
HTML_HEADING_RE = re.compile(r"^h([1-6])$")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass(slots=True)
class HtmlHeading:
    level: int
    text: str
    html_ids: list[str]


@dataclass(slots=True)
class MarkdownHeading:
    level: int
    text: str
    line_index: int
    anchor_ids: list[str] = field(default_factory=list)

    @property
    def primary_id(self) -> str:
        return self.anchor_ids[0]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Apache OpenNLP documentation HTML to Markdown."
    )
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--html-file")
    parser.add_argument("--output", default="opennlp_manual.md")
    parser.add_argument("--timeout", type=int, default=60)
    return parser.parse_args()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def canonical_heading_key(value: str) -> str:
    value = html.unescape(value)
    value = normalize_space(value)
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return normalize_space(value)


def slugify(value: str) -> str:
    value = canonical_heading_key(value)
    value = value.replace(" ", "-")
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "section"


def is_same_document_link(href: str, base_url: str) -> tuple[bool, str | None]:
    parsed_href = urlparse(urljoin(base_url, href))
    parsed_base = urlparse(base_url)
    same_doc = (
        parsed_href.scheme == parsed_base.scheme
        and parsed_href.netloc == parsed_base.netloc
        and parsed_href.path.rstrip("/") == parsed_base.path.rstrip("/")
    )
    if same_doc and parsed_href.fragment:
        return True, unquote(parsed_href.fragment)
    return False, None


def download_html(url: str, timeout: int) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def read_html_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def absolutize_links(soup: BeautifulSoup, base_url: str) -> None:
    for tag in soup.find_all(href=True):
        href = str(tag.get("href") or "").strip()
        if not href:
            continue
        if href.startswith("#"):
            continue
        same_doc, fragment = is_same_document_link(href, base_url)
        if same_doc and fragment:
            tag["href"] = f"#{fragment}"
        else:
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


def find_heading_source_ids(tag: Tag) -> list[str]:
    ids: list[str] = []

    def add(value: str | None) -> None:
        if value and value not in ids:
            ids.append(value)

    add(tag.get("id"))
    add(tag.get("name"))

    for sibling in tag.previous_siblings:
        if isinstance(sibling, NavigableString):
            if sibling.strip():
                break
            continue
        if isinstance(sibling, Tag) and sibling.name == "a":
            add(sibling.get("id"))
            add(sibling.get("name"))
            continue
        break

    return ids


def extract_html_headings(html_text: str, base_url: str) -> list[HtmlHeading]:
    soup = BeautifulSoup(html_text, "lxml")
    remove_unwanted_elements(soup)
    absolutize_links(soup, base_url)
    root = pick_root(soup)

    headings: list[HtmlHeading] = []
    for tag in root.find_all(HTML_HEADING_RE):
        level = int(tag.name[1])
        text = normalize_space(tag.get_text(" ", strip=True))
        if not text:
            continue
        headings.append(HtmlHeading(level=level, text=text, html_ids=find_heading_source_ids(tag)))

    return headings


def parse_markdown_headings(markdown: str) -> list[MarkdownHeading]:
    lines = markdown.splitlines()
    headings: list[MarkdownHeading] = []
    in_fence = False
    fence_token = ""

    for index, raw_line in enumerate(lines):
        stripped = raw_line.strip()

        fence_match = FENCE_RE.match(stripped)
        if fence_match:
            token = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_token = token[0] * len(token)
            elif stripped.startswith(fence_token):
                in_fence = False
                fence_token = ""
            continue

        if in_fence:
            continue

        match = HEADING_RE.match(raw_line)
        if not match:
            continue

        level = len(match.group(1))
        text = match.group(2).strip()
        headings.append(MarkdownHeading(level=level, text=text, line_index=index))

    return headings


def align_html_ids_to_markdown(
    markdown_headings: list[MarkdownHeading],
    html_headings: list[HtmlHeading],
) -> dict[int, list[str]]:
    mapping: dict[int, list[str]] = {}
    html_keys = [canonical_heading_key(h.text) for h in html_headings]
    search_start = 0

    for md_index, heading in enumerate(markdown_headings):
        md_key = canonical_heading_key(heading.text)
        found_index = None

        for candidate_index in range(search_start, len(html_headings)):
            if html_keys[candidate_index] == md_key:
                found_index = candidate_index
                break

        if found_index is None:
            continue

        mapping[md_index] = list(html_headings[found_index].html_ids)
        search_start = found_index + 1

    return mapping


def assign_anchor_ids(
    headings: list[MarkdownHeading],
    html_ids_map: dict[int, list[str]],
) -> list[MarkdownHeading]:
    slug_counts: dict[str, int] = {}

    for index, heading in enumerate(headings):
        base_slug = slugify(heading.text)
        slug_counts[base_slug] = slug_counts.get(base_slug, 0) + 1
        slug = base_slug if slug_counts[base_slug] == 1 else f"{base_slug}-{slug_counts[base_slug]}"

        ids = [slug]
        for html_id in html_ids_map.get(index, []):
            if html_id not in ids:
                ids.append(html_id)
        heading.anchor_ids = ids

    return headings


def render_global_toc(headings: list[MarkdownHeading]) -> list[str]:
    lines = [
        '<a id="table-of-contents"></a>',
        "## Table of Contents",
        "",
    ]

    for heading in headings:
        indent = "  " * (heading.level - 1)
        lines.append(f"{indent}- [{heading.text}](#{heading.primary_id})")

    lines.append("")
    return lines


def rewrite_fragment_links_to_primary_ids(markdown: str, alias_to_primary: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()
        if not target.startswith("#"):
            return match.group(0)
        fragment = target[1:]
        primary = alias_to_primary.get(fragment, fragment)
        return f"[{label}](#{primary})"

    return MARKDOWN_LINK_RE.sub(repl, markdown)


def add_navigation_to_markdown(markdown: str, html_headings: list[HtmlHeading]) -> str:
    lines = markdown.splitlines()
    headings = parse_markdown_headings(markdown)
    html_ids_map = align_html_ids_to_markdown(headings, html_headings)
    headings = assign_anchor_ids(headings, html_ids_map)

    heading_by_line = {heading.line_index: heading for heading in headings}

    output: list[str] = ['<a id="top"></a>', ""]
    output.extend(render_global_toc(headings))

    for index, line in enumerate(lines):
        heading = heading_by_line.get(index)
        if heading is not None:
            for anchor_id in heading.anchor_ids:
                output.append(f'<a id="{anchor_id}"></a>')
        output.append(line)

    text = "\n".join(output)
    text = re.sub(r"\n{3,}", "\n\n", text)

    alias_to_primary: dict[str, str] = {}
    for heading in headings:
        for anchor_id in heading.anchor_ids:
            alias_to_primary.setdefault(anchor_id, heading.primary_id)

    return rewrite_fragment_links_to_primary_ids(text, alias_to_primary).strip() + "\n"


def main() -> int:
    args = parse_args()

    try:
        if args.html_file:
            html_text = read_html_file(args.html_file)
        else:
            html_text = download_html(args.url, args.timeout)

        markdown = html_to_markdown(html_text, args.url)
        html_headings = extract_html_headings(html_text, args.url)
        markdown = add_navigation_to_markdown(markdown, html_headings)
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
