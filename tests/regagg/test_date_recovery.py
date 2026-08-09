"""Recovering a publication date — and refusing to invent one.

74% of the corpus has no date, so every time query silently misses most of it.
But a *wrong* date is worse than a missing one: a missing date excludes a
document from a window, a wrong date files it in the wrong week and it is never
questioned again. So the bar for returning something is high, and "none" is a
perfectly good answer.
"""

from __future__ import annotations

import datetime as _dt

import pytest

from sajha.regagg import date_recovery as D


# ── from the URL: the publisher wrote it, so it is the strongest evidence ────

@pytest.mark.parametrize("url,expect", [
    ("https://x.gov/news/2026/08/07/rule-final", _dt.date(2026, 8, 7)),
    ("https://x.gov/2026-08-07-statement", _dt.date(2026, 8, 7)),
    ("https://x.gov/press/2026/08/", _dt.date(2026, 8, 1)),      # month only
    ("https://x.gov/guidance/b-13", None),
    ("", None),
])
def test_dates_in_url_paths(url, expect):
    assert D.from_url(url) == expect


def test_an_impossible_url_date_is_rejected_not_clamped():
    assert D.from_url("https://x.gov/2026/13/45/thing") is None


# ── from the text ───────────────────────────────────────────────────────────

@pytest.mark.parametrize("text,expect", [
    ("7 August 2026\n\nThe Board announced…", _dt.date(2026, 8, 7)),
    ("August 7, 2026\nPress release", _dt.date(2026, 8, 7)),
    ("2026-08-07\nNotice", _dt.date(2026, 8, 7)),
])
def test_dates_at_the_top_of_a_document(text, expect):
    assert D.from_text(text) == expect


def test_an_effective_date_is_not_a_publication_date():
    """"Effective 1 November 2026" is when the rule bites, not when it was
    published — filing it as publication would put it in a future week."""
    assert D.from_text("Effective 1 November 2026\n\nThis guideline…") is None


@pytest.mark.parametrize("line", [
    "Comment period closes 20 July 2026",
    "Last updated 3 March 2026",
    "Accessed 1 January 2026",
    "© 2026 Some Regulator",
])
def test_other_dated_lines_are_ignored(line):
    assert D.from_text(f"{line}\n\nBody text follows.") is None


def test_a_real_date_after_a_rejected_line_is_still_found():
    text = "Effective 1 November 2026\n7 August 2026\nThe Board announced…"
    assert D.from_text(text) == _dt.date(2026, 8, 7)


def test_only_the_opening_is_scanned():
    """A date on page 40 is not this document's publication date."""
    text = ("filler line\n" * 900) + "7 August 2026\n"
    assert D.from_text(text) is None


def test_a_future_date_is_refused():
    far = _dt.date.today().year + 3
    assert D.from_text(f"1 January {far}\nNotice") is None


def test_nothing_found_returns_none_rather_than_today():
    assert D.from_text("No dates here at all.") is None
    assert D.recover(url="https://x.gov/a", text="nothing") == (None, "none")


# ── precedence and provenance ───────────────────────────────────────────────

def test_the_url_beats_the_text_when_both_are_present():
    got, how = D.recover(url="https://x.gov/2026/08/07/x",
                         text="1 February 2020\nOld reprint")
    assert got == _dt.date(2026, 8, 7) and how == "url"


def test_the_source_of_the_date_is_reported():
    """Stored as a tag, so a reader can tell an inferred date from a collected
    one — they are not equal evidence."""
    _, how = D.recover(url="https://x.gov/no-date", text="7 August 2026\nx")
    assert how == "text"
