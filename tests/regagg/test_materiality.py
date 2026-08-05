"""
Materiality scoring — priority must be deterministic, explainable, and put a
binding rule from a primary regulator above a routine press release.
"""
from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from sajha.regagg import materiality

REPO = Path(__file__).resolve().parents[2]
CFG = materiality.load_config(str(REPO / materiality.CONFIG_PATH))


def _s(**kw):
    kw.setdefault("cfg", CFG)
    return materiality.score(**kw)


def test_binding_rule_outranks_routine_announcement():
    """The headline requirement: a new capital rule from our primary regulator
    must rank far above a weather/press announcement from a watched regulator."""
    rule = _s(regulator_id="osfi", doc_type="final_rule",
              title="Capital Adequacy Requirements — amendments",
              text="capital requirement changes", change_kind="new")
    presser = _s(regulator_id="rbi", doc_type="announcement",
                 title="Office closure due to weather", change_kind="new")
    assert rule.score > presser.score + 40
    assert rule.band == "Critical" and presser.band in ("Low", "Informational")


def test_regulator_tier_scales_rather_than_floors():
    """Tier multiplies document weight: a home-regulator announcement stays low,
    while a home-regulator rule scales up (an additive tier floored everything)."""
    home_note = _s(regulator_id="osfi", doc_type="announcement", change_kind="new")
    watch_note = _s(regulator_id="rbi", doc_type="announcement", change_kind="new")
    home_rule = _s(regulator_id="osfi", doc_type="final_rule", change_kind="new")
    assert home_note.score > watch_note.score          # tier still matters
    assert home_note.band in ("Low", "Informational")  # but doesn't inflate noise
    assert home_rule.band == "Critical"


def test_deadline_proximity_raises_priority():
    soon = _s(regulator_id="osfi", doc_type="consultation", change_kind="new",
              comment_deadline=date.today() + timedelta(days=10))
    later = _s(regulator_id="osfi", doc_type="consultation", change_kind="new",
               comment_deadline=date.today() + timedelta(days=200))
    assert soon.score > later.score
    assert "comment deadline" in soon.reason


def test_revision_magnitude_counts():
    small = _s(regulator_id="frb", doc_type="guidance", change_kind="revised",
               lines_changed=3)
    large = _s(regulator_id="frb", doc_type="guidance", change_kind="revised",
               lines_changed=500)
    assert large.score > small.score and "lines changed" in large.reason


def test_topic_keyword_fallback_when_no_tags():
    """Rule-based corpus has no LLM tags — keywords must still find the domain."""
    m = _s(regulator_id="frb", doc_type="guidance",
           title="Interagency guidance on counterparty credit risk",
           text="This guidance addresses counterparty credit exposures.",
           change_kind="new")
    assert any("ccr" in r or "credit_risk" in r for r in m.reasons)


def test_every_score_is_explainable_and_bounded():
    m = _s(regulator_id="osfi", doc_type="final_rule",
           title="Capital rule", text="capital requirement",
           change_kind="revised", lines_changed=900,
           comment_deadline=date.today() + timedelta(days=5))
    assert 0 <= m.score <= 100
    assert m.reason and len(m.reasons) >= 3   # never an unexplained number
    assert m.band in materiality.BAND_ORDER


def test_scoring_is_deterministic():
    a = _s(regulator_id="osfi", doc_type="guidance", title="X", change_kind="new")
    b = _s(regulator_id="osfi", doc_type="guidance", title="X", change_kind="new")
    assert (a.score, a.band, a.reason) == (b.score, b.band, b.reason)
