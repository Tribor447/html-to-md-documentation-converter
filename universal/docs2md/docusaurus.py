#docusaurus sidebar discovery and parsing

from __future__ import annotations

from bs4 import BeautifulSoup
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from urllib.parse import SplitResult
from urllib.parse import unquote
from urllib.parse import urljoin
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
import json
import posixpath
import re
import yaml

from .models import NavNode
from .navigation import (
    clean_nav_title_value,
    dedupe_nav,
    nav_link_count,
    nav_tree_basic_score,
)
from .text import dedupe_preserve_order
from .urls import (
    ensure_trailing_slash,
    normalize_url,
)


def strip_json_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"(?m)^\s*//.*$", "", text)
    return text


def parse_json_or_jsonish(text: str) -> Optional[Any]:
    raw = text.strip()
    if not raw:
        return None
    for candidate in [raw]:
        try:
            return json.loads(candidate)
        except Exception:
            pass

    cleaned = strip_json_comments(raw)
    cleaned = re.sub(r"^\s*(?:module\.exports\s*=|export\s+default)\s*", "", cleaned)
    cleaned = re.sub(r";\s*$", "", cleaned.strip())
    start_positions = [idx for idx in [cleaned.find("{"), cleaned.find("[")] if idx >= 0]
    if start_positions:
        start = min(start_positions)
        end = max(cleaned.rfind("}"), cleaned.rfind("]"))
        if end > start:
            cleaned = cleaned[start : end + 1]
    cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
    for candidate in [cleaned]:
        try:
            return json.loads(candidate)
        except Exception:
            pass
        try:
            return yaml.safe_load(candidate)
        except Exception:
            pass
    return None


def title_from_doc_id(doc_id: str) -> str:
    leaf = doc_id.rstrip("/").rsplit("/", 1)[-1] or doc_id
    leaf = re.sub(r"\.(?:mdx?|html?)$", "", leaf, flags=re.I)
    if leaf.lower() in {"index", "overview"} and "/" in doc_id:
        leaf = doc_id.rstrip("/").rsplit("/", 2)[-2]
    return clean_nav_title_value(leaf.replace("_", " ").replace("-", " ").title()) or "Page"


def normalize_docusaurus_doc_id(doc_id: str) -> str:
    doc_id = str(doc_id or "").strip().strip("/").replace("\\", "/")
    doc_id = re.sub(r"\.(?:mdx?|html?)$", "", doc_id, flags=re.I)
    parts = [part for part in doc_id.split("/") if part]
    if len(parts) >= 2 and parts[0] == "docs":
        parts = parts[1:]
    if len(parts) >= 2 and parts[0] == "versioned_docs" and parts[1].startswith("version-"):
        parts = parts[2:]
    if parts and parts[-1].lower() == "index":
        parts = parts[:-1]
    return "/".join(parts)


def docusaurus_doc_id_to_url(doc_id: str, entry_url: str, site_prefix: str) -> str:
    doc_id = normalize_docusaurus_doc_id(doc_id)
    parts = urlsplit(entry_url)
    base = urlunsplit(SplitResult(
        scheme=parts.scheme,
        netloc=parts.netloc,
        path=ensure_trailing_slash(site_prefix),
        query="",
        fragment="",
    ))
    if not doc_id:
        return normalize_url(base)
    return normalize_url(urljoin(base, doc_id))


def docusaurus_link_to_href(link: object, entry_url: str, site_prefix: str) -> Optional[str]:
    if isinstance(link, str):
        return docusaurus_doc_id_to_url(link, entry_url, site_prefix)
    if not isinstance(link, dict):
        return None
    link_type = str(link.get("type") or "").lower()
    if link.get("href"):
        href = str(link.get("href") or "").strip()
        if href.startswith(("http://", "https://", "/")):
            return normalize_url(urljoin(entry_url, href))
    doc_id = link.get("id") or link.get("docId")
    if doc_id:
        return docusaurus_doc_id_to_url(str(doc_id), entry_url, site_prefix)
    if link_type == "generated-index":
        slug = str(link.get("slug") or "").strip("/")
        if slug:
            return normalize_url(urljoin(entry_url, slug))
    return None


def parse_docusaurus_sidebar_item(item: object, entry_url: str, site_prefix: str) -> Optional[NavNode]:
    if isinstance(item, str):
        href = docusaurus_doc_id_to_url(item, entry_url, site_prefix)
        return NavNode(title=title_from_doc_id(item), href=href, kind="link")

    if not isinstance(item, dict):
        return None

    item_type = str(item.get("type") or "doc").lower()
    label = clean_nav_title_value(str(item.get("label") or item.get("title") or ""))

    if item_type in {"category", "subcategory"} or "items" in item:
        children: List[NavNode] = []
        for child in item.get("items") or []:
            parsed = parse_docusaurus_sidebar_item(child, entry_url, site_prefix)
            if parsed is not None:
                children.append(parsed)
        href = docusaurus_link_to_href(item.get("link"), entry_url, site_prefix)
        if not label:
            label = title_from_doc_id(str(item.get("id") or item.get("docId") or href or "Section"))
        return NavNode(title=label or "Section", href=href, children=dedupe_nav(children), kind="category")

    if item_type in {"doc", "ref"} or item.get("id") or item.get("docId"):
        doc_id = str(item.get("id") or item.get("docId") or "")
        href = docusaurus_doc_id_to_url(doc_id, entry_url, site_prefix) if doc_id else None
        return NavNode(title=label or title_from_doc_id(doc_id), href=href, kind="link")

    if item_type == "link" or item.get("href"):
        href = docusaurus_link_to_href(item, entry_url, site_prefix)
        if not href:
            return None
        return NavNode(title=label or title_from_doc_id(href), href=href, kind="link")

    return None


def parse_docusaurus_sidebar_payload(payload: Any, entry_url: str, site_prefix: str) -> List[NavNode]:
    candidates: List[List[NavNode]] = []

    def parse_items(items: Any) -> List[NavNode]:
        nodes: List[NavNode] = []
        if isinstance(items, list):
            for item in items:
                parsed = parse_docusaurus_sidebar_item(item, entry_url, site_prefix)
                if parsed is not None:
                    nodes.append(parsed)
        return dedupe_nav(nodes)

    if isinstance(payload, list):
        candidates.append(parse_items(payload))
    elif isinstance(payload, dict):
        if isinstance(payload.get("default"), (dict, list)):
            nested = parse_docusaurus_sidebar_payload(payload["default"], entry_url, site_prefix)
            if nested:
                candidates.append(nested)
        for value in payload.values():
            if isinstance(value, list):
                candidates.append(parse_items(value))
            elif isinstance(value, dict) and isinstance(value.get("items"), list):
                parsed = parse_docusaurus_sidebar_item(value, entry_url, site_prefix)
                if parsed is not None:
                    candidates.append([parsed])

    candidates = [nodes for nodes in candidates if nav_link_count(nodes) > 0]
    if not candidates:
        return []
    candidates.sort(key=lambda nodes: nav_tree_basic_score(nodes), reverse=True)
    return candidates[0]


def docusaurus_sidebar_candidate_urls(entry_url: str, site_prefix: str, soup: BeautifulSoup) -> List[str]:
    parts = urlsplit(entry_url)
    root = f"{parts.scheme}://{parts.netloc}"
    candidates: List[str] = []

    prefixes = dedupe_preserve_order([
        site_prefix,
        posixpath.dirname(site_prefix.rstrip("/")) + "/" if site_prefix.rstrip("/") else "/",
        "/docs/",
        "/",
    ])
    for prefix in prefixes:
        relative_prefix = ensure_trailing_slash(prefix).lstrip("/")
        for name in ("sidebars.json", "sidebar.json", "sidebars.js"):
            candidates.append(normalize_url(urljoin(root + "/", relative_prefix + name)))

    for link in soup.select("a[href*='github.com'][href*='/edit/'], a[href*='github.com'][href*='/blob/']"):
        href = str(link.get("href") or "").strip()
        if not href:
            continue
        gh = urlsplit(href)
        bits = [unquote(bit) for bit in gh.path.strip("/").split("/") if bit]
        if len(bits) < 5:
            continue
        marker_index = -1
        for marker in ("edit", "blob"):
            if marker in bits:
                marker_index = bits.index(marker)
                break
        if marker_index < 2 or marker_index + 2 >= len(bits):
            continue
        org, repo = bits[0], bits[1]
        branch = bits[marker_index + 1]
        file_parts = bits[marker_index + 2:]
        raw_root = f"https://raw.githubusercontent.com/{org}/{repo}/{branch}/"

        dirs: List[str] = [""]
        for idx in range(1, min(len(file_parts), 6)):
            dirs.append("/".join(file_parts[:idx]) + "/")
        for directory in dedupe_preserve_order(dirs):
            for name in ("sidebars.json", "sidebar.json", "sidebars.js"):
                candidates.append(normalize_url(urljoin(raw_root, directory + name)))

        if "versioned_docs" in file_parts:
            vd_idx = file_parts.index("versioned_docs")
            if vd_idx + 1 < len(file_parts):
                version_dir = file_parts[vd_idx + 1]
                base_dir = "/".join(file_parts[:vd_idx])
                sidebars_dir = (base_dir + "/" if base_dir else "") + "versioned_sidebars/"
                for ext in ("json", "js"):
                    candidates.append(normalize_url(urljoin(raw_root, f"{sidebars_dir}{version_dir}-sidebars.{ext}")))

    return dedupe_preserve_order(candidates)

