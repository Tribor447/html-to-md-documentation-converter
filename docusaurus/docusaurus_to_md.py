#!/usr/bin/env python3
    if not resp.encoding:
        resp.encoding = resp.apparent_encoding or "utf-8"
    return resp.text


def select_article(soup: BeautifulSoup) -> Optional[Tag]:
    for selector in ARTICLE_SELECTORS:
        node = soup.select_one(selector)
        if node is not None:
            return node
    return soup.body or soup


def extract_title(soup: BeautifulSoup) -> str:
    h1 = soup.find("h1")
    if h1 is not None:
        text = h1.get_text(" ", strip=True)
        if text:
            return text
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "Untitled"


def extract_candidate_links(soup: BeautifulSoup, base_url: str, domain: str) -> Set[str]:
    links: Set[str] = set()
    for a in soup.select("a[href]"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        abs_url = normalize_url(urljoin(base_url, href))
        if urlsplit(abs_url).netloc != domain:
            continue
        links.add(abs_url)
    return links


def crawl(entry_url: str, max_pages: int = 20) -> Dict[str, str]:
    entry_url = normalize_url(entry_url)
    domain = urlsplit(entry_url).netloc
    queue: deque[str] = deque([entry_url])
    seen: Set[str] = set()
    pages: Dict[str, str] = {}

    while queue and len(pages) < max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        html = fetch_text(url)
        pages[url] = html
        soup = BeautifulSoup(html, "html.parser")

        for link in extract_candidate_links(soup, url, domain):
            if link not in seen:
                queue.append(link)

    return pages


def build_combined_markdown(pages: Dict[str, str]) -> str:
    parts: List[str] = []
    for url, html in pages.items():
        soup = BeautifulSoup(html, "html.parser")
        title = extract_title(soup)
        article = select_article(soup)
        markdown = md(str(article), heading_style="ATX").strip()
        parts.append(f"# {title}\n\n<!-- source_url: {url} -->\n\n{markdown}\n")
    return "\n---\n\n".join(parts) + "\n"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out", type=Path, default=Path("combined.md"))
    parser.add_argument("--max-pages", type=int, default=20)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    pages = crawl(args.url, max_pages=args.max_pages)
    text = build_combined_markdown(pages)
    args.out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
