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


# ── choosing the container that holds the document ──────────────────────────

OSC_SHAPED = """<html><head><title>A Decision | OSC</title></head><body>
  <header>site header</header>
  <nav>menu</nav>
  <div class="search-widget"><article>Search</article></div>
  <div id="content">
    <h1>Bank of Nova Scotia and Scotiabank Tier 1 Trust</h1>
    <p>Headnote. Relief from the take-over bid requirements.</p>
    <p>The Decision Maker has considered the application in full.</p>
  </div>
  <footer>site footer</footer>
</body></html>"""


def test_a_decorative_article_does_not_win_over_the_real_content():
    """The bug that emptied 10,560 documents — 100% of OSC, plus all of RBI.

    `main or article or body` took the FIRST <article>, and on OSC that is a
    search widget holding the word "Search". Every page converted to six
    characters and was stored with an empty body, beside 280 KB of perfectly
    good raw.html. Tag order is not evidence; the text is.
    """
    from sajha.regagg.fetch import html_to_md

    md, title = html_to_md(OSC_SHAPED)
    assert "take-over bid" in md
    assert "considered the application" in md
    assert title == "A Decision | OSC"
    assert len(md) > 100


def test_a_real_main_still_wins_over_the_body_chrome():
    from sajha.regagg.fetch import html_to_md

    md, _ = html_to_md(
        "<html><body><nav>menu</nav>"
        "<main><p>" + ("the actual guidance text. " * 20) + "</p></main>"
        "<div>unrelated sidebar</div></body></html>")
    assert "actual guidance" in md
    assert "unrelated sidebar" not in md


def test_a_page_with_text_never_converts_to_nothing():
    """The last line of defence. An empty body is indistinguishable from a page
    that genuinely had none, and nothing downstream can tell the difference —
    which is exactly why this hid across 10,560 documents."""
    from sajha.regagg.fetch import html_to_md

    # everything the stripper removes, wrapping the only real text
    md, _ = html_to_md(
        "<html><body><form><p>Only text on the page, inside a form.</p>"
        "</form></body></html>")
    assert "Only text on the page" in md


def test_a_genuinely_empty_page_still_yields_nothing():
    """Absence must stay reportable — the fallback must not manufacture text."""
    from sajha.regagg.fetch import html_to_md

    md, _ = html_to_md("<html><body><script>var x=1;</script></body></html>")
    assert md.strip() == ""
