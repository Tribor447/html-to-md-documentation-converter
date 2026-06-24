#unicode, decoding, and general text helpers

from __future__ import annotations

from bs4 import UnicodeDammit
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
import re
import requests

from .constants import (
    MOJIBAKE_HINT_RE,
    SOFT_SPACE_RE,
    ZERO_WIDTH_RE,
)


def dedupe_preserve_order(items: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen: Set[str] = set()
    for item in items:
        if not item or item in seen:
            continue
        out.append(item)
        seen.add(item)
    return out


def normalize_unicode_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = ZERO_WIDTH_RE.sub("", text)
    text = text.replace("\u00ad", "")
    text = SOFT_SPACE_RE.sub(" ", text)
    text = text.replace("\u2028", "\n").replace("\u2029", "\n")
    return text


def mojibake_badness(text: str) -> int:
    score = 0
    score += len(MOJIBAKE_HINT_RE.findall(text)) * 10
    score += text.count("�") * 20
    score += text.count("\x00") * 50
    return score


def maybe_fix_mojibake(text: str) -> str:
    text = normalize_unicode_text(text)
    best = text
    best_score = mojibake_badness(text)
    for enc in ("latin-1", "cp1252"):
        try:
            repaired = text.encode(enc).decode("utf-8")
        except Exception:
            continue
        repaired = normalize_unicode_text(repaired)
        score = mojibake_badness(repaired)
        if score < best_score:
            best = repaired
            best_score = score
    return best


def decode_response_text(resp: requests.Response) -> str:
    payload = resp.content
    text: Optional[str] = None

    dammit = UnicodeDammit(payload, is_html=True, smart_quotes_to=None)
    if dammit.unicode_markup:
        text = dammit.unicode_markup

    if text is None:
        candidates = dedupe_preserve_order([
            getattr(resp, "apparent_encoding", None) or "",
            getattr(resp, "encoding", None) or "",
            "utf-8", "utf-8-sig", "cp1252", "latin-1",
        ])
        for enc in candidates:
            try:
                text = payload.decode(enc)
                break
            except Exception:
                continue

    if text is None:
        text = payload.decode("utf-8", errors="replace")
    return normalize_unicode_text(maybe_fix_mojibake(text))


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()

