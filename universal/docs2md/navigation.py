#navigation tree parsing, merging, filtering, and heading-based fallback

from __future__ import annotations

from bs4 import NavigableString
from bs4 import Tag
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from urllib.parse import urlsplit
import copy
import re

from .constants import (
    DOC_PAGE_EXTENSIONS,
    GLOBAL_NAV_TITLE_HINTS,
)
from .html_analysis import (
    is_inside_global_chrome,
    is_nav_heading_tag,
    is_sidebarish_tag,
    is_toc_like_tag,
    link_visible_text,
    url_path_in_prefix,
)
from .models import NavNode
from .text import (
    clean_text,
    dedupe_preserve_order,
)
from .urls import (
    nav_href_base,
    repair_legacy_maven_javadoc_url,
    should_skip_crawl_url,
    slugify_anchor,
    split_and_normalize,
    split_stored_href,
    url_equivalence_variants,
    url_with_fragment,
)


def nav_link_count(nodes: List[NavNode]) -> int:
    total = 0
    for node in nodes:
        if node.href:
            total += 1
        total += nav_link_count(node.children)
    return total


def nav_has_categories(nodes: List[NavNode]) -> bool:
    return any((not node.href) or node.children or nav_has_categories(node.children) for node in nodes)


def nav_tree_depth_basic(nodes: List[NavNode]) -> int:
    if not nodes:
        return 0
    return 1 + max((nav_tree_depth_basic(node.children) for node in nodes), default=0)


def nav_tree_basic_score(nodes: List[NavNode]) -> int:



    if not nodes:
        return 0
    links = nav_link_count(nodes)
    cats = sum(1 for node in nodes if node.children or not node.href)
    depth = nav_tree_depth_basic(nodes)
    return links * 100 + cats * 55 + depth * 180 + len(nodes) * 8


def is_nav_header_item(item: Tag) -> bool:

    classes = " ".join(item.get("class", [])).lower()
    if "nav-header" in classes or "nav_header" in classes or "sidebar-heading" in classes:
        return True
    if item.find(["ul", "ol"], recursive=False) is not None:
        return False
    if item.find("a", href=True) is not None:
        return False
    text = clean_text(item.get_text(" ", strip=True))
    if not text or len(text) > 140:
        return False
   
    return item.name in {"li", "dt", "dd"}


def clean_nav_title_value(title: str) -> str:
    title = clean_text(title)
    title = re.sub(r"^(?:expand|collapse)\s+sidebar\s+category\s+", "", title, flags=re.I)
    title = re.sub(r"^(?:open|close)\s+", "", title, flags=re.I)
    title = re.sub(r"^[•›»·\-\s]+", "", title)
    title = re.sub(r"\s*[¶#]+\s*$", "", title)
    title = re.sub(r"\s+", " ", title).strip()
   
   
    if "_" in title and " " not in title:
        title = title.replace("_", " ")
    return title[:180].strip()


def direct_label_text(tag: Tag) -> str:

    pieces: List[str] = []
    for child in tag.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
        elif isinstance(child, Tag):
            if child.name in {"ul", "ol", "script", "style", "svg", "button"}:
                continue
            if child.find(["ul", "ol"]):
                pieces.append(direct_label_text(child))
            else:
                pieces.append(child.get_text(" ", strip=True))
    return clean_nav_title_value(" ".join(pieces))


def best_anchor_text(link: Tag) -> str:
    text = clean_nav_title_value(link.get_text(" ", strip=True))
    if text:
        return text
    for attr in ("aria-label", "title"):
        value = link.get(attr)
        if value:
            text = clean_nav_title_value(str(value))
            if text:
                return text
    return ""


def is_explicit_nav_header_item(item: Tag) -> bool:
    classes = " ".join(item.get("class", [])).lower()
    role = str(item.get("role", "")).lower()
    return (
        "nav-header" in classes
        or "nav_header" in classes
        or "sidebar-heading" in classes
        or "menu-heading" in classes
        or (role in {"heading", "separator"} and item.find("a", href=True) is None)
    )


def extract_heading_title(tag: Tag) -> str:
   
    title = direct_label_text(tag) or clean_nav_title_value(tag.get_text(" ", strip=True))
    return title[:140].strip()


def parse_nav_container_sequence(
    container: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
    depth: int = 0,
) -> List[NavNode]:



    nodes: List[NavNode] = []
    current_heading: Optional[NavNode] = None

    def append_parsed(parsed: List[NavNode]) -> None:
        nonlocal current_heading
        if not parsed:
            return
        if current_heading is not None:
            current_heading.children.extend(parsed)
            current_heading = None
        else:
            nodes.extend(parsed)

    for child in container.children:
        if isinstance(child, NavigableString):
            if clean_text(str(child)):
               
               
                continue
            continue
        if not isinstance(child, Tag):
            continue

        if child.name in {"script", "style", "noscript", "template"}:
            continue

        if is_nav_heading_tag(child):
            title = extract_heading_title(child)
            if title:
                current_heading = NavNode(title=title, kind="category")
                nodes.append(current_heading)
            continue

        if child.name in {"ul", "ol"}:
            parsed = parse_nav_list(child, current_domain=current_domain, base_url=base_url)
            append_parsed(parsed)
            continue

        if child.name == "a" and child.get("href"):
            title = best_anchor_text(child)
            href = str(child.get("href") or "").strip()
            if title and href and not href.startswith("#"):
                abs_url, frag = split_and_normalize(base_url or ("https://" + current_domain), href)
                if urlsplit(abs_url).netloc == current_domain:
                    append_parsed([NavNode(title=title, href=url_with_fragment(abs_url, frag), kind="link")])
            continue

       
       
       
        if depth < 4 and child.name in {"div", "section", "nav", "aside", "td", "li"}:
            parsed = parse_nav_container_sequence(
                child,
                current_domain=current_domain,
                base_url=base_url,
                depth=depth + 1,
            )
            if nav_link_count(parsed) or nav_has_categories(parsed):
                append_parsed(parsed)

   
    nodes = [node for node in nodes if node.href or node.children or node.kind == "category"]
    return dedupe_nav(nodes)


def extract_nav_tree(
    sidebar: Optional[Tag],
    current_domain: str,
    base_url: Optional[str] = None,
) -> List[NavNode]:
    if sidebar is None:
        return []

   
   
    if sidebar.name in {"ul", "ol"}:
        listed = parse_nav_list(sidebar, current_domain=current_domain, base_url=base_url)
        if listed:
            return listed

    structured = parse_nav_container_sequence(
        sidebar,
        current_domain=current_domain,
        base_url=base_url,
    )

   
   
   
   
   
    best_list_nodes: List[NavNode] = []
    best_list_score = 0
    list_candidates = list(sidebar.find_all(["ul", "ol"]))
    if list_candidates:
        top_level = [
            lst for lst in list_candidates
            if not any(
                isinstance(parent, Tag) and parent.name in {"ul", "ol"}
                and parent is not lst
                for parent in lst.parents
            )
        ]
       
       
        ordered_lists: List[Tag] = []
        seen_list_ids: Set[int] = set()
        for lst in [*top_level, *list_candidates]:
            if id(lst) in seen_list_ids:
                continue
            seen_list_ids.add(id(lst))
            ordered_lists.append(lst)
        for lst in ordered_lists:
            parsed = parse_nav_list(lst, current_domain=current_domain, base_url=base_url)
            if not parsed:
                continue
            links = [u for u in flatten_nav_urls(parsed) if urlsplit(u).netloc == current_domain]
            scoped_bonus = len(set(links)) * 20
            score = nav_tree_basic_score(parsed) + scoped_bonus
            if score > best_list_score:
                best_list_score = score
                best_list_nodes = parsed

    structured_score = nav_tree_basic_score(structured)
    if best_list_nodes:
       
       
       
        if (
            not structured
            or best_list_score >= int(structured_score * 1.25)
            or (
                nav_link_count(best_list_nodes) >= nav_link_count(structured) + 4
                and nav_tree_depth_basic(best_list_nodes) >= nav_tree_depth_basic(structured)
            )
        ):
            return dedupe_nav(best_list_nodes)

    if nav_link_count(structured) >= 2 or nav_has_categories(structured):
        return structured

   
    nodes: List[NavNode] = []
    seen: Set[str] = set()
    for a in sidebar.select("a[href]"):
        href = (a.get("href") or "").strip()
        title = best_anchor_text(a)
        if not href or not title or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        abs_url, frag = split_and_normalize(base_url or ("https://" + current_domain), href)
        stored_href = url_with_fragment(abs_url, frag)
        if stored_href in seen:
            continue
        seen.add(stored_href)
        nodes.append(NavNode(title=title, href=stored_href, kind="link"))
    return dedupe_nav(nodes)


def first_direct_child_list(item: Tag) -> Optional[Tag]:
    for child in item.children:
        if isinstance(child, Tag) and child.name in {"ul", "ol"}:
            return child
    for child in item.find_all(True, recursive=False):
        found = child.find(["ul", "ol"], recursive=False)
        if found is not None:
            return found
    return None


def parse_single_nav_item(
    item: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> Optional[NavNode]:
    child_list = first_direct_child_list(item)
    title, href = extract_nav_label(item, current_domain=current_domain, base_url=base_url)
    if child_list is not None:
        children = parse_nav_list(child_list, current_domain=current_domain, base_url=base_url)
        if title or children:
            return NavNode(
                title=title or (children[0].title if children else "Section"),
                href=href,
                children=children,
                kind="category",
            )
    elif href and title:
        return NavNode(title=title, href=href, kind="link")
    elif title:
        return NavNode(title=title, kind="category")
    return None


def collapse_target_ids_from_nav_item(item: Tag) -> List[str]:



    ids: List[str] = []
    for el in item.find_all(["a", "button", "span", "div"], recursive=True):
       
       
        if any(isinstance(parent, Tag) and parent.name in {"ul", "ol"} and parent is not item for parent in el.parents):
            continue
        for attr in ("href", "data-target", "data-bs-target"):
            value = str(el.get(attr) or "").strip()
            if value.startswith("#") and len(value) > 1:
                ids.append(value[1:])
        aria_controls = str(el.get("aria-controls") or "").strip()
        if aria_controls:
            ids.extend([part for part in re.split(r"\s+", aria_controls) if part])
    return dedupe_preserve_order(ids)


def first_list_in_nav_container(container: Tag) -> Optional[Tag]:
    for child in container.children:
        if isinstance(child, Tag) and child.name in {"ul", "ol"}:
            return child
    return container.find(["ul", "ol"])


def sibling_collapse_lists_for_nav_list(ul: Tag) -> Dict[str, Tag]:

    out: Dict[str, Tag] = {}
    for child in ul.children:
        if not isinstance(child, Tag):
            continue
        if child.name in {"li", "dt", "dd"}:
            continue
        child_id = str(child.get("id") or "").strip()
        if not child_id:
            continue
        lst = first_list_in_nav_container(child)
        if lst is not None:
            out[child_id] = lst
    return out


def parse_nav_list(
    ul: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> List[NavNode]:
    nodes: List[NavNode] = []

   
   
    collapse_lists = sibling_collapse_lists_for_nav_list(ul)
    used_collapse_ids: Set[str] = set()

    direct_children = [child for child in ul.children if isinstance(child, Tag)]
    item_tags = [child for child in direct_children if child.name in {"li", "dt", "dd"}]
    if not item_tags and ul.name in {"li", "dt", "dd"}:
        item_tags = [ul]

   
   
    has_inline_headers = any(is_explicit_nav_header_item(item) for item in item_tags)
    current_group: Optional[NavNode] = None

    for item in item_tags:
        if has_inline_headers and is_explicit_nav_header_item(item):
            title = extract_heading_title(item)
            if title:
                current_group = NavNode(title=title, kind="category")
                nodes.append(current_group)
            continue

        parsed = parse_single_nav_item(item, current_domain=current_domain, base_url=base_url)
        if parsed is None:
            continue

       
       
       
        for target_id in collapse_target_ids_from_nav_item(item):
            collapse_list = collapse_lists.get(target_id)
            if collapse_list is None:
                continue
            child_nodes = parse_nav_list(collapse_list, current_domain=current_domain, base_url=base_url)
            if child_nodes:
                parsed.kind = "category"
                merge_nav_lists(parsed.children, child_nodes)
                used_collapse_ids.add(target_id)

        if current_group is not None:
            current_group.children.append(parsed)
        else:
            nodes.append(parsed)

   
   
   
    for collapse_id, collapse_list in collapse_lists.items():
        if collapse_id in used_collapse_ids:
            continue
        child_nodes = parse_nav_list(collapse_list, current_domain=current_domain, base_url=base_url)
        if child_nodes:
            nodes.append(NavNode(
                title=clean_nav_title_value(collapse_id.replace("_", " ").replace("-", " ")) or "Section",
                children=child_nodes,
                kind="category",
            ))

    return dedupe_nav(nodes)


def first_direct_nav_link(tag: Tag) -> Optional[Tag]:
   
   
   
   
    if tag.name == "a":
        return tag
    for child in tag.children:
        if isinstance(child, Tag):
            if child.name in {"ul", "ol"}:
                continue
            if child.name == "a":
                return child
           
            for grand in child.children:
                if isinstance(grand, Tag):
                    if grand.name in {"ul", "ol"}:
                        continue
                    if grand.name == "a":
                        return grand
    return None


def extract_nav_label(
    li: Tag,
    current_domain: str,
    base_url: Optional[str] = None,
) -> Tuple[Optional[str], Optional[str]]:
    title: Optional[str] = None
    href: Optional[str] = None

    for child in li.children:
        if isinstance(child, NavigableString):
            raw = clean_nav_title_value(str(child))
            if raw and not title:
                title = raw
            continue
        if not isinstance(child, Tag):
            continue
        if child.name in {"ul", "ol"}:
            continue

        link = first_direct_nav_link(child)
        if link is not None:
            label = best_anchor_text(link)
            if label and not title:
                title = label
            if link.get("href"):
                raw_href = str(link.get("href") or "").strip()
                if raw_href and not raw_href.startswith(("#", "javascript:", "mailto:", "tel:")):
                    abs_url, frag = split_and_normalize(
                        base_url or ("https://" + current_domain),
                        raw_href,
                    )
                    href = url_with_fragment(abs_url, frag)
                    href = repair_legacy_maven_javadoc_url(href, title or label)
            if title and href:
                break

        if not title:
            for tag_name in ["a", "button", "span", "div", "strong", "p"]:
                label_tag = child if child.name == tag_name else child.find(tag_name)
                if label_tag is not None:
                    label = direct_label_text(label_tag) or clean_nav_title_value(label_tag.get_text(" ", strip=True))
                    if label:
                        title = label
                        break
    return title, href


def normalize_nav_title_key(title: str) -> str:
    title = clean_nav_title_value(title).casefold()
    title = re.sub(r"\s+", " ", title)
    return title.strip()


def normalize_nav_href_key(href: Optional[str]) -> Optional[str]:
    if not href:
        return None
    base_url, fragment = split_stored_href(href)
    if not base_url:
        return None
    key = base_url.rstrip("/") or base_url
    if fragment:
        key += "#" + slugify_anchor(fragment)
    return key


def nav_key(node: NavNode) -> Tuple[str, str]:
    href_key = normalize_nav_href_key(node.href)
    if href_key:
        return ("href", href_key)
    return ("title", normalize_nav_title_key(node.title))


def nav_identity_keys(node: NavNode) -> Set[Tuple[str, str]]:
    keys: Set[Tuple[str, str]] = set()
    href_key = normalize_nav_href_key(node.href)
    if href_key:
        keys.add(("href", href_key))
    title_key = normalize_nav_title_key(node.title)
    if title_key:
        keys.add(("title", title_key))
    return keys


def _collect_nav_href_keys(nodes: List[NavNode], out: Set[str]) -> None:
    for node in nodes:
        href_key = normalize_nav_href_key(node.href)
        if href_key:
            out.add(href_key)
        if node.children:
            _collect_nav_href_keys(node.children, out)


def _collect_nav_href_title_keys(nodes: List[NavNode], out: Set[Tuple[str, str]]) -> None:
    for node in nodes:
        href_key = normalize_nav_href_key(node.href)
        title_key = normalize_nav_title_key(node.title)
        if href_key:
            out.add((href_key, title_key))
        if node.children:
            _collect_nav_href_title_keys(node.children, out)


def _collect_nav_keys(nodes: List[NavNode], out: Set[Tuple[str, str]]) -> None:
    for node in nodes:
        out.update(nav_identity_keys(node))
        if node.children:
            _collect_nav_keys(node.children, out)


def find_matching_sibling(index: Dict[Tuple[str, str], NavNode], node: NavNode) -> Optional[NavNode]:
    href_key = normalize_nav_href_key(node.href)
    title_key = normalize_nav_title_key(node.title)
    if href_key:
        match = index.get(("href", href_key))
        if match is not None:
            match_title_key = normalize_nav_title_key(match.title)
           
           
           
            if not title_key or not match_title_key or title_key == match_title_key:
                return match
    if title_key:
        return index.get(("title", title_key))
    return None


def index_sibling(node: NavNode, index: Dict[Tuple[str, str], NavNode]) -> None:
    for key in nav_identity_keys(node):
        index.setdefault(key, node)


def merge_nav_lists(dst: List[NavNode], src: List[NavNode]) -> None:



    sibling_index: Dict[Tuple[str, str], NavNode] = {}
    for node in dst:
        index_sibling(node, sibling_index)

    existing_href_titles: Set[Tuple[str, str]] = set()
    _collect_nav_href_title_keys(dst, existing_href_titles)

    for src_node in src:
        dst_node = find_matching_sibling(sibling_index, src_node)
        if dst_node is not None:
            if not dst_node.href and src_node.href:
                dst_node.href = src_node.href
                index_sibling(dst_node, sibling_index)
                href_key = normalize_nav_href_key(src_node.href)
                title_key = normalize_nav_title_key(src_node.title)
                if href_key:
                    existing_href_titles.add((href_key, title_key))
            if dst_node.title and src_node.title:
                dst_sluggy = "_" in dst_node.title or "-" in dst_node.title
                src_cleaner = "_" not in src_node.title and len(src_node.title) >= len(dst_node.title.replace("_", " "))
                if dst_sluggy and src_cleaner:
                    dst_node.title = src_node.title
            if src_node.children:
                merge_nav_lists(dst_node.children, src_node.children)
            continue

        href_key = normalize_nav_href_key(src_node.href)
        title_key = normalize_nav_title_key(src_node.title)
        if href_key and (href_key, title_key) in existing_href_titles:
            continue

        cloned = copy.deepcopy(src_node)
        dst.append(cloned)
        index_sibling(cloned, sibling_index)
        _collect_nav_href_title_keys([cloned], existing_href_titles)


def dedupe_nav(nodes: List[NavNode]) -> List[NavNode]:
    out: List[NavNode] = []
    sibling_index: Dict[Tuple[str, str], NavNode] = {}
    for node in nodes:
        match = find_matching_sibling(sibling_index, node)
        if match is not None:
            if not match.href and node.href:
                match.href = node.href
                index_sibling(match, sibling_index)
            if node.children:
                merge_nav_lists(match.children, node.children)
            continue
        out.append(node)
        index_sibling(node, sibling_index)
    return out


def flatten_nav_urls(nodes: List[NavNode]) -> List[str]:
    urls: List[str] = []
    for node in nodes:
        base_url = nav_href_base(node.href)
        if base_url:
            urls.append(base_url)
        if node.children:
            urls.extend(flatten_nav_urls(node.children))
    return urls


def mark_active_nav_item(
    nodes: List[NavNode],
    current_url: str,
    current_title: str,
) -> None:

    page_slug = slugify_anchor(current_title)
    for node in nodes:
        if not node.href:
            node_slug = slugify_anchor(node.title)
            exact = node_slug == page_slug
            leaf_suffix = (not node.children) and page_slug.endswith("-" + node_slug)
            if exact or leaf_suffix:
                node.href = current_url
        if node.children:
            mark_active_nav_item(node.children, current_url, current_title)


def nav_category_count(nodes: List[NavNode]) -> int:
    total = 0
    for node in nodes:
        if node.children or not node.href:
            total += 1
        total += nav_category_count(node.children)
    return total


def nav_max_depth(nodes: List[NavNode], depth: int = 0) -> int:
    if not nodes:
        return depth
    return max(nav_max_depth(node.children, depth + 1) for node in nodes)


def nav_tree_quality(
    nodes: List[NavNode],
    site_prefix: Optional[str] = None,
    domain: Optional[str] = None,
) -> int:

    links = flatten_nav_urls(nodes)
    unique_links = set(links)
    scoped = 0
    offscope = 0
    for url in unique_links:
        parts = urlsplit(url)
        if domain and parts.netloc and parts.netloc != domain:
            offscope += 1
            continue
        if url_path_in_prefix(url, site_prefix):
            scoped += 1
        else:
            offscope += 1

    categories = nav_category_count(nodes)
    depth = nav_max_depth(nodes)
    top_titles = {clean_text(node.title).lower() for node in nodes[:8]}

    score = scoped * 140
    score += categories * 90
    score += depth * 220
    score -= offscope * 80

   
   
    noisy = len(top_titles & GLOBAL_NAV_TITLE_HINTS)
    score -= noisy * 260

   
    if depth < 2 and scoped < 4:
        score -= 400

    return score


def merged_nav_from_snapshots(
    snapshots: List[List[NavNode]],
    site_prefix: Optional[str] = None,
    domain: Optional[str] = None,
) -> List[NavNode]:
    if not snapshots:
        return []
    ranked = [
        (nav_tree_quality(snapshot, site_prefix=site_prefix, domain=domain), idx, snapshot)
        for idx, snapshot in enumerate(snapshots)
        if snapshot
    ]
    if not ranked:
        return []
    ranked.sort(key=lambda item: (item[0], -item[1]), reverse=True)

    merged = copy.deepcopy(ranked[0][2])
    for _quality, _idx, snapshot in ranked[1:]:
        merge_nav_lists(merged, copy.deepcopy(snapshot))
    return merged


def heading_fragment_id(heading: Tag) -> str:
    for attr in ("id", "name"):
        value = heading.get(attr)
        if value:
            return slugify_anchor(str(value))
    anchor = heading.find("a", attrs={"id": True}) or heading.find("a", attrs={"name": True})
    if isinstance(anchor, Tag):
        value = anchor.get("id") or anchor.get("name")
        if value:
            return slugify_anchor(str(value))
    return slugify_anchor(clean_text(heading.get_text(" ", strip=True)))


def extract_heading_nav_tree(
    content_root: Optional[Tag],
    current_url: str,
    page_title: str = "",
    max_headings: int = 250,
) -> List[NavNode]:
    if content_root is None:
        return []

    headings: List[Tag] = []
    for heading in content_root.find_all(re.compile(r"^h[1-6]$")):
        if is_inside_global_chrome(heading) or is_sidebarish_tag(heading) or is_toc_like_tag(heading):
            continue
        title = clean_nav_title_value(heading.get_text(" ", strip=True))
        if not title:
            continue
        if title.casefold() in {"navigation", "table of contents", "on this page"}:
            continue
        headings.append(heading)
        if len(headings) >= max_headings:
            break

    if len(headings) < 2:
        return []

    root_nodes: List[NavNode] = []
    stack: List[Tuple[int, List[NavNode]]] = [(0, root_nodes)]
    seen_fragments: Set[str] = set()

    for heading in headings:
        title = clean_nav_title_value(heading.get_text(" ", strip=True))
        if not title:
            continue
        try:
            level = int(heading.name[1])
        except Exception:
            level = 2
        fragment = heading_fragment_id(heading)
        if not fragment:
            continue
        base_fragment = fragment
        suffix = 2
        while fragment in seen_fragments:
            fragment = f"{base_fragment}-{suffix}"
            suffix += 1
        seen_fragments.add(fragment)

        node = NavNode(title=title, href=url_with_fragment(current_url, fragment), kind="heading")
        while len(stack) > 1 and stack[-1][0] >= level:
            stack.pop()
        stack[-1][1].append(node)
        stack.append((level, node.children))

    return dedupe_nav(root_nodes)


def content_internal_doc_link_count(
    content_root: Optional[Tag],
    domain: str,
    base_url: str,
    site_prefix: Optional[str],
    profile: str = "generic",
) -> int:
    if content_root is None:
        return 0
    count = 0
    seen: Set[str] = set()
    for a in content_root.select("a[href]"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        abs_url, _frag = split_and_normalize(base_url, href)
        parts = urlsplit(abs_url)
        if parts.netloc != domain:
            continue
        if not url_path_in_prefix(abs_url, site_prefix):
            continue
        if Path(parts.path).suffix.lower() not in DOC_PAGE_EXTENSIONS:
            continue
        if should_skip_crawl_url(abs_url, link_text=link_visible_text(a), profile=profile, allow_javadoc=profile == "javadoc"):
            continue
        if abs_url in seen:
            continue
        seen.add(abs_url)
        count += 1
    return count


def cleanup_nav_tree(nodes: List[NavNode]) -> List[NavNode]:

    cleaned: List[NavNode] = []
    for node in nodes:
        node = copy.deepcopy(node)
        if node.href:
            node.href = repair_legacy_maven_javadoc_url(node.href, node.title)
        if node.children:
            node.children = cleanup_nav_tree(node.children)
        merge_nav_lists(cleaned, [node])
    return dedupe_nav(cleaned)


def resolve_known_href(
    href: Optional[str],
    known_urls: Set[str],
    alias: Dict[str, str],
) -> Optional[str]:
    if not href:
        return None
    href = repair_legacy_maven_javadoc_url(href)
    base_url, fragment = split_stored_href(href)
    if not base_url:
        return None

    candidates = [base_url, *sorted(url_equivalence_variants(base_url))]
    for candidate in candidates:
        canon = alias.get(candidate, candidate)
        if canon in known_urls:
            return url_with_fragment(canon, fragment)
    return None


def filter_nav_to_known_urls(
    nodes: List[NavNode],
    known_urls: Set[str],
    alias: Dict[str, str],
) -> List[NavNode]:



    out: List[NavNode] = []
    for node in nodes:
        node = copy.deepcopy(node)
        children = filter_nav_to_known_urls(node.children, known_urls, alias) if node.children else []

        resolved_href = resolve_known_href(node.href, known_urls, alias)
        node.href = resolved_href
        node.children = children

        if node.href or node.children:
            out.append(node)

    return dedupe_nav(out)

