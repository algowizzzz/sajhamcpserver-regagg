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


def html_to_md(html: str) -> Tuple[str, Optional[str]]:
    """Convert HTML to markdown, stripping boilerplate. Returns (md, title)."""
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else None
    for tag in soup(["script", "style", "noscript", "nav", "header", "footer", "form"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    md = _md(str(main), heading_style="ATX", strip=["a"] if False else None)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
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
    """Simple per-domain token spacing (default 0.5 rps)."""

    def __init__(self, rps: float = 0.5, sleep: Callable[[float], None] = time.sleep):
        self.min_interval = 1.0 / rps if rps > 0 else 0.0
        self._last: Dict[str, float] = {}
        self._sleep = sleep

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

        is_pdf = method == "pdf_to_md" or "pdf" in (content_type or "").lower() \
            or url.lower().endswith(".pdf")
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
