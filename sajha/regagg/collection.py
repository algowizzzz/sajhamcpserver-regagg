"""The Collection page: did it run, and can I make it run.

Written for the person who is accountable for the data being current. That
person asks four questions in order, and the payload answers them in that
order:

    is today done?          the today bar — and, when it isn't, whether that
                            is a weekend or a dead scheduler
    is the week clean?      the coverage matrix, one cell per category per day
    is the shape normal?    trend lines, so a collapse in volume shows up even
                            when every run "succeeded"
    what do I rerun?        candidates already sorted into failed / stale /
                            silent / never-run, ready to multi-select

A note on the counters, because it constrains what this module may claim:
``detected``, ``fetched``, ``ingested``, ``archived`` and ``errors`` are
independent counters, not a partition. Measured across the real corpus,
``fetched <= detected`` always holds, but ``ingested + archived`` can exceed
``fetched`` (a document can be created and have a version archived in the same
run) and ``detected != fetched + errors``. So nothing here presents an identity
that balances; it presents a funnel, and the inconsistent runs are reported as
a defect rather than hidden by arithmetic.
"""

from __future__ import annotations

import datetime as _dt
from collections import defaultdict
from typing import Dict, List, Optional, Sequence

from sqlalchemy import func, select

from sajha.regagg import schedule as _sched
from sajha.regagg.models import Document, Regulator, Run

CATEGORIES = [("regulatory", "Regulatory"), ("news", "News wires")]


def _utc(now: Optional[_dt.datetime] = None) -> _dt.datetime:
    now = now or _dt.datetime.now(_dt.timezone.utc)
    return now if now.tzinfo else now.replace(tzinfo=_dt.timezone.utc)


def _sources(session, lane: Optional[str] = None) -> List[Regulator]:
    q = select(Regulator).where(Regulator.active.is_(True))
    if lane:
        q = q.where(Regulator.category == lane)
    return list(session.scalars(q).all())


def _runs_since(session, start: _dt.date, ids: Sequence[str]) -> List[Run]:
    if not ids:
        return []
    return list(session.scalars(
        select(Run).where(Run.logical_date >= start, Run.regulator_id.in_(ids))).all())


def _is_empty(r: Run) -> bool:
    """Succeeded but brought nothing back — the failure that looks like health."""
    return (r.status or "").startswith("success") and not (r.ingested or 0) \
        and not (r.archived or 0)


def _is_failed(r: Run) -> bool:
    return (r.status or "") == "failed" or (r.errors or 0) > 0


def _duration_s(runs: Sequence[Run]) -> Optional[int]:
    """Wall-clock for a batch, or None when the timestamps cannot support it.

    Most rows on record have ``finished_at`` earlier than ``started_at`` — the
    poller stamps one finish time for the whole batch before the per-source
    starts. Rather than print a negative or a zero that looks like speed, this
    returns None and the UI omits the figure. A missing number is honest; a
    wrong one gets quoted in a status report.
    """
    pairs = [(r.started_at, r.finished_at) for r in runs
             if r.started_at and r.finished_at]
    if not pairs:
        return None
    started, finished = min(p[0] for p in pairs), max(p[1] for p in pairs)
    return int((finished - started).total_seconds()) if finished > started else None


# ── the day grid ────────────────────────────────────────────────────────────

def _day_index(runs: Sequence[Run]) -> Dict[_dt.date, Dict[str, set]]:
    """date -> {ran, failed, empty, running} as sets of source ids.

    Sets, not counts: a source that runs twice in a day must not count twice,
    and a source that fails then succeeds on rerun should not stay red.
    """
    idx: Dict[_dt.date, Dict[str, set]] = defaultdict(
        lambda: {"ran": set(), "failed": set(), "empty": set(),
                 "running": set(), "clean": set()})
    for r in runs:
        d = idx[r.logical_date]
        d["ran"].add(r.regulator_id)
        if (r.status or "") == "running":
            d["running"].add(r.regulator_id)
        elif _is_failed(r):
            d["failed"].add(r.regulator_id)
        elif _is_empty(r):
            d["empty"].add(r.regulator_id)
        else:
            d["clean"].add(r.regulator_id)
    # A rerun that worked settles the day for that source. Membership has to be
    # tracked, not inferred by subtraction: a source that failed and then
    # succeeded appears in both `ran` and `failed`, so deriving "clean" as
    # ran-minus-failed yields the empty set and the cell stays red after the
    # person has already fixed it.
    for d in idx.values():
        d["failed"] -= d["clean"]
        d["empty"] -= d["clean"]
    return idx


def coverage_matrix(session, *, days: int = 7, lane: Optional[str] = None,
                    now: Optional[_dt.datetime] = None) -> dict:
    """One row per category, one cell per day, each cell knowing why it looks
    the way it does. A gap the schedule never promised is rendered as expected,
    which is the whole reason the schedule is declared."""
    sched = _sched.get_schedule()
    now = _utc(now)
    today = sched.local_now(now).date()
    day_list = [today - _dt.timedelta(days=i) for i in range(days)]
    start = day_list[-1]

    rows = []
    for key, label in CATEGORIES:
        if lane and key != lane:
            continue
        srcs = _sources(session, key)
        ids = [s.regulator_id for s in srcs]
        idx = _day_index(_runs_since(session, start, ids))
        cells = []
        for day in day_list:
            d = idx.get(day, {"ran": set(), "failed": set(), "empty": set(),
                              "running": set()})
            st = sched.state_for(
                day, ran=len(d["ran"]), failed=len(d["failed"]),
                empty=len(d["empty"]), running=len(d["running"]),
                active_sources=len(ids), now=now)
            st["date"] = day.isoformat()
            st["total"] = len(ids)
            st["missing"] = sorted(set(ids) - d["ran"]) if st["expected"] else []
            cells.append(st)
        rows.append({"key": key, "label": label, "total": len(ids), "cells": cells})

    return {"days": [{"date": d.isoformat(), "weekday": d.strftime("%a"),
                      "day": d.day, "is_today": d == today,
                      "expected": sched.is_expected(d)} for d in day_list],
            "rows": rows}


# ── the today bar ───────────────────────────────────────────────────────────

def today_bar(session, *, lane: Optional[str] = None,
              now: Optional[_dt.datetime] = None) -> dict:
    """Everything the top strip needs, including why today looks like it does."""
    sched = _sched.get_schedule()
    now = _utc(now)
    today = sched.local_now(now).date()
    srcs = _sources(session, lane)
    ids = [s.regulator_id for s in srcs]

    idx = _day_index(_runs_since(session, today, ids))
    d = idx.get(today, {"ran": set(), "failed": set(), "empty": set(),
                        "running": set()})
    state = sched.state_for(today, ran=len(d["ran"]), failed=len(d["failed"]),
                            empty=len(d["empty"]), running=len(d["running"]),
                            active_sources=len(ids), now=now)
    state["date"] = today.isoformat()
    state["weekday"] = today.strftime("%A")
    state["date_long"] = today.strftime("%A %-d %B %Y") if hasattr(today, "strftime") \
        else today.isoformat()
    state["total"] = len(ids)

    # The last day anything ran — deliberately not called "last complete".
    # Regulatory and news are collected on different cadences, so on a typical
    # day only one of them reports; a bar claiming "complete" over 25 of 55
    # sources would hide exactly the outage this page exists to show.
    last = None
    lookback = _runs_since(session, today - _dt.timedelta(days=30), ids)
    by_day = _day_index(lookback)
    for day in sorted(by_day, reverse=True):
        got = by_day[day]
        if not got["ran"] or got["running"]:
            continue
        same = [r for r in lookback if r.logical_date == day]
        last = {"date": day.isoformat(),
                "sources": len(got["ran"]), "total": len(ids),
                "failed": len(got["failed"]), "empty": len(got["empty"]),
                "finished_at": max((r.finished_at for r in same if r.finished_at),
                                   default=None),
                "duration_s": _duration_s(same)}
        if last["finished_at"] is not None:
            last["finished_at"] = last["finished_at"].isoformat()
        break

    # which category last reported, since "nothing ran today" is usually only
    # true of one of them
    per_cat = []
    for key, label in CATEGORIES:
        cat_ids = {s.regulator_id for s in srcs if s.category == key}
        if not cat_ids:
            continue    # a lane holds one category; "News wires never" inside
                        # the regulatory lane is noise, not a warning
        days_seen = [r.logical_date for r in lookback if r.regulator_id in cat_ids]
        per_cat.append({"key": key, "label": label, "total": len(cat_ids),
                        "last_run": max(days_seen).isoformat() if days_seen else None,
                        "days_ago": (today - max(days_seen)).days if days_seen else None})

    live = [{"regulator_id": r.regulator_id, "status": r.status,
             "detected": r.detected or 0, "fetched": r.fetched or 0,
             "ingested": r.ingested or 0,
             "started_at": r.started_at.isoformat() if r.started_at else None}
            for r in lookback if (r.status or "") == "running"]

    return {"today": state, "schedule": sched.describe(now),
            "last_activity": last, "by_category": per_cat, "live": live}


# ── trends ──────────────────────────────────────────────────────────────────

def trend(session, *, days: int = 30, lane: Optional[str] = None,
          now: Optional[_dt.datetime] = None) -> dict:
    """Volume over time. A source that silently stops returning documents keeps
    reporting success, so the only way to see it is the shape of the line."""
    now = _utc(now)
    today = _sched.get_schedule().local_now(now).date()
    start = today - _dt.timedelta(days=days - 1)
    ids = [s.regulator_id for s in _sources(session, lane)]
    if not ids:
        return {"days": [], "series": {}, "today": {}, "avg7": {}}

    agg = {d: dict(detected=0, fetched=0, ingested=0, archived=0, errors=0, runs=0)
           for d in (start + _dt.timedelta(days=i) for i in range(days))}
    for day, n, det, fet, ing, arc, err in session.execute(
            select(Run.logical_date, func.count(), func.sum(Run.detected),
                   func.sum(Run.fetched), func.sum(Run.ingested),
                   func.sum(Run.archived), func.sum(Run.errors))
            .where(Run.logical_date >= start, Run.regulator_id.in_(ids))
            .group_by(Run.logical_date)).all():
        if day in agg:
            agg[day] = dict(runs=n, detected=int(det or 0), fetched=int(fet or 0),
                            ingested=int(ing or 0), archived=int(arc or 0),
                            errors=int(err or 0))

    ordered = sorted(agg)
    metrics = ("detected", "fetched", "ingested", "errors")
    series = {m: [agg[d][m] for d in ordered] for m in metrics}

    # Headline the last day that actually ran, not the calendar day. On a
    # Saturday "today" is legitimately zero, and reporting -100% against the
    # weekly average turns a quiet weekend into four red panels.
    active = [d for d in ordered if agg[d]["runs"]]
    latest = active[-1] if active else (ordered[-1] if ordered else None)

    def avg_before(m: str) -> Optional[float]:
        """Mean over the seven active days before `latest` — days with no run
        are excluded, or the baseline just measures how many weekends fell in
        the window."""
        prior = [agg[d][m] for d in active if d < latest][-7:] if latest else []
        return round(sum(prior) / len(prior), 1) if prior else None

    return {"days": [d.isoformat() for d in ordered],
            "series": series,
            "latest_date": latest.isoformat() if latest else None,
            "is_today": latest == today if latest else False,
            "latest": {m: agg[latest][m] for m in metrics} if latest else {},
            "avg7": {m: avg_before(m) for m in metrics}}


# ── what actually arrived ───────────────────────────────────────────────────

def arrived(session, *, day: Optional[_dt.date] = None, lane: Optional[str] = None,
            top: int = 8, now: Optional[_dt.datetime] = None) -> dict:
    """What landed, per source, against that source's own recent normal.

    Absolute counts are close to meaningless here — 8 documents is a big day for
    a regulator and a dead one for a newswire. The comparison is what carries
    the signal, so every row is shown against its own 7-day average.
    """
    now = _utc(now)
    sched = _sched.get_schedule()
    srcs = {s.regulator_id: s for s in _sources(session, lane)}
    ids = list(srcs)
    if not ids:
        return {"date": None, "totals": {}, "by_source": []}

    if day is None:
        idx = _day_index(_runs_since(session,
                                     sched.local_now(now).date() - _dt.timedelta(days=30),
                                     ids))
        candidates = [d for d, v in idx.items() if v["ran"] and not v["running"]]
        day = max(candidates) if candidates else sched.local_now(now).date()

    start = day - _dt.timedelta(days=7)
    per: Dict[str, dict] = {i: {"new": 0, "revised": 0, "hist": []} for i in ids}
    for r in _runs_since(session, start, ids):
        if r.regulator_id not in per:
            continue
        if r.logical_date == day:
            per[r.regulator_id]["new"] += r.ingested or 0
            per[r.regulator_id]["revised"] += r.archived or 0
        elif r.logical_date < day:
            per[r.regulator_id]["hist"].append(r.ingested or 0)

    rows = []
    for rid, v in per.items():
        if not v["new"] and not v["revised"]:
            continue
        hist = v["hist"]
        base = round(sum(hist) / len(hist), 1) if hist else None
        rows.append({"regulator_id": rid, "name": getattr(srcs[rid], "name", rid),
                     "category": getattr(srcs[rid], "category", ""),
                     "new": v["new"], "revised": v["revised"],
                     "avg7": base,
                     "vs_avg7": None if base is None else round(v["new"] - base, 1)})
    rows.sort(key=lambda r: -r["new"])

    critical = session.scalar(
        select(func.count()).select_from(Document).where(
            Document.regulator_id.in_(ids),
            Document.materiality_band == "Critical",
            func.date(Document.ingested_at) == day.isoformat())) or 0

    totals = {"new_docs": sum(r["new"] for r in rows),
              "revised": sum(r["revised"] for r in rows),
              "critical": int(critical),
              "sources_reporting": len(rows)}
    return {"date": day.isoformat(), "totals": totals,
            "by_source": rows[:top], "more": max(0, len(rows) - top),
            "more_new": sum(r["new"] for r in rows[top:]),
            "more_revised": sum(r["revised"] for r in rows[top:])}


# ── rerun candidates ────────────────────────────────────────────────────────

def candidates(session, *, lane: Optional[str] = None,
               now: Optional[_dt.datetime] = None) -> dict:
    """Every source, with the one fact that decides whether to rerun it.

    Sorted into the buckets a person actually picks from. `silent` is the
    important one: those runs are green, so nothing else on the page complains
    about them, and the data quietly ages out.
    """
    now = _utc(now)
    today = _sched.get_schedule().local_now(now).date()
    srcs = _sources(session, lane)
    ids = [s.regulator_id for s in srcs]
    runs = _runs_since(session, today - _dt.timedelta(days=90), ids)

    by_src: Dict[str, List[Run]] = defaultdict(list)
    for r in runs:
        by_src[r.regulator_id].append(r)

    rows = []
    for s in srcs:
        mine = sorted(by_src.get(s.regulator_id, []),
                      key=lambda r: (r.logical_date, r.started_at or _dt.datetime.min))
        window = int(getattr(s, "staleness_alert_days", 14) or 14)
        clean = [r for r in mine if not _is_failed(r) and not _is_empty(r)]
        last_clean = clean[-1].logical_date if clean else None
        last_any = mine[-1].logical_date if mine else None

        streak = 0
        for r in reversed(mine):
            if _is_failed(r):
                streak += 1
            else:
                break

        days_stale = (today - last_clean).days if last_clean else None
        if not mine:
            bucket, note = "never", "no run on record"
        elif streak:
            bucket = "failed"
            note = f"{streak} consecutive failure{'s' if streak > 1 else ''}"
        elif days_stale is not None and days_stale > window:
            bucket = "stale"
            note = f"{days_stale}d since a clean run — window is {window}d"
        elif mine and _is_empty(mine[-1]):
            runs_empty = 0
            for r in reversed(mine):
                if _is_empty(r):
                    runs_empty += 1
                else:
                    break
            bucket = "silent"
            note = (f"succeeded but returned nothing, "
                    f"{runs_empty} run{'s' if runs_empty > 1 else ''} in a row")
        else:
            bucket, note = "ok", ""

        rows.append({
            "regulator_id": s.regulator_id, "name": s.name,
            "category": s.category, "jurisdiction": s.jurisdiction,
            "bucket": bucket, "note": note,
            "window_days": window, "days_stale": days_stale,
            "fail_streak": streak,
            "last_clean": last_clean.isoformat() if last_clean else None,
            "last_run": last_any.isoformat() if last_any else None,
        })

    order = {"failed": 0, "stale": 1, "silent": 2, "never": 3, "ok": 4}
    rows.sort(key=lambda r: (order[r["bucket"]], -(r["days_stale"] or 0)))
    counts = {b: sum(1 for r in rows if r["bucket"] == b) for b in order}
    return {"counts": counts, "sources": rows}


def overview(session, *, lane: Optional[str] = None, days: int = 7,
             trend_days: int = 30, now: Optional[_dt.datetime] = None) -> dict:
    """One call for the whole page — the panels share a clock, so they agree."""
    now = _utc(now)
    bar = today_bar(session, lane=lane, now=now)
    return {**bar,
            "matrix": coverage_matrix(session, days=days, lane=lane, now=now),
            "trend": trend(session, days=trend_days, lane=lane, now=now),
            "arrived": arrived(session, lane=lane, now=now),
            "candidates": candidates(session, lane=lane, now=now)}
