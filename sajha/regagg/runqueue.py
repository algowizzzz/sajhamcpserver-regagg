"""A queue for UI-triggered collection runs. Every click is accepted.

The bug this closes: `runtime.spawn_ingest` refused a second run while one was
in flight, returned that refusal *inside* an HTTP 200, and the dashboard tested
`d.queued === false` against a dict — a branch that can never be true. Nine
clicks produced one run and nine "started" messages. The refusal was correct at
every layer except the one the operator could see.

Two things change here. A click now **joins a queue** instead of being dropped,
and every source carries a state the page can draw: `queued` → `running` →
`done` / `failed`.

**Why a queue and not N concurrent processes.** `regagg_ingest_live.py` ends
with an enrichment sweep over the entire corpus. Eight copies of it means eight
sweeps contending for one SQLite writer, which is exactly how a backfill was
lost once already (`08_KNOWN_ISSUES_AND_ROADMAP.md`). So pending ids are
*coalesced*: everything waiting goes into a single `--only a,b,c` batch. That
runs the same sources with one sweep instead of eight, which is both safe and
faster than spawning them separately. From the operator's seat it is fully
concurrent — click as many as you like, all of them run, each reports its own
outcome.

**Outcomes are read back from the database, not assumed.** When the batch exits
we look up each source's newest run row and use what it says. A source the
runner never recorded is reported as failed, not quietly marked done.
"""

from __future__ import annotations

import subprocess
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

QUEUED, RUNNING, DONE, FAILED = "queued", "running", "done", "failed"

# How long a finished outcome stays on the button before the row goes back to
# its normal state. Long enough to read, short enough not to look like status.
RECENT_TTL_S = 180

# A batch that outlives this is treated as stuck rather than left spinning
# forever on a page that offers no way out.
BATCH_TIMEOUT_S = 30 * 60

# Bounded wait for an ingest started outside the app (a manual CLI run, the
# scheduled poll). Colliding with it is the SQLite-lock failure mode.
EXTERNAL_WAIT_S = 15 * 60


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@dataclass
class _Job:
    """One submission. `key` is what makes two jobs safe to merge."""
    ids: List[str]
    key: Tuple
    operator: str


@dataclass
class _State:
    state: str
    note: str = ""
    counts: Dict[str, int] = field(default_factory=dict)
    at: str = ""
    position: int = 0


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _naive_utc(dt: datetime) -> datetime:
    """reg_runs stores naive UTC; compare like with like."""
    return dt.astimezone(timezone.utc).replace(tzinfo=None)


def _external_ingest_pids() -> List[str]:
    try:
        probe = subprocess.run(["pgrep", "-f", "regagg_ingest_live"],
                               capture_output=True, text=True, timeout=10)
        return [p for p in probe.stdout.split() if p]
    except Exception:  # noqa: BLE001 — no pgrep is not a reason to refuse work
        return []


def _read_outcomes(ids: Sequence[str], since: datetime,
                   db_path: Optional[Path] = None) -> Dict[str, dict]:
    """What the database says happened, per source, for runs at or after `since`."""
    import sqlite3

    db = db_path or (repo_root() / "data" / "sajha.db")
    out: Dict[str, dict] = {}
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=30)
    except Exception as e:  # noqa: BLE001
        return {rid: {"ok": False, "note": f"could not read run history: {e}"} for rid in ids}
    try:
        cutoff = _naive_utc(since).isoformat(sep=" ")
        for rid in ids:
            row = con.execute(
                "SELECT status, detected, fetched, ingested, errors, started_at "
                "FROM reg_runs WHERE regulator_id = ? AND started_at >= ? "
                "ORDER BY started_at DESC LIMIT 1", (rid, cutoff)).fetchone()
            if row is None:
                # The batch ran but this source produced no row — a config that
                # failed to load, or a crash before the run was recorded.
                out[rid] = {"ok": False, "note": "the runner recorded no run for this source"}
                continue
            status, detected, fetched, ingested, errors, _ = row
            out[rid] = {
                "ok": status != "failed",
                "note": status,
                "counts": {"detected": detected or 0, "fetched": fetched or 0,
                           "ingested": ingested or 0, "errors": errors or 0},
            }
    finally:
        con.close()
    return out


class RunQueue:
    """Accepts every submission; runs them in coalesced batches, one at a time."""

    def __init__(self, spawn: Optional[Callable] = None,
                 outcomes: Optional[Callable] = None,
                 wait_for_external: bool = True):
        self._lock = threading.RLock()
        self._jobs: List[_Job] = []
        self._states: Dict[str, _State] = {}
        self._running: List[str] = []
        self._worker: Optional[threading.Thread] = None
        self._batch_started: Optional[datetime] = None
        self._waiting_on: List[str] = []
        self._spawn = spawn
        self._outcomes = outcomes or _read_outcomes
        self._wait_for_external = wait_for_external

    # ── submission ──────────────────────────────────────────────────────────

    def submit(self, ids: Sequence[str], *, logical_date: Optional[str] = None,
               max_docs: Optional[int] = None, include: Optional[str] = None,
               operator: str = "ui") -> dict:
        """Accept a click. Nothing is ever refused; already-running ids are
        reported as such rather than being queued a second time."""
        ids = [i for i in dict.fromkeys(ids) if i]
        if not ids:
            return {"accepted": False, "queued": [], "already_running": [],
                    "detail": "no sources to run"}

        key = (logical_date, max_docs, include)
        with self._lock:
            self._expire_locked()
            already, fresh = [], []
            for rid in ids:
                st = self._states.get(rid)
                if st and st.state in (QUEUED, RUNNING):
                    already.append(rid)
                else:
                    fresh.append(rid)
            if fresh:
                self._jobs.append(_Job(ids=fresh, key=key, operator=operator))
                for rid in fresh:
                    self._states[rid] = _State(state=QUEUED, note="waiting to start",
                                               at=_utcnow().isoformat())
                self._renumber_locked()
            self._ensure_worker_locked()
            pending = self._pending_count_locked()

        return {"accepted": True, "queued": fresh, "already_running": already,
                "pending": pending, "running": list(self._running),
                "detail": self._describe(fresh, already)}

    @staticmethod
    def _describe(fresh: List[str], already: List[str]) -> str:
        bits = []
        if fresh:
            bits.append(f"queued {len(fresh)} source" + ("s" if len(fresh) != 1 else ""))
        if already:
            bits.append(f"{len(already)} already in this run")
        return " · ".join(bits) or "nothing to do"

    # ── what the page draws ─────────────────────────────────────────────────

    def snapshot(self) -> dict:
        with self._lock:
            self._expire_locked()
            active = bool(self._running) or bool(self._jobs)
            return {
                "active": active,
                "running": list(self._running),
                "pending": self._pending_count_locked(),
                "waiting_on_external": list(self._waiting_on),
                "batch_started": self._batch_started.isoformat() if self._batch_started else None,
                "sources": {rid: {"state": s.state, "note": s.note, "counts": s.counts,
                                  "at": s.at, "position": s.position}
                            for rid, s in self._states.items()},
            }

    # ── internals (all callers hold the lock) ───────────────────────────────

    def _pending_count_locked(self) -> int:
        return sum(len(j.ids) for j in self._jobs)

    def _renumber_locked(self) -> None:
        pos = 0
        for job in self._jobs:
            for rid in job.ids:
                pos += 1
                st = self._states.get(rid)
                if st and st.state == QUEUED:
                    st.position = pos

    def _expire_locked(self) -> None:
        """Drop finished outcomes once they have been on screen long enough."""
        cutoff = _utcnow() - timedelta(seconds=RECENT_TTL_S)
        for rid in [r for r, s in self._states.items() if s.state in (DONE, FAILED)]:
            try:
                if datetime.fromisoformat(self._states[rid].at) < cutoff:
                    del self._states[rid]
            except (ValueError, KeyError):
                del self._states[rid]

    def _ensure_worker_locked(self) -> None:
        if self._worker is not None and self._worker.is_alive():
            return
        self._worker = threading.Thread(target=self._drain, name="regagg-runqueue",
                                        daemon=True)
        self._worker.start()

    def _set(self, ids: Sequence[str], state: str, note: str = "",
             counts: Optional[dict] = None) -> None:
        with self._lock:
            for rid in ids:
                self._states[rid] = _State(state=state, note=note,
                                           counts=dict(counts or {}),
                                           at=_utcnow().isoformat())

    # ── the worker ──────────────────────────────────────────────────────────

    def _take_batch(self) -> Optional[Tuple[List[str], Tuple, str]]:
        """All consecutive jobs sharing the first job's key, merged into one."""
        with self._lock:
            if not self._jobs:
                self._worker = None
                return None
            key = self._jobs[0].key
            operator = self._jobs[0].operator
            batch, rest = [], []
            for job in self._jobs:
                (batch if job.key == key else rest).append(job)
            self._jobs = rest
            ids = list(dict.fromkeys([i for job in batch for i in job.ids]))
            self._running = ids
            self._batch_started = _utcnow()
            self._renumber_locked()
            return ids, key, operator

    def _drain(self) -> None:
        while True:
            taken = self._take_batch()
            if taken is None:
                return
            ids, key, operator = taken
            started = _utcnow()
            try:
                self._set(ids, RUNNING, "collecting")
                self._await_external()
                result = self._launch(ids, key, operator)
                if result.get("started") is False:
                    # The coarse guard fired anyway (a run started underneath
                    # us). Say so — the operator can click again.
                    self._set(ids, FAILED, result.get("reason", "could not start"))
                else:
                    self._record(ids, started)
            except Exception as e:  # noqa: BLE001 — one bad batch must not kill the worker
                self._set(ids, FAILED, f"could not run: {e}")
            finally:
                with self._lock:
                    self._running = []
                    self._batch_started = None
                    self._waiting_on = []

    def _await_external(self) -> None:
        if not self._wait_for_external:
            return
        deadline = time.monotonic() + EXTERNAL_WAIT_S
        while time.monotonic() < deadline:
            pids = _external_ingest_pids()
            if not pids:
                break
            with self._lock:
                self._waiting_on = pids
            self._set(self._running, RUNNING, "waiting for an ingest already running")
            time.sleep(2)
        with self._lock:
            self._waiting_on = []

    def _launch(self, ids: List[str], key: Tuple, operator: str) -> dict:
        """Run the batch and block until it finishes.

        Goes through `runtime.get_rerun_trigger()` so a stubbed trigger (tests,
        or an external scheduler wired via `set_providers`) still works. A
        trigger that cannot wait is treated as synchronous.
        """
        import inspect

        from sajha.regagg import runtime

        trigger = self._spawn or runtime.get_rerun_trigger()
        logical_date, max_docs, include = key
        kwargs = dict(scope="ids", logical_date=logical_date, ids=ids,
                      operator=operator, max_docs=max_docs, include=include)
        try:
            if "wait" in inspect.signature(trigger).parameters:
                kwargs["wait"] = True
        except (TypeError, ValueError):
            pass
        return trigger(**kwargs) or {}

    def _record(self, ids: List[str], since: datetime) -> None:
        outcomes = self._outcomes(ids, since)
        for rid in ids:
            o = outcomes.get(rid) or {"ok": False, "note": "no outcome reported"}
            self._set([rid], DONE if o.get("ok") else FAILED,
                      o.get("note", ""), o.get("counts"))


_QUEUE: Optional[RunQueue] = None
_QUEUE_LOCK = threading.Lock()


def get_queue() -> RunQueue:
    global _QUEUE
    with _QUEUE_LOCK:
        if _QUEUE is None:
            _QUEUE = RunQueue()
        return _QUEUE


def reset_queue(queue: Optional[RunQueue] = None) -> RunQueue:
    """Tests only — replace the process-wide queue."""
    global _QUEUE
    with _QUEUE_LOCK:
        _QUEUE = queue or RunQueue()
        return _QUEUE
