#shared constants, selectors, and regular expressions

from __future__ import annotations

import re

USER_AGENT = (
    "Mozilla/5.0 (compatible; docs2md/2.0; +https://example.invalid/bot)"
)

HTTP_TIMEOUT = 20

BROWSER_TIMEOUT_MS = 45000

DEFAULT_MAX_ASSET_BYTES = 25 * 1024 * 1024

DEFAULT_CONCURRENCY = 12

DEFAULT_ASSET_CONCURRENCY = 8

DEFAULT_MAX_DEPTH = 20

CACHE_SCHEMA_VERSION = 6

GENERIC_CONTENT_SELECTORS = [
    "main article",
    "article[role='main']",
    "div[role='main'] article",
    "article.theme-doc-markdown",
    ".theme-doc-markdown",
    ".vp-doc",
    ".VPDoc .vp-doc",
    ".VPDoc .content",
    ".VPDoc .content-container",
    ".VPDoc",
    ".md-content__inner",
    "main.article",
    "main article.doc",
    "article.doc",
    "main .doc",
    "[role='main'] .doc",
    ".doc",
    ".sect1",
    ".sect2",
    ".javadoc-content",
    ".main-grid",
    ".class-description",
    ".package-description",
    ".contentContainer",
    "article.bd-article",
    ".bd-article",
    ".bd-content",
    "main#main-content",
    "div.body",
    ".rst-content",
    ".documentwrapper .body",
    ".document",
    "[data-testid='page.content']",
    "[data-testid*='page-content' i]",
    "main#main-content",
    "#main-content",
    "main article.doc",
    "article.doc",
    "main .doc",
    "[role='main'] .doc",
    ".article .content",
    ".article-content",
    ".doc-content",
    ".documentation-content",
    ".td-content",
    "#xooki-body",
    ".xooki-body",
    "td#main",
    "td#body",
    "td#doc-content",
    "td.content",
    "td.main",
    "td[class*='content' i]",
    "td[class*='main' i]",
    "#docs-content",
    ".docs-content",
    ".guide-content",
    ".markdown-section",
    ".gitbook-page",
    ".content",
    ".page-inner",
    ".page-content",
    ".book-page",
    ".book-post",
    ".markdown",
    ".markdown-body",
    ".prose",
    "#bodyColumn",
    "td#bodyColumn",
    "#content",
    "#contentBox",
    "td#contentBox",
    "main",
    "article",
    "body",
]

GENERIC_NAV_SELECTORS = [
    "aside nav",
    "aside[class*='sidebar']",
    "aside[class*='Sidebar']",
    "nav[aria-label*='sidebar' i]",
    "nav[aria-label*='navigation' i]",
    "nav[class*='sidebar']",
    "nav[class*='Sidebar']",
    "div[class*='sidebar']",
    "div[class*='Sidebar']",
    ".theme-doc-sidebar-container",
    ".menu.menu__list",
    ".VPSidebar",
    ".VPSidebarNav",
    ".VPNavScreenMenu",
    ".md-sidebar",
    "nav[data-md-level]",
    ".wy-menu.wy-menu-vertical",
    ".sphinxsidebar",
    ".bd-sidebar-primary",
    ".bd-sidebar",
    "nav.bd-links",
    ".globaltoc",
    ".toctree-wrapper",
    ".nav-container",
    ".nav-panel",
    ".nav-list",
    ".nav-menu",
    ".nav-panel-menu",
    ".nav-tree",
    ".toc-menu",
    ".docs-menu",
    ".docs-nav",
    ".sidebar-nav",
    ".site-sidebar",
    ".toc-menu",
    ".nav-sidebar",
    "#xooki-menu",
    ".xooki-menu",
    "#xooki-toc",
    ".xooki-toc",
    ".side-navigation",
    "[data-testid*='sidebar' i]",
    "[data-testid*='navigation' i]",
    ".gitbook-navigation",
    "#toc",
    ".toc",
    "#table-of-contents",
    "#left",
    "#right",
    "#leftColumn",
    "#navcolumn",
    ".book-menu",
    ".book-menu-content",
    "aside",
    "nav",
]

PROFILE_HINTS = {
    "docusaurus": {
        "content": ["article.theme-doc-markdown", ".theme-doc-markdown", "main article"],
        "nav": [".theme-doc-sidebar-container", "aside[class*='docSidebar']", "nav.menu"],
    },
    "vitepress": {
        "content": [".vp-doc", ".VPDoc .vp-doc", ".VPDoc .content-container", ".VPDoc", "main article"],
        "nav": [".VPSidebar", ".VPSidebarNav", ".VPNavScreenMenu", "aside nav"],
    },
    "sphinx": {
        "content": ["article.bd-article", ".bd-article", "div[role='main']", ".rst-content", ".documentwrapper .body", "div.body", "main#main-content", ".document"],
        "nav": [".wy-menu.wy-menu-vertical", ".sphinxsidebar", ".bd-sidebar-primary", ".bd-sidebar", "nav.bd-links", "nav[aria-label*='Navigation' i]", "nav[aria-label*='Section Navigation' i]"],
    },
    "mkdocs": {
        "content": [".md-content__inner", "main article"],
        "nav": [".md-sidebar--primary", ".md-sidebar", "nav[data-md-level]"],
    },
    "maven": {
        "content": ["#bodyColumn", "#contentBox", "main article"],
        "nav": ["#navcolumn", "#leftColumn"],
    },
    "antora": {
        "content": ["main.article", "article.doc", "main article.doc", "main .doc", ".doc", "#content", "main"],
        "nav": [".nav-container", ".nav-menu", ".nav-panel-menu", ".nav-list", "aside nav", "nav[aria-label*='navigation' i]"],
    },
    "asciidoctor": {
        "content": ["#content", "main", ".sect1", "article", "body"],
        "nav": ["#toc", ".toc", "#table-of-contents", ".toc2", ".toc-menu"],
    },
    "javadoc": {
        "content": ["main", ".javadoc-content", ".main-grid", ".class-description", ".package-description", ".contentContainer", ".overview-summary", "body"],
        "nav": ["nav", ".sub-nav", ".packages", ".overview-summary", "main"],
    },
    "book": {
        "content": ["[data-testid='page.content']", "[data-testid*='page-content' i]", ".markdown-section", ".gitbook-page", ".book-page", ".book-post", ".page-inner", "main article"],
        "nav": ["[data-testid*='sidebar' i]", "[data-testid*='navigation' i]", ".gitbook-navigation", ".book-menu", ".book-menu-content", "aside nav", "nav[role='navigation']"],
    },
}

NOISE_SELECTORS = [
    "script", "style", "noscript", "wbr", "template",
    "svg[class*='icon']",
    "form[role='search']",
    "form[action*='search' i]",
    "input[type='search']",
    "a.hash-link", "a.headerlink",
    "button[aria-label*='copy' i]",
    "button[title*='copy' i]",
    "button[class*='copy']",
    "button[class*='Copy']",
    "button[class*='clean-btn']",
    "[class*='breadcrumbs']",
    "[class*='breadcrumb']",
    "nav[aria-label*='breadcrumb' i]",
    "nav.pagination-nav",
    "[class*='pagination-nav']",
    "[class*='theme-edit-this-page']",
    "[class*='editThisPage']",
    "[class*='lastUpdated']",
    "[class*='tocCollapsible']",
    "[class*='tableOfContents']",
    "[class*='OnThisPage']",
    "[class*='on-this-page']",
    "[class*='page-tools']",
    "[class*='pageTools']",
    "[class*='feedback']",
    "[class*='Feedback']",
    "#searchbox", "#searchBox",
    "#poweredBy",
    "#banner", "#bannerLeft", "#bannerRight",
    ".clear",
]

RAW_HTML_BLOCK_TAGS = {"iframe", "video", "audio", "svg", "details", "math"}

DOC_PAGE_EXTENSIONS = {
    "", ".html", ".htm", ".xhtml", ".php", ".asp", ".aspx",
    ".jsp", ".jspx", ".shtml",
}

ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico",
    ".pdf", ".zip", ".gz", ".tgz", ".bz2", ".xz", ".jar", ".war", ".ear",
    ".tar", ".txt", ".csv", ".json", ".yaml", ".yml", ".xml", ".asc", ".sha1",
    ".sha256", ".sha512", ".md5", ".pom", ".apk", ".deb", ".rpm", ".mp4",
    ".mp3", ".ogg", ".wav", ".woff", ".woff2", ".ttf", ".eot", ".otf",
}

SKIP_URL_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in [
        r"/search(?:/|\.html)?$",
        r"/genindex\.html$",
        r"/py-modindex\.html$",
        r"/objects\.inv$",
        r"/sitemap(?:\.xml)?$",
        r"/feed(?:\.xml)?$",
        r"/rss(?:\.xml)?$",
        r"/atom(?:\.xml)?$",
        r"/404(?:\.html)?$",
        r"/print(?:/|\.html)?$",
        r"/tag(?:s)?(?:/|\.html)?$",
        r"/categor(?:y|ies)(?:/|\.html)?$",
        r"/blog(?:/|\.html?|$)",
        r"/news(?:/|\.html?|$)",
        r"/apidocs(?:/|\.html?|$)",
        r"/api-release(?:/|\.html?|$)",
        r"/testapidocs(?:/|\.html?|$)",
        r"/xref(?:/|\.html?|$)",
        r"/xref-test(?:/|\.html?|$)",
        r"/jacoco(?:/|\.html?|$)",
        r"/cobertura(?:/|\.html?|$)",
        r"/jxr(?:/|\.html?|$)",
        r"/class-use(?:/|$)",
        r"/allclasses(?:-index)?\.html$",
        r"/index-all\.html$",
        r"/overview-tree\.html$",
        r"/deprecated-list\.html$",
        r"/serialized-form\.html$",
        r"/package-summary\.html$",
        r"/package-tree\.html$",
        r"/package-use\.html$",
        r"/help-doc\.html$",
        r"/constant-values\.html$",
        r"/(?:changes|changes-report|jira-changes|rat-report|checkstyle|pmd|cpd)\.html$",
        r"/(?:spotbugs|findbugs|japicmp|clirr|taglist|surefire-report|failsafe-report)\.html$",
        r"/(?:jdepend|jdeps|junit-report|test-results|project-reports)\.html$",
        r"/(?:dependencies|dependency-convergence|dependency-info|dependency-management)\.html$",
        r"/(?:distribution-management|issue-management|license|licenses|mail-lists)\.html$",
        r"/(?:plugin-management|plugins|project-info|project-modules|scm-usage|source-repository)\.html$",
        r"/(?:team-list)\.html$",
    ]
]


SOFT_NOISE_PATH_TOKENS = {
    "javadoc", "apidocs", "api-docs", "reference-api", "api-reference",
    "coverage", "reports", "report",
}

ZERO_WIDTH_RE = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff]")

SOFT_SPACE_RE = re.compile(r"[\u00a0\u202f\u2007\u2009\u200a]")

MOJIBAKE_HINT_RE = re.compile(r"(?:Ã.|Â.|â.|ï¼|ï½|ï»¿|ðŸ|â€|â€™|â€œ|â€“|â€”|�)")

SKIP_TEXT_NORMALIZATION_TAGS = {"pre", "code", "script", "style", "textarea"}

INLINE_BREAK_PARENT_TAGS = {"p", "td", "th", "li", "dd", "dt", "span", "div", "a", "strong", "em"}

ADMONITION_KIND_MAP = {
    "note": "note", "info": "info", "tip": "tip", "success": "tip",
    "hint": "tip", "important": "important", "warning": "warning",
    "caution": "warning", "danger": "danger", "error": "danger",
}

CALL_OUT_KIND_MAP = {
    "note": "NOTE", "info": "NOTE", "tip": "TIP",
    "important": "IMPORTANT", "warning": "WARNING", "danger": "CAUTION",
}

SANITIZED_HTML_ATTRS = {
    "href", "src", "alt", "title", "rowspan", "colspan", "width", "height",
    "target", "rel", "id", "name", "open", "start", "type", "align",
    "scope", "headers",
}

DOC_LIKE_KEYWORDS = {
    "docs", "doc", "documentation", "manual", "guide", "guides", "reference",
    "references", "tutorial", "tutorials", "learn", "book", "books",
    "user-guide", "getting-started", "how-to", "concepts", "design",
    "handbook", "cookbook",
}

TRACKING_QUERY_PARAMS = {
    "fbclid", "gclid", "dclid", "msclkid", "yclid", "mc_cid", "mc_eid",
    "igshid", "spm", "ref_src", "ref_url", "source", "from", "campaign",
}

TRACKING_QUERY_PREFIXES = ("utm_",)

VERSION_QUERY_PARAMS = {
    "version", "ver", "v", "docs_version", "doc_version", "release",
    "branch", "tag", "rev", "revision", "ref", "lang", "language",
    "locale", "hl",
}

SEARCH_QUERY_PARAMS = {"q", "query", "search", "keyword", "keywords", "term", "terms"}

LANGUAGE_QUERY_PARAMS = {"lang", "language", "locale", "hl"}

PREFERRED_LANGUAGE_DEFAULT = "en"

ENGLISH_LANGUAGE_CODES = {
    "en", "en-us", "en-gb", "en-ca", "en-au", "en-nz", "en-ie", "en-za",
}

KNOWN_LANGUAGE_CODES = {
    "af", "am", "ar", "az", "be", "bg", "bn", "bs", "ca", "cs", "cy", "da",
    "de", "el", "es", "et", "eu", "fa", "fi", "fr", "ga", "gl", "gu", "he",
    "hi", "hr", "hu", "hy", "id", "is", "it", "ja", "ka", "kk", "km", "kn",
    "ko", "lt", "lv", "mk", "ml", "mn", "mr", "ms", "my", "nb", "ne", "nl",
    "nn", "no", "pa", "pl", "pt", "ro", "ru", "si", "sk", "sl", "sq", "sr",
    "sv", "sw", "ta", "te", "th", "tl", "tr", "uk", "ur", "uz", "vi", "zh",
    "zh-cn", "zh-tw", "zh-hans", "zh-hant", "pt-br", "pt-pt", "es-es", "es-mx",
    "fr-fr", "de-de", "ja-jp", "ko-kr", *ENGLISH_LANGUAGE_CODES,
}

LANGUAGE_SEGMENT_RE = re.compile(r"^[a-z]{2,3}(?:[-_][a-z0-9]{2,8}){0,2}$", re.I)

SIDEBAR_CONTEXT_RE = re.compile(
    r"(?:^|[-_\s])(?:sidebar|side-nav|sidenav|docs-sidebar|doc-sidebar|"
    r"docsidebar|toc-tree|toctree|navcolumn|leftcolumn|book-menu|wy-menu|"
    r"bd-sidebar|bd-links|nav-container|nav-panel|nav-list|docs-menu|"
    r"docs-nav|sidebar-nav|site-sidebar|toc-menu|nav-sidebar|side-navigation|"
    r"md-sidebar|vpsidebar|vpsidebarnav|theme-doc-sidebar|"
    r"gitbook-navigation|menu)(?:$|[-_\s])",
    re.I,
)

GLOBAL_CHROME_RE = re.compile(
    r"(?:^|[-_\s])(?:navbar|nav-bar|topbar|top-bar|masthead|header|"
    r"site-header|global-nav|main-nav|footer|site-footer|dropdown|"
    r"version|versions|language|locale|social|foundation)(?:$|[-_\s])",
    re.I,
)

TOC_CONTEXT_RE = re.compile(
    r"(?:on-this-page|table-of-contents|toccollapsible|toc-collapsible|"
    r"page-toc|toc-list|right-sidebar|contents)",
    re.I,
)

CONTENT_CHROME_SELECTORS = [
    "header", "footer", "[role='banner']", "[role='contentinfo']",
    "#leftColumn", "#navcolumn", "#sidebar", "#sideNav", "#sidenav",
    ".theme-doc-sidebar-container", ".docSidebar", "[class*='docSidebar']",
    ".VPSidebar", ".VPSidebarNav", ".vp-sidebar", ".md-sidebar", ".wy-nav-side",
    ".sphinxsidebar", ".bd-sidebar", ".bd-sidebar-primary", "nav.bd-links",
    ".nav-container", ".nav-panel", ".nav-list", ".docs-menu", ".docs-nav",
    ".sidebar-nav", ".site-sidebar", ".toc-menu", ".nav-sidebar", ".side-navigation",
    ".book-menu", ".book-menu-content", ".gitbook-navigation",
    "#toc", ".toc", "#table-of-contents", ".table-of-contents",
    "#left", "#right", "#quickReference", "#quick-reference",
    ".quickref", ".quick-reference", ".quickReference",
    ".version-selector", ".versions", ".edit-page",
    "[data-testid*='sidebar' i]", "[data-testid*='navigation' i]",
    "aside[class*='sidebar' i]", "div[class*='sidebar' i]",
    "nav[class*='sidebar' i]", "nav[aria-label*='sidebar' i]",
    "nav[aria-label*='navigation' i]",
    "aside[class*='side-nav' i]", "nav[class*='side-nav' i]",
    "div[class*='side-nav' i]", "aside[class*='sidenav' i]",
    "nav[class*='sidenav' i]", "div[class*='sidenav' i]",
    ".navbar", "[class*='navbar' i]",
    "[class*='topbar' i]", "[class*='site-header' i]", "[class*='site-footer' i]",
]

GLOBAL_NAV_TITLE_HINTS = {
    "blog", "blogs", "community", "communities", "download", "downloads",
    "foundation", "apache", "asf", "github", "license", "events",
    "security", "sponsorship", "thanks", "privacy", "code of conduct",
    "resources", "others", "benchmark",
}

GENERIC_DOC_LINK_TEXT_RE = re.compile(
    r"\b(?:"
    r"docs?|documentation|manual|guide|guides|tutorial|tutorials|reference|"
    r"getting\s+started|quick\s+start|overview|introduction|install(?:ation)?|"
    r"build(?:ing)?|subprojects?|modules?|components?|features?|platforms?|"
    r"setup|configure|configuration|usage|examples?|concepts?|how\s*to|faq|"
    r"api|cli|sdk|reference|developer|developers?|user\s+guide|admin\s+guide|"
    r"next|previous|prev|continue|read\s+more"
    r")\b",
    re.I,
)

GENERIC_BAD_LINK_TEXT_RE = re.compile(
    r"\b(?:"
    r"blog|news|press|release\s+notes?|changelog|download|downloads|pricing|"
    r"login|log\s*in|sign\s*in|signup|sign\s*up|contact|careers?|jobs?|"
    r"privacy|terms|license|licenses|github|gitlab|twitter|x\.com|facebook|"
    r"linkedin|youtube|discord|slack|rss|atom|feed|subscribe"
    r")\b",
    re.I,
)

GENERIC_SKIP_PATH_TOKENS = {
    "blog", "blogs", "news", "press", "releases", "release-notes",
    "changelog", "changes", "download", "downloads", "pricing", "plans",
    "login", "signin", "sign-in", "signup", "sign-up", "account",
    "contact", "contacts", "about", "company", "careers", "jobs",
    "privacy", "terms", "legal", "license", "licenses", "security",
    "events", "community", "communities", "forum", "forums",
    "search", "tags", "tag", "category", "categories", "author", "authors",
}

GENERIC_CONTENT_CLASS_RE = re.compile(
    r"(?:^|[-_\s])(?:"
    r"content|main|article|post|page|body|entry|markdown|md|prose|docs?|"
    r"documentation|manual|guide|chapter|section|container|wrapper"
    r")(?:$|[-_\s])",
    re.I,
)

GENERIC_CHROME_CLASS_RE = re.compile(
    r"(?:^|[-_\s])(?:"
    r"nav|navbar|menu|sidebar|aside|toc|breadcrumb|header|footer|"
    r"masthead|hero|banner|search|toolbar|cookie|modal|popup|drawer|"
    r"social|share|pagination|pager|comments?"
    r")(?:$|[-_\s])",
    re.I,
)

