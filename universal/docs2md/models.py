#data models used by the crawler and navigation tree

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional

from .paths import compose_heading_anchor
from .urls import split_stored_href


@dataclass
class NavNode:
    title: str
    href: Optional[str] = None
    children: List["NavNode"] = field(default_factory=list)
    kind: str = "link" 

    def to_dict(
        self,
        url_to_anchor: Dict[str, str],
        url_to_virtual_path: Dict[str, Path],
    ) -> Dict[str, object]:
        payload: Dict[str, object] = {"title": self.title, "kind": self.kind}
        if self.href:
            payload["source_url"] = self.href
            base_url, fragment = split_stored_href(self.href)
            if base_url:
                anchor = url_to_anchor.get(base_url)
                if anchor:
                    payload["anchor"] = compose_heading_anchor(anchor, fragment) if fragment else anchor
                if base_url in url_to_virtual_path:
                    payload["virtual_path"] = url_to_virtual_path[base_url].as_posix()
        if self.children:
            payload["children"] = [
                child.to_dict(url_to_anchor, url_to_virtual_path)
                for child in self.children
            ]
        return payload


@dataclass
class PageRecord:
    url: str
    final_url: str
    title: str
    html_text: str
    nav_tree: List[NavNode] = field(default_factory=list)
    virtual_path: Optional[Path] = None
    page_anchor: Optional[str] = None
    markdown_body: str = ""
    profile: str = "generic"
    content_score: int = 0
    depth: int = 0


@dataclass
class FetchResult:
    text: str
    final_url: str
    from_cache: bool = False

