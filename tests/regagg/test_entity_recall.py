"""
Entity-matching recall: the metric that decides whether this product works.

A miss means a desk sees nothing on the day its own obligor is in the news.
This suite pins recall against the ways companies are ACTUALLY written by
newsrooms and by the extractor, and it fails loudly rather than drifting.

"possible" counts as a catch: the analyst sees the item flagged for
verification. What is not allowed is a silent miss, or a wrong company
asserted as confirmed.
"""

from __future__ import annotations

import pytest

from sajha.regagg.matching import (WatchlistMatcher, acronym, core_tokens,
                                   generate_aliases, recall_report)

# (what the analyst typed, how the story wrote it, should it be caught)
SHOULD_CATCH = [
    # legal suffixes
    ("Goodfood", "Goodfood Market Corp.", True),
    ("Goodfood Market Corp.", "Goodfood", True),
    ("WestJet", "WestJet Airlines Ltd.", True),
    ("HSBC Holdings plc", "HSBC", True),
    ("Citadel LLC", "Citadel", True),
    ("Shopify Inc.", "Shopify", True),
    ("SoftBank Group Corp.", "SoftBank", True),
    # spacing and punctuation
    ("JPMorgan Chase & Co.", "JPMorgan", True),
    ("JPMorgan Chase & Co.", "JP Morgan", True),
    ("JPMorgan", "J.P. Morgan Chase", True),
    ("Warner Bros. Discovery", "Warner Bros Discovery", True),
    # possessives and short forms
    ("Shopify Inc.", "Shopify's", True),
    ("Uber Technologies Inc.", "Uber", True),
    ("Meta Platforms, Inc.", "Meta", True),
    ("Alphabet Inc.", "Alphabet", True),
    ("Toyota Motor Corp", "Toyota", True),
    ("Chipotle Mexican Grill", "Chipotle", True),
    ("Suncor Energy", "Suncor", True),
    ("The Walt Disney Company", "Disney", True),
    ("RioCan Real Estate Investment Trust", "RioCan REIT", True),
    # acronyms
    ("Advanced Micro Devices, Inc.", "AMD", True),
    ("Bank of America", "Bank of America Corp", True),
]

MUST_NOT_CONFIRM = [
    ("Bank of America", "Bank of Montreal", False),
    ("Bank of America", "Royal Bank of Canada", False),
    ("Goldman Sachs", "Goldman Environmental Prize", False),
    ("Meta Platforms, Inc.", "Metavante", False),
    ("Toyota Motor Corp", "Toyota Industries", False),
    ("Apple Inc.", "Apple Hospitality REIT", False),
    ("Suncor Energy", "Sun Life Financial", False),
    ("Citadel LLC", "Citadel Broadcasting", False),
]

RECALL_FLOOR = 1.0          # every known way of writing these must be caught

# Which of those are certainties rather than judgement calls. "Goodfood" vs
# "Goodfood Market Corp." is structurally identical to "Citadel" vs "Citadel
# Broadcasting" — one is the same company, one is not, and the strings cannot
# tell you which. Those stay "possible" (shown, flagged, one click to teach);
# only differences that are provably cosmetic are confirmed.
MUST_CONFIRM = [
    ("HSBC Holdings plc", "HSBC"),                  # legal suffix only
    ("Citadel LLC", "Citadel"),
    ("Shopify Inc.", "Shopify's"),                  # possessive
    ("Warner Bros. Discovery", "Warner Bros Discovery"),   # punctuation
    ("Advanced Micro Devices, Inc.", "AMD"),        # acronym
    ("Bank of America", "Bank of America Corp"),
]


def test_recall_against_real_name_variants():
    r = recall_report(SHOULD_CATCH)
    assert r["recall"] >= RECALL_FLOOR, (
        f"recall {r['recall']:.0%} — a desk would miss: {r['misses']}")


def test_cosmetic_differences_are_confirmed_not_merely_flagged():
    """Suffixes, punctuation and acronyms are certainties — do not nag the user."""
    for watch, written in MUST_CONFIRM:
        name, confidence, reason = WatchlistMatcher([watch]).match(written)
        assert (name, confidence) == (watch, "confirmed"), (watch, written, confidence)


def test_never_confirms_a_different_company():
    r = recall_report(MUST_NOT_CONFIRM)
    assert r["false_positives"] == 0, r["false_hits"]


def test_ambiguity_is_reported_not_guessed():
    """The one-word case cannot be settled from the text, so it is flagged."""
    m = WatchlistMatcher(["Apple Inc."])
    name, confidence, reason = m.match("Apple Hospitality REIT")
    assert name == "Apple Inc." and confidence == "possible"
    assert "may be" in reason                     # the page can explain itself


def test_a_shared_generic_word_is_not_a_match():
    """'Bank' identifies nothing; two banks must not collapse into one."""
    m = WatchlistMatcher(["Bank of America", "Royal Bank of Canada"])
    assert m.match("Bank of Montreal")[1] != "confirmed"
    assert m.match("First National Bank")[1] != "confirmed"


def test_a_two_word_name_yields_no_acronym():
    """'Goodfood Market' -> 'GM' would collide with General Motors."""
    assert acronym("Goodfood Market Corp.") is None
    assert acronym("Advanced Micro Devices, Inc.") == "amd"
    m = WatchlistMatcher(["Goodfood Market Corp."])
    assert m.match("General Motors")[1] != "confirmed"


def test_alias_generation_covers_the_common_spellings():
    aliases = generate_aliases("JPMorgan Chase & Co.")
    assert "jpmorgan chase" in aliases and "jpmorganchase" in aliases
    assert acronym("Advanced Micro Devices, Inc.") == "amd"
    assert core_tokens("Goodfood Market Corp.") == ["goodfood", "market"]


def test_a_user_taught_alias_is_honoured():
    """Nicknames the system cannot derive ('BofA') are learnable, not lost."""
    m = WatchlistMatcher(["Bank of America"],
                         extra_aliases={"Bank of America": ["BofA", "BAC"]})
    assert m.match("BofA")[:2] == ("Bank of America", "confirmed")
    assert m.match("BAC")[:2] == ("Bank of America", "confirmed")


def test_scale_does_not_degrade_precision():
    """With thousands of names, a generic word must still identify nothing."""
    names = ["Bank of America", "Goodfood"] + [f"Holdco {i} Capital" for i in range(2000)]
    m = WatchlistMatcher(names)
    assert m.match("Goodfood Market Corp.")[0] == "Goodfood"      # still caught
    assert m.match("Bank of Montreal")[1] != "confirmed"
    # 'capital' is shared by 2,000 names, so it identifies none of them
    assert m.match("Capital Power Corporation")[1] != "confirmed"
