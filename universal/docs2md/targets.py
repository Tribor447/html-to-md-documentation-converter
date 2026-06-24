#CLI target URL loading and validation

from __future__ import annotations

from pathlib import Path
from typing import List
from typing import Optional
from urllib.parse import urlsplit
import re

from .text import dedupe_preserve_order
from .urls import normalize_url


def normalize_target_url(raw: str) -> Optional[str]:
    raw = (raw or "").strip()
    if not raw or raw.startswith("#"):
        return None
    if not re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", raw):
        if re.match(r"^[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/|$)", raw):
            raw = "https://" + raw
        else:
            return None
    parts = urlsplit(raw)
    if parts.scheme.lower() not in {"http", "https"} or not parts.netloc:
        return None
    return normalize_url(raw)


def load_targets(targets_file: Optional[Path], urls: List[str]) -> List[str]:
    out: List[str] = []
    for raw in urls:
        target = normalize_target_url(raw)
        if target:
            out.append(target)
    if targets_file is not None:
        for line in targets_file.read_text(encoding="utf-8").splitlines():
            target = normalize_target_url(line)
            if target:
                out.append(target)
    return dedupe_preserve_order(out)

