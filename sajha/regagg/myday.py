"""
My Day: dossier -> UI spec -> cached page.

The composer decides WHAT TO SHOW AND HOW TO SAY IT; it never invents a number.
Two composers behind one interface — a template composer (always available,
deterministic) and an LLM composer (when a key is set) that writes the lede.
Whatever composes, the spec is validated before it can be rendered:

  coverage  every dossier item is rendered or explicitly suppressed-with-reason
  citation  every referenced doc id exists in the dossier
  numeric   every number in the prose appears in the dossier

A spec that fails validation is discarded and the deterministic template is
used instead. A degraded My Day is a page without narrative — never a page
with wrong figures, and never no page at all.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

from sajha.regagg.models import PageSpec, Persona

LAYOUTS = ("exception_first", "change_first", "narrative_first")


# ── template composer (the floor, and the fallback) ─────────────────────────

def _fmt(n: int) -> str:
    return f"{n:,}"


def compose_template(dossier: dict, layout: str) -> dict:
    led = dossier["ledger"]
    items = dossier["items"]
    serious = [i for i in items if i["severity"] == "serious"]
    watch = [i for i in items if i["severity"] == "watch"]
    lane = dossier["lane"]

    if layout == "exception_first":
        if led["watchlist_size"]:
            lede = (f"{led['entities_with_events']} of {_fmt(led['watchlist_size'])} "
                    f"names you follow had events. {_fmt(led['quiet_entities'])} were quiet.")
        else:
            lede = f"{led['shown']} items matched your scope today."
        if serious:
            lede += f" {len(serious)} need attention first: {serious[0]['title']}."
        else:
            lede += " Nothing reached your serious threshold."
    elif layout == "change_first":
        fams = dossier.get("rule_families_watched") or []
        changed = [i for i in items if i["rule_families"]]
        if fams and not changed:
            lede = (f"Your {len(fams)} rule famil{'y is' if len(fams) == 1 else 'ies are'} "
                    f"unchanged — verified against {_fmt(led['scanned_documents'])} "
                    f"documents collected for {dossier['day']}.")
        elif changed:
            lede = (f"{len(changed)} of your watched rules moved: "
                    f"{changed[0]['title']}.")
        else:
            lede = (f"{led['shown']} items in your scope today; no watched rule changed.")
    else:  # narrative_first
        if items:
            top = items[0]
            lede = (f"{top['title']} leads your day"
                    + (f" — {top['corroboration']} sources carrying it." if top["corroboration"] > 1
                       else "."))
        else:
            lede = f"Nothing in your scope today across {_fmt(led['scanned_documents'])} documents."

    sections: List[dict] = [
        {"component": "lede", "text": lede,
         "citations": [d["doc_id"] for i in items[:3] for d in i["docs"][:1]]},
        {"component": "stats", "stats": [
            {"label": "serious", "value": led["serious"], "tone": "crit"},
            {"label": "watch", "value": led["watch"], "tone": "warn"},
            {"label": "quiet", "value": led["quiet_entities"], "tone": "good"},
            {"label": "documents scanned", "value": led["scanned_documents"]},
            {"label": "matched", "value": led["matched"]},
        ]},
    ]
    if serious:
        sections.append({"component": "event_list", "title": "Serious",
                         "severity": "serious",
                         "items": [i["cluster_key"] for i in serious]})
    if watch:
        sections.append({"component": "event_list", "title": "Watch",
                         "severity": "watch",
                         "items": [i["cluster_key"] for i in watch]})
    if lane == "regulatory" and dossier.get("rule_families_watched"):
        sections.append({"component": "rule_state",
                         "families": dossier["rule_families_watched"],
                         "changed": [i["cluster_key"] for i in items if i["rule_families"]]})
    if not items:
        sections.append({"component": "quiet_note",
                         "text": (f"No items matched your scope on {dossier['day']}. "
                                  f"{_fmt(led['scanned_documents'])} documents were checked.")})
    sections.append({"component": "ledger", "ledger": led,
                     "suppressed": [{"title": s["title"], "reason": "below your noise floor"}
                                    for s in dossier.get("suppressed", [])[:20]]})
    return {"layout": layout, "day": dossier["day"], "lane": lane,
            "persona_id": dossier["persona_id"],
            "persona_name": dossier["persona_name"], "sections": sections,
            "generator": "template"}


# ── validation gates ────────────────────────────────────────────────────────

_NUM = re.compile(r"\d[\d,]*")


def validate_spec(spec: dict, dossier: dict) -> Tuple[bool, List[str]]:
    """Return (ok, problems). A composer may summarise; it may not lose an item,
    cite something that does not exist, or introduce a number."""
    problems: List[str] = []
    if spec.get("layout") not in LAYOUTS:
        problems.append(f"unknown layout {spec.get('layout')!r}")
    if not isinstance(spec.get("sections"), list) or not spec["sections"]:
        problems.append("no sections")
        return False, problems

    rendered = set()
    for s in spec["sections"]:
        for key in s.get("items", []) or []:
            rendered.add(key)
    expected = {i["cluster_key"] for i in dossier["items"]}
    missing = expected - rendered
    # a lede may summarise items, so only *listed* sections must cover them;
    # an item that appears nowhere at all is a silent drop and fails the spec
    if missing and any(s["component"] == "event_list" for s in spec["sections"]):
        problems.append(f"{len(missing)} dossier items rendered nowhere")

    valid_ids = {d["doc_id"] for i in dossier["items"] for d in i["docs"]}
    for s in spec["sections"]:
        for cid in s.get("citations", []) or []:
            if cid not in valid_ids:
                problems.append(f"citation {cid} not in dossier")

    allowed_numbers = {str(v) for v in _dossier_numbers(dossier)}
    for s in spec["sections"]:
        text = s.get("text") or ""
        for token in _NUM.findall(text):
            if token.replace(",", "") not in allowed_numbers:
                problems.append(f"number {token!r} is not in the dossier")
    return (not problems), problems


def _dossier_numbers(dossier: dict) -> set:
    nums = set()
    for v in (dossier.get("ledger") or {}).values():
        if isinstance(v, int):
            nums.add(v)
    for i in dossier["items"]:
        nums.update({i["corroboration"], i["score"], i["materiality"],
                     len(i["entities"]), len(i["rule_families"])})
    nums.update({len(dossier["items"]), len(dossier.get("suppressed", [])),
                 len(dossier.get("rule_families_watched") or [])})
    # years and dates in the day string are legitimate
    for part in re.findall(r"\d+", dossier.get("day", "")):
        nums.add(int(part))
    return {int(n) for n in nums if isinstance(n, int)}


# ── LLM composer (optional) ─────────────────────────────────────────────────

class LLMComposer:
    PROMPT = (
        "You write the opening line of a daily risk briefing for a bank. "
        "You are given a JSON dossier that has ALREADY been selected and scored. "
        "Write ONE paragraph (max 3 sentences) naming the most important item and "
        "why it matters to credit risk. RULES: use only facts and numbers present "
        "in the dossier; never invent a figure; never mention an item not in the "
        "dossier. Return ONLY JSON: {\"lede\": \"...\"}"
    )

    def __init__(self, model: Optional[str] = None, client=None):
        self.model = model or os.getenv("REGAGG_COMPOSE_MODEL", "claude-sonnet-5")
        self._client = client

    def _get_client(self):
        if self._client is None:
            import anthropic
            self._client = anthropic.Anthropic()
        return self._client

    def compose(self, dossier: dict, layout: str) -> dict:
        spec = compose_template(dossier, layout)
        payload = {"day": dossier["day"], "ledger": dossier["ledger"],
                   "items": [{k: i[k] for k in
                              ("title", "event_type", "entities", "corroboration",
                               "severity", "why", "rule_families")}
                             for i in dossier["items"][:12]]}
        try:
            resp = self._get_client().messages.create(
                model=self.model, max_tokens=400, system=self.PROMPT,
                messages=[{"role": "user", "content": json.dumps(payload)}])
            raw = "".join(getattr(b, "text", "") for b in resp.content)
            lede = json.loads(raw[raw.index("{"):raw.rindex("}") + 1]).get("lede")
        except Exception:  # noqa: BLE001
            return spec
        if not lede:
            return spec
        candidate = json.loads(json.dumps(spec))
        candidate["sections"][0]["text"] = lede
        candidate["generator"] = f"llm:{self.model}"
        ok, _problems = validate_spec(candidate, dossier)
        return candidate if ok else spec        # never ship an invalid spec


def get_composer():
    if os.getenv("ANTHROPIC_API_KEY"):
        return LLMComposer()
    return None


# ── the entry point the API and the scheduler both call ─────────────────────

def build_my_day(session, persona: Persona, day: Optional[str] = None,
                 force: bool = False, now: Optional[datetime] = None) -> dict:
    """Build (or reuse) today's page for one persona."""
    from sajha.regagg import personas as _p
    from sajha.regagg.dossier import build_dossier

    now = now or datetime.now(timezone.utc)
    requested_day = day
    day = day or latest_day_with_data(session, persona.lane, now) or now.date().isoformat()

    cached = session.get(PageSpec, {"persona_id": persona.persona_id, "day": day})
    if cached is not None and not force and cached.persona_version == persona.version_n:
        return {"spec": cached.spec, "ledger": cached.ledger,
                "dossier": cached.dossier, "generator": cached.generator,
                "cached": True, "updated_note": cached.updated_note,
                "generated_at": str(cached.created_at or "")}

    dossier = build_dossier(session, persona, day=day, now=now)
    layout = _p.derive_layout(persona.config or {},
                              _p.entity_count(session, persona.persona_id))
    composer = get_composer()
    spec = composer.compose(dossier, layout) if composer else compose_template(dossier, layout)
    ok, problems = validate_spec(spec, dossier)
    if not ok:
        spec = compose_template(dossier, layout)      # deterministic fallback
        spec["fallback_reason"] = problems[:3]

    row = PageSpec(persona_id=persona.persona_id, day=day, lane=persona.lane,
                   spec=spec, dossier=dossier, ledger=dossier["ledger"],
                   generator=spec.get("generator", "template"),
                   persona_version=persona.version_n)
    session.merge(row)
    session.commit()
    return {"spec": spec, "ledger": dossier["ledger"], "dossier": dossier,
            "generator": spec.get("generator", "template"), "cached": False,
            "updated_note": None, "generated_at": str(now),
            "day_note": (None if requested_day or day == now.date().isoformat()
                         else f"Showing {day} — the latest day with collected data.")}


def latest_day_with_data(session, lane: str, now: datetime) -> Optional[str]:
    """The most recent day this lane actually collected anything.

    Opening the app at 06:00 before the run finishes should not show an empty
    page and imply a quiet market — it should show the last real day and say so.
    """
    from sqlalchemy import func, select
    from sajha.regagg.models import Document, Regulator
    ids = [r.regulator_id for r in session.scalars(select(Regulator)).all()
           if getattr(r, "category", "regulatory") == ("news" if lane == "news"
                                                       else "regulatory")]
    if not ids:
        return None
    day_col = func.coalesce(Document.published_date, func.date(Document.ingested_at))
    today = now.date().isoformat()
    row = session.execute(
        select(day_col).where(Document.regulator_id.in_(ids), day_col <= today)
        .order_by(day_col.desc()).limit(1)).first()
    return str(row[0]) if row and row[0] else None


def note_intraday_update(session, persona_id: str, day: str, note: str) -> None:
    """Stamp an update strip without rewriting the morning page."""
    row = session.get(PageSpec, {"persona_id": persona_id, "day": day})
    if row is not None:
        row.updated_note = note
        session.commit()
