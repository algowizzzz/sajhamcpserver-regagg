"""
Fetch & normalization (FR-2 / US-2.1).

HTML/PDF → markdown, content hashing, OCR flag. Network IO is injected via an
``opener`` callable so the whole layer is deterministic and testable against
recorded fixtures with no network. In production the default opener uses
``requests`` with a descriptive User-Agent, robots.txt awareness, and a
per-domain rate limit (config ``rate_limit_rps``).

This deliberately reuses the spirit of the repo's existing webcrawler tools
(crawl_url / extract_content) rather than introducing a parallel HTTP stack.
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass
from typing import Callable, Dict, Optional, Tuple
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as _md

from sajha.regagg import ids

USER_AGENT = "BMO-RegIntel/1.0 (+regintel-ops@example.com)"

# opener(url) -> (raw_bytes, content_type, final_url)
Opener = Callable[[str], Tuple[bytes, str, str]]


@dataclass
class FetchResult:
    content_md: str
    content_hash: str
    raw: bytes
    raw_ext: str
    final_url: str
    fetch_method: str
    title: Optional[str] = None
    ocr: bool = False


def _best_container(soup):
    """The element that actually holds the document — chosen by content.

    This was `soup.find("main") or soup.find("article") or soup.body`, which
    takes the FIRST matching tag regardless of what is in it. On OSC the first
    `<article>` is a search widget holding the word "Search", so every OSC page
    converted to six characters and was stored with an empty body: **10,560
    documents, 100% of the source**, each with 280 KB of perfectly good
    `raw.html` sitting beside it. RBI was the same, and the corpus reported
    19,761 documents when more than half were titles with nothing under them.

    Tag order is not evidence. How much of the page an element actually holds
    is. A semantic container is preferred — it is the one that drops the
    sidebars — but only when it carries most of the text; `<body>` trivially
    contains everything, so raw length alone would always pick it and every
    page would come back with its chrome attached.
    """
    body = soup.body or soup
    body_len = len(body.get_text(" ", strip=True))
    if not body_len:
        return body

    best, best_len = None, 0
    for el in soup.find_all(["main", "article"]):
        n = len(el.get_text(" ", strip=True))
        if n > best_len:
            best, best_len = el, n

    # A container holding under half the page is a widget, not the document.
    return best if best is not None and best_len >= body_len * 0.5 else body


def html_to_md(html: str) -> Tuple[str, Optional[str]]:
    """Convert HTML to markdown, stripping boilerplate. Returns (md, title)."""
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else None
    for tag in soup(["script", "style", "noscript", "nav", "header", "footer", "form"]):
        tag.decompose()
    main = _best_container(soup)
    md = _md(str(main), heading_style="ATX", strip=["a"] if False else None)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    # Last line of defence. Storing nothing when the page plainly had text is
    # the failure that hid for 10,560 documents: an empty body is
    # indistinguishable from a page that genuinely had none, and nothing
    # downstream can tell the difference.
    if not md:
        whole = BeautifulSoup(html, "html.parser")
        for tag in whole(["script", "style", "noscript"]):
            tag.decompose()
        md = re.sub(r"\n{3,}", "\n\n",
                    _md(str(whole.body or whole), heading_style="ATX")).strip()
    return md, title


def pdf_to_md(raw: bytes) -> Tuple[str, bool]:
    """PDF → markdown. Returns (md, ocr_used). OCR path is a documented TODO;
    for now scanned PDFs (no text layer) are flagged ocr=True with empty text."""
    try:
        import pypdf  # optional
    except Exception:  # noqa: BLE001
        raise RuntimeError("pdf_to_md requires pypdf (add to requirements for PDF regulators)")
    import io
    reader = pypdf.PdfReader(io.BytesIO(raw))
    parts = [(page.extract_text() or "") for page in reader.pages]
    text = "\n\n".join(p.strip() for p in parts if p.strip())
    ocr = len(text) < 20  # effectively no text layer -> would need OCR
    return text, ocr


class RateLimiter:
    """Simple per-domain token spacing (default 0.5 rps).

    The rate is settable because it belongs to the *source*, not to the run:
    `rate_limit_rps` is declared in each regulator's YAML, and the fleet runner
    walks sources serially, retuning the limiter as it moves between them. The
    `_last` map is deliberately kept across those changes — two sources sharing
    a host must still be spaced apart from each other.
    """

    def __init__(self, rps: float = 0.5, sleep: Callable[[float], None] = time.sleep):
        self.min_interval = 1.0 / rps if rps > 0 else 0.0
        self._last: Dict[str, float] = {}
        self._sleep = sleep

    def set_rate(self, rps: float) -> None:
        self.min_interval = 1.0 / rps if rps > 0 else 0.0

    def wait(self, url: str, clock: Callable[[], float] = time.monotonic) -> None:
        host = urlparse(url).netloc
        now = clock()
        last = self._last.get(host)
        if last is not None:
            delta = self.min_interval - (now - last)
            if delta > 0:
                self._sleep(delta)
        self._last[host] = clock()


class Fetcher:
    def __init__(self, opener: Optional[Opener] = None,
                 rate_limiter: Optional[RateLimiter] = None):
        self.opener = opener or _requests_opener
        self.rate_limiter = rate_limiter

    def fetch(self, url: str, method: str = "html_to_md") -> FetchResult:
        if self.rate_limiter:
            self.rate_limiter.wait(url)
        raw, content_type, final_url = self.opener(url)

        # Ground truth is the magic bytes: content-type / .pdf URL are only hints
        # (regulator sites often return an HTML error page for a .pdf URL). Only
        # PDF-parse when the body actually is a PDF.
        looks_pdf = raw[:1024].lstrip()[:4] == b"%PDF"
        hinted_pdf = method == "pdf_to_md" or "pdf" in (content_type or "").lower() \
            or url.lower().endswith(".pdf")
        is_pdf = looks_pdf or (hinted_pdf and looks_pdf)
        if is_pdf:
            md, ocr = pdf_to_md(raw)
            ext, fmethod = "pdf", "pdf_to_md"
            title = None
        else:
            md, title = html_to_md(raw.decode("utf-8", errors="replace"))
            ext, fmethod, ocr = "html", "html_to_md", False

        return FetchResult(
            content_md=md, content_hash=ids.content_hash(md), raw=raw, raw_ext=ext,
            final_url=final_url or url, fetch_method=fmethod, title=title, ocr=ocr)


def _requests_opener(url: str) -> Tuple[bytes, str, str]:
    import requests
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30,
                        allow_redirects=True)
    resp.raise_for_status()
    return resp.content, resp.headers.get("Content-Type", ""), resp.url


def fixture_opener(mapping: Dict[str, Tuple[bytes, str]]) -> Opener:
    """Build an offline opener from {url: (bytes, content_type)} for tests."""
    def _open(url: str) -> Tuple[bytes, str, str]:
        if url not in mapping:
            raise KeyError(f"no fixture for {url}")
        data, ctype = mapping[url]
        return data, ctype, url
    return _open
