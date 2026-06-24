#HTML cleanup and Markdown rendering helpers

from __future__ import annotations

from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
from markdownify import markdownify as md
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
import copy
import html
import re

from .constants import (
    ADMONITION_KIND_MAP,
    CALL_OUT_KIND_MAP,
    INLINE_BREAK_PARENT_TAGS,
    RAW_HTML_BLOCK_TAGS,
    SANITIZED_HTML_ATTRS,
    SIDEBAR_CONTEXT_RE,
    SKIP_TEXT_NORMALIZATION_TAGS,
    TOC_CONTEXT_RE,
)
from .html_analysis import (
    generic_content_candidate_score,
    tag_context_signature,
)
from .text import (
    clean_text,
    maybe_fix_mojibake,
    normalize_unicode_text,
)

ADMONITION_STYLE = "callout"


def set_admonition_style(style: str) -> None:
    """Set the process-wide Markdown admonition rendering style."""
    if style not in {"callout", "html"}:
        raise ValueError(f"unsupported admonition style: {style}")
    global ADMONITION_STYLE
    ADMONITION_STYLE = style


def is_inside_tags(node: NavigableString, tag_names: Set[str]) -> bool:
    parent = node.parent
    while isinstance(parent, Tag):
        if parent.name in tag_names:
            return True
        parent = parent.parent
    return False


def normalize_dom_text_nodes(root: Tag) -> None:
    for node in list(root.find_all(string=True)):
        if not isinstance(node, NavigableString):
            continue
        if is_inside_tags(node, SKIP_TEXT_NORMALIZATION_TAGS):
            continue
        original = str(node)
        cleaned = maybe_fix_mojibake(original)
        cleaned = normalize_unicode_text(cleaned)
        if cleaned != original:
            node.replace_with(NavigableString(cleaned))


def has_block_descendants(parent: Tag) -> bool:
    for child in parent.find_all(True, recursive=False):
        if child.name in {
            "table", "ul", "ol", "dl", "pre", "code", "blockquote",
            "section", "article", "aside", "nav", "header", "footer",
            "div", "p",
        } and child.name != "br":
            return True
    return False


def replace_inline_breaks(root: Tag) -> None:
    for br in list(root.find_all("br")):
        parent = br.parent
        if not isinstance(parent, Tag):
            br.replace_with(NavigableString(" "))
            continue
        if parent.name in SKIP_TEXT_NORMALIZATION_TAGS:
            br.replace_with(NavigableString("\n"))
            continue
        if parent.name in INLINE_BREAK_PARENT_TAGS and not has_block_descendants(parent):
            br.replace_with(NavigableString(" "))
        else:
            br.replace_with(NavigableString("\n"))


def collapse_accidental_hardbreaks(text: str) -> str:
    text = re.sub(
        r"(?<=\S) {2,}\n(?=(?:\[[^\]]+\]\([^)]+\)|<a\b|[A-Za-z0-9_(@`]))",
        " ", text,
    )
    text = re.sub(
        r"(?<=,)\n(?=(?:\[[^\]]+\]\([^)]+\)|<a\b|[A-Za-z0-9_(@`]))",
        " ", text,
    )
    return text


def clone_tag(node: Tag) -> Tag:
    soup = BeautifulSoup(str(node), "html.parser")
    cloned = soup.find()
    assert cloned is not None
    return cloned


def sanitize_raw_html_tree(root: Tag) -> None:
    for tag in root.find_all(True):
        attrs_to_drop = [name for name in list(tag.attrs) if name not in SANITIZED_HTML_ATTRS]
        for name in attrs_to_drop:
            del tag.attrs[name]
        if tag.has_attr("href"):
            tag["href"] = str(tag["href"])
        if tag.has_attr("src"):
            tag["src"] = str(tag["src"])


def extract_preformatted_text(pre: Tag) -> Tuple[str, str]:
    language = detect_code_language(pre) or detect_code_language(pre.find("code"))

    line_nodes = find_code_line_nodes(pre)
    if line_nodes:
        lines = [extract_inline_text(node).replace("\xa0", " ") for node in line_nodes]
        text = "\n".join(line.rstrip("\n") for line in lines)
        text = clean_extracted_code_text(text)
        return repair_shell_command_wrapping(text, language), language

    code = pre.find("code")
    if code is not None:
        if not language:
            language = detect_code_language(code)
        text = code.get_text("", strip=False)
    else:
        text = pre.get_text("", strip=False)
    text = clean_extracted_code_text(text)
    return repair_shell_command_wrapping(text, language), language


def detect_code_language(node: Optional[Tag]) -> str:
    if node is None:
        return ""
    classes = node.get("class", [])
    for cls in classes:
        if cls.startswith("language-"):
            return cls.split("language-", 1)[1]
        if cls.startswith("lang-"):
            return cls.split("lang-", 1)[1]
        if cls.startswith("highlight-"):
            return cls.split("highlight-", 1)[1]
    if node.has_attr("data-lang"):
        return str(node["data-lang"])
    if node.has_attr("data-language"):
        return str(node["data-language"])
    return ""


def find_code_line_nodes(root: Tag) -> List[Tag]:
    selectors = [
        ".token-line", ".line",
        "[class*=tokenLine]", "[class*=codeLine]",
        ".code-line", "[class*=lineContent]",
        "[class~=line]",
        "[data-code-line]",
        'span[style*="display:block"]',
    ]
    for selector in selectors:
        matches = list(root.select(selector))
        if not matches:
            continue
        filtered = [
            node for node in matches
            if not any(
                isinstance(parent, Tag) and parent is not root and parent in matches
                for parent in node.parents
            )
        ]
        if filtered and line_node_candidates_are_reasonable(filtered, root):
            return filtered

    direct_tag_children = [child for child in root.children if isinstance(child, Tag)]
    if direct_tag_children and not any(
        isinstance(child, NavigableString) and clean_text(str(child))
        for child in root.children
    ):
        if all(child.name in {"div", "p", "span"} for child in direct_tag_children):
            return direct_tag_children
    return []


def extract_inline_text(node) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if not isinstance(node, Tag):
        return ""
    pieces: List[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            pieces.append(str(child))
        elif isinstance(child, Tag):
            if child.name == "br":
                pieces.append("\n")
            else:
                pieces.append(extract_inline_text(child))
    return "".join(pieces)


def repair_shell_command_wrapping(text: str, language: str) -> str:
    lang = (language or "").lower()
    if lang not in {"", "bash", "shell", "sh", "zsh", "console", "terminal", "shell-session"}:
        return text

    lines = text.splitlines()
    out: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        if re.match(r"^\s*(?:\$|#|>|%|PS>)(?:\s.*)?$", stripped):
            parts = [stripped]
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if not nxt:
                    break
                if re.match(r"^(?:\$|#|>|%|PS>)\s", nxt):
                    break
                if looks_like_command_output(nxt):
                    break
                parts.append(nxt)
                j += 1
            out.append(normalize_shell_fragments(parts))
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def looks_like_command_output(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if re.match(r"^[A-Za-z0-9_.-]+\s*=\s*.+$", stripped):

        return True
    if re.match(r"^[A-Za-z]:\\", stripped):
        return True
    if re.match(r"^/[A-Za-z0-9_.-]+", stripped):
        return True
    if re.match(r"^(?:Error|Warning|Note|INFO|DEBUG|TRACE)\b", stripped, re.I):
        return True
    return False


def normalize_shell_fragments(parts: List[str]) -> str:
    prompt = parts[0]
    rest = [frag.strip() for frag in parts[1:] if frag.strip()]
    if not rest:
        return prompt
    merged = prompt.rstrip()
    for frag in rest:
        if merged.endswith(("=", ":", ",", "(", "[", "{", "/", "-")):
            merged += frag
        elif frag.startswith(("=", ":", ",", ".", ")", "]", "}", "/", ";")):
            merged += frag
        else:
            merged += " " + frag
    return re.sub(r"\s+", " ", merged).strip()


def looks_like_admonition(node: Tag) -> bool:
    attrs = " ".join([node.get("id", ""), *node.get("class", []), node.name]).lower()
    if any(word in attrs for word in ["admonition", "alert", "callout", "notice", "hint"]):
        return True
    heading = find_admonition_heading(node)
    heading_text = clean_text(heading.get_text(" ", strip=True)).lower() if heading else ""
    if heading_text in ADMONITION_KIND_MAP:
        return True
    return False


def looks_like_tab_container(node: Tag) -> bool:
    classes = " ".join(node.get("class", []))
    if "tabs-container" in classes:
        return True
    if "tabs" in classes and node.get("role") == "tablist":
        return True
    return False


def nearest_table_ancestor(tag: Tag) -> Optional[Tag]:
    current = tag.parent
    while isinstance(current, Tag):
        if current.name == "table":
            return current
        current = current.parent
    return None


def direct_table_rows(table: Tag) -> List[Tag]:
    rows: List[Tag] = []
    for tr in table.find_all("tr"):
        if nearest_table_ancestor(tr) is table:
            rows.append(tr)
    return rows


def direct_row_cells(row: Tag) -> List[Tag]:
    cells: List[Tag] = []
    for cell in row.find_all(["td", "th"], recursive=False):
        cells.append(cell)
    return cells


def direct_table_cells(table: Tag) -> List[Tag]:
    cells: List[Tag] = []
    for row in direct_table_rows(table):
        cells.extend(direct_row_cells(row))
    if not cells:
        for cell in table.find_all(["td", "th"]):
            if nearest_table_ancestor(cell) is table:
                cells.append(cell)
    return cells


def table_has_nested_tables(table: Tag) -> bool:
    return any(nested is not table for nested in table.find_all("table"))


def table_attr_text(table: Tag) -> str:
    return " ".join([
        table.name or "",
        str(table.get("id", "")),
        *[str(cls) for cls in table.get("class", [])],
        str(table.get("role", "")),
        str(table.get("summary", "")),
    ]).lower()


def table_has_layout_attrs(table: Tag) -> bool:
    attrs = table_attr_text(table)
    if re.search(r"(?:^|[-_\s])(?:layout|container|wrapper|shell|page|main|content|body|columns?|grid)(?:$|[-_\s])", attrs):
        return True
    border = str(table.get("border") or "").strip()
    cellpadding = str(table.get("cellpadding") or "").strip()
    cellspacing = str(table.get("cellspacing") or "").strip()
    width = str(table.get("width") or "").strip()
    if border in {"0", "", "none"} and (width in {"100%", "100", ""} or cellpadding or cellspacing):
        return True
    return False


def cell_is_probably_chrome(cell: Tag) -> bool:
    text_len = len(clean_text(cell.get_text(" ", strip=True)))
    attrs = tag_context_signature(cell, max_ancestors=2)
    if SIDEBAR_CONTEXT_RE.search(attrs) or TOC_CONTEXT_RE.search(attrs):
        return True
    links = cell.find_all("a", href=True)
    if not links:
        return False
    link_text_len = sum(len(clean_text(a.get_text(" ", strip=True))) for a in links)
    link_density = link_text_len / max(text_len, 1)
    paragraphs = len(cell.find_all("p"))
    headings = len(cell.find_all(re.compile(r"^h[1-6]$")))
    if len(links) >= 5 and link_density > 0.45 and paragraphs < 2 and headings < 2:
        return True
    if len(links) >= 12 and paragraphs < 3:
        return True
    return False


def cell_is_contentish(cell: Tag) -> bool:
    text_len = len(clean_text(cell.get_text(" ", strip=True)))
    if text_len >= 500:
        return True
    if cell.find(re.compile(r"^h[1-6]$")) and text_len >= 80:
        return True
    if cell.find("pre") or cell.find("blockquote"):
        return True
    if len(cell.find_all("p")) >= 2 and text_len >= 180:
        return True
    if table_has_nested_tables(cell):
        return True
    return False


def table_row_widths(table: Tag) -> List[int]:
    widths: List[int] = []
    for row in direct_table_rows(table):
        cells = direct_row_cells(row)
        if cells:
            widths.append(len(cells))
    return widths


def looks_like_data_table(node: Tag) -> bool:
    if node.name != "table":
        return False
    if table_has_nested_tables(node):
        return False
    rows = direct_table_rows(node)
    cells = direct_table_cells(node)
    if len(rows) < 2 or len(cells) < 4:
        return False
    widths = [len(direct_row_cells(row)) for row in rows if direct_row_cells(row)]
    if not widths or max(widths) < 2:
        return False
    common_width = max(set(widths), key=widths.count)
    if widths.count(common_width) / max(len(widths), 1) < 0.60:
        return False
    direct_headers = [cell for cell in cells if cell.name == "th"]
    if direct_headers:
        return True
    heavy_cells = sum(1 for cell in cells if cell_is_contentish(cell))
    short_first_row = all(len(clean_text(cell.get_text(" ", strip=True))) <= 80 for cell in direct_row_cells(rows[0]))
    return heavy_cells == 0 and short_first_row and len(rows) >= 3


def looks_like_layout_table(node: Tag) -> bool:
    if node.name != "table":
        return False

    rows = direct_table_rows(node)
    cells = direct_table_cells(node)
    if not rows and not cells:
        return False

    widths = table_row_widths(node)
    if widths and max(widths) <= 1:
        return True

    if table_has_nested_tables(node):
        return True

    if looks_like_data_table(node):
        return False

    if table_has_layout_attrs(node):
        return True

    text_len = len(clean_text(node.get_text(" ", strip=True)))
    headings = len(node.find_all(re.compile(r"^h[1-6]$")))
    pre_blocks = len(node.find_all("pre"))
    paragraphs = len(node.find_all("p"))
    direct_headers = any(cell.name == "th" for cell in cells)

    chrome_cells = sum(1 for cell in cells[:16] if cell_is_probably_chrome(cell))
    content_cells = sum(1 for cell in cells[:16] if cell_is_contentish(cell))
    if chrome_cells >= 1 and content_cells >= 1:
        return True

    if not direct_headers and text_len >= 600 and (headings >= 1 or pre_blocks >= 1 or paragraphs >= 2):
        if len(rows) <= 6 or content_cells >= 1:
            return True

    if widths and len(set(widths)) > 2 and not direct_headers:
        return True

    return False


def best_layout_content_cell(root: Tag) -> Optional[Tag]:
    tables: List[Tag] = []
    if isinstance(root, Tag) and root.name == "table":
        tables.append(root)
    tables.extend([table for table in root.find_all("table") if isinstance(table, Tag)])

    best_cell: Optional[Tag] = None
    best_score = -10**9
    for table in tables:
        if not looks_like_layout_table(table):
            continue
        for cell in direct_table_cells(table):
            text_len = len(clean_text(cell.get_text(" ", strip=True)))
            if text_len < 20:
                continue
            if cell_is_probably_chrome(cell):
                continue
            score = generic_content_candidate_score(cell)
            score += min(text_len, 5000)
            if cell.find(re.compile(r"^h[1-6]$")):
                score += 900
            if cell.find("pre"):
                score += 600
            if table_has_nested_tables(cell):
                score += 300
            if cell.find("iframe") or cell.find("object") or cell.find("embed"):
                score -= 3000
            if score > best_score:
                best_score = score
                best_cell = cell
    return best_cell


def unwrap_layout_table_content(root: Tag) -> Tag:
    target: Optional[Tag] = None
    if isinstance(root, Tag) and root.name == "table" and looks_like_layout_table(root):
        target = root
    elif isinstance(root, Tag):
        root_text_len = len(clean_text(root.get_text(" ", strip=True)))
        direct_tables = [child for child in root.find_all("table", recursive=False) if isinstance(child, Tag)]
        for table in direct_tables:
            if not looks_like_layout_table(table):
                continue
            table_text_len = len(clean_text(table.get_text(" ", strip=True)))
            outside_text_len = max(0, root_text_len - table_text_len)
            if table_text_len >= max(200, int(root_text_len * 0.82)) and outside_text_len <= 220:
                target = table
                break
    if target is None:
        return root

    cell = best_layout_content_cell(target)
    if cell is None:
        return root
    wrapper_soup = BeautifulSoup("<div></div>", "html.parser")
    wrapper = wrapper_soup.div
    assert wrapper is not None
    for child in list(cell.children):
        wrapper.append(copy.copy(child))
    return wrapper


def markdownify_table_cell_contents(cell: Tag) -> str:
    wrapper_soup = BeautifulSoup("<div></div>", "html.parser")
    wrapper = wrapper_soup.div
    assert wrapper is not None
    for child in list(cell.children):
        wrapper.append(copy.copy(child))
    return markdownify_fragment(wrapper)


def flatten_layout_table_to_markdown(node: Tag) -> str:
    rows = direct_table_rows(node)
    parts: List[str] = []

    def append_cell(cell: Tag) -> None:
        if cell_is_probably_chrome(cell):
            return
        text = markdownify_table_cell_contents(cell).strip()
        text = re.sub(r"\s*\|\s*$", "", text).strip()
        if not text:
            return
        parts.append(text)

    if rows:
        for row in rows:
            for cell in direct_row_cells(row):
                append_cell(cell)
    else:
        for cell in direct_table_cells(node):
            append_cell(cell)

    if not parts:
        text = clean_text(node.get_text(" ", strip=True))
        return f"\n{text}\n" if text else "\n"
    return "\n\n" + "\n\n".join(parts) + "\n"


def cell_text_for_markdown_table(cell: Tag) -> str:
    wrapper_soup = BeautifulSoup("<div></div>", "html.parser")
    wrapper = wrapper_soup.div
    assert wrapper is not None
    for child in list(cell.children):
        wrapper.append(copy.copy(child))
    for br in list(wrapper.find_all("br")):
        br.replace_with(NavigableString(" "))
    text = markdownify_fragment(wrapper)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*\|\s*$", "", text).strip()
    text = text.replace("|", r"\|")
    return text


def render_markdown_table(node: Tag) -> Optional[str]:
    rows: List[List[str]] = []
    header_seen = False
    for tr in direct_table_rows(node):
        direct_cells = direct_row_cells(tr)
        if not direct_cells:
            continue
        if any((cell.get("rowspan") and str(cell.get("rowspan")).strip() not in {"", "1"}) or (cell.get("colspan") and str(cell.get("colspan")).strip() not in {"", "1"}) for cell in direct_cells):
            return None
        if any(cell.find(["table", "pre", "blockquote", "ul", "ol", "dl"]) for cell in direct_cells):
            return None
        row = [cell_text_for_markdown_table(cell) for cell in direct_cells]
        if not any(row):
            continue
        rows.append(row)
        if any(cell.name == "th" for cell in direct_cells):
            header_seen = True
    if not rows:
        return None
    width = max(len(row) for row in rows)
    if width < 2:
        return None
    normalized = [row + [""] * (width - len(row)) for row in rows]
    if not header_seen:
        first = normalized[0]
        header_seen = len(normalized) >= 3 and all(0 < len(cell) <= 80 for cell in first)
    if not header_seen:
        return None
    header = normalized[0]
    body = normalized[1:]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * width) + " |"]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    return "\n" + "\n".join(lines) + "\n"


def render_html_table(node: Tag) -> str:
    clone = clone_tag(node)
    sanitize_raw_html_tree(clone)
    for tag in clone.find_all(True):
        if tag.name not in {"table", "thead", "tbody", "tfoot", "tr", "th", "td", "caption", "colgroup", "col", "a", "img", "br", "p", "strong", "em", "code", "span", "div", "ul", "ol", "li", "pre"}:
            tag.unwrap()
    return "\n" + str(clone) + "\n"


def table_is_simple(node: Tag) -> bool:
    if table_has_nested_tables(node):
        return False
    for cell in direct_table_cells(node):
        if cell.get("rowspan") and str(cell["rowspan"]).strip() not in {"", "1"}:
            return False
        if cell.get("colspan") and str(cell["colspan"]).strip() not in {"", "1"}:
            return False
        for block in cell.find_all(["ul", "ol", "pre", "table", "blockquote", "dl"]):
            return False
    return True


def render_complex_block(node: Tag) -> str:
    if node.name == "pre":
        return render_code_block(node)
    if looks_like_admonition(node):
        return render_admonition_block(node)
    if node.name == "table":
        if looks_like_layout_table(node):
            return flatten_layout_table_to_markdown(node)
        markdown_table = render_markdown_table(node) if table_is_simple(node) else None
        if markdown_table is not None:
            return markdown_table
        if looks_like_data_table(node):
            return render_html_table(node)
        return flatten_layout_table_to_markdown(node)
    clone = clone_tag(node)
    sanitize_raw_html_tree(clone)
    return "\n" + str(clone) + "\n"


def replace_markdown_placeholders(markdown: str, placeholders: Dict[str, str]) -> str:
    for _ in range(max(1, len(placeholders) + 1)):
        changed = False
        for token, replacement in placeholders.items():
            if token in markdown:
                markdown = markdown.replace(token, replacement)
                changed = True
        if not changed:
            break
    return markdown


def clean_extracted_code_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = maybe_fix_mojibake(text)
    lines = text.splitlines()
    if len(lines) >= 8:
        nonblank = [line for line in lines if line.strip()]
        short_ratio = sum(1 for line in nonblank if len(line.strip()) <= 3) / max(len(nonblank), 1)
        punct_ratio = sum(1 for line in nonblank if re.fullmatch(r"[{}()\[\],.;:=:+\-*/<>!&|]+", line.strip())) / max(len(nonblank), 1)
        if short_ratio > 0.45 or punct_ratio > 0.20:
            rebuilt: List[str] = []
            current = ""
            for raw in lines:
                part = raw.strip()
                if not part:
                    if current.strip():
                        rebuilt.append(current.rstrip())
                        current = ""
                    continue
                if not current:
                    current = part
                elif part in {"::", ".", ",", ";", ":", ")", "]", "}", ">"}:
                    current += part
                    if part == ";":
                        rebuilt.append(current.rstrip())
                        current = ""
                elif current.endswith(("::", ".", "(", "[", "{", "<", "=", ":", ",")):
                    current += part
                elif part in {"(", "[", "{"}:
                    current += " " + part
                else:
                    current += " " + part
            if current.strip():
                rebuilt.append(current.rstrip())
            if rebuilt and sum(len(line) for line in rebuilt) >= max(20, len("".join(nonblank)) // 2):
                text = "\n".join(rebuilt)
    return text


def line_node_candidates_are_reasonable(nodes: List[Tag], root: Tag) -> bool:
    if not nodes:
        return False
    if any(node.name in {"div", "p"} for node in nodes):
        return True
    classes = [" ".join(node.get("class", [])).lower() for node in nodes]
    strong_line_class = any(re.search(r"(?:^|[-_\s])(?:token-line|code-line|line-content|linecontent)(?:$|[-_\s])", cls) for cls in classes)
    if strong_line_class:
        return True
    texts = [extract_inline_text(node).strip() for node in nodes if extract_inline_text(node).strip()]
    if not texts:
        return False
    root_text = root.get_text("", strip=False)
    root_newlines = max(1, root_text.count("\n"))
    if len(texts) > root_newlines + 8:
        short_ratio = sum(1 for t in texts if len(t) <= 3) / len(texts)
        if short_ratio > 0.35:
            return False
    return True


def render_code_block(pre: Tag) -> str:
    text, language = extract_preformatted_text(pre)
    text = text.replace("\r\n", "\n").rstrip("\n")
    fence = "```"
    while fence in text:
        fence += "`"
    return f"\n{fence}{language}\n{text}\n{fence}\n"


def render_admonition_block(node: Tag) -> str:
    clone = clone_tag(node)
    for icon in list(clone.select("[class*=admonitionIcon], [class*=alertIcon], i.fa, i.icon")):
        icon.decompose()
    for svg in list(clone.select("svg")):
        svg.decompose()

    kind = detect_admonition_kind(clone)
    label = CALL_OUT_KIND_MAP.get(kind, "NOTE")
    heading = find_admonition_heading(clone)
    title = clean_text(heading.get_text(" ", strip=True)) if heading is not None else label.title()

    content = find_admonition_content(clone)
    if heading is not None:
        heading.decompose()
        if content is None:
            content = clone
    if content is None:
        content = clone

    content = clone_tag(content)
    admon_md = markdownify_fragment(content)

    if ADMONITION_STYLE == "html":
        border_map = {
            "NOTE": "#2563eb", "TIP": "#16a34a", "IMPORTANT": "#7c3aed",
            "WARNING": "#d97706", "CAUTION": "#dc2626",
        }
        border = border_map.get(label, "#2563eb")
        body_html = markdown_to_safe_html(admon_md)
        return (
            "\n"
            f"<div style=\"border-left:4px solid {border}; padding:0.75rem 1rem; "
            f"margin:1rem 0; background:rgba(127,127,127,0.08);\">"
            f"<p><strong>{html.escape(title or label)}</strong></p>"
            f"{body_html}</div>\n"
        )

    lines: List[str] = [f"> [!{label}]"]
    normalized_title = clean_text(title).upper()
    if normalized_title and normalized_title != label:
        lines.append(f"> **{escape_markdown_text(title)}**")

    body_lines = admon_md.splitlines() or [title]
    prev_blank = False
    for line in body_lines:
        stripped = line.rstrip()
        if not stripped:
            if not prev_blank:
                lines.append(">")
            prev_blank = True
            continue
        lines.append(f"> {stripped}")
        prev_blank = False
    return "\n" + "\n".join(lines).rstrip() + "\n"


def markdown_to_safe_html(text: str) -> str:
    safe = html.escape(text)
    safe = safe.replace("\n\n", "</p><p>").replace("\n", "<br>")
    return f"<p>{safe}</p>"


def escape_markdown_text(text: str) -> str:
    return re.sub(r"([*_`\[\]\\])", r"\\\1", text)


def detect_admonition_kind(node: Tag) -> str:
    classes = [cls.lower() for cls in node.get("class", [])]
    for cls in classes:
        for prefix in ["theme-admonition-", "admonition-", "alert--", "callout-", "notice-"]:
            if cls.startswith(prefix):
                key = cls.split(prefix, 1)[1]
                if key in ADMONITION_KIND_MAP:
                    return ADMONITION_KIND_MAP[key]
        if cls in ADMONITION_KIND_MAP:
            return ADMONITION_KIND_MAP[cls]

    heading = find_admonition_heading(node)
    heading_text = clean_text(heading.get_text(" ", strip=True)).lower() if heading else ""
    for key, mapped in ADMONITION_KIND_MAP.items():
        if heading_text == key or heading_text.startswith(key + " "):
            return mapped
    return "note"


def find_admonition_heading(node: Tag) -> Optional[Tag]:
    selectors = [
        "[class*=admonitionHeading]",
        "[class*=admonitionTitle]",
        "[class*=alertHeading]",
        "[class*=alertTitle]",
        "[class*=callout-title]",
        ".admonition-title",
        ".markdown-alert-title",
        "summary",
    ]
    for selector in selectors:
        match = node.select_one(selector)
        if match is not None:
            return match
    for child in node.find_all(["p", "div", "strong", "summary"], recursive=False):
        text = clean_text(child.get_text(" ", strip=True))
        if text and len(text) <= 140:
            return child
    return None


def find_admonition_content(node: Tag) -> Optional[Tag]:
    selectors = [
        "[class*=admonitionContent]",
        "[class*=alertContent]",
        "[class*=callout-content]",
        ".admonition-content",
        ".markdown-alert-content",
    ]
    for selector in selectors:
        match = node.select_one(selector)
        if match is not None:
            return match
    return None


def markdownify_fragment(root: Tag) -> str:
    fragment = clone_tag(root)
    placeholders: Dict[str, str] = {}
    idx = 0

    complex_nodes: List[Tag] = []
    for tag in list(fragment.find_all(True)):
        if tag.name in RAW_HTML_BLOCK_TAGS:
            complex_nodes.append(tag)
            continue
        if tag.name == "pre":
            complex_nodes.append(tag)
            continue
        if tag.name == "code" and tag.parent and tag.parent.name == "pre":
            continue
        if tag.name == "table":
            complex_nodes.append(tag)
            continue
        if looks_like_tab_container(tag):
            complex_nodes.append(tag)
            continue
        if looks_like_admonition(tag):
            complex_nodes.append(tag)
            continue

    processed: Set[int] = set()
    for node in complex_nodes:
        if id(node) in processed:
            continue
        if any(id(parent) in processed for parent in node.parents if isinstance(parent, Tag)):
            continue
        token = f"DOC2MDFRAGMENTTOKEN{idx}END"
        idx += 1
        placeholders[token] = render_complex_block(node)
        processed.add(id(node))
        node.replace_with(NavigableString(f"\n\n{token}\n\n"))

    html_text = str(fragment)
    markdown = md(html_text, heading_style="ATX", bullets="-", strong_em_symbol="*")
    markdown = replace_markdown_placeholders(markdown, placeholders)
    return postprocess_markdown(markdown)


def html_fragment_to_markdown(root: Tag) -> str:
    return root.get_text("", strip=False)


def protect_fenced_code_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    placeholders: Dict[str, str] = {}
    pattern = re.compile(r"(?ms)^(?P<fence>`{3,})(?P<info>[^\n]*)\n.*?^(?P=fence)[ \t]*$")

    def repl(match: re.Match[str]) -> str:
        token = f"DOC2MDCODEBLOCKTOKEN{len(placeholders)}END"
        placeholders[token] = match.group(0)
        return token

    return pattern.sub(repl, text), placeholders


def restore_placeholders(text: str, placeholders: Dict[str, str]) -> str:
    for token, block in placeholders.items():
        text = text.replace(token, block)
    return text


def postprocess_markdown(text: str) -> str:
    text = maybe_fix_mojibake(text)
    text = normalize_unicode_text(text)
    text = text.replace("\r\n", "\n")
    protected, placeholders = protect_fenced_code_blocks(text)
    protected = collapse_accidental_hardbreaks(protected)
    protected = re.sub(r"(\]\([^\)]+\))(?=\[)", r"\1\n", protected)
    protected = re.sub(r"\n{3,}", "\n\n", protected)
    protected = re.sub(r"[ \t]+\n", "\n", protected)
    protected = re.sub(r"\n([*-] )\n", r"\n\1", protected)
    text = restore_placeholders(protected, placeholders)
    return text.strip() + "\n"


def starts_with_markdown_heading(text: str) -> bool:
    probe = text.lstrip()
    probe = re.sub(r'^(?:<a\s+id="[^"]+"></a>\s*)+', "", probe)
    probe = probe.lstrip()
    return bool(re.match(r"^#{1,6}\s+", probe))


def repair_combined_markdown_layout(text: str) -> str:
    protected, placeholders = protect_fenced_code_blocks(text)
    protected = normalize_unicode_text(protected)
    protected = re.sub(r"(?<!\n)(##\s+Navigation\b)", r"\n\n\1", protected)
    protected = re.sub(r"(?<!\n)(##\s+Content\b)", r"\n\n\1", protected)
    protected = re.sub(r"(?<!\n)(<!--\s*source_url:)", r"\n\n\1", protected)
    protected = re.sub(r"(?<!\n)(<!--\s*page_index:)", r"\n\1", protected)
    protected = re.sub(r'(?<!\n)(<a\s+id=")', r'\n\n\1', protected)
    protected = re.sub(
        r"(?<=[^\s\n])(?P<indent>[ \t]*)(?P<item>-\s+\[[^\]]+\]\(#)",
        lambda match: "\n" + match.group("indent") + match.group("item"),
        protected,
    )
    protected = re.sub(r"\n{4,}", "\n\n\n", protected)
    return restore_placeholders(protected, placeholders).strip() + "\n"

