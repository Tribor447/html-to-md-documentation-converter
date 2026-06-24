#high-level documentation crawler and converter managment

from __future__ import annotations

from bs4 import BeautifulSoup
from bs4 import Comment
from bs4 import NavigableString
from bs4 import Tag
from collections import deque
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from markdownify import markdownify as md
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from urllib.parse import urlsplit
import copy
import hashlib
import html
import json
import re
import threading
import yaml

from .constants import (
    BROWSER_TIMEOUT_MS,
    CONTENT_CHROME_SELECTORS,
    DEFAULT_ASSET_CONCURRENCY,
    DEFAULT_CONCURRENCY,
    DEFAULT_MAX_ASSET_BYTES,
    DEFAULT_MAX_DEPTH,
    DOC_PAGE_EXTENSIONS,
    HTTP_TIMEOUT,
    NOISE_SELECTORS,
    PREFERRED_LANGUAGE_DEFAULT,
    RAW_HTML_BLOCK_TAGS,
    SOFT_NOISE_PATH_TOKENS,
)
from .docusaurus import (
    docusaurus_sidebar_candidate_urls,
    parse_docusaurus_sidebar_payload,
    parse_json_or_jsonish,
)
from .html_analysis import (
    compute_content_score,
    detect_profile,
    extract_crawl_links,
    extract_title,
    first_nonempty_attr,
    generic_nav_is_weak,
    is_doc_like_page,
    select_content_root,
    select_nav_root,
)
from .markdown import (
    html_fragment_to_markdown,
    looks_like_admonition,
    looks_like_tab_container,
    normalize_dom_text_nodes,
    postprocess_markdown,
    render_complex_block,
    repair_combined_markdown_layout,
    replace_inline_breaks,
    replace_markdown_placeholders,
    starts_with_markdown_heading,
    unwrap_layout_table_content,
)
from .models import (
    NavNode,
    PageRecord,
)
from .navigation import (
    cleanup_nav_tree,
    content_internal_doc_link_count,
    extract_heading_nav_tree,
    extract_nav_tree,
    filter_nav_to_known_urls,
    flatten_nav_urls,
    mark_active_nav_item,
    merged_nav_from_snapshots,
    nav_link_count,
    nav_tree_quality,
)
from .network import (
    BrowserPool,
    Fetcher,
    HttpCache,
    PLAYWRIGHT_AVAILABLE,
    RateLimiter,
    build_session,
)
from .output import (
    build_url_tree,
    render_singlefile_navigation,
)
from .paths import (
    compose_heading_anchor,
    derive_bundle_title,
    extension_for_asset,
    path_relative_to,
    uniquify_path,
    url_to_rel_output,
    virtual_path_to_page_anchor,
)
from .scope import (
    build_site_slug,
    guess_site_prefix,
)
from .text import (
    clean_text,
    decode_response_text,
    dedupe_preserve_order,
)
from .urls import (
    absolutize,
    clamp_prefix_to_version_scope,
    infer_version_scope_prefix,
    is_probably_asset,
    javadoc_allowed_for_entry,
    looks_versionish,
    normalize_url,
    preferred_language_key,
    query_looks_search_like,
    query_scope_from_url,
    repair_legacy_maven_javadoc_url,
    safe_stem,
    should_skip_crawl_url,
    soup_allowed_for_language,
    split_and_normalize,
    split_stored_href,
    url_allowed_for_language,
    url_equivalence_variants,
    url_matches_query_scope,
)

class UniversalDocsConverter:
    def __init__(
        self,
        entry_url: str,
        out_dir: Path,
        delay: float = 0.15,
        max_pages: Optional[int] = None,
        max_depth: int = DEFAULT_MAX_DEPTH,
        save_html: bool = False,
        use_sitemap: bool = False,
        site_prefix_override: Optional[str] = None,
        combined_filename: str = "combined.md",
        browser_mode: str = "auto",
        browser_timeout_ms: int = BROWSER_TIMEOUT_MS,
        front_matter: bool = False,
        profile_override: Optional[str] = None,
        concurrency: int = DEFAULT_CONCURRENCY,
        follow_content_links: bool = False,
        respect_robots: bool = True,
        max_asset_bytes: int = DEFAULT_MAX_ASSET_BYTES,
        cache_dir: Optional[Path] = None,
        use_cache: bool = True,
        download_external_assets: bool = False,
        asset_concurrency: int = DEFAULT_ASSET_CONCURRENCY,
        skip_assets: bool = False,
        strict_version_scope: bool = True,
        preferred_language: str = PREFERRED_LANGUAGE_DEFAULT,
    ) -> None:
        self.entry_url = normalize_url(entry_url)
        self.entry_parts = urlsplit(self.entry_url)
        self.domain = self.entry_parts.netloc
        self.out_root = out_dir
        self.delay = delay
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.save_html = save_html
        self.use_sitemap = use_sitemap
        self.site_prefix_override = site_prefix_override
        self.combined_filename = combined_filename
        self.browser_mode = browser_mode
        self.browser_timeout_ms = browser_timeout_ms
        self.front_matter = front_matter
        self.profile_override = profile_override
        self.concurrency = max(1, concurrency)
        self.follow_content_links = follow_content_links
        self.respect_robots = respect_robots
        self.download_external_assets = download_external_assets
        self.asset_concurrency = max(1, asset_concurrency)
        self.skip_assets = skip_assets
        self.strict_version_scope = strict_version_scope
        self.preferred_language = preferred_language_key(preferred_language)

        self.session = build_session()
        self.rate_limiter = RateLimiter(delay)

        cache_root = cache_dir or (out_dir / ".cache")
        self.cache = HttpCache(cache_root, enabled=use_cache)

        self.browser_pool: Optional[BrowserPool] = None
        if browser_mode != "never" and PLAYWRIGHT_AVAILABLE:
            self.browser_pool = BrowserPool(timeout_ms=browser_timeout_ms)

        self.fetcher = Fetcher(
            session=self.session,
            cache=self.cache,
            rate_limiter=self.rate_limiter,
            browser_pool=self.browser_pool,
            browser_mode=browser_mode,
            respect_robots=respect_robots,
            max_asset_bytes=max_asset_bytes,
        )

        self.asset_cache: Dict[str, Path] = {}
        self.asset_cache_lock = threading.Lock()
        self.url_to_virtual_path: Dict[str, Path] = {}
        self.url_to_anchor: Dict[str, str] = {}
        self.url_alias_to_canonical: Dict[str, str] = {}
        self.pages: Dict[str, PageRecord] = {}
        self.nav_tree: List[NavNode] = []
        self.nav_snapshots: List[List[NavNode]] = []
        self.extra_seed_urls: List[str] = []
        self.site_prefix: Optional[str] = None
        self.site_slug: Optional[str] = None
        self.site_dir: Optional[Path] = None
        self.combined_output_path: Optional[Path] = None
        self.entry_final_url: Optional[str] = None
        self.profile: str = "generic"
        self.version_scope_prefix: Optional[str] = None
        self.version_query_scope: Tuple[Tuple[str, str], ...] = ()
        self._pages_lock = threading.Lock()
        self._nav_lock = threading.Lock()

   
    def run(self) -> None:
        print(f"\n=== {self.entry_url} ===")
        try:
            entry_result = self.fetcher.fetch_text(self.entry_url)
        except Exception as exc:
            print(f"[error] cannot fetch entry URL: {exc}")
            return
        entry_html = entry_result.text
        entry_final_url = entry_result.final_url
        self.entry_final_url = entry_final_url
        entry_soup = BeautifulSoup(entry_html, "html.parser")

        self.profile = self.profile_override or detect_profile(entry_soup, entry_final_url)
        self.site_prefix = self.site_prefix_override or guess_site_prefix(
            entry_final_url, entry_soup, self.profile,
        )
        if self.strict_version_scope:
            self.version_scope_prefix = infer_version_scope_prefix(
                urlsplit(entry_final_url).path,
                self.site_prefix,
            )
            self.version_query_scope = query_scope_from_url(entry_final_url)
            if self.version_scope_prefix and not self.site_prefix_override:
                self.site_prefix = clamp_prefix_to_version_scope(
                    urlsplit(entry_final_url).path,
                    self.site_prefix,
                )
        self.site_slug = build_site_slug(entry_final_url, self.site_prefix)
        self.site_dir = self.out_root / self.site_slug
        self.combined_output_path = self.site_dir / self.combined_filename
        assets_dir = self.site_dir / "assets"
        self.site_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)
        if self.save_html:
            (self.site_dir / "html_cache").mkdir(parents=True, exist_ok=True)

        print(f"profile    : {self.profile}")
        print(f"site prefix: {self.site_prefix}")
        if self.preferred_language != "any":
            print(f"language   : {self.preferred_language}")
        if self.version_scope_prefix or self.version_query_scope:
            print(f"version pin: {self.version_scope_prefix or '-'} {dict(self.version_query_scope) if self.version_query_scope else ''}")
        print(f"output dir : {self.site_dir}")
        print(f"concurrency: pages={self.concurrency}, assets={self.asset_concurrency}")
        if self.skip_assets:
            print("assets     : skipped (--no-assets)")
        if self.browser_mode != "never":
            browser_note = "available" if PLAYWRIGHT_AVAILABLE else "not installed"
            print(f"browser    : {self.browser_mode} ({browser_note})")

        structured_nav = self.discover_external_navigation(entry_soup, entry_final_url)
        if structured_nav:
            self.nav_snapshots.append(copy.deepcopy(structured_nav))
            self.extra_seed_urls = [
                url for url in dedupe_preserve_order(flatten_nav_urls(structured_nav))
                if self.is_allowed_page(url)
            ]
            print(f"external nav: {nav_link_count(structured_nav)} links, seeds={len(self.extra_seed_urls)}")

        try:
            self.crawl(entry_html=entry_html, entry_final_url=entry_final_url)
            self.dedupe_equivalent_pages()
            self.assign_virtual_paths()
            self.assign_page_anchors()
            self.prefetch_assets()
            self.convert_pages_to_fragments()
            self.write_navigation_sidecars()
            self.write_combined_markdown()
            self.write_manifests()
        finally:
            self.cache.flush()
            if self.browser_pool is not None:
                self.browser_pool.close()
        print(f"done: {len(self.pages)} pages, {len(self.asset_cache)} assets")

    def discover_external_navigation(
        self,
        entry_soup: BeautifulSoup,
        entry_final_url: str,
    ) -> List[NavNode]:
        if self.profile != "docusaurus" or not self.site_prefix:
            return []

        best_nav: List[NavNode] = []
        best_score = 0
        candidates = docusaurus_sidebar_candidate_urls(
            entry_final_url,
            self.site_prefix,
            entry_soup,
        )
        for candidate_url in candidates[:80]:
            try:
                result = self.fetcher.fetch_text(candidate_url)
            except Exception:
                continue
            payload = parse_json_or_jsonish(result.text)
            nav = parse_docusaurus_sidebar_payload(payload, entry_final_url, self.site_prefix)
            if not nav:
                continue
            score = nav_tree_quality(nav, site_prefix=self.site_prefix, domain=self.domain)
            if score > best_score:
                best_nav = nav
                best_score = score

        return cleanup_nav_tree(best_nav)
   
    def crawl(self, entry_html: str, entry_final_url: str) -> None:

        assert self.site_prefix is not None
        start_urls: List[Tuple[str, int]] = [(entry_final_url, 0)]
        for seed_url in self.extra_seed_urls:
            if seed_url != entry_final_url:
                start_urls.append((seed_url, 0))
        use_sitemap_seed = self.use_sitemap
        if use_sitemap_seed:
            sitemap_urls = self.discover_from_sitemap()
            if sitemap_urls:
                print(f"sitemap seeds: {len(sitemap_urls)}")
                for url in sorted(sitemap_urls):
                    if url != entry_final_url:
                        start_urls.append((url, 0))

        queued: Set[str] = set(url for url, _ in start_urls)
        seen_done: Set[str] = set()
       
        self._preloaded_entry = (entry_final_url, entry_html)

        executor = ThreadPoolExecutor(max_workers=self.concurrency)
        in_flight: Dict[Future, Tuple[str, int]] = {}
        pending: deque[Tuple[str, int]] = deque(start_urls)
        reached_max = False

        try:
            while pending or in_flight:
               
                while pending and len(in_flight) < self.concurrency:
                    if self.max_pages is not None and len(self.pages) + len(in_flight) >= self.max_pages:
                        break
                    url, depth = pending.popleft()
                    if url in seen_done:
                        continue
                    future = executor.submit(self._fetch_and_parse, url, depth)
                    in_flight[future] = (url, depth)

                if not in_flight:
                    break
               
                done = next(as_completed(in_flight))
                url, depth = in_flight.pop(done)
                seen_done.add(url)

                try:
                    result = done.result()
                except Exception as exc:
                    print(f"[warn] failed to process {url}: {exc}")
                    continue

                if result is None:
                    continue

                record, new_links = result
                with self._pages_lock:
                    if record.final_url not in self.pages:
                        self.pages[record.final_url] = record

                if self.max_pages is not None and len(self.pages) >= self.max_pages:
                    if not reached_max:
                        print("max-pages reached; stopping dispatch")
                        reached_max = True

                if reached_max:
                    continue
               
                next_depth = depth + 1
                if next_depth > self.max_depth:
                    continue
                for link in new_links:
                    if link in seen_done or link in queued:
                        continue
                    if not self.is_allowed_page(link):
                        continue
                    queued.add(link)
                    pending.append((link, next_depth))
        finally:
            executor.shutdown(wait=True)

    def dedupe_equivalent_pages(self) -> None:

        if not self.pages:
            return

        canonical_by_variant: Dict[str, str] = {}
        deduped: Dict[str, PageRecord] = {}
        duplicates = 0

        ordered_items = sorted(
            self.pages.items(),
            key=lambda item: (
                0 if item[0] == self.entry_final_url or item[1].url == self.entry_url else 1,
                item[1].depth,
                item[0],
            ),
        )

        for url, record in ordered_items:
            variants: Set[str] = set()
            for candidate in dedupe_preserve_order([url, record.url, record.final_url]):
                variants.update(url_equivalence_variants(candidate))
            variants.add(url)

            existing = next((canonical_by_variant[v] for v in variants if v in canonical_by_variant), None)
            if existing is not None:
                duplicates += 1
                for variant in variants:
                    self.url_alias_to_canonical[variant] = existing
                self.url_alias_to_canonical[url] = existing
                self.url_alias_to_canonical[record.url] = existing
                self.url_alias_to_canonical[record.final_url] = existing
                if self.entry_final_url == url:
                    self.entry_final_url = existing
                continue

            deduped[url] = record
            for variant in variants:
                canonical_by_variant[variant] = url
                self.url_alias_to_canonical[variant] = url
            self.url_alias_to_canonical[url] = url
            self.url_alias_to_canonical[record.url] = url
            self.url_alias_to_canonical[record.final_url] = url

        if duplicates:
            print(f"deduped equivalent pages: {duplicates}")
        self.pages = deduped

    def _fetch_and_parse(
        self,
        url: str,
        depth: int,
    ) -> Optional[Tuple[PageRecord, List[str]]]:
        if self.respect_robots and not self.fetcher.allowed_by_robots(url):
            print(f"[skip] blocked by robots.txt: {url}")
            return None

       
        if (
            getattr(self, "_preloaded_entry", None) is not None
            and self._preloaded_entry[0] == url
        ):
            html_text, final_url = self._preloaded_entry[1], url
        else:
            try:
                result = self.fetcher.fetch_text(url)
            except Exception as exc:
                print(f"[warn] fetch failed {url}: {exc}")
                return None
            html_text, final_url = result.text, result.final_url

        if final_url != url and not self.is_allowed_page(final_url):
            return None

        soup = BeautifulSoup(html_text, "html.parser")
        if not soup_allowed_for_language(soup, self.preferred_language):
            print(f"[skip] non-{self.preferred_language} page {final_url}")
            return None
        profile = detect_profile(soup, final_url, hint=self.profile)
        content_root = select_content_root(soup, profile=profile)
        nav_root = select_nav_root(
            soup,
            current_domain=self.domain,
            base_url=final_url,
            content_root=content_root,
            profile=profile,
            current_url=final_url,
            site_prefix=self.site_prefix,
        )

        score = compute_content_score(content_root) if content_root is not None else 0
        if not is_doc_like_page(content_root, nav_root, score):
            print(f"[skip] weak/non-doc page {final_url}")
            return None
       
        path_parts = [seg.lower() for seg in urlsplit(final_url).path.strip("/").split("/")]
        if (
            profile != "javadoc"
            and any(p in SOFT_NOISE_PATH_TOKENS for p in path_parts)
            and score < 1200
        ):
            print(f"[skip] soft-noise path {final_url}")
            return None

        title = extract_title(soup, content_root)
        if profile == "generic" and generic_nav_is_weak(
            nav_root,
            domain=self.domain,
            base_url=final_url,
            current_url=final_url,
            site_prefix=self.site_prefix or "/",
        ):
            nav_tree = []
        else:
            nav_tree = extract_nav_tree(
                nav_root,
                current_domain=self.domain,
                base_url=final_url,
            )

        if not nav_tree and content_internal_doc_link_count(
            content_root,
            domain=self.domain,
            base_url=final_url,
            site_prefix=self.site_prefix or "/",
            profile=profile,
        ) <= 1:
            nav_tree = extract_heading_nav_tree(content_root, final_url, page_title=title)

        if nav_tree:
            mark_active_nav_item(nav_tree, final_url, title)
            with self._nav_lock:
               
                self.nav_snapshots.append(copy.deepcopy(nav_tree))

        print(f"[page] {final_url}")
        record = PageRecord(
            url=url,
            final_url=final_url,
            title=title,
            html_text=html_text,
            nav_tree=nav_tree,
            profile=profile,
            content_score=score,
            depth=depth,
        )
        with self._pages_lock:
            self.url_alias_to_canonical[url] = final_url
            self.url_alias_to_canonical[final_url] = final_url

        assert self.site_prefix is not None
        candidate_links = extract_crawl_links(
            soup=soup,
            domain=self.domain,
            site_prefix=self.site_prefix,
            base_url=final_url,
            profile=profile,
            follow_content_links=self.follow_content_links,
            current_url=final_url,
            preferred_language=self.preferred_language,
        )
        return record, candidate_links

    def discover_from_sitemap(self) -> Set[str]:
        assert self.site_prefix is not None
        scheme = urlsplit(self.entry_final_url or self.entry_url).scheme or self.entry_parts.scheme
        site_root = f"{scheme}://{self.domain}"
        queue: deque[str] = deque([f"{site_root}/sitemap.xml", f"{site_root}/sitemap_index.xml"])
        visited: Set[str] = set()
        discovered: Set[str] = set()

        while queue and len(visited) < 25:
            sitemap_url = normalize_url(queue.popleft())
            if sitemap_url in visited:
                continue
            visited.add(sitemap_url)
            try:
                resp = self.session.get(sitemap_url, timeout=HTTP_TIMEOUT)
                if resp.status_code >= 400:
                    continue
                xml = decode_response_text(resp)
                for loc in re.findall(r"<loc[^>]*>(.*?)</loc>", xml, flags=re.I | re.S):
                    loc = html.unescape(re.sub(r"\s+", "", loc.strip()))
                    if not loc:
                        continue
                    url = normalize_url(loc)
                    path = urlsplit(url).path.lower()
                    if path.endswith(".xml") and urlsplit(url).netloc == self.domain:
                        queue.append(url)
                        continue
                    if self.is_allowed_page(url):
                        discovered.add(url)
            except Exception as exc:
                print(f"[warn] sitemap fetch failed {sitemap_url}: {exc}")
        return discovered
   
    def assign_virtual_paths(self) -> None:
        assert self.site_prefix is not None
        taken: Set[Path] = set()
        for url in sorted(self.pages.keys()):
            rel = url_to_rel_output(url, self.site_prefix)
            virtual = Path("docs") / rel
            if virtual in taken:
                virtual = uniquify_path(virtual, taken)
            taken.add(virtual)
            self.url_to_virtual_path[url] = virtual
            self.pages[url].virtual_path = virtual

    def assign_page_anchors(self) -> None:
        seen: Set[str] = set()
        for url, record in sorted(
            self.pages.items(),
            key=lambda item: self.url_to_virtual_path[item[0]].as_posix(),
        ):
            assert record.virtual_path is not None
            anchor = virtual_path_to_page_anchor(record.virtual_path)
            if anchor in seen:
                base = anchor
                idx = 2
                while f"{base}-{idx}" in seen:
                    idx += 1
                anchor = f"{base}-{idx}"
            seen.add(anchor)
            record.page_anchor = anchor
           
            for candidate in dedupe_preserve_order([url, record.url, record.final_url]):
                for variant in url_equivalence_variants(candidate):
                    self.url_to_anchor[variant] = anchor
                    self.url_alias_to_canonical.setdefault(variant, url)
                    self.url_to_virtual_path.setdefault(variant, record.virtual_path)
   
    def collect_asset_urls_for_record(self, record: PageRecord) -> Set[str]:
        if self.skip_assets:
            return set()

        soup = BeautifulSoup(record.html_text, "html.parser")
        root = select_content_root(soup, profile=record.profile)
        if root is None:
            root = soup.find("main") or soup.body or soup

        urls: Set[str] = set()

        for img in root.find_all("img"):
            src = first_nonempty_attr(img, [
                "src", "data-src", "data-original",
                "data-lazy-src", "data-src-retina",
            ])
            if not src or src.startswith("data:"):
                continue
            abs_url = normalize_url(absolutize(record.final_url, src))
            if self.should_download_asset(abs_url):
                urls.add(abs_url)

        for a in root.find_all("a", href=True):
            href = (a.get("href") or "").strip()
            if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
                continue
            abs_url, _frag = split_and_normalize(record.final_url, href)
            if is_probably_asset(abs_url) and self.should_download_asset(abs_url):
                urls.add(abs_url)

        return urls

    def prefetch_assets(self) -> None:
        if self.skip_assets or self.asset_concurrency <= 1:
            return

        asset_urls: Set[str] = set()
        for record in self.pages.values():
            asset_urls.update(self.collect_asset_urls_for_record(record))

       
        with self.asset_cache_lock:
            asset_urls = {url for url in asset_urls if normalize_url(url) not in self.asset_cache}

        if not asset_urls:
            return

        print(f"assets prefetch: {len(asset_urls)} urls, concurrency={self.asset_concurrency}")
        with ThreadPoolExecutor(max_workers=self.asset_concurrency) as executor:
            futures = {executor.submit(self.download_asset, url): url for url in sorted(asset_urls)}
            for future in as_completed(futures):
                url = futures[future]
                try:
                    future.result()
                except Exception as exc:
                    print(f"[warn] asset prefetch failed {url}: {exc}")

   
    def convert_pages_to_fragments(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        for url, record in sorted(self.pages.items()):
            soup = BeautifulSoup(record.html_text, "html.parser")
            root = select_content_root(soup, profile=record.profile)
            if root is None:
                root = soup.find("main") or soup.body or soup

            root = copy.copy(root)
            root = BeautifulSoup(str(root), "html.parser")
            content = root.find() or root
            if isinstance(content, Tag):
                content = unwrap_layout_table_content(content)
            if isinstance(content, Tag) and content.name in {"td", "th"}:
                wrapper_soup = BeautifulSoup("<div></div>", "html.parser")
                wrapper = wrapper_soup.div
                assert wrapper is not None
                for child in list(content.children):
                    wrapper.append(copy.copy(child))
                content = wrapper

            assert record.page_anchor is not None
            self.prepare_content(
                content,
                current_url=url,
                page_anchor=record.page_anchor,
                current_output=self.combined_output_path,
            )
            markdown_body = html_fragment_to_markdown(content)
            markdown_body = postprocess_markdown(markdown_body)
            if not starts_with_markdown_heading(markdown_body):
                markdown_body = f"# {record.title}\n\n" + markdown_body.lstrip()
            record.markdown_body = markdown_body.strip() + "\n"

            if self.save_html:
                assert record.virtual_path is not None
                cache_path = self.site_dir / "html_cache" / record.virtual_path.relative_to("docs")
                cache_path = cache_path.with_suffix(".html")
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(record.html_text, encoding="utf-8")

    def prepare_content(
        self,
        root: Tag,
        current_url: str,
        page_anchor: str,
        current_output: Optional[Path],
    ) -> None:
        assert self.site_dir is not None
        placeholders: Dict[str, str] = {}
        idx = 0

        for selector in NOISE_SELECTORS:
            for tag in list(root.select(selector)):
                tag.decompose()

        for selector in CONTENT_CHROME_SELECTORS:
            for tag in list(root.select(selector)):
                if tag is not root:
                    tag.decompose()

        replacement_root = unwrap_layout_table_content(root)
        if replacement_root is not root:
            root.clear()
            for child in list(replacement_root.children):
                root.append(copy.copy(child))

        for text_node in list(root.find_all(string=re.compile(r"^\s*Improve this doc\s*$", re.I))):
            parent = text_node.parent
            if isinstance(parent, Tag) and parent.name == "a":
                parent.decompose()
            else:
                text_node.extract()

        if getattr(root, "name", None) == "body" or root.select_one("#navcolumn, #leftColumn, #left, #right, #toc, .toc, .theme-doc-sidebar-container, .VPSidebar, .md-sidebar, .sphinxsidebar"):
            nav_in_content = select_nav_root(
                root,
                current_domain=self.domain,
                base_url=current_url,
                content_root=None,
                profile=self.profile,
                current_url=current_url,
                site_prefix=self.site_prefix,
            )
            if nav_in_content is not None and nav_in_content is not root:
                try:
                    nav_in_content.decompose()
                except Exception:
                    pass

        for comment in list(root.find_all(string=lambda x: isinstance(x, Comment))):
            comment.extract()

        replace_inline_breaks(root)
        normalize_dom_text_nodes(root)

        used_heading_anchor_ids: Set[str] = set()
        for heading in list(root.find_all(re.compile(r"^h[1-6]$"))):
            raw_ids: List[str] = []
            for attr in ("id", "name"):
                value = heading.get(attr)
                if value:
                    raw_ids.append(str(value))
            for a in list(heading.select("a.hash-link, a.headerlink")):
                a.decompose()
            heading_text = clean_text(heading.get_text(" ", strip=True))
            if heading_text:
                raw_ids.append(heading_text)

            anchor_ids: List[str] = []
            heading_base_seen: Set[str] = set()
            for raw_id in dedupe_preserve_order(raw_ids):
                base_anchor = compose_heading_anchor(page_anchor, raw_id)
                if base_anchor in heading_base_seen:
                    continue
                heading_base_seen.add(base_anchor)
                anchor_id = base_anchor
                suffix = 2
                while anchor_id in used_heading_anchor_ids:
                    anchor_id = f"{base_anchor}-{suffix}"
                    suffix += 1
                used_heading_anchor_ids.add(anchor_id)
                anchor_ids.append(anchor_id)

            if anchor_ids:
                token = f"DOC2MDPLACEHOLDERTOKEN{idx}END"
                idx += 1
                placeholders[token] = "".join(
                    f'<a id="{html.escape(anchor_id, quote=True)}"></a>\n'
                    for anchor_id in anchor_ids
                ) + "\n"
                heading.insert_before(NavigableString(token))

        for img in list(root.find_all("img")):
            src = first_nonempty_attr(img, [
                "src", "data-src", "data-original",
                "data-lazy-src", "data-src-retina",
            ])
            if not src or src.startswith("data:"):
                continue
            abs_url = absolutize(current_url, src)
            if not self.should_download_asset(abs_url):
               
                img["src"] = abs_url
                for attr in ["srcset", "data-src", "data-original", "data-lazy-src", "data-src-retina"]:
                    if img.has_attr(attr) and attr != "src":
                        del img[attr]
                continue
            try:
                local_path = self.download_asset(abs_url)
                rel = path_relative_to(current_output, self.site_dir / local_path)
                img["src"] = rel
                for attr in ["srcset", "data-src", "data-original", "data-lazy-src", "data-src-retina"]:
                    if img.has_attr(attr) and attr != "src":
                        del img[attr]
            except Exception as exc:
                print(f"[warn] asset fetch failed {abs_url}: {exc}")

       
        for a in list(root.find_all("a", href=True)):
            href = (a.get("href") or "").strip()
            if not href or href.startswith(("javascript:", "mailto:", "tel:")):
                continue

            if href.startswith("#"):
                frag = href[1:]
                a["href"] = "#" + (
                    compose_heading_anchor(page_anchor, frag) if frag else page_anchor
                )
                continue

            abs_url, frag = split_and_normalize(current_url, href)
            abs_url = repair_legacy_maven_javadoc_url(abs_url, clean_text(a.get_text(" ", strip=True)))
            canon = self.canonicalize_page_url(abs_url)
            if canon in self.pages and canon in self.url_to_anchor:
                target_anchor = self.url_to_anchor[canon]
                if frag:
                    target_anchor = compose_heading_anchor(target_anchor, frag)
                a["href"] = "#" + target_anchor
                continue

            if is_probably_asset(abs_url):
                if not self.should_download_asset(abs_url):
                    a["href"] = abs_url + (f"#{frag}" if frag else "")
                    continue
                try:
                    local_path = self.download_asset(abs_url)
                    target = self.site_dir / local_path
                    a["href"] = path_relative_to(current_output, target)
                    continue
                except Exception:
                    pass

            if urlsplit(abs_url).netloc == self.domain:
                a["href"] = abs_url + (f"#{frag}" if frag else "")

        complex_nodes: List[Tag] = []
        for tag in list(root.find_all(True)):
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
            if tag.name == "figure" and tag.find("table"):
                complex_nodes.append(tag)
                continue

        processed: Set[int] = set()
        for node in complex_nodes:
            if id(node) in processed:
                continue
            if any(id(parent) in processed for parent in node.parents if isinstance(parent, Tag)):
                continue
            token = f"DOC2MDPLACEHOLDERTOKEN{idx}END"
            idx += 1
            placeholders[token] = render_complex_block(node)
            processed.add(id(node))
            node.replace_with(NavigableString(f"\n\n{token}\n\n"))

        html_text = str(root)
        markdown = md(
            html_text,
            heading_style="ATX",
            bullets="-",
            strong_em_symbol="*",
        )
        markdown = replace_markdown_placeholders(markdown, placeholders)
        root.clear()
        root.append(NavigableString(markdown))

   
    def should_download_asset(self, asset_url: str) -> bool:
        if self.skip_assets:
            return False
        if self.download_external_assets:
            return True
        try:
            parts = urlsplit(normalize_url(asset_url))
        except Exception:
            return False
        return parts.netloc == self.domain

    def download_asset(self, asset_url: str) -> Path:
        assert self.site_dir is not None
        asset_url = normalize_url(asset_url)
        if not self.should_download_asset(asset_url):
            raise ValueError(f"external asset download disabled: {asset_url}")
        with self.asset_cache_lock:
            if asset_url in self.asset_cache:
                return self.asset_cache[asset_url]

        payload, final_url, content_type = self.fetcher.fetch_binary(asset_url)
        if not self.download_external_assets and urlsplit(final_url).netloc != self.domain:
            raise ValueError(f"asset redirected to external host: {final_url}")
        ext = extension_for_asset(final_url, content_type)
        stem = safe_stem(Path(urlsplit(final_url).path).stem or "asset")
        digest = hashlib.sha1(final_url.encode("utf-8")).hexdigest()[:16]
        subdir = "images" if (content_type or "").startswith("image/") else "files"
        rel_path = Path("assets") / subdir / f"{stem}_{digest}{ext}"
        abs_path = self.site_dir / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_bytes(payload)
        with self.asset_cache_lock:
            self.asset_cache[asset_url] = rel_path
            if final_url != asset_url:
                self.asset_cache[final_url] = rel_path
        return rel_path

   
    def canonicalize_page_url(self, url: str) -> str:
        base_url, _fragment = split_stored_href(url)
        probe = base_url or url
        direct = self.url_alias_to_canonical.get(probe)
        if direct:
            return direct
        for variant in url_equivalence_variants(probe):
            direct = self.url_alias_to_canonical.get(variant)
            if direct:
                return direct
        return probe

    def effective_nav_tree(self) -> List[NavNode]:
       
        nav = merged_nav_from_snapshots(
            self.nav_snapshots,
            site_prefix=self.site_prefix,
            domain=self.domain,
        )
        if not nav:
            nav = copy.deepcopy(self.nav_tree)

       
        nav = filter_nav_to_known_urls(nav, set(self.pages.keys()), self.url_alias_to_canonical)
        nav = cleanup_nav_tree(nav)
        if not nav:
            nav = build_url_tree(self.pages, self.url_to_virtual_path)

        nav_urls = {self.canonicalize_page_url(url) for url in flatten_nav_urls(nav)}
        missing_urls = [
            url for url in self.pages.keys()
            if self.canonicalize_page_url(url) not in nav_urls
        ]
        if missing_urls:
           
            missing_urls.sort(key=lambda u: self.url_to_virtual_path[u].as_posix())
            other_children = [
                NavNode(title=self.pages[url].title, href=url, kind="link")
                for url in missing_urls
            ]
            nav.append(NavNode(title="Other pages", children=other_children, kind="category"))
        return nav

    def ordered_page_urls_from_nav(self, nav: List[NavNode]) -> List[str]:
        ordered: List[str] = []
        seen: Set[str] = set()
        for url in flatten_nav_urls(nav):
            canon = self.canonicalize_page_url(url)
            if canon in self.pages and canon not in seen:
                ordered.append(canon)
                seen.add(canon)
        for url in sorted(self.pages.keys(), key=lambda u: self.url_to_virtual_path[u].as_posix()):
            canon = self.canonicalize_page_url(url)
            if canon not in seen:
                ordered.append(canon)
                seen.add(canon)
        return ordered

    def write_navigation_sidecars(self) -> None:
        assert self.site_dir is not None
        nav = self.effective_nav_tree()
        nav_dict = [node.to_dict(self.url_to_anchor, self.url_to_virtual_path) for node in nav]
        (self.site_dir / "navigation.json").write_text(
            json.dumps(nav_dict, ensure_ascii=False, indent=2), encoding="utf-8",
        )
        (self.site_dir / "navigation.yml").write_text(
            yaml.safe_dump(nav_dict, sort_keys=False, allow_unicode=True), encoding="utf-8",
        )
        summary_lines = ["# Summary", ""]
        summary_lines.extend(render_singlefile_navigation(nav, self.url_to_anchor))
        (self.site_dir / "SUMMARY.md").write_text(
            "\n".join(summary_lines).rstrip() + "\n", encoding="utf-8",
        )

    def write_combined_markdown(self) -> None:
        assert self.site_dir is not None
        assert self.combined_output_path is not None

        nav = self.effective_nav_tree()
        ordered_urls = self.ordered_page_urls_from_nav(nav)
        entry_record = self.pages.get(
            self.entry_final_url or self.entry_url,
            PageRecord("", "", "", ""),
        )
        site_title = derive_bundle_title(
            entry_url=self.entry_final_url or self.entry_url,
            entry_title=entry_record.title,
            site_slug=self.site_slug or "site",
        )

        parts: List[str] = []
        if self.front_matter:
            front_matter = {
                "entry_url": self.entry_url,
                "page_count": len(self.pages),
                "asset_count": len(self.asset_cache),
                "profile": self.profile,
            }
            parts.append(
                "---\n"
                + yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True).strip()
                + "\n---\n\n"
            )

        parts.append(f"# {site_title}\n\n")
        parts.append("## Navigation\n\n")
        nav_lines = render_singlefile_navigation(nav, self.url_to_anchor)
        if nav_lines:
            parts.append("\n".join(nav_lines) + "\n")
        else:
            parts.append("- No navigation extracted\n")

        parts.append("\n## Content\n")
        for index, url in enumerate(ordered_urls, start=1):
            record = self.pages[url]
            assert record.page_anchor is not None
            body = record.markdown_body.strip() or f"# {record.title}\n"
            parts.append(f'\n<a id="{record.page_anchor}"></a>\n')
            parts.append(f"\n<!-- source_url: {url} -->\n")
            parts.append(f"\n<!-- page_index: {index} -->\n\n")
            parts.append(body)
            parts.append("\n\n---\n")

        combined_text = "".join(parts).rstrip() + "\n"
        combined_text = repair_combined_markdown_layout(combined_text)
        self.combined_output_path.write_text(combined_text, encoding="utf-8")

    def write_manifests(self) -> None:
        assert self.site_dir is not None
        assert self.site_prefix is not None
        assert self.combined_output_path is not None

        manifest = {
            "entry_url": self.entry_url,
            "site_prefix": self.site_prefix,
            "site_slug": self.site_slug,
            "profile": self.profile,
            "combined_markdown": self.combined_output_path.name,
            "page_count": len(self.pages),
            "asset_count": len(self.asset_cache),
            "pages": [
                {
                    "source_url": url,
                    "title": record.title,
                    "anchor": record.page_anchor,
                    "virtual_path": self.url_to_virtual_path[url].as_posix(),
                    "profile": record.profile,
                    "score": record.content_score,
                    "depth": record.depth,
                }
                for url, record in sorted(
                    self.pages.items(),
                    key=lambda item: self.url_to_virtual_path[item[0]].as_posix(),
                )
            ],
        }
        (self.site_dir / "site_manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8",
        )

   
    def is_allowed_page(self, url: str) -> bool:
        assert self.site_prefix is not None
        url = normalize_url(url)
        parts = urlsplit(url)
        if parts.netloc != self.domain:
            return False
        if not url_allowed_for_language(url, self.preferred_language):
            return False
        if query_looks_search_like(url):
            return False
        if should_skip_crawl_url(
            url,
            profile=self.profile,
            allow_javadoc=javadoc_allowed_for_entry(self.entry_url, self.profile),
        ):
            return False
        ext = Path(parts.path).suffix.lower()
        if ext not in DOC_PAGE_EXTENSIONS:
            return False
        if not parts.path.startswith(self.site_prefix):
            return False
       
        if self.strict_version_scope:
            if self.version_scope_prefix and not parts.path.startswith(self.version_scope_prefix):
                return False
            if self.version_query_scope and not url_matches_query_scope(url, self.version_query_scope):
                return False
           
            if not self.version_scope_prefix:
                rel = parts.path[len(self.site_prefix):].lstrip("/") if parts.path.startswith(self.site_prefix) else ""
                first = rel.split("/", 1)[0] if rel else ""
                if first and "/" in rel and looks_versionish(first):
                    return False
        return True

