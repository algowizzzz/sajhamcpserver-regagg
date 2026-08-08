"""A focused view narrows what you already have. It never widens it.

The risk with a free-text box over a generated page is that the two become
indistinguishable: a filtered page that looks like the daily page will be
quoted as one, and a prompt that could add documents would be a search box
wearing a summary's clothes. Every test here defends one of those lines.
"""

from __future__ import annotations

import json

import pytest

from sajha.regagg import focus as F


def _item(key, title, *, entities=(), possible=(), sources=(), severity="watch",
          preview=""):
    return {"cluster_key": key, "title": title, "entities": list(entities),
            "possible_entities": [{"name": p} for p in possible],
            "sources": list(sources),
            "docs": [{"regulator_id": s, "doc_id": f"d-{s}"} for s in sources],
            "severity": severity, "event_type": "credit", "preview": preview}


ITEMS = [
    _item("a", "Warren presses OCC on United Texas Bank",
          entities=["United Texas Bank"], sources=["american_banker"],
          severity="serious", preview="The senator asked the comptroller to act."),
    _item("b", "Apollo raises credit fund target", entities=["Apollo"],
          sources=["reuters"]),
    _item("c", "MAS consults on stablecoin disclosure", sources=["mas"]),
    _item("d", "Barclays hires for private credit", possible=["Barclays plc"],
          sources=["reuters"]),
]

PAGE = {"spec": {"day": "2026-08-07"},
        "dossier": {"items": ITEMS, "ledger": {"scanned_documents": 338,
                                               "matched": 16, "shown": 4}}}


class Echo:
    """A model that reverses the order and writes a clean note."""
    def __init__(self, order=None, note="Top item concerns United Texas Bank."):
        self.order, self.note = order, note

    def complete(self, system, user, **kw):
        keys = [l.split("]")[0][1:] for l in user.splitlines() if l.startswith("[")]
        return json.dumps({"order": self.order or list(reversed(keys)),
                           "note": self.note})


# ── filtering is deterministic ──────────────────────────────────────────────

def test_an_entity_filter_keeps_only_cards_naming_it():
    kept, acc = F.apply_filters(ITEMS, entities=["Apollo"])
    assert [i["cluster_key"] for i in kept] == ["b"]
    assert acc["input"] == 4 and acc["kept"] == 1
    assert acc["dropped_no_entity_match"] == 3


def test_an_ambiguous_match_is_kept_not_quietly_dropped():
    """Filtering by a name must surface the uncertain hits, not hide them —
    those are the ones the person most needs to judge."""
    kept, _ = F.apply_filters(ITEMS, entities=["Barclays"])
    assert [i["cluster_key"] for i in kept] == ["d"]


def test_a_source_filter_matches_the_documents_behind_the_card():
    kept, acc = F.apply_filters(ITEMS, sources=["reuters"])
    assert {i["cluster_key"] for i in kept} == {"b", "d"}
    assert acc["dropped_no_source_match"] == 2


def test_clauses_combine_as_and():
    kept, _ = F.apply_filters(ITEMS, entities=["Apollo"], sources=["mas"])
    assert kept == []


def test_no_filter_keeps_everything():
    kept, acc = F.apply_filters(ITEMS)
    assert len(kept) == 4 and acc["kept"] == 4


def test_terms_accept_a_pasted_string_as_well_as_a_list():
    assert F._terms("Apollo, United Texas Bank\nBarclays") == \
        ["Apollo", "United Texas Bank", "Barclays"]
    assert F._terms(["a", "A", " a "]) == ["a"]      # case-insensitive dedupe
    assert F._terms(None) == []


# ── the prompt may reorder and narrate, nothing else ────────────────────────

def test_the_prompt_reorders_without_adding_or_losing_anything():
    out = F.rank_by_prompt(list(ITEMS), "what touches CRE", client=Echo())
    assert out["ranked"] is True
    assert [i["cluster_key"] for i in out["items"]] == ["d", "c", "b", "a"]
    assert len(out["items"]) == len(ITEMS)


def test_an_item_the_model_invents_voids_the_ranking():
    """If it can name a card that does not exist, its order cannot be trusted."""
    out = F.rank_by_prompt(list(ITEMS), "x", client=Echo(order=["a", "ghost"]))
    assert out["ranked"] is False
    assert "not in the list" in out["reason"]
    assert [i["cluster_key"] for i in out["items"]] == ["a", "b", "c", "d"]


def test_a_note_with_an_invented_figure_is_withheld_but_the_order_survives():
    out = F.rank_by_prompt(list(ITEMS), "x",
                           client=Echo(note="Exposure totals $947 million."))
    assert out["note"] is None
    assert "947" in out["reason"]
    assert out["ranked"] is True


def test_no_prompt_means_no_call_and_no_reorder():
    out = F.rank_by_prompt(list(ITEMS), "", client=Echo())
    assert out["ranked"] is False
    assert [i["cluster_key"] for i in out["items"]] == ["a", "b", "c", "d"]


def test_a_provider_failure_degrades_to_the_deterministic_order():
    class Broken:
        def complete(self, *a, **k):
            raise RuntimeError("upstream 503")

    out = F.rank_by_prompt(list(ITEMS), "x", client=Broken())
    assert out["ranked"] is False
    assert "unavailable" in out["reason"]
    assert len(out["items"]) == 4


def test_with_no_model_the_filter_still_works():
    out = F.rank_by_prompt(list(ITEMS), "x", client=None)
    assert out["ranked"] is False
    assert "not reordered" in out["reason"]


# ── the view as a whole ─────────────────────────────────────────────────────

def test_a_focused_view_says_it_is_not_the_daily_page():
    v = F.focus(PAGE, entities=["Apollo"], client=Echo())
    assert v["focused"] is True
    assert "daily page is" in v["notice"] and "unchanged" in v["notice"]
    assert v["criteria"]["entities"] == ["Apollo"]


def test_focus_never_mutates_the_page_it_was_given():
    """The cached page is a record; someone may already have acted on it."""
    before = json.dumps(PAGE, sort_keys=True, default=str)
    F.focus(PAGE, prompt="anything", entities=["Apollo"], sources=["reuters"],
            client=Echo())
    assert json.dumps(PAGE, sort_keys=True, default=str) == before


def test_the_ledger_is_recounted_for_what_survived():
    v = F.focus(PAGE, entities=["United Texas Bank"], client=Echo())
    assert v["ledger"]["shown"] == 1
    assert v["ledger"]["serious"] == 1
    assert v["ledger"]["scanned_documents"] == 338     # provenance preserved


def test_the_view_reports_what_each_clause_removed():
    v = F.focus(PAGE, entities=["Apollo"], client=Echo())
    assert v["filtering"] == {"input": 4, "kept": 1,
                              "dropped_no_entity_match": 3,
                              "dropped_no_source_match": 0}


def test_a_prompt_can_never_reintroduce_a_filtered_out_card():
    """The ordering step only ever sees what survived the filters."""
    v = F.focus(PAGE, prompt="tell me about MAS", entities=["Apollo"],
                client=Echo(order=["b"]))
    assert [i["cluster_key"] for i in v["items"]] == ["b"]


def test_an_over_long_prompt_is_truncated_not_rejected():
    v = F.focus(PAGE, prompt="x" * 5000, client=Echo())
    assert len(v["criteria"]["prompt"]) == F.MAX_PROMPT
