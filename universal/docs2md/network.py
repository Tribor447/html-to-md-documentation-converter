#HTTP cache, rate limiting, requests session, and browser rendering

from __future__ import annotations

from bs4 import BeautifulSoup
from pathlib import Path
from requests.adapters import HTTPAdapter
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from urllib.parse import urlsplit
from urllib3.util.retry import Retry
import hashlib
import json
import re
import requests
import threading
import time
import urllib.robotparser

try:
    from playwright.sync_api import Browser, sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except Exception:
    Browser = None
    sync_playwright = None
    PLAYWRIGHT_AVAILABLE = False

from .constants import (
    CACHE_SCHEMA_VERSION,
    DEFAULT_MAX_ASSET_BYTES,
    HTTP_TIMEOUT,
    USER_AGENT,
)
from .html_analysis import (
    compute_content_score,
    detect_profile,
    select_content_root,
    select_nav_root,
)
from .models import FetchResult
from .text import (
    clean_text,
    decode_response_text,
    maybe_fix_mojibake,
    normalize_unicode_text,
)
from .urls import normalize_url


class RateLimiter:


    def __init__(self, min_interval: float) -> None:
        self.min_interval = max(0.0, min_interval)
        self._last: Dict[str, float] = {}
        self._lock = threading.Lock()


    def wait(self, domain: str) -> None:
        if self.min_interval <= 0:
            return
        while True:
            with self._lock:
                now = time.monotonic()
                last = self._last.get(domain, 0.0)
                wait_for = self.min_interval - (now - last)
                if wait_for <= 0:
                    self._last[domain] = now
                    return
            time.sleep(wait_for)


class HttpCache:


    def __init__(self, root: Path, enabled: bool = True) -> None:
        self.root = root
        self.enabled = enabled
        self.root.mkdir(parents=True, exist_ok=True)
        self._index_path = root / "index.json"
        self._index: Dict[str, Dict[str, str]] = {}
        self._lock = threading.Lock()
        self._dirty_writes = 0
        if enabled and self._index_path.exists():
            try:
                self._index = json.loads(self._index_path.read_text(encoding="utf-8"))
            except Exception:
                self._index = {}
        schema = self._index.get("__schema__", {}) if isinstance(self._index, dict) else {}
        if not isinstance(schema, dict) or schema.get("version") != CACHE_SCHEMA_VERSION:
            self._index = {"__schema__": {"version": CACHE_SCHEMA_VERSION}}

    def _key(self, url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()[:24]

    def _path_for(self, key: str) -> Path:
        return self.root / f"{key}.html"

    def get(self, url: str) -> Optional[Tuple[str, str]]:
        if not self.enabled:
            return None
        key = self._key(url)
        with self._lock:
            entry = self._index.get(key)
        if not entry:
            return None
        path = self._path_for(key)
        if not path.exists():
            return None
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            return None
        return text, entry.get("final_url", url)

    def put(self, url: str, text: str, final_url: str) -> None:
        if not self.enabled:
            return
        key = self._key(url)
        path = self._path_for(key)
        try:
            path.write_text(text, encoding="utf-8")
        except Exception:
            return
        with self._lock:
            self._index[key] = {"url": url, "final_url": final_url}
            self._dirty_writes += 1
           
           
           
            if self._dirty_writes >= 25:
                self._flush_locked()

    def flush(self) -> None:
        if not self.enabled:
            return
        with self._lock:
            self._flush_locked()

    def _flush_locked(self) -> None:
        try:
            self._index_path.write_text(
                json.dumps(self._index, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            self._dirty_writes = 0
        except Exception:
            pass


class BrowserPool:


    def __init__(self, timeout_ms: int) -> None:
        self.timeout_ms = timeout_ms
        self._pw = None
        self._browser: Optional["Browser"] = None
        self._lock = threading.Lock()

    def _ensure(self) -> None:
        if self._browser is not None:
            return
        if not PLAYWRIGHT_AVAILABLE:
            raise RuntimeError("Playwright is not installed")
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=True)

    def render(self, url: str) -> Tuple[str, str]:
        with self._lock:
            self._ensure()
            assert self._browser is not None
            context = self._browser.new_context(user_agent=USER_AGENT)
            page = context.new_page()
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=self.timeout_ms)
                try:
                    page.wait_for_load_state("networkidle", timeout=self.timeout_ms)
                except Exception:
                    pass
                page.wait_for_timeout(250)
                html_text = page.content()
                final_url = normalize_url(page.url)
            finally:
                page.close()
                context.close()
        html_text = maybe_fix_mojibake(normalize_unicode_text(html_text))
        return html_text, final_url

    def close(self) -> None:
        with self._lock:
            try:
                if self._browser is not None:
                    self._browser.close()
            finally:
                self._browser = None
            try:
                if self._pw is not None:
                    self._pw.stop()
            finally:
                self._pw = None


def build_session() -> requests.Session:
    session = requests.Session()
    retries = Retry(
        total=3, connect=3, read=3, backoff_factor=0.4,
        allowed_methods=frozenset(["GET", "HEAD"]),
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retries, pool_connections=96, pool_maxsize=96)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": USER_AGENT})
    return session


class Fetcher:


    def __init__(
        self,
        session: requests.Session,
        cache: HttpCache,
        rate_limiter: RateLimiter,
        browser_pool: Optional[BrowserPool],
        browser_mode: str = "never",
        respect_robots: bool = True,
        max_asset_bytes: int = DEFAULT_MAX_ASSET_BYTES,
    ) -> None:
        self.session = session
        self.cache = cache
        self.rate_limiter = rate_limiter
        self.browser_pool = browser_pool
        self.browser_mode = browser_mode
        self.respect_robots = respect_robots
        self.max_asset_bytes = max_asset_bytes
        self._robots: Dict[str, urllib.robotparser.RobotFileParser] = {}
        self._robots_lock = threading.Lock()

   

    def _robots_for(self, url: str) -> Optional[urllib.robotparser.RobotFileParser]:
        if not self.respect_robots:
            return None
        parts = urlsplit(url)
        base = f"{parts.scheme}://{parts.netloc}"
        with self._robots_lock:
            if base in self._robots:
                return self._robots[base]
        rp = urllib.robotparser.RobotFileParser()
        try:
            resp = self.session.get(base + "/robots.txt", timeout=HTTP_TIMEOUT)
            if resp.status_code < 400 and resp.text:
                rp.parse(resp.text.splitlines())
            else:
                rp.parse([])
        except Exception:
            rp.parse([])
        with self._robots_lock:
            self._robots[base] = rp
        return rp

    def allowed_by_robots(self, url: str) -> bool:
        rp = self._robots_for(url)
        if rp is None:
            return True
        try:
            return rp.can_fetch(USER_AGENT, url)
        except Exception:
            return True

   

    def fetch_text(self, url: str) -> FetchResult:
        url = normalize_url(url)
        cached = self.cache.get(url)
        if cached is not None:
            text, final_url = cached
            return FetchResult(text=text, final_url=final_url, from_cache=True)

        if self.browser_mode == "always" and self.browser_pool is not None:
            self.rate_limiter.wait(urlsplit(url).netloc)
            text, final_url = self.browser_pool.render(url)
            self.cache.put(url, text, final_url)
            return FetchResult(text=text, final_url=final_url)

        self.rate_limiter.wait(urlsplit(url).netloc)
        resp = self.session.get(url, timeout=HTTP_TIMEOUT)
        resp.raise_for_status()
        text = decode_response_text(resp)
        final_url = normalize_url(resp.url)

        if (
            self.browser_mode == "auto"
            and self.browser_pool is not None
            and should_try_browser_render(text, url)
        ):
            try:
                b_text, b_final = self.browser_pool.render(url)
                if b_text and browser_quality_score(b_text) > browser_quality_score(text):
                    text, final_url = b_text, b_final
            except Exception as exc:
                print(f"[warn] browser render failed for {url}: {exc}")

        self.cache.put(url, text, final_url)
        return FetchResult(text=text, final_url=final_url)

   

    def fetch_binary(self, url: str) -> Tuple[bytes, str, Optional[str]]:
        self.rate_limiter.wait(urlsplit(url).netloc)
        with self.session.get(url, timeout=HTTP_TIMEOUT, stream=True) as resp:
            resp.raise_for_status()
            content_length = resp.headers.get("content-length")
            if content_length and content_length.isdigit():
                if int(content_length) > self.max_asset_bytes:
                    raise ValueError(
                        f"asset too large: {content_length} bytes > "
                        f"{self.max_asset_bytes}"
                    )
            content_type = resp.headers.get("content-type", "").split(";", 1)[0].strip()
            chunks: List[bytes] = []
            total = 0
            for chunk in resp.iter_content(chunk_size=65536):
                if not chunk:
                    continue
                total += len(chunk)
                if total > self.max_asset_bytes:
                    raise ValueError(
                        f"asset exceeded size limit of {self.max_asset_bytes} bytes"
                    )
                chunks.append(chunk)
            payload = b"".join(chunks)
            final_url = normalize_url(resp.url)
        return payload, final_url, content_type or None


def should_try_browser_render(text: str, url: Optional[str] = None) -> bool:
    if not PLAYWRIGHT_AVAILABLE:
        return False
    soup = BeautifulSoup(text, "html.parser")
    script_count = len(soup.find_all("script"))
    body_text = clean_text(soup.get_text(" ", strip=True))

    if len(body_text) < 250:
        shell_ids = {"app", "root", "__docusaurus", "__next", "vitepress", "content"}
        for node in soup.select("[id]"):
            if node.get("id", "") in shell_ids:
                return True
        if script_count >= 5:
            return True

    if soup.find(string=re.compile(r"enable javascript|requires javascript", re.I)):
        return True

    root = select_content_root(soup)
    if root is None or len(clean_text(root.get_text(" ", strip=True))) < 180:
        if script_count >= 6:
            return True

   
   
   
   
    if url and script_count >= 5:
        parts = urlsplit(url)
        if parts.netloc:
            profile = detect_profile(soup, url)
            nav_root = select_nav_root(
                soup,
                current_domain=parts.netloc.lower(),
                base_url=url,
                content_root=root,
                profile=profile,
                current_url=url,
                site_prefix=None,
            )
            nav_links = 0
            if nav_root is not None:
                for a in nav_root.select("a[href]"):
                    href = (a.get("href") or "").strip()
                    if href and not href.startswith(("#", "javascript:", "mailto:", "tel:")):
                        nav_links += 1
            if nav_root is None or nav_links < 3:
                if soup.select_one("#__docusaurus, #app, #root, [data-vitepress], [data-reactroot]"):
                    return True

    return False


def browser_quality_score(text: str) -> int:
    soup = BeautifulSoup(text, "html.parser")
    root = select_content_root(soup)
    if root is None:
        return len(clean_text(soup.get_text(" ", strip=True)))
    return compute_content_score(root)

