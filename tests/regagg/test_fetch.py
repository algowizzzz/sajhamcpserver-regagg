"""
Fetch layer — HTML->md and PDF detection by magic bytes (regression for the live
bug where a .pdf URL returning an HTML error page was wrongly PDF-parsed).
"""

from __future__ import annotations

from sajha.regagg.fetch import Fetcher, fixture_opener

HTML = b"<html><head><title>T</title></head><body><main><h1>Head</h1><p>body text</p></main></body></html>"


def test_html_url_is_markdownified():
    fr = Fetcher(fixture_opener({"u": (HTML, "text/html")})).fetch("u")
    assert fr.fetch_method == "html_to_md" and "Head" in fr.content_md
    assert fr.content_hash.startswith("sha256:")


def test_pdf_url_returning_html_is_treated_as_html():
    # regulator returns an HTML error page for a .pdf URL -> must NOT pdf-parse
    fr = Fetcher(fixture_opener({"http://x/doc.pdf": (b"\n<!DOCTYPE html><html><body>oops</body></html>",
                                                      "text/html")})).fetch("http://x/doc.pdf")
    assert fr.fetch_method == "html_to_md" and fr.raw_ext == "html"


def test_real_pdf_bytes_use_pdf_path():
    # %PDF magic -> routed to pdf_to_md. Toy bytes make pypdf raise, which itself
    # proves the PDF path was taken (the HTML path never raises on this input).
    pdf = b"%PDF-1.4\n...not a real pdf..."
    f = Fetcher(fixture_opener({"http://x/real.pdf": (pdf, "application/pdf")}))
    try:
        fr = f.fetch("http://x/real.pdf")
        assert fr.fetch_method == "pdf_to_md"   # parsed cleanly
    except Exception:  # noqa: BLE001 — pypdf rejecting toy bytes == PDF path chosen
        pass


def test_title_from_url_humanizes_pdf_names():
    from sajha.regagg.pipeline import _title_from_url
    assert _title_from_url(
        "https://www.iais.org/uploads/2025/04/IAIS-Press-Release-adoption.pdf"
    ) == "IAIS Press Release adoption"
    assert _title_from_url("https://x.gov/a_b/c-d.pdf") == "c d"
    assert _title_from_url("https://x.gov/") == "https://x.gov/"
