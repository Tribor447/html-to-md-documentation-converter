#output paths, anchors, asset names, and bundle metadata helpers

from __future__ import annotations

from pathlib import Path
from typing import Optional
from typing import Set
from urllib.parse import urlsplit
import mimetypes
import os

from .text import clean_text
from .urls import slugify_anchor


def url_to_rel_output(url: str, site_prefix: str) -> Path:
    path = urlsplit(url).path
    rel = path[len(site_prefix):] if path.startswith(site_prefix) else path.lstrip("/")
    rel = rel.lstrip("/")
    if not rel or rel.endswith("/"):
        rel = rel.rstrip("/")
        if rel:
            return Path(rel) / "index.md"
        return Path("index.md")
    suffix = Path(rel).suffix.lower()
    if suffix:
        rel = str(Path(rel).with_suffix(".md"))
    else:
        rel = rel + ".md"
    return Path(rel)


def uniquify_path(path: Path, taken: Set[Path]) -> Path:
    if path not in taken:
        return path
    counter = 2
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if candidate not in taken:
            return candidate
        counter += 1


def virtual_path_to_page_anchor(path: Path) -> str:
    rel = path
    if rel.parts and rel.parts[0] == "docs":
        rel = Path(*rel.parts[1:]) if len(rel.parts) > 1 else Path("index.md")
    parts = list(rel.parts)
    if parts and parts[-1] == "index.md":
        parts = parts[:-1] or ["index"]
    elif parts:
        parts[-1] = Path(parts[-1]).stem
    return slugify_anchor("-".join(parts) or "index")


def compose_heading_anchor(page_anchor: str, fragment: str) -> str:
    frag = slugify_anchor(fragment)
    return f"{page_anchor}--{frag}"


def derive_bundle_title(entry_url: str, entry_title: str, site_slug: str) -> str:
    if entry_title:
        clean = clean_text(entry_title)
        if clean:
            return clean
    host = urlsplit(entry_url).netloc
    return site_slug.replace("_", " ").title() or host


def path_relative_to(current_output: Optional[Path], target: Path) -> str:
    if current_output is None:
        return target.as_posix()
    rel = os.path.relpath(target, start=current_output.parent)
    return Path(rel).as_posix()


def extension_for_asset(final_url: str, content_type: Optional[str]) -> str:
    ext = Path(urlsplit(final_url).path).suffix
    if ext:
        return ext
    if content_type:
        guessed = mimetypes.guess_extension(content_type, strict=False)
        if guessed:
            return guessed
    return ".bin"

