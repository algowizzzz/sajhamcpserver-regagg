"""Previews: the first thing worth reading, or nothing at all.

The whole value of a preview is that it saves a click. A wrong one costs a
click AND trust, so the bar for showing something is higher than the bar for
showing nothing — every case below is a real shape from the corpus.
"""

from __future__ import annotations

import time

import pytest

from sajha.regagg import excerpt as E

OSFI = """---
title: "Guideline B-12"
---

255 Albert Street
Ottawa, Canada
K1A 0H2

www.osfi-bsif.gc.ca

Unclassified / Non classifié

Guideline

Subject: Interest Rate Risk Management Category: Sound Business and Financial
Practices No: B-12 Date: May 21, 2026

This guideline sets out OSFI's expectations for the management of interest rate
risk in the banking book. It applies to all federally regulated deposit-taking
institutions and takes effect on 1 November 2026.
"""

NEWS = """---
title: "Scott Bessent's Yen Trade Has Unintended Consequences"
---

# Scott Bessent's Yen Trade Has Unintended Consequences

The way it's being done should make us worry that the Federal Reserve is being
roped into easing monetary conditions.

[Read the full story at the source](https://example.com/a)

> Headline and summary as published in the source's public feed; full text
> remains at the publisher.
"""

NEWS_HEADLINE_ONLY = """---
title: "Prediction: Can Apple Stock Reach $400 This Year?"
---

# Prediction: Can Apple Stock Reach $400 This Year?



[Read the full story at the source](https://example.com/b)

> Headline and summary as published in the source's public feed.
"""

CONTENTS = """---
title: "Report on Selected Cybersecurity Practices"
---

Report on Selected Cybersecurity Practices – 2018 1 Contents Branch Controls 2
Phishing 5 Insider Threats 8 Penetration Testing 11 Mobile Devices 14

Firms increasingly rely on third-party providers for core services, and the
report describes the controls examiners expect to see around that reliance.
"""

FOOTER = """---
title: "Newsletter"
---

For more information or to subscribe or unsubscribe to the newsletter and email
alerts, please visit our website. Comments and suggestions are welcome.

The Board approved final amendments to the capital rules for large banking
organisations, which take effect in January.
"""


# ── regulatory ──────────────────────────────────────────────────────────────

def test_a_letterhead_is_never_the_preview():
    """The failure that started this: an OSFI card showing a postal address."""
    out = E.from_markdown(OSFI, title="Guideline B-12")
    assert "255 Albert" not in out
    assert "K1A 0H2" not in out
    assert "osfi-bsif" not in out


def test_a_labelled_subject_is_preferred_over_guessing():
    """When the document says what it is about, believe it."""
    out = E.from_markdown(OSFI, title="Guideline B-12")
    assert out.startswith("Interest Rate Risk Management")
    # and the metadata train after the subject is dropped
    assert "Category" not in out and "No: B-12" not in out


def test_a_table_of_contents_is_not_a_summary():
    out = E.from_markdown(CONTENTS, title="Report on Selected Cybersecurity Practices")
    assert "Phishing 5" not in out
    assert out.startswith("Firms increasingly rely")


def test_subscribe_boilerplate_is_skipped():
    out = E.from_markdown(FOOTER, title="Newsletter")
    assert "unsubscribe" not in out.lower()
    assert out.startswith("The Board approved")


def test_a_document_with_no_prose_gets_no_preview():
    """A list of statute names is not a summary. Blank beats wrong."""
    md = "---\ntitle: t\n---\n\nEnglish\nAct on the Rational Use of Energy\n" \
         "Foreign Exchange and Foreign Trade Act\n"
    assert E.from_markdown(md, title="t") == ""


def test_the_title_repeated_as_the_first_line_is_not_a_preview():
    md = ('---\ntitle: "Terrorist Financing Assessment 2018"\n---\n\n'
          'Terrorist Financing Assessment 2018\n\n'
          'This assessment describes the terrorist financing methods observed in '
          'Canadian reporting during the period under review.\n')
    out = E.from_markdown(md, title="Terrorist Financing Assessment 2018")
    assert out.startswith("This assessment describes")


# ── news ────────────────────────────────────────────────────────────────────

def test_news_shows_the_publishers_own_summary():
    out = E.from_markdown(NEWS, title="Scott Bessent's Yen Trade Has Unintended Consequences",
                          lane="news")
    assert out.startswith("The way it's being done")


def test_news_never_shows_the_boilerplate_note_or_the_link():
    out = E.from_markdown(NEWS, title="x", lane="news")
    assert "Read the full story" not in out
    assert "remains at the publisher" not in out
    assert "http" not in out


def test_a_headline_only_feed_yields_nothing_rather_than_the_headline_again():
    """Repeating the title under the title is noise dressed as information."""
    out = E.from_markdown(NEWS_HEADLINE_ONLY,
                          title="Prediction: Can Apple Stock Reach $400 This Year?",
                          lane="news")
    assert out == ""


# ── shape and safety ────────────────────────────────────────────────────────

def test_a_preview_is_bounded_and_never_cut_mid_word():
    md = "---\ntitle: t\n---\n\n" + ("The committee considered the proposal at length. " * 40)
    out = E.from_markdown(md, title="t", max_chars=120)
    assert len(out) <= 121
    assert not out.rstrip("…").endswith(" ")
    assert out.endswith(".") or out.endswith("…")


def test_missing_or_empty_input_is_not_an_error():
    for bad in ("", None, "---\n---\n", "   "):
        assert E.from_markdown(bad, title="t") == ""


def test_long_prose_without_a_full_stop_does_not_hang():
    """A nested-quantifier regex backtracked catastrophically here and would
    have hung the page render, not just this test."""
    md = "---\ntitle: t\n---\n\n" + ("word " * 4000)
    start = time.monotonic()
    E.from_markdown(md, title="t")
    assert time.monotonic() - start < 1.0


def test_for_document_survives_storage_that_is_absent_or_broken():
    class Boom:
        def read_content(self, _):
            raise RuntimeError("storage down")

    class Doc:
        s3_prefix = "p/1"
        title = "t"

    assert E.for_document(None, Doc()) == ""
    assert E.for_document(Boom(), Doc()) == ""
    assert E.for_document(Boom(), type("D", (), {"s3_prefix": None, "title": ""})()) == ""
