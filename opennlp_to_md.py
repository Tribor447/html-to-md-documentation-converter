#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests

DEFAULT_URL = "https://opennlp.apache.org/docs/2.5.7/manual/opennlp.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download Apache OpenNLP documentation."
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"Documentation URL (default: {DEFAULT_URL})",
    )
    parser.add_argument(
        "--html-file",
        help="Read HTML from local file instead of downloading",
    )
    parser.add_argument(
        "--output",
        default="opennlp_manual.md",
        help="Output markdown file",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="HTTP timeout in seconds",
    )
    return parser.parse_args()


def download_html(url: str, timeout: int) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def read_html_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    args = parse_args()

    try:
        if args.html_file:
            html_text = read_html_file(args.html_file)
        else:
            html_text = download_html(args.url, args.timeout)
    except requests.RequestException as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"File error: {exc}", file=sys.stderr)
        return 1

    Path(args.output).write_text(html_text, encoding="utf-8")
    print(f"Saved to: {Path(args.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
