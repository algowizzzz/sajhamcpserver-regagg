"""The Health page: can I trust what is in here.

Collection answers "did it run". This answers the harder question, which is
whether a green run actually left good data behind. The two failures that
matter most are invisible to a pass rate:

    a source that succeeds and returns nothing, quietly ageing out
    a document that lands without the fields the rest of the product needs

The second one is the larger problem in practice. Three quarters of the corpus
has no publication date, which is why "what changed at OSFI in the last month"
cannot be answered from it — every collection run that produced those documents
reported success.

On conservation: the run counters are NOT a partition, and this module does not
pretend otherwise. Measured over the corpus, ``fetched <= detected`` and
``errors <= detected`` hold, but ``ingested + archived`` can exceed ``fetched``
and ``detected != fetched + errors``. Both of those are legitimate — they are
event counters, and one document can be created and have a version archived in
the same run. So the funnel is shown as measured, and the only thing flagged as
a defect is the one genuine impossibility: fetching more than was detected.
"""

from __future__ import annotations

import datetime as _dt
from typing import Dict, List, Optional

from sqlalchemy import func, select

from sajha.regagg import collection as _col
from sajha.regagg import schedule as _sched
from sajha.regagg.models import Document, DocumentVersion, Regulator, Run

# The short codes region_of understands. Anything else is not wrong today —
# news sources are regioned by category before jurisdiction is consulted — but
# it is vocabulary drift in a column that other views do read.
KNOWN_JURISDICTIONS = {"CA", "US", "EU", "UK", "SG", "HK", "AU", "JP", "IN", "INTL"}


def _utc(now: Optional[_dt.datetime] = None) -> _dt.datetime:
    now = now or _dt.datetime.now(_dt.timezone.utc)
    return now if now.tzinfo else now.replace(tzinfo=_dt.timezone.utc)


# ── freshness ───────────────────────────────────────────────────────────────

def freshness(session, *, now: Optional[_dt.datetime] = None) -> dict:
    """Each category against its own window, because they are not comparable.

    A newswire silent for three days is broken; a regulator silent for three
    days is Tuesday. Judging both by one number would either cry wolf about the
    regulators or say nothing about the wires.
    """
    now = _utc(now)
    cand = _col.candidates(session, now=now)["sources"]
    out = []
    for key, label in _col.CATEGORIES:
        mine = [r for r in cand if r["category"] == key]
        if not mine:
            continue
        window = max((r["window_days"] for r in mine), default=14)
        fresh = [r for r in mine if r["bucket"] == "ok"]
        aging = [r for r in mine if r["bucket"] == "silent"]
        past = [r for r in mine if r["bucket"] in ("stale", "failed", "never")]
        out.append({"key": key, "label": label, "window_days": window,
                    "total": len(mine), "fresh": len(fresh),
                    "aging": len(aging), "past": len(past),
                    "past_ids": [r["regulator_id"] for r in past]})
    return {"categories": out}


# ── the collection funnel (as measured, not as wished) ──────────────────────

def funnel(session, *, day: Optional[_dt.date] = None,
           now: Optional[_dt.datetime] = None) -> dict:
    """Where documents went on the last day that ran, plus counter integrity."""
    now = _utc(now)
    ids = [s.regulator_id for s in _col._sources(session)]
    if day is None:
        day = _dt.date.fromisoformat(_col.arrived(session, now=now)["date"]) \
            if _col.arrived(session, now=now)["date"] else \
            _sched.get_schedule().local_now(now).date()

    runs = [r for r in _col._runs_since(session, day, ids) if r.logical_date == day]
    det = sum(r.detected or 0 for r in runs)
    fet = sum(r.fetched or 0 for r in runs)
    ing = sum(r.ingested or 0 for r in runs)
    arc = sum(r.archived or 0 for r in runs)
    err = sum(r.errors or 0 for r in runs)

    # The only genuine contradiction: you cannot fetch more than you detected.
    #
    # An earlier version flagged `ingested + archived > fetched` as inconsistent.
    # It is not. Both are EVENT counters and one document can produce both in a
    # single run — created, then a version archived when it is seen again. All
    # six runs that tripped the old check were legitimate, so the check was
    # manufacturing a defect and sending someone to reconcile clean data.
    inconsistent = [{"regulator_id": r.regulator_id, "date": r.logical_date.isoformat(),
                     "detected": r.detected, "fetched": r.fetched,
                     "why": "fetched exceeds detected"}
                    for r in _col._runs_since(session, day - _dt.timedelta(days=90), ids)
                    if (r.fetched or 0) > (r.detected or 0)]

    return {"date": day.isoformat(), "runs": len(runs),
            "detected": det, "fetched": fet, "ingested": ing,
            "archived": arc, "errors": err,
            "not_fetched": max(0, det - fet),
            "unchanged": max(0, fet - ing - arc),
            "holds": {"fetched_le_detected": fet <= det,
                      "errors_le_detected": err <= det},
            "inconsistent_runs": inconsistent[:10],
            "inconsistent_count": len(inconsistent),
            "note": "event counters, not a partition — errors can overlap "
                    "fetched, and one document can be both ingested and "
                    "archived in a single run, so the parts may exceed the whole"}


# ── data quality: defects in what we already hold ───────────────────────────

def quality(session) -> dict:
    """Checks against the corpus itself. Each one names what it breaks.

    A count with no consequence attached gets ignored, so every row says which
    capability stops working — that is what makes it worth someone's afternoon.
    """
    total = session.scalar(select(func.count()).select_from(Document)) or 0
    checks: List[dict] = []

    def add(key, count, severity, headline, breaks, action=None, of=None):
        """`of` names the population — a run-level check divided by the document
        count reads as 1.6% when it is really 87%."""
        denom = total if of is None else of
        checks.append({"key": key, "count": int(count), "severity": severity,
                       "headline": headline, "breaks": breaks, "action": action,
                       "of": denom,
                       "pct": round(100 * count / denom, 1) if denom else 0.0})

    no_pub = session.scalar(select(func.count()).select_from(Document)
                            .where(Document.published_date.is_(None))) or 0
    by_cat = {c: n for c, n in session.execute(
        select(Regulator.category, func.count())
        .select_from(Document).join(Regulator, Regulator.regulator_id == Document.regulator_id)
        .where(Document.published_date.is_(None))
        .group_by(Regulator.category)).all()}
    add("no_published_date", no_pub, "high",
        "documents with no publication date",
        "any question of the form 'what changed in the last N days' silently "
        "misses these — the assistant hits this constantly",
        "backfill from the document body or the source page")
    checks[-1]["by_category"] = by_cat

    no_extract = session.scalar(select(func.count()).select_from(Document)
                                .where(Document.extraction.is_(None))) or 0
    add("no_extraction", no_extract, "high",
        "documents with no extraction",
        "no entities, no event type — invisible to entity lookup and to every "
        "persona whose watchlist depends on it",
        "run the extraction backfill")

    no_band = session.scalar(select(func.count()).select_from(Document)
                             .where(Document.materiality_score == 0)) or 0
    add("no_materiality", no_band, "medium",
        "documents with no materiality score",
        "rank last in every prioritised view, so they are effectively unread",
        "rescore")

    orphan = session.scalar(
        select(func.count()).select_from(DocumentVersion)
        .where(~select(Document.doc_id).where(
            Document.regulator_id == DocumentVersion.regulator_id,
            Document.doc_id == DocumentVersion.doc_id).exists())) or 0
    add("orphan_versions", orphan, "high", "archived versions with no document",
        "the audit trail points at something that no longer exists")

    untitled = session.scalar(select(func.count()).select_from(Document)
                              .where((Document.title.is_(None)) |
                                     (Document.title == ""))) or 0
    add("untitled", untitled, "medium", "documents with no title",
        "unreadable in every list and unsearchable by name")

    bad_ts = session.scalar(
        select(func.count()).select_from(Run).where(
            Run.started_at.isnot(None), Run.finished_at.isnot(None),
            Run.finished_at < Run.started_at)) or 0
    total_runs = session.scalar(select(func.count()).select_from(Run)) or 0
    add("run_timestamps_inverted", bad_ts, "medium",
        "runs whose finish time precedes their start",
        "run duration cannot be computed, so a collection that is slowing down "
        "gives no warning before it starts timing out",
        "stamp finished_at per source when that source completes",
        of=total_runs)

    odd = [{"jurisdiction": j, "count": n} for j, n in session.execute(
        select(Regulator.jurisdiction, func.count())
        .where(Regulator.jurisdiction.notin_(KNOWN_JURISDICTIONS))
        .group_by(Regulator.jurisdiction)).all()]
    n_sources = session.scalar(select(func.count()).select_from(Regulator)) or 0
    add("jurisdiction_vocabulary", sum(o["count"] for o in odd), "low",
        "sources whose jurisdiction is spelled out rather than coded",
        "harmless today because news sources are grouped by category before "
        "jurisdiction is read — but the column is the input to region rollups, "
        "so it is one refactor away from mattering", of=n_sources)
    checks[-1]["values"] = odd

    # ── exposure ────────────────────────────────────────────────────────────
    # Not a data defect, but it belongs on the page a platform team reads. The
    # KB claimed this server was localhost-only; it is not — the default bind
    # is 0.0.0.0, and the shipped admin account is still present.
    import os as _os
    try:
        from sajha.core.config import get_settings as _gs
        bind = getattr(_gs(), "server_host", "0.0.0.0")
    except Exception:  # noqa: BLE001
        bind = _os.getenv("SAJHA_SERVER_HOST", "0.0.0.0")
    exposed = bind not in ("127.0.0.1", "localhost", "::1")
    try:
        from sajha.db.models import User as _U
        stock = session.scalar(select(func.count()).select_from(_U)
                               .where(_U.username == "admin")) or 0
    except Exception:  # noqa: BLE001
        stock = 0
    add("network_exposure", 1 if (exposed and stock) else 0, "high",
        f"reachable on {bind} with the shipped admin account present",
        "anyone who can route to this host can attempt the default credentials; "
        "the corpus and the run controls are behind that login",
        "bind to 127.0.0.1, or change the admin password and put TLS in front",
        of=1)
    checks[-1]["bind"] = bind
    checks[-1]["stock_admin"] = bool(stock)

    checks.sort(key=lambda c: ({"high": 0, "medium": 1, "low": 2}[c["severity"]],
                               -c["count"]))
    return {"documents": total, "checks": checks,
            "clean": [c["key"] for c in checks if not c["count"]],
            "open": [c["key"] for c in checks if c["count"]]}


# ── schedule reliability ────────────────────────────────────────────────────

def reliability(session, *, days: int = 30,
                now: Optional[_dt.datetime] = None) -> dict:
    """Did the scheduler fire when it said it would, over the last month."""
    sched = _sched.get_schedule()
    now = _utc(now)
    today = sched.local_now(now).date()
    start = today - _dt.timedelta(days=days - 1)
    ids = [s.regulator_id for s in _col._sources(session)]

    # Nothing can be late before the system was collecting at all. Without this
    # floor the window reaches back past the first run and reports every day of
    # prehistory as missed, which buries the one or two that are real.
    first = session.scalar(select(func.min(Run.logical_date)))
    if first and first > start:
        start = first

    runs = _col._runs_since(session, start, ids)
    idx = _col._day_index(runs)
    expected = sched.expected_days(start, today)

    # Per category, never pooled. Pooling lets a category that ran mask one that
    # did not: the news wires collected every weekday while regulatory sat dark
    # for three of them, and the combined figure reported zero missed runs —
    # contradicting the coverage matrix on the same screen.
    per_cat, missed_all = [], set()
    for key, label in _col.CATEGORIES:
        cat_ids = {s.regulator_id for s in _col._sources(session, key)}
        cidx = _col._day_index([r for r in runs if r.regulator_id in cat_ids])
        cat_missed, cat_fired = [], 0
        for day in expected:
            got = cidx.get(day, {})
            st = sched.state_for(day, ran=len(got.get("ran", ())),
                                 failed=len(got.get("failed", ())),
                                 empty=len(got.get("empty", ())),
                                 running=len(got.get("running", ())),
                                 active_sources=len(cat_ids), now=now)
            if st["state"] == _sched.MISSED:
                cat_missed.append(day.isoformat())
            elif st["state"] in (_sched.COMPLETE, _sched.PARTIAL, _sched.RUNNING):
                cat_fired += 1
        missed_all.update(cat_missed)
        per_cat.append({"key": key, "label": label, "sources": len(cat_ids),
                        "expected_days": len(expected), "fired": cat_fired,
                        "missed": cat_missed, "missed_count": len(cat_missed)})

    missed = sorted(missed_all)
    fired = sum(c["fired"] for c in per_cat)

    per_day = []
    for day in sorted(idx):
        mine = [r for r in runs if r.logical_date == day]
        ok = sum(1 for r in mine if not _col._is_failed(r))
        per_day.append({"date": day.isoformat(), "runs": len(mine),
                        "pass_rate": round(100 * ok / len(mine), 1) if mine else 100.0})

    attempts = sum(1 for r in runs)
    clean = sum(1 for r in runs if not _col._is_failed(r))
    return {"window_days": days, "since": start.isoformat(),
            "expected_days": len(expected), "fired": fired,
            "missed": missed, "missed_count": len(missed),
            "by_category": per_cat,
            "pass_rate": round(100 * clean / attempts, 1) if attempts else 100.0,
            "runs": attempts, "per_day": per_day,
            "declared": sched.describe(now)}


# ── the verdict ─────────────────────────────────────────────────────────────

def verdict(fresh: dict, qual: dict, rel: dict, fnl: dict) -> dict:
    """One sentence, in the order a person would triage.

    Deliberately blunt: "degraded" with a reason beats a green tick that hides
    four stale sources, and a page that is always green stops being read.
    """
    past = sum(c["past"] for c in fresh["categories"])
    aging = sum(c["aging"] for c in fresh["categories"])
    high = [c for c in qual["checks"] if c["severity"] == "high" and c["count"]]
    bits = []
    if past:
        bits.append(f"{past} source(s) past their window")
    if aging:
        bits.append(f"{aging} succeeding but returning nothing")
    if rel["missed_count"]:
        bits.append(f"{rel['missed_count']} missed scheduled run(s)")
    if fnl["inconsistent_count"]:
        bits.append(f"{fnl['inconsistent_count']} run(s) with contradictory counters")
    for c in high:
        bits.append(f"{c['count']:,} {c['headline']}")

    if past or rel["missed_count"]:
        level, head = "degraded", "Degraded — collection is not keeping up"
    elif high:
        level, head = "degraded", "Collecting cleanly, but the corpus has gaps"
    elif aging or fnl["inconsistent_count"]:
        level, head = "watch", "Healthy, with things worth watching"
    else:
        level, head = "healthy", "Healthy — collection current, corpus complete"

    return {"level": level, "headline": head, "points": bits,
            "actionable": past + aging + rel["missed_count"]}


def overview(session, *, now: Optional[_dt.datetime] = None) -> dict:
    """One call for the page, one clock, so no two panels disagree."""
    now = _utc(now)
    fresh = freshness(session, now=now)
    qual = quality(session)
    rel = reliability(session, now=now)
    fnl = funnel(session, now=now)
    cand = _col.candidates(session, now=now)
    attention = [r for r in cand["sources"] if r["bucket"] != "ok"]
    return {"verdict": verdict(fresh, qual, rel, fnl),
            "freshness": fresh, "funnel": fnl, "quality": qual,
            "reliability": rel,
            "attention": attention, "attention_count": len(attention),
            "counts": cand["counts"]}
