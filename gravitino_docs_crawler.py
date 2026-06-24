#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import mimetypes
import os
import re
import sys
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set, Tuple
from urllib.parse import urljoin, urlparse, urlunparse, urldefrag

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter


@dataclass
class Section:
    level: int
    title: str
    anchor: str


@dataclass
class Page:
    url: str
    title: str
    slug: str
    markdown: str
    order: int
    assets: List[str] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)


class BetterMarkdownConverter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags):
        code = el.get_text("", strip=False).rstrip("\n")
        language = ""

        classes = el.get("class", []) or []
        for cls in classes:
            if cls.startswith("language-"):
                language = cls.split("language-", 1)[1]
                break

        code_child = el.find("code")
        if code_child:
            classes = code_child.get("class", []) or []
            for cls in classes:
                if cls.startswith("language-"):
                    language = cls.split("language-", 1)[1]
                    break

        return f"\n```{language}\n{code}\n```\n"

    def convert_code(self, el, text, parent_tags):
        if el.parent and el.parent.name == "pre":
            return text
        return f"`{text}`"

    def convert_img(self, el, text, parent_tags):
        alt = el.get("alt", "")
        src = el.get("src", "")
        title = el.get("title")
        title_part = f' "{title}"' if title else ""
        return f"![{alt}]({src}{title_part})"

    def convert_a(self, el, text, parent_tags):
        href = el.get("href", "")
        label = text.strip() if text else href
        return f"[{label}]({href})"


def html_to_md(html: str) -> str:
    converter = BetterMarkdownConverter(
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    return converter.convert(html).strip()


def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return urlunparse((parsed.scheme, parsed.netloc, path, "", "", ""))


def with_trailing_slash(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path
    if not path.endswith("/"):
        path += "/"
    return urlunparse((parsed.scheme, parsed.netloc, path, "", "", ""))


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text, flags=re.UNICODE).strip("-")
    return text or "page"


def unique_slug(base: str, used: Set[str]) -> str:
    slug = base
    i = 2
    while slug in used:
        slug = f"{base}-{i}"
        i += 1
    used.add(slug)
    return slug


def discover_doc_prefix(start_url: str) -> str:
    parsed = urlparse(start_url)
    parts = [p for p in parsed.path.split("/") if p]

    if "docs" in parts:
        idx = parts.index("docs")
        if idx + 1 < len(parts) and re.fullmatch(r"\d+\.\d+\.\d+", parts[idx + 1]):
            prefix_parts = parts[: idx + 2]
        else:
            prefix_parts = parts[: idx + 1]
    else:
        prefix_parts = parts

    path = "/" + "/".join(prefix_parts) + "/"
    return urlunparse((parsed.scheme, parsed.netloc, path, "", "", ""))


def split_fragment(url: str) -> Tuple[str, str]:
    clean, frag = urldefrag(url)
    return normalize_url(clean), frag


def has_bad_scheme(url: str) -> bool:
    lower = url.strip().lower()
    return (
        lower.startswith("javascript:")
        or lower.startswith("mailto:")
        or lower.startswith("tel:")
        or lower.startswith("data:")
        or lower.startswith("blob:")
    )


def path_looks_like_html(path: str) -> bool:
    lower = path.lower()

    non_html_exts = (
        ".md", ".markdown", ".rst", ".txt",
        ".json", ".xml", ".yml", ".yaml", ".toml",
        ".pdf", ".zip", ".tgz", ".gz",
        ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico",
        ".css", ".js", ".map",
        ".woff", ".woff2", ".ttf", ".eot", ".otf",
        ".csv", ".tsv",
        ".mp4", ".mp3", ".wav", ".ogg", ".webm",
    )

    return not lower.endswith(non_html_exts)


class MultiPageDocsCrawler:
    def __init__(
        self,
        start_url: str,
        out_dir: Path,
        timeout: int = 30,
        exclude_api: bool = False,
    ):
        self.start_url = with_trailing_slash(start_url)
        self.doc_prefix = discover_doc_prefix(self.start_url)
        self.out_dir = out_dir
        self.images_dir = out_dir / "images"
        self.timeout = timeout
        self.exclude_api = exclude_api

        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "html-to-md-crawler/1.5",
                "Accept-Language": "en",
            }
        )

        self.pages: List[Page] = []
        self.url_to_page: Dict[str, Page] = {}
        self.used_slugs: Set[str] = set()

    def fetch(self, url: str) -> requests.Response:
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()

        if not response.encoding or response.encoding.lower() == "iso-8859-1":
            apparent = response.apparent_encoding
            response.encoding = apparent or "utf-8"

        return response

    def is_probably_doc_page(self, url: str) -> bool:
        if has_bad_scheme(url):
            return False

        parsed = urlparse(url)

        if parsed.scheme not in ("http", "https"):
            return False
        if not url.startswith(self.doc_prefix):
            return False
        if parsed.query:
            return False
        if not path_looks_like_html(parsed.path):
            return False

        lower = parsed.path.lower()

        if self.exclude_api:
            prefix_path = urlparse(self.doc_prefix).path.rstrip("/")
            banned_prefixes = [
                f"{prefix_path}/api/java/",
                f"{prefix_path}/api/python/",
                f"{prefix_path}/api/rest/",
                f"{prefix_path}/generated/",
                f"{prefix_path}/javadoc/",
            ]
            for p in banned_prefixes:
                if lower.startswith(p):
                    return False

        return True

    def extract_title(self, soup: BeautifulSoup) -> str:
        selectors = [
            "article h1",
            "main h1",
            ".theme-doc-markdown h1",
            "h1",
        ]
        for selector in selectors:
            node = soup.select_one(selector)
            if node:
                text = node.get_text(" ", strip=True)
                if text:
                    return text

        if soup.title:
            title = soup.title.get_text(" ", strip=True)
            if title:
                return title

        return "Untitled"

    def remove_heading_artifacts(self, container) -> None:
        for heading in container.select("h1, h2, h3, h4, h5, h6"):
            for bad in heading.select(
                "a.hash-link, a.anchor, a.header-anchor, a[aria-label], span.anchor, span.hash-link"
            ):
                bad.decompose()

            for child in list(heading.children):
                if getattr(child, "name", None) == "a":
                    classes = child.get("class", []) or []
                    aria = (child.get("aria-label") or "").lower()
                    href = child.get("href") or ""

                    if (
                        "hash-link" in classes
                        or "anchor" in classes
                        or "header-anchor" in classes
                        or aria
                        or href.startswith("#")
                    ):
                        child.decompose()

    def extract_main(self, soup: BeautifulSoup):
        selectors = [
            "article",
            "main article",
            "main .theme-doc-markdown",
            "main",
        ]
        main = None
        for selector in selectors:
            main = soup.select_one(selector)
            if main:
                break

        if main is None:
            raise RuntimeError("Cannot find main content container")

        removable = [
            "nav",
            "aside",
            "footer",
            "script",
            "style",
            ".theme-edit-this-page",
            ".pagination-nav",
            ".table-of-contents",
            ".theme-doc-toc-desktop",
            ".theme-doc-toc-mobile",
            ".breadcrumbs",
            ".theme-doc-version-banner",
            ".theme-doc-footer",
        ]

        for selector in removable:
            for node in main.select(selector):
                node.decompose()

        self.remove_heading_artifacts(main)
        return main

    def collect_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        result: List[str] = []
        seen: Set[str] = set()

        for a in soup.select("aside a, nav a, article a, main a"):
            href = a.get("href")
            if not href:
                continue

            href = href.strip()
            if not href or href.startswith("#") or has_bad_scheme(href):
                continue

            absolute = urljoin(current_url, href)
            absolute = normalize_url(absolute)

            if self.is_probably_doc_page(absolute) and absolute not in seen:
                seen.add(absolute)
                result.append(absolute)

        return result

    def local_image_path(self, image_url: str, content_type: str | None = None) -> Path:
        parsed = urlparse(image_url)
        ext = os.path.splitext(parsed.path)[1].lower()

        if not ext:
            guessed = None
            if content_type:
                guessed = mimetypes.guess_extension(content_type.split(";")[0].strip())
            ext = guessed or ".bin"

        if len(ext) > 8:
            ext = ".bin"

        digest = hashlib.sha1(image_url.encode("utf-8")).hexdigest()[:16]
        return self.images_dir / f"{digest}{ext}"

    def download_images_and_rewrite(self, container, page_url: str) -> List[str]:
        saved: List[str] = []

        for img in container.select("img[src]"):
            src = img.get("src", "").strip()
            if not src or has_bad_scheme(src):
                continue

            image_url = urljoin(page_url, src)
            parsed = urlparse(image_url)
            if parsed.scheme not in ("http", "https"):
                continue

            try:
                response = self.fetch(image_url)
            except Exception as e:
                print(f"[warn] failed to fetch image {image_url}: {e}", file=sys.stderr)
                continue

            content_type = response.headers.get("Content-Type", "")
            if content_type and not content_type.lower().startswith("image/"):
                continue

            local_path = self.local_image_path(image_url, content_type)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(response.content)

            relative = local_path.relative_to(self.out_dir).as_posix()
            img["src"] = relative
            saved.append(relative)

        return saved

    def rewrite_links(self, container, current_url: str) -> None:
        for a in container.select("a[href]"):
            href = a.get("href", "").strip()
            if not href or has_bad_scheme(href):
                continue

            absolute = urljoin(current_url, href)
            absolute_no_frag, frag = split_fragment(absolute)

            if absolute_no_frag == normalize_url(current_url):
                a["href"] = f"#{frag}" if frag else "#"
                continue

            if self.is_probably_doc_page(absolute_no_frag):
                a["href"] = absolute_no_frag + (f"#{frag}" if frag else "")

    def extract_sections(self, container, page_slug: str) -> List[Section]:
        sections: List[Section] = []
        used_local: Set[str] = set()

        for heading in container.select("h2, h3"):
            title = heading.get_text(" ", strip=True)
            if not title:
                continue

            level = int(heading.name[1])
            base = f"page-{page_slug}-{slugify(title)}"
            anchor = base
            i = 2
            while anchor in used_local:
                anchor = f"{base}-{i}"
                i += 1
            used_local.add(anchor)

            sections.append(Section(level=level, title=title, anchor=anchor))

        return sections

    def inject_section_anchors_into_markdown(self, markdown: str, sections: List[Section]) -> str:
        lines = markdown.splitlines()
        result: List[str] = []
        section_index = 0

        for line in lines:
            stripped = line.strip()

            if section_index < len(sections):
                sec = sections[section_index]
                expected_prefix = "#" * sec.level + " "
                if stripped == expected_prefix + sec.title:
                    result.append(f'<a id="{sec.anchor}"></a>')
                    result.append(line)
                    section_index += 1
                    continue

            result.append(line)

        return "\n".join(result)

    def crawl(self) -> None:
        queue = deque([normalize_url(self.start_url)])
        visited: Set[str] = set()

        while queue:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)

            try:
                response = self.fetch(url)
            except Exception as e:
                print(f"[warn] failed to fetch {url}: {e}", file=sys.stderr)
                continue

            content_type = response.headers.get("Content-Type", "").lower()
            if content_type and "html" not in content_type:
                continue

            soup = BeautifulSoup(response.text, "lxml")

            try:
                title = self.extract_title(soup)
                main = self.extract_main(soup)
            except Exception as e:
                print(f"[warn] failed to parse {url}: {e}", file=sys.stderr)
                continue

            self.rewrite_links(main, url)
            assets = self.download_images_and_rewrite(main, url)

            slug = unique_slug(slugify(title), self.used_slugs)
            sections = self.extract_sections(main, slug)
            markdown = html_to_md(str(main))
            markdown = self.inject_section_anchors_into_markdown(markdown, sections)

            page = Page(
                url=url,
                title=title,
                slug=slug,
                markdown=markdown,
                order=len(self.pages) + 1,
                assets=assets,
                sections=sections,
            )

            self.pages.append(page)
            self.url_to_page[url] = page

            for link in self.collect_links(soup, url):
                if link not in visited:
                    queue.append(link)

    def replace_doc_links_with_anchors(self, text: str) -> str:
        items = sorted(self.url_to_page.items(), key=lambda x: len(x[0]), reverse=True)

        for url, page in items:
            pattern = re.escape(url) + r"(#([A-Za-z0-9\-_:.]+))?"

            def repl(match):
                frag = match.group(2)
                if frag:
                    frag_slug = slugify(frag)
                    for sec in page.sections:
                        if sec.anchor == f"page-{page.slug}-{frag_slug}" or sec.anchor.endswith("-" + frag_slug):
                            return f"#{sec.anchor}"
                return f"#page-{page.slug}"

            text = re.sub(pattern, repl, text)

        return text

    def build_navigation(self) -> str:
        lines = ["## Navigation", ""]

        for page in self.pages:
            lines.append(f"- [{page.title}](#page-{page.slug})")

            for sec in page.sections:
                if sec.level == 2:
                    lines.append(f"  - [{sec.title}](#{sec.anchor})")
                elif sec.level == 3:
                    lines.append(f"    - [{sec.title}](#{sec.anchor})")

        return "\n".join(lines)

    def build_markdown(self) -> str:
        parts = [
            "# Documentation",
            "",
            f"Source root: `{self.doc_prefix}`",
            "",
            self.build_navigation(),
            "",
        ]

        for page in self.pages:
            parts.append(f'<a id="page-{page.slug}"></a>')
            parts.append(f"## {page.title}")
            parts.append("")
            parts.append(self.replace_doc_links_with_anchors(page.markdown))
            parts.append("")

        return "\n".join(parts).strip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-url", required=True, help="Documentation start URL")
    parser.add_argument("--out-dir", default="docs_md", help="Output directory")
    parser.add_argument("--out-file", default="documentation.md", help="Output markdown filename")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds")
    parser.add_argument(
        "--exclude-api",
        action="store_true",
        help="Exclude API docs sections like /api/java, /api/python, /api/rest",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    crawler = MultiPageDocsCrawler(
        start_url=args.start_url,
        out_dir=out_dir,
        timeout=args.timeout,
        exclude_api=args.exclude_api,
    )
    crawler.crawl()

    markdown = crawler.build_markdown()
    output_path = out_dir / args.out_file
    output_path.write_text(markdown, encoding="utf-8")

    print(f"Saved {len(crawler.pages)} pages to {output_path}")
    print(f"Images directory: {crawler.images_dir}")


if __name__ == "__main__":
    main()
