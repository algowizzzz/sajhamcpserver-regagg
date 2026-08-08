"""One row per watched entity, whether or not it made the news.

The point of the table is completeness. A persona with 500 names produces 500
rows, and the ones with nothing to report are the reassurance: an analyst who
sees 470 "no news" rows knows the sweep looked. A table that silently omitted
them would be a list of hits pretending to be a review of the book.

So every entity ends the sweep in exactly one state, and the state is recorded:

    ok        news found, snippet and link on the row
    none      searched, nothing published in the window
    error     the search failed for this name — retryable, and visible
    skipped   the sweep hit its budget before reaching this name

Three things keep it affordable and honest:

  cached per persona, day and entity, because each row is a billed search;
  a re-run fills only the gaps, so a retry after a partial failure is cheap
  and opening the page never spends anything;

  a hard budget, checked before each call, with the remainder marked skipped
  rather than the sweep pretending it finished;

  classification is validated against the persona's own declared values, so a
  generated column can be sorted and filtered without wondering what is in it.
"""

from __future__ import annotations

import datetime as _dt
import json
from typing import Callable, Dict, List, Optional, Sequence

from sqlalchemy import select

from sajha.regagg import table_schema as _ts
from sajha.regagg import tavily as _tv
from sajha.regagg.models import EntityScan, PersonaEntity

BATCH = 20               # rows per classification call
DEFAULT_BUDGET = 600     # searches per sweep, before anyone has to think about it

CLASSIFY_SYSTEM = """You label financial-news snippets for a credit risk desk.

You are given rows, each with a company name and ONE news snippet. For each row
return the requested fields, judged only from that row's snippet.

Rules, without exception:
1. Judge only from the snippet given. Never use outside knowledge of the company.
2. If the snippet does not support a value, return "unknown". A guess in a
   column an analyst filters on is worse than an admission.
3. Return one object per row id you were given, and no others.
Return ONLY JSON: {"rows": [{"id": "...", "<field>": "<value>", ...}]}"""


def entities_for(session, persona_id: str) -> List[str]:
    return [c for (c,) in session.execute(
        select(PersonaEntity.canonical)
        .where(PersonaEntity.persona_id == persona_id)
        .order_by(PersonaEntity.canonical)).all()]


def columns_for(persona) -> tuple[List[_ts.Column], List[str]]:
    cfg = (persona.config or {}) if persona is not None else {}
    spec = (cfg.get("table") or {}).get("columns") if isinstance(cfg.get("table"), dict) \
        else cfg.get("table_columns")
    return _ts.parse(spec)


def _existing(session, persona_id: str, day: str) -> Dict[str, EntityScan]:
    rows = session.scalars(select(EntityScan).where(
        EntityScan.persona_id == persona_id, EntityScan.day == day)).all()
    return {r.entity: r for r in rows}


# ── the sweep ───────────────────────────────────────────────────────────────

def sweep(session, persona, *, day: Optional[str] = None, budget: int = DEFAULT_BUDGET,
          depth: str = "basic", days: int = 7, client=None,
          progress: Optional[Callable[[int, int], None]] = None,
          refresh: bool = False) -> dict:
    """Search each entity that has no cached row for the day.

    Returns what it did, including what it did not do — a sweep that stopped at
    its budget says so, with the names it never reached.
    """
    day = day or _dt.date.today().isoformat()
    names = entities_for(session, persona.persona_id)
    if not names:
        return {"day": day, "entities": 0, "searched": 0, "credits": 0,
                "skipped": 0, "errors": 0, "configured": _tv.configured(),
                "detail": "this persona has no entities"}

    if client is None:
        client = _tv.client_for(day, depth=depth, days=days)
    mode = "demo" if isinstance(client, _tv.DemoNews) else "live"

    have = _existing(session, persona.persona_id, day)
    todo = names if refresh else [n for n in names
                                  if n not in have or have[n].status == "error"]
    searched = errors = skipped = 0

    for i, name in enumerate(todo):
        if searched >= budget:
            skipped = len(todo) - i
            for rest in todo[i:]:
                session.merge(EntityScan(
                    persona_id=persona.persona_id, day=day, entity=rest,
                    status="skipped", mode=mode, hits=[], columns={},
                    classified=False,
                    detail=f"sweep budget of {budget} searches was reached first"))
            break
        try:
            hits = client.search(name)
            searched += 1
            row = EntityScan(
                persona_id=persona.persona_id, day=day, entity=name,
                status="ok" if hits else "none", mode=mode,
                hits=[h.as_dict() for h in hits], columns={}, classified=False,
                detail="" if hits else "no financial news in the window")
        except _tv.NotConfigured as e:
            return {"day": day, "entities": len(names), "searched": searched,
                    "credits": getattr(client, "credits", searched),
                    "skipped": len(todo) - i, "errors": errors,
                    "configured": False, "detail": str(e)}
        except Exception as e:  # noqa: BLE001 — one bad name must not end the sweep
            errors += 1
            searched += 1
            row = EntityScan(persona_id=persona.persona_id, day=day, entity=name,
                             status="error", mode=mode, hits=[], columns={},
                             classified=False, detail=str(e)[:200])
        session.merge(row)
        if progress and (i % 10 == 0 or i == len(todo) - 1):
            progress(i + 1, len(todo))
    session.commit()

    return {"day": day, "entities": len(names), "searched": searched,
            "credits": getattr(client, "credits", searched),
            "skipped": skipped, "errors": errors,
            "configured": _tv.configured(), "mode": mode,
            "cached": len(names) - len(todo),
            "detail": (f"stopped at the {budget}-search budget; {skipped} name(s) "
                       f"were not reached" if skipped else "")}


# ── classification ──────────────────────────────────────────────────────────

def classify(session, persona, *, day: Optional[str] = None, client=None,
             batch: int = BATCH) -> dict:
    """Fill the persona's declared columns for rows that have news.

    Rows with no news are not sent to the model: there is nothing to judge, and
    paying to be told "unknown" would be an odd way to spend a token budget.
    """
    day = day or _dt.date.today().isoformat()
    cols, problems = columns_for(persona)
    if not cols:
        return {"columns": 0, "classified": 0, "problems": problems,
                "detail": "no columns declared on this persona"}

    rows = [r for r in session.scalars(select(EntityScan).where(
        EntityScan.persona_id == persona.persona_id, EntityScan.day == day,
        EntityScan.status == "ok")).all() if not r.classified]
    if not rows:
        return {"columns": len(cols), "classified": 0, "problems": problems,
                "detail": "nothing new to classify"}

    if client is None:
        try:
            from sajha.regagg.extraction import _provider_from_env
            _p, client = _provider_from_env()
        except Exception:  # noqa: BLE001
            client = None
        if client is None:
            return {"columns": len(cols), "classified": 0, "problems": problems,
                    "detail": "no model configured — the news columns are filled, "
                              "the judged columns are not"}

    done = 0
    field_spec = _ts.prompt_fragment(cols)
    for start in range(0, len(rows), batch):
        chunk = rows[start:start + batch]
        payload = [{"id": r.entity, "company": r.entity,
                    "snippet": (r.hits[0].get("title", "") + " — " +
                                r.hits[0].get("snippet", ""))[:600]}
                   for r in chunk if r.hits]
        if not payload:
            continue
        user = (f"FIELDS:\n{field_spec}\n\nROWS:\n" +
                json.dumps(payload, ensure_ascii=False))
        try:
            raw = client.complete(CLASSIFY_SYSTEM, user, max_tokens=1600)
            data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
            by_id = {str(o.get("id")): o for o in (data.get("rows") or [])
                     if isinstance(o, dict)}
        except Exception:  # noqa: BLE001 — a failed batch stays unclassified
            continue
        for r in chunk:
            got = by_id.get(r.entity)
            if got is None:
                continue                      # left unclassified, not guessed
            r.columns = _ts.coerce_row(cols, got)
            r.classified = True
            done += 1
    session.commit()
    return {"columns": len(cols), "classified": done, "problems": problems,
            "detail": ""}


# ── reading it back ─────────────────────────────────────────────────────────

def table(session, persona, *, day: Optional[str] = None,
          status: Optional[str] = None, q: str = "") -> dict:
    """Every entity, one row, cached news and columns attached."""
    day = day or _dt.date.today().isoformat()
    cols, problems = columns_for(persona)
    names = entities_for(session, persona.persona_id)
    have = _existing(session, persona.persona_id, day)

    rows = []
    for name in names:
        r = have.get(name)
        top = (r.hits[0] if (r and r.hits) else {}) or {}
        rows.append({
            "entity": name,
            "status": r.status if r else "pending",
            "mode": (r.mode if r else "") or "",
            "detail": (r.detail if r else "not searched yet") or "",
            "title": top.get("title", ""),
            "snippet": top.get("snippet", "")[:400],
            "url": top.get("url", ""),
            "source": top.get("source", ""),
            "published": top.get("published", ""),
            "more": max(0, len(r.hits) - 1) if r and r.hits else 0,
            "columns": (r.columns or {}) if r else {},
        })

    if status:
        rows = [x for x in rows if x["status"] == status]
    if q:
        low = q.lower()
        rows = [x for x in rows
                if low in x["entity"].lower() or low in x["title"].lower()]

    counts: Dict[str, int] = {}
    for x in rows:
        counts[x["status"]] = counts.get(x["status"], 0) + 1
    # If any stored row came from the stand-in, the whole table is suspect and
    # must say so — a mixed table is the worst case, because a reader who spots
    # one real row assumes the rest are too.
    # Only rows that were actually searched carry a mode. Placeholder rows for
    # names nobody has swept yet must not make the table claim to be live.
    demo_rows = sum(1 for x in rows if x["mode"] == "demo")
    searched_modes = {x["mode"] for x in rows if x["mode"]}
    return {"day": day, "columns": _ts.to_dicts(cols), "schema_problems": problems,
            "rows": rows, "total": len(names), "showing": len(rows),
            "counts": counts, "configured": _tv.configured(),
            "mode": ("demo" if demo_rows else
                     "live" if searched_modes else ""),
            "demo_rows": demo_rows,
            "estimate": _tv.estimate(len(names))}


SUMMARY_SYSTEM = (
    "You brief a credit risk analyst on a table of their own obligors.\n"
    "Write at most three sentences saying which rows deserve attention first "
    "and why. Rules: name only companies present in the rows; never state a "
    "figure that is not in a snippet; if nothing stands out, say the book looks "
    "quiet and say how many names were checked.\n"
    'Return ONLY JSON: {"summary": "..."}'
)


def summarise(rows: List[dict], *, total: int, client=None) -> dict:
    """The 'what should I look at' line, validated before it is shown."""
    live = [r for r in rows if r["status"] == "ok"][:40]
    if not live:
        return {"summary": f"No news for any of the {total} names checked.",
                "generated": False}
    if client is None:
        try:
            from sajha.regagg.extraction import _provider_from_env
            _p, client = _provider_from_env()
        except Exception:  # noqa: BLE001
            client = None
        if client is None:
            return {"summary": f"{len(live)} of {total} names have news today.",
                    "generated": False,
                    "reason": "no model configured"}
    body = "\n".join(f'- {r["entity"]}: {r["title"]} — {r["snippet"][:180]}'
                     for r in live)
    try:
        raw = client.complete(SUMMARY_SYSTEM,
                              f"{len(live)} of {total} names have news.\n\n{body}",
                              max_tokens=350)
        text = str(json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
                   .get("summary", "")).strip()
    except Exception as e:  # noqa: BLE001
        return {"summary": f"{len(live)} of {total} names have news today.",
                "generated": False, "reason": f"assistant unavailable ({str(e)[:60]})"}

    names = {r["entity"].lower() for r in live}
    import re as _re
    allowed = {t.replace(",", "").rstrip(".")
               for t in _re.findall(r"\d[\d,.]*", json.dumps(live) + f" {total}")}
    for tok in _re.findall(r"\d[\d,.]*", text):
        c = tok.replace(",", "").rstrip(".")
        if c.isdigit() and len(c) > 1 and c not in allowed:
            return {"summary": f"{len(live)} of {total} names have news today.",
                    "generated": False,
                    "reason": f"summary withheld: figure {tok!r} is not in the rows"}
    return {"summary": text or f"{len(live)} of {total} names have news today.",
            "generated": bool(text)}
