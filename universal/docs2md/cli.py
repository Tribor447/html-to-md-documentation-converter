#command-line interface for docs2md

from __future__ import annotations

from pathlib import Path
from typing import List
from typing import Optional
import argparse
import sys

from .constants import (
    BROWSER_TIMEOUT_MS,
    DEFAULT_ASSET_CONCURRENCY,
    DEFAULT_CONCURRENCY,
    DEFAULT_MAX_ASSET_BYTES,
    DEFAULT_MAX_DEPTH,
    PREFERRED_LANGUAGE_DEFAULT,
)
from .converter import UniversalDocsConverter
from .markdown import set_admonition_style
from .targets import load_targets

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawl an HTML documentation site and convert it into a single Markdown file.",
    )
    parser.add_argument("urls", nargs="*", help="One or more docs entry URLs.")
    parser.add_argument("--targets-file", type=Path, help="Text file with one URL per line.")
    parser.add_argument("--out-dir", type=Path, default=Path("./converted_docs"),
                        help="Output directory (default: ./converted_docs).")
    parser.add_argument("--delay", type=float, default=0.05,
                        help="Minimum interval between requests to the same host (default: 0.05s).")
    parser.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY,
                        help=f"Number of concurrent fetches (default: {DEFAULT_CONCURRENCY}).")
    parser.add_argument("--max-pages", type=int, default=None,
                        help="Maximum number of pages per site.")
    parser.add_argument("--max-depth", type=int, default=DEFAULT_MAX_DEPTH,
                        help=f"Maximum link-depth from entry URL (default: {DEFAULT_MAX_DEPTH}).")
    parser.add_argument("--save-html", action="store_true",
                        help="Save original HTML files next to the output for debugging.")
    parser.add_argument("--use-sitemap", action="store_true",
                        help="Use sitemap.xml as extra crawl seeds.")
    parser.add_argument("--site-prefix", default=None,
                        help="Force the crawl path prefix, e.g. /docs/ or /manual/.")
    parser.add_argument("--combined-filename", default="combined.md",
                        help="Name of the single combined Markdown file.")
    parser.add_argument("--browser", choices=["auto", "always", "never"], default="auto",
                        help="Whether to use Playwright rendering for JS-heavy docs.")
    parser.add_argument("--browser-timeout-ms", type=int, default=BROWSER_TIMEOUT_MS,
                        help=f"Playwright timeout in ms (default: {BROWSER_TIMEOUT_MS}).")
    parser.add_argument("--admonition-style", choices=["callout", "html"], default="callout",
                        help="How to render note/tip/warning blocks.")
    parser.add_argument("--front-matter", action="store_true",
                        help="Include a YAML front matter block at the top of combined.md.")
    parser.add_argument("--profile",
                        choices=["generic", "docusaurus", "sphinx", "mkdocs", "vitepress", "maven", "book", "gitbook", "antora", "asciidoctor", "javadoc"],
                        default=None,
                        help="Force a site profile if auto-detection gets it wrong.")
    parser.add_argument("--follow-content-links", action="store_true",
                        help="Also follow links found in page content (default: only sidebar+pagination).")
    parser.add_argument("--no-robots", action="store_true", help="Ignore robots.txt.")
    parser.add_argument("--max-asset-mb", type=float,
                        default=DEFAULT_MAX_ASSET_BYTES / (1024 * 1024),
                        help="Maximum size of any single downloaded asset (default: 25 MB).")
    parser.add_argument("--asset-concurrency", type=int, default=DEFAULT_ASSET_CONCURRENCY,
                        help=f"Concurrent asset downloads during prefetch (default: {DEFAULT_ASSET_CONCURRENCY}).")
    parser.add_argument("--no-assets", action="store_true",
                        help="Do not download images/files; keep their absolute URLs in Markdown. Fastest mode.")
    parser.add_argument("--download-external-assets", action="store_true",
                        help="Download images/files from external hosts. Default: keep external URLs unchanged.")
    parser.add_argument("--loose-version-scope", action="store_true",
                        help="Allow crawling sibling documentation versions. Default: stay pinned to the entry URL's version.")
    parser.add_argument("--language", default=PREFERRED_LANGUAGE_DEFAULT,
                        help="Preferred documentation language. Default: en. Use 'any' to disable language filtering.")
    parser.add_argument("--cache-dir", type=Path, default=None,
                        help="HTTP cache directory (default: <out-dir>/.cache).")
    parser.add_argument("--no-cache", action="store_true", help="Disable the HTTP cache.")
    return parser

def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    set_admonition_style(args.admonition_style)
    targets = load_targets(args.targets_file, args.urls)
    if not targets:
        parser.error("Provide at least one URL or --targets-file.")

    max_asset_bytes = int(args.max_asset_mb * 1024 * 1024)

    for entry_url in targets:
        converter = UniversalDocsConverter(
            entry_url=entry_url,
            out_dir=args.out_dir,
            delay=args.delay,
            max_pages=args.max_pages,
            max_depth=args.max_depth,
            save_html=args.save_html,
            use_sitemap=args.use_sitemap,
            site_prefix_override=args.site_prefix,
            combined_filename=args.combined_filename,
            browser_mode=args.browser,
            browser_timeout_ms=args.browser_timeout_ms,
            front_matter=args.front_matter,
            profile_override=("book" if args.profile == "gitbook" else args.profile),
            concurrency=args.concurrency,
            follow_content_links=args.follow_content_links,
            respect_robots=not args.no_robots,
            max_asset_bytes=max_asset_bytes,
            cache_dir=args.cache_dir,
            use_cache=not args.no_cache,
            download_external_assets=args.download_external_assets,
            asset_concurrency=args.asset_concurrency,
            skip_assets=args.no_assets,
            strict_version_scope=not args.loose_version_scope,
            preferred_language=args.language,
        )
        try:
            converter.run()
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"[error] {entry_url}: {exc}", file=sys.stderr)
    return 0

