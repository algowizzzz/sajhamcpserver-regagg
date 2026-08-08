"""The entity table: every name accounted for, every column trustworthy.

Two properties carry the whole feature. A row exists for every watched name,
because the quiet ones are the reassurance that the sweep looked. And a
generated column only ever holds a value the desk declared, because an analyst
will sort and filter on it — a column that silently widened its own vocabulary
would break every filter built on it without looking broken.
"""

from __future__ import annotations

import datetime as _dt
import json

import pytest

from sajha.regagg import entity_table as ET
from sajha.regagg import table_schema as TS
from sajha.regagg import tavily as TV
from sajha.regagg.models import EntityScan, PersonaEntity

DAY = "2026-08-08"

SPEC = """
columns:
  - name: event
    label: Event
    values: [major, minor, none]
  - name: note
    type: text
    max_chars: 40
"""


# ── the column schema ───────────────────────────────────────────────────────

def test_yaml_and_json_are_both_accepted():
    a, _ = TS.parse(SPEC)
    b, _ = TS.parse(json.dumps({"columns": [
        {"name": "event", "label": "Event", "values": ["major", "minor", "none"]},
        {"name": "note", "type": "text", "max_chars": 40}]}))
    assert [c.name for c in a] == [c.name for c in b] == ["event", "note"]


def test_a_value_outside_the_declared_set_becomes_unknown_not_a_guess():
    """The property the whole table rests on."""
    cols, _ = TS.parse(SPEC)
    ev = cols[0]
    assert ev.coerce("major") == "major"
    assert ev.coerce(" MAJOR. ") == "major"        # case and punctuation only
    assert ev.coerce("major event") == TS.UNKNOWN  # near-miss is still a miss
    assert ev.coerce("catastrophic") == TS.UNKNOWN
    assert ev.coerce(None) == TS.UNKNOWN


def test_every_declared_column_appears_on_every_row():
    cols, _ = TS.parse(SPEC)
    row = TS.coerce_row(cols, {"event": "minor", "invented": "x"})
    assert set(row) == {"event", "note"}           # nothing undeclared survives
    assert row["event"] == "minor"


def test_text_columns_are_truncated_to_their_declared_length():
    cols, _ = TS.parse(SPEC)
    assert len(cols[1].coerce("x" * 500)) == 40


def test_reserved_names_cannot_be_redefined():
    cols, problems = TS.parse("columns:\n  - name: entity\n    values: [a, b]\n")
    assert cols == []
    assert any("cannot be redefined" in p for p in problems)


def test_a_broken_schema_reports_why_instead_of_vanishing():
    cols, problems = TS.parse("columns: [ unclosed")
    assert cols == []
    assert problems and "parse" in problems[0]


def test_an_enum_with_no_values_degrades_to_text_and_says_so():
    cols, problems = TS.parse("columns:\n  - name: x\n    type: enum\n")
    assert cols[0].kind == "text"
    assert any("needs values" in p for p in problems)


def test_the_prompt_fragment_is_generated_from_the_schema():
    """So the instruction and the validation cannot drift apart."""
    cols, _ = TS.parse(SPEC)
    frag = TS.prompt_fragment(cols)
    for v in ("major", "minor", "none"):
        assert f'"{v}"' in frag
    assert TS.UNKNOWN in frag


# ── the sweep ───────────────────────────────────────────────────────────────

@pytest.fixture()
def persona_with_names(session, storage):
    from sajha.regagg import runtime
    from sajha.regagg.models import Persona
    p = Persona(persona_id="p-1", owner_id="u-1", name="Book", lane="news",
                config={"table": {"columns": SPEC}}, version_n=1)
    session.add(p)
    for n in ["Alpha Corp", "Beta Bank", "Gamma Insurance", "Delta Energy"]:
        session.add(PersonaEntity(persona_id="p-1", canonical=n, kind="obligor"))
    session.commit()
    runtime.set_providers(session=lambda: session, storage=lambda: storage)
    yield p
    runtime.set_providers(session=lambda: None)


class OneHit:
    """A search that finds something for every name."""
    credits = 4

    def __init__(self):
        self.searches = 0

    def search(self, name, **kw):
        self.searches += 1
        return [TV.Hit(title=f"{name} in the news", url=f"https://x/{name}",
                       snippet="Something happened.", source="x.com",
                       published=DAY)]


class Silent:
    credits = 0
    searches = 0

    def search(self, name, **kw):
        return []


def test_every_watched_name_gets_a_row_even_with_no_news(session, persona_with_names):
    ET.sweep(session, persona_with_names, day=DAY, client=Silent())
    t = ET.table(session, persona_with_names, day=DAY)
    assert t["total"] == 4 and len(t["rows"]) == 4
    assert {r["status"] for r in t["rows"]} == {"none"}
    # and the row says WHY it is empty
    assert all(r["detail"] for r in t["rows"])


def test_a_rerun_does_not_pay_for_names_already_searched(session, persona_with_names):
    c1 = OneHit()
    ET.sweep(session, persona_with_names, day=DAY, client=c1)
    assert c1.searches == 4
    c2 = OneHit()
    out = ET.sweep(session, persona_with_names, day=DAY, client=c2)
    assert c2.searches == 0                 # the whole point of the cache
    assert out["cached"] == 4


def test_refresh_re_searches_deliberately(session, persona_with_names):
    ET.sweep(session, persona_with_names, day=DAY, client=OneHit())
    c = OneHit()
    ET.sweep(session, persona_with_names, day=DAY, client=c, refresh=True)
    assert c.searches == 4


def test_the_budget_stops_the_sweep_and_names_what_it_missed(session, persona_with_names):
    out = ET.sweep(session, persona_with_names, day=DAY, budget=2, client=OneHit())
    assert out["searched"] == 2 and out["skipped"] == 2
    assert "budget" in out["detail"]
    t = ET.table(session, persona_with_names, day=DAY)
    skipped = [r for r in t["rows"] if r["status"] == "skipped"]
    assert len(skipped) == 2
    # "not reached" must not read as "nothing found"
    assert all("budget" in r["detail"] for r in skipped)


def test_one_failing_name_does_not_end_the_sweep(session, persona_with_names):
    class Flaky(OneHit):
        def search(self, name, **kw):
            if name == "Beta Bank":
                raise RuntimeError("upstream 500")
            return super().search(name)

    out = ET.sweep(session, persona_with_names, day=DAY, client=Flaky())
    assert out["errors"] == 1
    t = ET.table(session, persona_with_names, day=DAY)
    assert {r["status"] for r in t["rows"]} == {"ok", "error"}


def test_a_failed_row_is_retried_by_the_next_sweep_but_a_quiet_one_is_not(
        session, persona_with_names):
    """An error is a gap; 'no news' is an answer."""
    session.add(EntityScan(persona_id="p-1", day=DAY, entity="Alpha Corp",
                           status="error", mode="live", hits=[], columns={}))
    session.add(EntityScan(persona_id="p-1", day=DAY, entity="Beta Bank",
                           status="none", mode="live", hits=[], columns={}))
    session.commit()
    c = OneHit()
    ET.sweep(session, persona_with_names, day=DAY, client=c)
    assert c.searches == 3          # Alpha retried, Beta left alone, 2 new


# ── demo mode is never mistaken for real ────────────────────────────────────

def test_demo_rows_are_marked_at_every_level(session, persona_with_names):
    ET.sweep(session, persona_with_names, day=DAY, client=TV.DemoNews(day=DAY))
    t = ET.table(session, persona_with_names, day=DAY)
    assert t["mode"] == "demo"
    assert t["demo_rows"] == 4
    assert all(r["mode"] == "demo" for r in t["rows"])
    hits = [h for r in session.scalars(
        __import__("sqlalchemy").select(EntityScan)).all() for h in (r.hits or [])]
    assert hits and all(h["demo"] for h in hits)


def test_demo_costs_nothing_and_is_stable_across_calls():
    a = TV.DemoNews(day=DAY).search("Alpha Corp")
    b = TV.DemoNews(day=DAY).search("Alpha Corp")
    assert [h.title for h in a] == [h.title for h in b]
    assert TV.DemoNews(day=DAY).credits == 0


def test_an_unswept_table_claims_neither_live_nor_demo(session, persona_with_names):
    t = ET.table(session, persona_with_names, day=DAY)
    assert t["mode"] == ""          # nothing searched yet, so no claim
    assert t["counts"] == {"pending": 4}


def test_the_live_client_refuses_rather_than_inventing():
    with pytest.raises(TV.NotConfigured):
        TV.TavilyNews(key=None).search("Alpha Corp")


# ── classification ──────────────────────────────────────────────────────────

class Labeller:
    def __init__(self, values):
        self.values = values

    def complete(self, system, user, **kw):
        ids = [r["id"] for r in json.loads(user.split("ROWS:\n", 1)[1])]
        return json.dumps({"rows": [dict(id=i, **self.values) for i in ids]})


def test_classification_fills_declared_columns(session, persona_with_names):
    ET.sweep(session, persona_with_names, day=DAY, client=OneHit())
    out = ET.classify(session, persona_with_names, day=DAY,
                      client=Labeller({"event": "major", "note": "watch this"}))
    assert out["classified"] == 4
    t = ET.table(session, persona_with_names, day=DAY)
    assert all(r["columns"]["event"] == "major" for r in t["rows"])


def test_a_model_value_outside_the_schema_lands_as_unknown(session, persona_with_names):
    ET.sweep(session, persona_with_names, day=DAY, client=OneHit())
    ET.classify(session, persona_with_names, day=DAY,
                client=Labeller({"event": "catastrophic"}))
    t = ET.table(session, persona_with_names, day=DAY)
    assert all(r["columns"]["event"] == TS.UNKNOWN for r in t["rows"])


def test_rows_with_no_news_are_not_sent_to_the_model(session, persona_with_names):
    ET.sweep(session, persona_with_names, day=DAY, client=Silent())
    calls = []

    class Counting(Labeller):
        def complete(self, s, u, **kw):
            calls.append(u)
            return super().complete(s, u, **kw)

    out = ET.classify(session, persona_with_names, day=DAY,
                      client=Counting({"event": "none"}))
    assert calls == [] and out["classified"] == 0


def test_a_failed_batch_leaves_rows_unclassified_rather_than_guessed(
        session, persona_with_names):
    class Broken:
        def complete(self, *a, **k):
            raise RuntimeError("down")

    ET.sweep(session, persona_with_names, day=DAY, client=OneHit())
    out = ET.classify(session, persona_with_names, day=DAY, client=Broken())
    assert out["classified"] == 0
    t = ET.table(session, persona_with_names, day=DAY)
    assert all(r["columns"] == {} for r in t["rows"])


# ── the headline ────────────────────────────────────────────────────────────

def test_the_headline_is_withheld_if_it_invents_a_figure():
    rows = [{"entity": "Alpha Corp", "status": "ok", "title": "t", "snippet": "s"}]

    class Liar:
        def complete(self, *a, **k):
            return json.dumps({"summary": "Alpha Corp faces a $874 million charge."})

    out = ET.summarise(rows, total=4, client=Liar())
    assert out["generated"] is False
    assert "874" in out["reason"]


def test_with_nothing_to_report_the_headline_says_so_without_a_model():
    out = ET.summarise([{"entity": "a", "status": "none"}], total=4)
    assert out["generated"] is False
    assert "4" in out["summary"]
