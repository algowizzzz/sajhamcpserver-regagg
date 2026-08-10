"""The command line the UI actually launches.

Three bugs lived here, all of the same shape: a parameter the API accepted,
documented, and then dropped on the floor.

`logical_date` was the worst of them. The coverage matrix offers "▶ Run these N"
on a missed day; that date reached `spawn_ingest` and went nowhere, because the
runner had no `--date` and called `date.today()`. The run was filed under today,
the gap stayed open, and clicking it again did the same thing.

`max_docs` was accepted but never defaulted, so the Health page's Rerun ran
uncapped — on a source listing 29,000 URLs that is half an hour of queue.
"""

from __future__ import annotations

import subprocess

import pytest

from sajha.regagg import runtime


class _Proc:
    def __init__(self, *a, **kw):
        self.pid = 4242
        self.waited = False

    def wait(self):
        self.waited = True
        return 0


@pytest.fixture()
def launched(monkeypatch, tmp_path):
    """Capture argv instead of starting anything."""
    seen = {}

    def fake_run(cmd, **kw):          # the pgrep guard: report nothing running
        class R:
            stdout = ""
        return R()

    def fake_popen(cmd, **kw):
        seen["cmd"] = list(cmd)
        seen["proc"] = _Proc()
        return seen["proc"]

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(subprocess, "Popen", fake_popen)
    return seen


def flag(cmd, name):
    """The value following `name`, or None if the flag is absent."""
    return cmd[cmd.index(name) + 1] if name in cmd else None


# ── the logical date ────────────────────────────────────────────────────────

def test_a_backfill_date_reaches_the_runner(launched):
    """The bug: this argument was accepted and silently discarded, so a rerun
    for a missed day collected under today and the gap never closed."""
    runtime.spawn_ingest(scope="ids", ids=["osfi"], logical_date="2026-08-05")
    assert flag(launched["cmd"], "--date") == "2026-08-05"


def test_no_date_means_no_flag_so_the_runner_uses_today(launched):
    runtime.spawn_ingest(scope="ids", ids=["osfi"])
    assert "--date" not in launched["cmd"]


# ── the cap ─────────────────────────────────────────────────────────────────

def test_a_cap_reaches_the_runner(launched):
    runtime.spawn_ingest(scope="ids", ids=["osc"], max_docs=200)
    assert flag(launched["cmd"], "--max-docs") == "200"


def test_no_cap_is_passed_through_as_uncapped_rather_than_invented(launched):
    """The default belongs to the caller that knows the context, not here —
    the daily poll and a one-source rerun want different limits."""
    runtime.spawn_ingest(scope="ids", ids=["osc"])
    assert "--max-docs" not in launched["cmd"]


# ── scope ───────────────────────────────────────────────────────────────────

def test_only_the_named_sources_are_run(launched):
    runtime.spawn_ingest(scope="ids", ids=["a", "b"])
    assert flag(launched["cmd"], "--only") == "a,b"


def test_scope_all_does_not_narrow_the_fleet(launched):
    runtime.spawn_ingest(scope="all", ids=["a"])
    assert "--only" not in launched["cmd"]


def test_the_operator_is_attributed(launched):
    runtime.spawn_ingest(scope="ids", ids=["a"], operator="desk@bank.test")
    assert flag(launched["cmd"], "--operator") == "desk@bank.test"


# ── waiting, which is how the queue knows a batch is done ───────────────────

def test_wait_blocks_and_reports_the_exit_code(launched):
    out = runtime.spawn_ingest(scope="ids", ids=["a"], wait=True)
    assert launched["proc"].waited is True
    assert out["returncode"] == 0


def test_without_wait_it_returns_immediately(launched):
    out = runtime.spawn_ingest(scope="ids", ids=["a"])
    assert launched["proc"].waited is False
    assert "returncode" not in out and out["pid"] == 4242


# ── the guard ───────────────────────────────────────────────────────────────

def test_a_second_fleet_is_refused_while_one_is_running(monkeypatch):
    """SQLite has a single writer. The refusal is correct — the bug was that
    nobody could see it (see test_runqueue.py)."""
    class R:
        stdout = "991\n"

    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: R())
    out = runtime.spawn_ingest(scope="ids", ids=["a"])
    assert out["started"] is False
    assert "already active" in out["reason"] and out["active_pids"] == ["991"]
