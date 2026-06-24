#navigation rendering and fallback output tree construction

from __future__ import annotations

from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

from .models import NavNode, PageRecord
from .paths import compose_heading_anchor
from .urls import split_stored_href


def resolve_nav_href_anchor(href: Optional[str], url_to_anchor: Dict[str, str]) -> Optional[str]:
    if not href:
        return None
    base_url, fragment = split_stored_href(href)
    if not base_url:
        return None
    page_anchor = url_to_anchor.get(base_url)
    if not page_anchor:
        return None
    return compose_heading_anchor(page_anchor, fragment) if fragment else page_anchor


def render_singlefile_navigation(
    nodes: List[NavNode],
    url_to_anchor: Dict[str, str],
    indent: int = 0,
) -> List[str]:
    lines: List[str] = []
    for node in nodes:
        prefix = "  " * indent + "- "
        target_anchor = resolve_nav_href_anchor(node.href, url_to_anchor)
        if target_anchor:
            lines.append(f"{prefix}[{node.title}](#{target_anchor})")
        else:
           
           
            lines.append(f"{prefix}{node.title}")
        if node.children:
            lines.extend(render_singlefile_navigation(node.children, url_to_anchor, indent + 1))
    return lines


def build_url_tree(
    pages: Dict[str, PageRecord],
    url_to_virtual_path: Dict[str, Path],
) -> List[NavNode]:
    root = NavNode(title="root", kind="category")
    folder_nodes: Dict[Tuple[str, ...], NavNode] = {(): root}

    for url, record in sorted(pages.items(), key=lambda item: url_to_virtual_path[item[0]].as_posix()):
        rel = url_to_virtual_path[url]
        parts = list(rel.parts)
        folder_parts = tuple(parts[:-1])
        parent_key: Tuple[str, ...] = ()
        for i in range(len(folder_parts)):
            key = tuple(folder_parts[: i + 1])
            if key not in folder_nodes:
                title = key[-1].replace("_", " ").replace("-", " ").title()
                node = NavNode(title=title, kind="category")
                folder_nodes[parent_key].children.append(node)
                folder_nodes[key] = node
            parent_key = key
        folder_nodes[parent_key].children.append(
            NavNode(title=record.title, href=url, kind="link")
        )
    return root.children

