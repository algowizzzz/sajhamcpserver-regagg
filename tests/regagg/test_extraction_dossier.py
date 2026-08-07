"""
Sprint 2 — extraction and distillation.

The contract these prove: selection is deterministic and reproducible, the
ledger conserves, a credit event outranks market noise, and a 6,000-name
watchlist costs the same as a small one.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from sajha.regagg import dossier as D
from sajha.regagg import myday as M
from sajha.regagg import personas as P
from sajha.regagg.extraction import (DeterministicExtractor, EntityIndex,
                                     LLMExtractor, classify_event, normalize_name)
from sajha.regagg.models import Document, RegUser, Regulator

NOW = datetime(2026, 8, 6, 6, 0, tzinfo=timezone.utc)
DAY = "2026-08-06"


# ── extraction ──────────────────────────────────────────────────────────────

def test_name_normalisation_folds_how_newsrooms_write_companies():
    assert normalize_name("Goodfood Market Corp.") == normalize_name("goodfood market")
    assert normalize_name("The Suncor Energy Inc") == normalize_name("Suncor Energy")


def test_entity_index_finds_multiword_names_and_ignores_noise():
    idx = EntityIndex(["Goodfood Market Corp", "WestJet"])
    hits = {h["canonical"] for h in idx.find(
        "Meal kit company Goodfood Market granted creditor protection")}
    assert hits == {"Goodfood Market Corp"}
    assert idx.find("Bank of Canada holds rates") == []


def test_event_classification_ranks_credit_events_above_market_chatter():
    assert classify_event("Firm granted creditor protection")[0] == "credit_event"
    assert classify_event("Hedge fund meltdown, margin calls")[0] == "ccr_signal"
    assert classify_event("Stocks rally as shares climb")[0] == "general"


def test_llm_extractor_falls_back_when_the_provider_fails():
    class Boom:
        class messages:
            @staticmethod
            def create(**kw):
                raise RuntimeError("provider down")
    ex = LLMExtractor(EntityIndex(["Goodfood"]), client=Boom())
    out = ex.extract("Goodfood granted creditor protection")
    assert out["llm_error"] is True                      # flagged, not hidden
    assert out["event_type"] == "credit_event"           # still usable
    assert out["entities"][0]["canonical"] == "Goodfood"


def test_llm_extraction_is_attributable():
    class Fake:
        class messages:
            @staticmethod
            def create(**kw):
                class B:
                    text = ('{"entities":[{"canonical":"Goodfood Market Corp",'
                            '"as_written":"the Montreal meal-kit maker","confidence":"high"}],'
                            '"event_type":"credit_event","event_subtype":"creditor_protection",'
                            '"severity_signals":["court-granted"]}')
                return type("R", (), {"content": [B()]})()
    ex = LLMExtractor(EntityIndex([]), client=Fake())
    out = ex.extract("Montreal meal-kit maker granted protection")
    # resolves an oblique reference no keyword list would catch
    assert out["entities"][0]["canonical"] == "Goodfood Market Corp"
    assert out["entities"][0]["as_written"] == "the Montreal meal-kit maker"
    assert out["backend"] == "llm" and out["version"]


# ── distillation ────────────────────────────────────────────────────────────

def _seed_news_corpus(session, storage=None):
    session.add(Regulator(regulator_id="wire_a", name="Wire A", jurisdiction="CA",
                          connector="rss", config={}, category="news"))
    session.add(Regulator(regulator_id="wire_b", name="Wire B", jurisdiction="CA",
                          connector="rss", config={}, category="news"))
    rows = [
        ("wire_a", "d1", "Goodfood granted creditor protection from court"),
        ("wire_b", "d2", "Meal kit Goodfood granted creditor protection, court filing"),
        ("wire_a", "d3", "Stocks rally as shares climb on tech optimism"),
        ("wire_a", "d4", "WestJet resumes flights after work stoppage"),
        ("wire_a", "d5", "Unrelated company announces new packaging"),
    ]
    for rid, did, title in rows:
        session.add(Document(regulator_id=rid, doc_id=did, doc_type="news_story",
                             title=title, content_hash="h", s3_prefix=f"p/{did}",
                             source_url=f"https://x/{did}", published_date=None,
                             ingested_at=NOW, materiality_score=16,
                             materiality_band="Low"))
    session.commit()


def _persona(session, names, lane="news", **cfg):
    u, _ = __import__("sajha.regagg.auth", fromlist=["auth"]).create_user(
        session, f"{lane}{len(names)}@bank.test", "correct-horse-9")
    return P.save_persona(session, owner_id=u.user_id, name="P", lane=lane,
                          config=cfg or None,
                          entities=[{"canonical": n} for n in names])


def test_dossier_clusters_the_same_event_across_wires(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood", "WestJet"])
    d = D.build_dossier(session, p, day=DAY, now=NOW)
    titles = [i["title"] for i in d["items"]]
    assert len(titles) == 2                       # Goodfood cluster + WestJet
    top = d["items"][0]
    assert top["event_type"] == "credit_event"    # outranks the ops story
    assert top["corroboration"] == 2              # two wires, one event
    assert "credit event" in top["why"]


def test_ledger_conserves_and_reports_silence(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood", "WestJet", "Quiet Co", "Also Quiet"])
    d = D.build_dossier(session, p, day=DAY, now=NOW)
    led = d["ledger"]
    assert led["matched"] == led["shown"] + led["suppressed_below_floor"] \
        + led["suppressed_overflow"]
    assert led["watchlist_size"] == 4
    assert led["entities_with_events"] == 2
    assert led["quiet_entities"] == 2             # silence is a number
    assert led["scanned_documents"] == 5


def test_selection_is_reproducible(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood"])
    a = D.build_dossier(session, p, day=DAY, now=NOW)
    b = D.build_dossier(session, p, day=DAY, now=NOW)
    assert [i["cluster_key"] for i in a["items"]] == [i["cluster_key"] for i in b["items"]]
    assert a["ledger"] == b["ledger"]


def test_persona_weights_change_the_ordering_not_the_facts(session):
    _seed_news_corpus(session)
    default = _persona(session, ["Goodfood", "WestJet"])
    d1 = D.build_dossier(session, default, day=DAY, now=NOW)
    assert d1["items"][0]["event_type"] == "credit_event"

    ops_first = _persona(session, ["Goodfood", "WestJet", "x"],
                         salience={"topic_weights": {"operations": 99, "credit": 5}})
    d2 = D.build_dossier(session, ops_first, day=DAY, now=NOW)
    assert d2["items"][0]["event_type"] == "operations"
    assert len(d1["items"]) == len(d2["items"])    # same facts, different order


def test_a_big_watchlist_does_not_change_the_cost_model(session):
    """6,000 names must not mean 6,000 scans: matching is per-text, not per-name."""
    _seed_news_corpus(session)
    names = ["Goodfood"] + [f"Obligor {i}" for i in range(6000)]
    p = _persona(session, names)
    d = D.build_dossier(session, p, day=DAY, now=NOW)
    assert d["ledger"]["watchlist_size"] == 6001
    assert d["ledger"]["entities_with_events"] == 1
    assert d["ledger"]["quiet_entities"] == 6000
    assert d["items"][0]["event_type"] == "credit_event"


# ── my day ──────────────────────────────────────────────────────────────────

def test_my_day_page_is_built_validated_and_cached(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood", "WestJet"])
    out = M.build_my_day(session, p, day=DAY, now=NOW)
    assert out["cached"] is False
    # whichever composer ran, the page must satisfy the contract
    assert out["generator"] == "template" or out["generator"].startswith("llm:")
    ok, problems = M.validate_spec(out["spec"], out["dossier"])
    assert ok, problems
    again = M.build_my_day(session, p, day=DAY, now=NOW)
    assert again["cached"] is True                     # one truth per day
    assert again["spec"]["sections"][0]["text"] == out["spec"]["sections"][0]["text"]


def test_editing_the_persona_rebuilds_the_page(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood"])
    first = M.build_my_day(session, p, day=DAY, now=NOW)
    P.save_persona(session, owner_id=p.owner_id, name="P", lane="news",
                   persona_id=p.persona_id,
                   entities=[{"canonical": "Goodfood"}, {"canonical": "WestJet"}])
    p2 = session.get(type(p), p.persona_id)
    second = M.build_my_day(session, p2, day=DAY, now=NOW)
    assert second["cached"] is False
    assert second["ledger"]["watchlist_size"] == 2


def test_validator_rejects_invented_numbers_and_bad_citations(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood"])
    d = D.build_dossier(session, p, day=DAY, now=NOW)
    spec = M.compose_template(d, "narrative_first")
    assert M.validate_spec(spec, d)[0]

    bad = dict(spec)
    bad["sections"] = [dict(s) for s in spec["sections"]]
    bad["sections"][0] = {**bad["sections"][0],
                          "text": "Losses reached 47 billion dollars overnight."}
    ok, problems = M.validate_spec(bad, d)
    assert not ok and any("47" in p for p in problems)

    bad2 = dict(spec)
    bad2["sections"] = [{**spec["sections"][0], "citations": ["no-such-doc"]}]
    assert not M.validate_spec(bad2, d)[0]


def test_llm_composer_output_is_discarded_when_it_breaks_the_contract(session):
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood"])
    d = D.build_dossier(session, p, day=DAY, now=NOW)

    class Liar:
        class messages:
            @staticmethod
            def create(**kw):
                class B:
                    text = '{"lede": "Losses hit 999 million across 42 counterparties."}'
                return type("R", (), {"content": [B()]})()
    spec = M.LLMComposer(client=Liar()).compose(d, "narrative_first")
    assert spec["generator"] == "template"          # fabricated figures rejected
    assert "999" not in spec["sections"][0]["text"]

    class Honest:
        class messages:
            @staticmethod
            def create(**kw):
                class B:
                    text = '{"lede": "A watched name entered creditor protection."}'
                return type("R", (), {"content": [B()]})()
    good = M.LLMComposer(client=Honest()).compose(d, "narrative_first")
    assert good["generator"].startswith("llm:")
    assert "creditor protection" in good["sections"][0]["text"]


# ── S5: onboarding, intraday, scale ─────────────────────────────────────────

def test_starters_are_usable_as_saved_personas(session):
    """Every starter must produce a valid persona without editing."""
    from sajha.regagg.personas import STARTERS, save_persona, persona_dict, parse_entities
    u, _ = __import__("sajha.regagg.auth", fromlist=["auth"]).create_user(
        session, "starter@bank.test", "correct-horse-9")
    for s in STARTERS:
        p = save_persona(session, owner_id=u.user_id, name=s["name"], lane=s["lane"],
                         config=s["config"],
                         entities=parse_entities(s["example_entities"]))
        d = persona_dict(session, p)
        assert d["layout"] in ("narrative_first", "exception_first", "change_first")
        assert d["lane"] == s["lane"]


def test_intraday_update_annotates_without_rewriting_the_page(session):
    """Someone who read the 07:30 page must still see what they read."""
    _seed_news_corpus(session)
    p = _persona(session, ["Goodfood", "WestJet"])
    morning = M.build_my_day(session, p, day=DAY, now=NOW)
    morning_lede = morning["spec"]["sections"][0]["text"]

    # a new serious item lands at midday
    session.add(Document(regulator_id="wire_a", doc_id="d9",
                         doc_type="news_story",
                         title="WestJet seeks creditor protection after filing",
                         content_hash="h", s3_prefix="p/d9",
                         source_url="https://x/d9", ingested_at=NOW,
                         materiality_score=20, materiality_band="Low"))
    session.commit()

    later = datetime(2026, 8, 6, 14, 0, tzinfo=timezone.utc)
    updates = M.refresh_intraday(session, now=later)
    assert updates and updates[0]["new_serious"] >= 1
    assert updates[0]["note"].startswith("14:00")

    after = M.build_my_day(session, p, day=DAY, now=later)
    assert after["spec"]["sections"][0]["text"] == morning_lede   # not rewritten
    assert "new serious item" in (after["updated_note"] or "")    # but announced


def test_my_day_stays_fast_with_a_six_thousand_name_book(session):
    """The scale promise: a big book must not be a slow page."""
    import time
    _seed_news_corpus(session)
    names = ["Goodfood"] + [f"Obligor {i}" for i in range(6000)]
    p = _persona(session, names)
    start = time.perf_counter()
    out = M.build_my_day(session, p, day=DAY, now=NOW)
    elapsed = time.perf_counter() - start
    assert out["ledger"]["watchlist_size"] == 6001
    assert elapsed < 5.0, f"6,000-name page took {elapsed:.1f}s"


def test_watchlist_matches_how_analysts_actually_type_names(session):
    """An analyst types "Goodfood"; the extractor returns "Goodfood Market Corp."

    Exact matching silently dropped these, so a desk saw nothing on a day its
    own name was in the news — the worst possible failure for this product.
    """
    from sajha.regagg.dossier import _watch_match
    from sajha.regagg.extraction import normalize_name
    watch = {normalize_name(n): n for n in
             ["Goodfood", "WestJet", "Bank of America", "SpaceX"]}
    assert _watch_match("Goodfood Market Corp.", watch) == "Goodfood"
    assert _watch_match("WestJet Airlines Ltd.", watch) == "WestJet"
    assert _watch_match("SpaceX", watch) == "SpaceX"
    # and it must not over-match: a different bank is not your counterparty
    assert _watch_match("Bank of Montreal", watch) is None
    assert _watch_match("Royal Bank", watch) is None
    assert _watch_match("Alphabet Inc.", watch) is None


def test_topic_only_matches_are_context_not_exceptions(session):
    """A desk that follows a topic must not have every story marked serious."""
    _seed_news_corpus(session)
    session.add(Document(regulator_id="wire_a", doc_id="r1", doc_type="news_story",
                         title="Fed holds rates as inflation cools",
                         content_hash="h", s3_prefix="p/r1",
                         source_url="https://x/r1", ingested_at=NOW,
                         materiality_score=10, materiality_band="Low"))
    session.commit()
    p = _persona(session, [], salience={"topic_weights": {"rates": 85},
                                        "serious_threshold": 70},
                 )
    # give it the topic scope after creation
    from sajha.regagg import personas as _P
    p = _P.save_persona(session, owner_id=p.owner_id, name="P", lane="news",
                        persona_id=p.persona_id, entities=[],
                        config={"scope": {"topics": ["rates"]},
                                "salience": {"topic_weights": {"rates": 85},
                                             "serious_threshold": 70}})
    d = D.build_dossier(session, p, day=DAY, now=NOW)
    rates = [i for i in d["items"] if i["event_type"] == "rates"]
    assert rates, "the rates story should be in scope"
    # dampened: a topic match alone must not clear a high bar
    assert rates[0]["severity"] == "watch"
    assert "topic match" in rates[0]["why"]
