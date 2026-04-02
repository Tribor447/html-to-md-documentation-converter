#!/usr/bin/env python3
            if title or children:
                nodes.append(NavNode(title=title or "Section", href=href, children=children, kind="category"))
        elif title:
            nodes.append(NavNode(title=title, href=href, kind="link"))
    return nodes


def extract_sidebar_tree(soup: BeautifulSoup, base_url: str, domain: str) -> List[NavNode]:
    sidebar = select_sidebar(soup)
    if sidebar is None:
        return []
    ul = sidebar.find("ul")
    if ul is None:
        return []
    return parse_nav_list(ul, base_url, domain)


def flatten_nav_urls(nodes: List[NavNode]) -> List[str]:
    urls: List[str] = []
    for node in nodes:
        if node.href:
            urls.append(node.href)
        urls.extend(flatten_nav_urls(node.children))
    return urls


def crawl(entry_url: str, max_pages: int = 20) -> Tuple[Dict[str, PageRecord], List[NavNode]]:
    entry_url = normalize_url(entry_url)
    domain = urlsplit(entry_url).netloc
    queue: deque[str] = deque([entry_url])
    seen: Set[str] = set()
    pages: Dict[str, PageRecord] = {}
    sidebar_tree: List[NavNode] = []

    while queue and len(pages) < max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        html = fetch_text(url)
        soup = BeautifulSoup(html, "html.parser")
        title = extract_title(soup)
        pages[url] = PageRecord(url=url, title=title, html_text=html)

        nav = extract_sidebar_tree(soup, url, domain)
        if nav and not sidebar_tree:
            sidebar_tree = nav

        for link in flatten_nav_urls(nav):
            if link not in seen:
                queue.append(link)

    return pages, sidebar_tree


def render_navigation(nodes: List[NavNode], indent: int = 0) -> List[str]:
    lines: List[str] = []
    for node in nodes:
        prefix = "  " * indent + "- "
        if node.href:
            lines.append(f"{prefix}{node.title} ({node.href})")
        else:
            lines.append(f"{prefix}{node.title}")
        lines.extend(render_navigation(node.children, indent + 1))
    return lines


def build_combined_markdown(pages: Dict[str, PageRecord], nav: List[NavNode]) -> str:
    parts = ["# Documentation\n", "## Navigation\n"]
    parts.append("\n".join(render_navigation(nav)) + "\n")
    parts.append("\n## Content\n")

    ordered = flatten_nav_urls(nav)
    for url in ordered:
        if url not in pages:
            continue
        record = pages[url]
        soup = BeautifulSoup(record.html_text, "html.parser")
        article = select_article(soup)
        body = md(str(article), heading_style="ATX").strip()
        parts.append(f"\n# {record.title}\n\n<!-- source_url: {url} -->\n\n{body}\n")
    return "".join(parts)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--out", type=Path, default=Path("combined.md"))
    parser.add_argument("--max-pages", type=int, default=20)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    pages, nav = crawl(args.url, args.max_pages)
    result = build_combined_markdown(pages, nav)
    args.out.write_text(result, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
