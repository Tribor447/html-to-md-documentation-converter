#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

DEFAULT_URL = "https://opennlp.apache.org/docs/2.5.7/manual/opennlp.html"
FENCE_RE = re.compile(r"^(```+|~~~+)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
HTML_HEADING_RE = re.compile(r"^h([1-6])$")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^\)]+\)")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HTML_EMPTY_ANCHOR_RE = re.compile(r"<a\b[^>]*>\s*</a>", re.IGNORECASE)
HTML_TAG_RE = re.compile(r"<[^>]+>")


@dataclass(slots=True)
class HtmlHeading:
    level: int
    text: str
    html_ids: list[str]


@dataclass(slots=True)
class MarkdownHeading:
    level: int
    text: str
    raw_text: str
    line_index: int
    path: tuple[str, ...]
    anchor_ids: list[str] = field(default_factory=list)

    @property
    def primary_id(self) -> str:
        return self.anchor_ids[0]


class OpenNlpMarkdownConverter(MarkdownConverter):

    def convert_pre(self, el: Tag, text: str, parent_tags: Iterable[str]) -> str: 
        code = el.get_text("", strip=False).strip("\n")
        if not code:
            return "\n"
        return f"\n```\n{code}\n```\n\n"

    def convert_img(self, el: Tag, text: str, parent_tags: Iterable[str]) -> str:  
        src = (el.get("src") or "").strip()
        alt = normalize_space(el.get("alt") or "")
        if not src:
            return ""
        return f"![{alt}]({src})"

    def _cell_to_markdown(self, cell: Tag) -> str:
        inner_html = cell.decode_contents()
        markdown = self.convert(inner_html).strip()
        markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")
        markdown = re.sub(r"\n{3,}", "\n\n", markdown)
        markdown = re.sub(r"\n\s*\n", "<br><br>", markdown)
        markdown = re.sub(r"\s*\n\s*", "<br>", markdown)
        markdown = re.sub(r"\s+", " ", markdown).strip()
        markdown = markdown.replace("|", r"\|")
        return markdown

    def _expand_table(self, table: Tag) -> list[list[tuple[str, bool]]]:
        rows: list[list[tuple[str, bool]]] = []
        spans: dict[int, list[object]] = {}
        max_cols = 0

        def fill_pending(row: list[tuple[str, bool]], col: int) -> int:
            while col in spans:
                rows_left, value, is_header = spans[col]
                row.append((str(value), bool(is_header)))
                rows_left = int(rows_left) - 1
                if rows_left <= 0:
                    del spans[col]
                else:
                    spans[col] = [rows_left, value, is_header]
                col += 1
            return col

        for tr in table.find_all("tr"):
            row: list[tuple[str, bool]] = []
            col = fill_pending(row, 0)
            cells = tr.find_all(["th", "td"], recursive=False)
            for cell in cells:
                col = fill_pending(row, col)
                colspan = max(1, int(cell.get("colspan", 1) or 1))
                rowspan = max(1, int(cell.get("rowspan", 1) or 1))
                value = self._cell_to_markdown(cell)
                is_header = cell.name == "th"

                for offset in range(colspan):
                    row.append((value, is_header))
                    if rowspan > 1:
                        spans[col + offset] = [rowspan - 1, value, is_header]
                col += colspan

            fill_pending(row, col)
            rows.append(row)
            max_cols = max(max_cols, len(row))

        while spans:
            row = []
            col = 0
            while col in spans:
                rows_left, value, is_header = spans[col]
                row.append((str(value), bool(is_header)))
                rows_left = int(rows_left) - 1
                if rows_left <= 0:
                    del spans[col]
                else:
                    spans[col] = [rows_left, value, is_header]
                col += 1
            rows.append(row)
            max_cols = max(max_cols, len(row))

        normalized: list[list[tuple[str, bool]]] = []
        for row in rows:
            if len(row) < max_cols:
                row = row + [("", False)] * (max_cols - len(row))
            normalized.append(row)
        return normalized

    def convert_table(self, el: Tag, text: str, parent_tags: Iterable[str]) -> str: 
        grid = self._expand_table(el)
        if not grid:
            return "\n"

        has_header = bool(el.find("thead")) or any(is_header for _, is_header in grid[0])
        if has_header:
            header_row = [value for value, _ in grid[0]]
            data_rows = grid[1:]
        else:
            header_row = [f"Column {index + 1}" for index in range(len(grid[0]))]
            data_rows = grid

        lines = [
            "| " + " | ".join(header_row) + " |",
            "| " + " | ".join(["---"] * len(header_row)) + " |",
        ]
        for row in data_rows:
            lines.append("| " + " | ".join(value for value, _ in row) + " |")

        return "\n\n" + "\n".join(lines) + "\n\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Скачать HTML-документацию OpenNLP и сохранить её в Markdown "
            "с якорями и оглавлением."
        )
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"URL документации (по умолчанию: {DEFAULT_URL})",
    )
    parser.add_argument(
        "--html-file",
        help="Вместо скачивания прочитать HTML из локального файла",
    )
    parser.add_argument(
        "--output",
        default="opennlp_manual.md",
        help="Путь к итоговому .md файлу",
    )
    parser.add_argument(
        "--keep-toc",
        action="store_true",
        help="Не удалять исходное HTML-оглавление перед конвертацией",
    )
    parser.add_argument(
        "--no-global-toc",
        action="store_true",
        help="Не добавлять общее оглавление в начало Markdown-файла",
    )
    parser.add_argument(
        "--no-section-toc",
        action="store_true",
        help="Не добавлять локальные оглавления внутри глав",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Таймаут HTTP-запроса в секундах",
    )
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


def markdown_text_to_plain(value: str) -> str:
    value = HTML_EMPTY_ANCHOR_RE.sub("", value)
    value = MARKDOWN_IMAGE_RE.sub("", value)
    value = MARKDOWN_LINK_RE.sub(r"\1", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = HTML_TAG_RE.sub("", value)
    value = html.unescape(value)
    return normalize_space(value)


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
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; OpenNLPManualToMarkdown/2.1; "
            "+https://opennlp.apache.org/)"
        )
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    if not response.text.strip():
        raise ValueError("Сервер вернул пустой ответ")
    return response.text


def read_html_file(path: str | Path) -> str:
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


def remove_unwanted_elements(soup: BeautifulSoup, keep_toc: bool) -> None:
    for tag in soup(["script", "style", "noscript", "iframe", "form"]):
        tag.decompose()

    class_names_to_remove = {
        "navheader",
        "navfooter",
        "headerlink",
        "breadcrumbs",
    }
    if not keep_toc:
        class_names_to_remove.update({"toc", "lot", "list-of-tables"})

    for class_name in class_names_to_remove:
        for tag in soup.select(f".{class_name}"):
            tag.decompose()


def pick_root(soup: BeautifulSoup) -> Tag:
    selectors = [
        "div.book",
        "main",
        "article",
        "body",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node is not None:
            return node
    if soup.body is not None:
        return soup.body
    return soup  


def _append_id(ids: list[str], value: str | None) -> None:
    if not value:
        return
    value = str(value).strip()
    if value and value not in ids:
        ids.append(value)


def find_heading_source_ids(tag: Tag) -> list[str]:
    ids: list[str] = []

    _append_id(ids, tag.get("id"))
    _append_id(ids, tag.get("name"))

    for sibling in tag.previous_siblings:
        if isinstance(sibling, NavigableString):
            if sibling.strip():
                break
            continue
        if not isinstance(sibling, Tag):
            break
        if sibling.name == "a" and not normalize_space(sibling.get_text(" ", strip=True)):
            _append_id(ids, sibling.get("id"))
            _append_id(ids, sibling.get("name"))
            continue
        break

    for descendant in tag.find_all(attrs={"id": True}):
        _append_id(ids, descendant.get("id"))
    for descendant in tag.find_all(attrs={"name": True}):
        _append_id(ids, descendant.get("name"))

    for ancestor in tag.parents:
        if not isinstance(ancestor, Tag):
            continue
        if ancestor.name in {"html", "body"}:
            continue
        first_heading = ancestor.find(HTML_HEADING_RE)
        if first_heading is tag:
            _append_id(ids, ancestor.get("id"))
            _append_id(ids, ancestor.get("name"))

    return ids


def extract_html_headings(html_text: str, base_url: str, keep_toc: bool) -> list[HtmlHeading]:
    soup = BeautifulSoup(html_text, "lxml")
    remove_unwanted_elements(soup, keep_toc=keep_toc)
    absolutize_links(soup, base_url)
    root = pick_root(soup)

    headings: list[HtmlHeading] = []
    for tag in root.find_all(HTML_HEADING_RE):
        level_match = HTML_HEADING_RE.match(tag.name or "")
        if not level_match:
            continue
        raw_text = normalize_space(tag.get_text(" ", strip=True))
        text = markdown_text_to_plain(raw_text)
        if not text:
            continue
        headings.append(
            HtmlHeading(
                level=int(level_match.group(1)),
                text=text,
                html_ids=find_heading_source_ids(tag),
            )
        )
    return headings


def rewrite_same_page_links(markdown: str, base_url: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        same_doc, fragment = is_same_document_link(target, base_url)
        if same_doc and fragment:
            return f"[{label}](#{fragment})"
        return match.group(0)

    return MARKDOWN_LINK_RE.sub(repl, markdown)


def rewrite_fragment_links_to_primary_ids(markdown: str, alias_to_primary: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()
        if not target.startswith("#"):
            return match.group(0)
        fragment = unquote(target[1:])
        primary = alias_to_primary.get(fragment, fragment)
        return f"[{label}](#{primary})"

    return MARKDOWN_LINK_RE.sub(repl, markdown)


def postprocess_markdown(text: str, title: str | None, base_url: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = rewrite_same_page_links(text.strip(), base_url)

    if title:
        normalized_title = markdown_text_to_plain(title.strip())
        first_heading = None
        first_line = text.splitlines()[0] if text else ""
        if first_line.startswith("# "):
            first_heading = markdown_text_to_plain(first_line[2:].strip())
        if normalized_title and first_heading != normalized_title:
            text = f"# {normalized_title}\n\n{text}"
    return text.strip() + "\n"


def parse_markdown_headings(markdown: str) -> list[MarkdownHeading]:
    lines = markdown.splitlines()
    headings: list[MarkdownHeading] = []
    path_stack: list[str] = []
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
        raw_text = normalize_space(match.group(2))
        text = markdown_text_to_plain(raw_text)
        if not text:
            continue

        while len(path_stack) >= level:
            path_stack.pop()
        path_stack.append(text)
        headings.append(
            MarkdownHeading(
                level=level,
                text=text,
                raw_text=raw_text,
                line_index=index,
                path=tuple(path_stack),
            )
        )

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
        if not md_key:
            continue

        found_index: int | None = None
        upper_bound = min(len(html_headings), search_start + 120)
        for candidate_index in range(search_start, upper_bound):
            if html_keys[candidate_index] != md_key:
                continue
            if html_headings[candidate_index].level != heading.level:
                if found_index is None:
                    found_index = candidate_index
                continue
            found_index = candidate_index
            break

        if found_index is None:
            for candidate_index in range(search_start, len(html_headings)):
                if html_keys[candidate_index] == md_key:
                    found_index = candidate_index
                    break

        if found_index is None:
            continue

        if html_headings[found_index].html_ids:
            mapping[md_index] = list(html_headings[found_index].html_ids)
        search_start = found_index + 1

    return mapping


def fallback_aliases(path: tuple[str, ...]) -> list[str]:
    normalized_path = tuple(canonical_heading_key(item) for item in path)
    alias_map: dict[tuple[str, ...], list[str]] = {
        ("introduction", "command line interface cli"): ["intro.cli"],
        ("chapter 1 introduction", "command line interface cli"): ["intro.cli"],
        ("the command line interface",): ["tools.cli"],
        ("chapter 18 the command line interface",): ["tools.cli"],
        ("name finder",): ["tools.namefind"],
        ("document categorizer",): ["tools.doccat"],
        ("chunker", "chunker training"): ["tools.chunker.training"],
        ("chapter 9 chunker", "chunker training"): ["tools.chunker.training"],
        ("chunker", "chunker training", "training tool"): ["tools.chunker.training.tool"],
        ("chapter 9 chunker", "chunker training", "training tool"): ["tools.chunker.training.tool"],
        ("chunker", "chunker training", "training api"): ["tools.chunker.training.api"],
        ("chapter 9 chunker", "chunker training", "training api"): ["tools.chunker.training.api"],
    }
    return alias_map.get(normalized_path, [])


def assign_anchor_ids(
    headings: list[MarkdownHeading],
    html_ids_map: dict[int, list[str]] | None = None,
) -> list[MarkdownHeading]:
    slug_counts: dict[str, int] = {}
    html_ids_map = html_ids_map or {}

    for index, heading in enumerate(headings):
        base_slug = slugify(heading.text)
        slug_counts[base_slug] = slug_counts.get(base_slug, 0) + 1
        slug = base_slug if slug_counts[base_slug] == 1 else f"{base_slug}-{slug_counts[base_slug]}"

        ids: list[str] = [slug]
        for html_id in html_ids_map.get(index, []):
            if html_id not in ids:
                ids.append(html_id)
        for alias in fallback_aliases(heading.path):
            if alias not in ids:
                ids.append(alias)
        heading.anchor_ids = ids

    return headings


def render_anchor_tags(anchor_ids: list[str]) -> list[str]:
    return [f'<a id="{anchor_id}" name="{anchor_id}"></a>' for anchor_id in anchor_ids]


def render_global_toc(headings: list[MarkdownHeading], start_line: int) -> list[str]:
    toc_lines = [
        '<a id="table-of-contents" name="table-of-contents"></a>',
        '## Table of Contents',
        '',
    ]

    relevant = [heading for heading in headings if heading.line_index >= start_line and heading.level <= 4]
    for heading in relevant:
        indent = "   " * (heading.level - 1)
        bullet = "1." if heading.level == 1 else "-"
        toc_lines.append(f"{indent}{bullet} [{heading.text}](#{heading.primary_id})")

    toc_lines.append("")
    return toc_lines


def render_local_toc(chapter: MarkdownHeading, children: list[MarkdownHeading]) -> list[str]:
    if not children:
        return []

    toc_lines = ["**Contents**", ""]
    base_level = min(child.level for child in children)

    for child in children:
        indent = "  " * (child.level - base_level)
        toc_lines.append(f"{indent}- [{child.text}](#{child.primary_id})")

    toc_lines.append("")
    return toc_lines


def chapter_children(headings: list[MarkdownHeading], chapter_index: int) -> list[MarkdownHeading]:
    chapter = headings[chapter_index]
    children: list[MarkdownHeading] = []

    for next_index in range(chapter_index + 1, len(headings)):
        candidate = headings[next_index]
        if candidate.level <= chapter.level:
            break
        children.append(candidate)

    return children


def add_navigation_to_markdown(
    markdown: str,
    html_headings: list[HtmlHeading] | None = None,
    add_global_toc: bool = True,
    add_section_toc: bool = True,
) -> str:
    lines = markdown.splitlines()
    headings = parse_markdown_headings(markdown)
    html_ids_map = align_html_ids_to_markdown(headings, html_headings or [])
    headings = assign_anchor_ids(headings, html_ids_map=html_ids_map)

    heading_by_line = {heading.line_index: heading for heading in headings}
    global_toc_insert_at: int | None = None

    first_level_one_seen = False
    for heading in headings:
        if heading.level != 1:
            continue
        if not first_level_one_seen:
            first_level_one_seen = True
            continue
        global_toc_insert_at = heading.line_index
        break

    if global_toc_insert_at is None and headings:
        global_toc_insert_at = headings[0].line_index + 1

    chapter_local_toc: dict[int, list[str]] = {}
    if add_section_toc:
        for idx, heading in enumerate(headings):
            if heading.level != 1 or idx == 0:
                continue
            children = chapter_children(headings, idx)
            if children:
                chapter_local_toc[heading.line_index] = render_local_toc(heading, children)

    output: list[str] = ['<a id="top" name="top"></a>']
    if lines:
        output.append("")

    for line_index, line in enumerate(lines):
        if add_global_toc and global_toc_insert_at is not None and line_index == global_toc_insert_at:
            output.extend(render_global_toc(headings, start_line=global_toc_insert_at))

        heading = heading_by_line.get(line_index)
        if heading is None:
            output.append(line)
            continue

        output.extend(render_anchor_tags(heading.anchor_ids))
        output.append(line)

        local_toc_lines = chapter_local_toc.get(line_index)
        if local_toc_lines:
            output.append("")
            output.extend(local_toc_lines)

    text = "\n".join(output).rstrip() + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)

    alias_to_primary: dict[str, str] = {}
    for heading in headings:
        for anchor_id in heading.anchor_ids:
            alias_to_primary.setdefault(anchor_id, heading.primary_id)
    text = rewrite_fragment_links_to_primary_ids(text, alias_to_primary)
    return text


def html_to_markdown(
    html_text: str,
    base_url: str,
    keep_toc: bool,
    add_global_toc: bool,
    add_section_toc: bool,
) -> str:
    soup = BeautifulSoup(html_text, "lxml")
    title = soup.title.get_text(" ", strip=True) if soup.title else None

    remove_unwanted_elements(soup, keep_toc=keep_toc)
    absolutize_links(soup, base_url)
    root = pick_root(soup)

    converter = OpenNlpMarkdownConverter(
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
        strip=["span"],
    )
    markdown = converter.convert(str(root))
    markdown = postprocess_markdown(markdown, title, base_url)

    html_headings = extract_html_headings(html_text, base_url=base_url, keep_toc=keep_toc)
    markdown = add_navigation_to_markdown(
        markdown,
        html_headings=html_headings,
        add_global_toc=add_global_toc,
        add_section_toc=add_section_toc,
    )
    return markdown


def main() -> int:
    args = parse_args()
    output_path = Path(args.output)

    try:
        if args.html_file:
            html_text = read_html_file(args.html_file)
        else:
            html_text = download_html(args.url, args.timeout)
        markdown = html_to_markdown(
            html_text,
            base_url=args.url,
            keep_toc=args.keep_toc,
            add_global_toc=not args.no_global_toc,
            add_section_toc=not args.no_section_toc,
        )
    except requests.HTTPError as exc:
        print(f"HTTP error: {exc}", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  
        print(f"Conversion error: {exc}", file=sys.stderr)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Saved Markdown to: {output_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


