"""The run queue — every click is accepted, and every source reports its own fate.

The bug this closes was not a crash. `spawn_ingest` refused a second run while
one was in flight, and that refusal travelled back inside an HTTP 200 while the
dashboard tested `d.queued === false` against a dict. Nine clicks produced one
run and nine "started" messages: the guard was right at every layer except the
one an operator could see.

So the properties worth pinning are that nothing submitted is silently dropped,
that a batch is coalesced rather than run as N racing processes (one SQLite
writer), and that an outcome is *read back from the database* rather than
assumed from the fact that the process exited.
"""

from __future__ import annotations

import sqlite3
import threading
from datetime import datetime, timedelta, timezone

import pytest

from sajha.regagg import runqueue as RQ


class Spawn:
    """A stand-in for the ingest subprocess that records what it was asked to run."""

    def __init__(self, started=True, reason="", block=None):
        self.batches = []
        self.started = started
        self.reason = reason
        self.block = block          # an Event the batch waits on, to hold it "running"
        self.calls = 0

    def __call__(self, scope=None, logical_date=None, ids=None, operator=None,
                 max_docs=None, include=None, wait=False):
        self.calls += 1
        self.batches.append(list(ids or []))
        if self.block is not None:
            self.block.wait(timeout=5)
        if not self.started:
            return {"started": False, "reason": self.reason}
        return {"started": True, "returncode": 0}


def ok_outcomes(counts=None, status="success"):
    def _f(ids, since, db_path=None):
        return {rid: {"ok": True, "note": status,
                      "counts": counts or {"detected": 3, "fetched": 3,
                                           "ingested": 1, "errors": 0}}
                for rid in ids}
    return _f


def drained(q, timeout=5.0):
    """Wait for the worker to finish everything it has."""
    end = threading.Event()
    for _ in range(int(timeout / 0.02)):
        snap = q.snapshot()
        if not snap["active"]:
            return snap
        end.wait(0.02)
    raise AssertionError(f"queue did not drain: {q.snapshot()}")


def make(spawn=None, outcomes=None):
    return RQ.RunQueue(spawn=spawn or Spawn(), outcomes=outcomes or ok_outcomes(),
                       wait_for_external=False)


# ── nothing is dropped ──────────────────────────────────────────────────────

def test_a_click_arriving_during_a_run_is_queued_not_refused():
    """The whole bug in one test. The second click used to be thrown away."""
    gate = threading.Event()
    spawn = Spawn(block=gate)
    q = make(spawn)

    q.submit(["fincen"])
    for _ in range(200):                       # wait until the batch is really running
        if q.snapshot()["running"]:
            break
        threading.Event().wait(0.01)

    out = q.submit(["finra"])
    assert out["accepted"] is True
    assert out["queued"] == ["finra"]          # accepted, not refused
    gate.set()

    drained(q)
    assert spawn.batches == [["fincen"], ["finra"]]


def test_every_submitted_source_ends_up_in_a_batch():
    q = make(spawn := Spawn())
    for rid in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        q.submit([rid])
    drained(q)
    assert sorted(i for b in spawn.batches for i in b) == list("abcdefgh")


def test_the_same_source_clicked_twice_is_reported_not_queued_twice():
    """Nine clicks on one row must not mean nine runs of that source."""
    gate = threading.Event()
    q = make(Spawn(block=gate))
    q.submit(["osc"])
    second = q.submit(["osc"])
    gate.set()
    assert second["queued"] == []
    assert second["already_running"] == ["osc"]
    assert second["accepted"] is True          # accepted, and honestly described
    drained(q)


def test_an_empty_submission_is_refused_rather_than_starting_the_fleet():
    q = make()
    out = q.submit([])
    assert out["accepted"] is False and "no sources" in out["detail"]


# ── coalescing: one batch, not N racing processes ───────────────────────────

def test_pending_clicks_are_coalesced_into_a_single_batch():
    """Eight processes would mean eight enrichment sweeps against one SQLite
    writer — the failure that lost a backfill. They go in one `--only` batch."""
    gate = threading.Event()
    spawn = Spawn(block=gate)
    q = make(spawn)
    q.submit(["first"])                        # occupies the worker
    for _ in range(200):
        if q.snapshot()["running"]:
            break
        threading.Event().wait(0.01)
    for rid in ["b", "c", "d"]:
        q.submit([rid])
    gate.set()
    drained(q)
    assert spawn.batches == [["first"], ["b", "c", "d"]]
    assert spawn.calls == 2                    # not four


def test_submissions_with_different_options_are_not_merged():
    """A capped run and an uncapped run are different work; merging them would
    silently apply one caller's cap to the other's sources."""
    gate = threading.Event()
    spawn = Spawn(block=gate)
    q = make(spawn)
    q.submit(["first"])
    for _ in range(200):
        if q.snapshot()["running"]:
            break
        threading.Event().wait(0.01)
    q.submit(["capped"], max_docs=5)
    q.submit(["plain"])
    gate.set()
    drained(q)
    assert ["capped"] in spawn.batches and ["plain"] in spawn.batches


def test_the_batch_is_run_with_scope_ids_so_it_cannot_widen_to_the_fleet():
    seen = {}

    def spy(scope=None, ids=None, **kw):
        seen.update(scope=scope, ids=list(ids or []))
        return {"started": True}

    q = make(spy)
    q.submit(["eba"])
    drained(q)
    assert seen == {"scope": "ids", "ids": ["eba"]}


# ── the states a page draws ─────────────────────────────────────────────────

def test_a_source_is_queued_then_running_then_done():
    gate = threading.Event()
    q = make(Spawn(block=gate))
    q.submit(["hkma"])
    assert q.snapshot()["sources"]["hkma"]["state"] in (RQ.QUEUED, RQ.RUNNING)
    for _ in range(200):
        if q.snapshot()["sources"]["hkma"]["state"] == RQ.RUNNING:
            break
        threading.Event().wait(0.01)
    gate.set()
    drained(q)
    assert q.snapshot()["sources"]["hkma"]["state"] == RQ.DONE


def test_the_outcome_carries_the_counters_the_button_shows():
    q = make(outcomes=ok_outcomes({"detected": 9, "fetched": 9, "ingested": 4, "errors": 1}))
    q.submit(["frb"])
    drained(q)
    assert q.snapshot()["sources"]["frb"]["counts"]["ingested"] == 4


def test_queued_sources_carry_their_position():
    gate = threading.Event()
    q = make(Spawn(block=gate))
    q.submit(["first"])
    for _ in range(200):
        if q.snapshot()["running"]:
            break
        threading.Event().wait(0.01)
    q.submit(["b"])
    q.submit(["c"])
    snap = q.snapshot()
    assert snap["sources"]["b"]["position"] == 1
    assert snap["sources"]["c"]["position"] == 2
    assert snap["pending"] == 2
    gate.set()
    drained(q)


# ── failures are reported, never swallowed ──────────────────────────────────

def test_a_refusal_from_the_spawner_is_surfaced_on_the_source():
    """The original sin: this refusal existed and nobody could see it."""
    q = make(Spawn(started=False, reason="an ingest run is already active"))
    q.submit(["fincen"])
    drained(q)
    st = q.snapshot()["sources"]["fincen"]
    assert st["state"] == RQ.FAILED
    assert "already active" in st["note"]


def test_a_source_the_runner_never_recorded_is_failed_not_done():
    """The process exiting 0 is not evidence that a given source ran."""
    q = make(outcomes=lambda ids, since, db_path=None: {})
    q.submit(["ghost"])
    drained(q)
    st = q.snapshot()["sources"]["ghost"]
    assert st["state"] == RQ.FAILED and "no outcome" in st["note"]


def test_a_run_recorded_as_failed_is_reported_as_failed():
    def bad(ids, since, db_path=None):
        return {i: {"ok": False, "note": "failed", "counts": {}} for i in ids}

    q = make(outcomes=bad)
    q.submit(["fintrac"])
    drained(q)
    assert q.snapshot()["sources"]["fintrac"]["state"] == RQ.FAILED


def test_one_exploding_batch_does_not_kill_the_worker():
    """A dead worker would make every later click vanish — the original bug
    with extra steps."""
    calls = {"n": 0}

    def flaky(**kw):
        calls["n"] += 1
        if calls["n"] == 1:
            raise RuntimeError("boom")
        return {"started": True}

    q = make(flaky)
    q.submit(["a"])
    drained(q)
    assert q.snapshot()["sources"]["a"]["state"] == RQ.FAILED

    q.submit(["b"])
    drained(q)
    assert q.snapshot()["sources"]["b"]["state"] == RQ.DONE


# ── outcomes really are read from the database ──────────────────────────────

def _run_db(tmp_path, rows):
    db = tmp_path / "sajha.db"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE reg_runs (run_id TEXT, regulator_id TEXT, status TEXT, "
                "detected INT, fetched INT, ingested INT, errors INT, started_at TEXT)")
    con.executemany("INSERT INTO reg_runs VALUES (?,?,?,?,?,?,?,?)", rows)
    con.commit()
    con.close()
    return db


def test_outcomes_come_from_reg_runs(tmp_path):
    since = datetime.now(timezone.utc)
    at = RQ._naive_utc(since + timedelta(seconds=5)).isoformat(sep=" ")
    db = _run_db(tmp_path, [("r1", "osfi", "success", 40, 25, 7, 1, at)])
    out = RQ._read_outcomes(["osfi"], since, db_path=db)
    assert out["osfi"]["ok"] is True
    assert out["osfi"]["counts"] == {"detected": 40, "fetched": 25, "ingested": 7, "errors": 1}


def test_a_run_older_than_the_batch_does_not_count_as_this_run(tmp_path):
    """Otherwise a source that silently did nothing would show this morning's
    success and look like it had just been fixed."""
    since = datetime.now(timezone.utc)
    stale = RQ._naive_utc(since - timedelta(hours=6)).isoformat(sep=" ")
    db = _run_db(tmp_path, [("old", "osfi", "success", 1, 1, 1, 0, stale)])
    out = RQ._read_outcomes(["osfi"], since, db_path=db)
    assert out["osfi"]["ok"] is False
    assert "no run" in out["osfi"]["note"]


def test_a_failed_status_in_the_database_is_not_ok(tmp_path):
    since = datetime.now(timezone.utc)
    at = RQ._naive_utc(since + timedelta(seconds=1)).isoformat(sep=" ")
    db = _run_db(tmp_path, [("r", "mas", "failed", 5, 0, 0, 5, at)])
    assert RQ._read_outcomes(["mas"], since, db_path=db)["mas"]["ok"] is False


def test_an_unreadable_database_reports_that_rather_than_claiming_success(tmp_path):
    out = RQ._read_outcomes(["x"], datetime.now(timezone.utc), db_path=tmp_path / "nope.db")
    assert out["x"]["ok"] is False


# ── housekeeping ────────────────────────────────────────────────────────────

def test_finished_outcomes_expire_so_the_row_returns_to_normal(monkeypatch):
    q = make()
    q.submit(["eba"])
    drained(q)
    assert q.snapshot()["sources"]["eba"]["state"] == RQ.DONE

    monkeypatch.setattr(RQ, "RECENT_TTL_S", -1)     # everything is now stale
    assert q.snapshot()["sources"] == {}


def test_the_snapshot_is_quiet_when_nothing_has_been_asked_for():
    snap = make().snapshot()
    assert snap["active"] is False and snap["pending"] == 0 and snap["sources"] == {}
