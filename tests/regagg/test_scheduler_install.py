"""Installing the collection job — generated from the declaration, never typed.

The bug this closes is not a crash. `config/regagg_schedule.yaml` declared a
weekday schedule and **no scheduler existed on the host at all**; the runs
labelled `trigger=schedule` had been launched by hand. The Health page counted
missed runs against a promise nobody was keeping.

So the properties worth pinning are: the unit is derived from the declaration
(no second place to write a schedule), the timezone conversion is real, and
`status()` reports what the operating system says rather than a flag of ours.

Nothing here installs anything — rendering and conversion are pure, and the
install path is exercised by hand (see testing/03_RESULTS.md).
"""

from __future__ import annotations

import plistlib

import pytest

from sajha.regagg import schedule as S
from sajha.regagg import scheduler_install as SI


def _sched(**kw) -> S.Schedule:
    base = dict(enabled=True, at="06:00", timezone="America/Toronto",
                days=["mon", "tue", "wed", "thu", "fri"], grace_minutes=90)
    base.update(kw)
    return S.Schedule(**base)


# ── the conversion ──────────────────────────────────────────────────────────

def test_the_declared_time_is_converted_to_host_local(monkeypatch):
    """launchd has no timezones — it fires in host-local time. Installing
    06:00 Toronto verbatim on a Chicago machine is a silent one-hour error."""
    monkeypatch.setattr(SI, "host_timezone", lambda: "America/Chicago")
    t = SI.local_time_for(_sched())
    assert t["local"] == "05:00"
    assert t["shifted"] is True
    assert "America/Chicago" in t["note"]


def test_matching_zones_need_no_conversion(monkeypatch):
    monkeypatch.setattr(SI, "host_timezone", lambda: "America/Toronto")
    t = SI.local_time_for(_sched())
    assert t["local"] == "06:00" and t["shifted"] is False


def test_a_conversion_can_cross_midnight(monkeypatch):
    """01:00 Toronto is the previous evening in Los Angeles; the day shift is
    reported rather than silently dropping a weekday."""
    monkeypatch.setattr(SI, "host_timezone", lambda: "America/Los_Angeles")
    t = SI.local_time_for(_sched(at="01:00"))
    assert t["local"] == "22:00"
    assert t["day_shift"] == -1


def test_an_unknown_host_zone_does_not_raise(monkeypatch):
    monkeypatch.setattr(SI, "host_timezone", lambda: "Not/AZone")
    assert SI.local_time_for(_sched())["local"]


# ── rendering: the unit comes from the declaration ──────────────────────────

def test_the_plist_fires_on_the_declared_days_only(monkeypatch):
    monkeypatch.setattr(SI, "host_timezone", lambda: "America/Toronto")
    p = plistlib.loads(SI.launchd_plist(_sched(days=["mon", "wed"])))
    assert [i["Weekday"] for i in p["StartCalendarInterval"]] == [1, 3]
    assert {i["Hour"] for i in p["StartCalendarInterval"]} == {6}


def test_the_plist_uses_the_venv_interpreter():
    """A launchd agent gets a minimal environment; `python3` there is the
    system one, which has none of this project's dependencies."""
    p = plistlib.loads(SI.launchd_plist(_sched()))
    assert p["ProgramArguments"][0].endswith(".venv/bin/python")
    assert p["ProgramArguments"][1].endswith("regagg_daily_poll.py")


def test_the_plist_carries_no_empty_secrets(monkeypatch):
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    monkeypatch.setenv("REGAGG_SECRET", "s3cret")
    env = plistlib.loads(SI.launchd_plist(_sched()))["EnvironmentVariables"]
    assert env == {"REGAGG_SECRET": "s3cret"}      # absent, not empty-string


def test_the_systemd_timer_matches_the_declaration(monkeypatch):
    monkeypatch.setattr(SI, "host_timezone", lambda: "America/Toronto")
    units = SI.systemd_units(_sched(days=["mon", "fri"]))
    timer = units["riskgpt-collect.timer"]
    assert "OnCalendar=Mon,Fri 06:00:00" in timer
    assert "Persistent=true" in timer              # a missed window still runs
    svc = units["riskgpt-collect.service"]
    assert "regagg_daily_poll.py" in svc and "Type=oneshot" in svc


def test_changing_the_declaration_changes_the_unit(monkeypatch):
    """The point of generating it: there is no second place to edit."""
    monkeypatch.setattr(SI, "host_timezone", lambda: "America/Toronto")
    a = SI.systemd_units(_sched(at="06:00"))["riskgpt-collect.timer"]
    b = SI.systemd_units(_sched(at="19:30"))["riskgpt-collect.timer"]
    assert "06:00:00" in a and "19:30:00" in b


# ── refusals ────────────────────────────────────────────────────────────────

# ── the two jobs are independent ────────────────────────────────────────────

def test_the_intraday_job_runs_the_news_poll_not_the_daily_one():
    """Different scripts on purpose: the daily pass re-enriches the whole
    corpus, which is wasteful six times a day."""
    p = plistlib.loads(SI.launchd_plist(_sched(), job="intraday"))
    assert p["Label"] == SI.LABEL_INTRADAY
    assert p["ProgramArguments"][1].endswith("regagg_news_poll.py")


def test_the_intraday_job_fires_on_its_declared_window():
    iv = S.Intraday(enabled=True, every_hours=4, start="08:00", end="16:00",
                    days=["mon", "tue"])
    p = plistlib.loads(SI.launchd_plist(_sched(intraday=iv), job="intraday"))
    assert sorted({i["Hour"] for i in p["StartCalendarInterval"]}) == [8, 12, 16]
    assert sorted({i["Weekday"] for i in p["StartCalendarInterval"]}) == [1, 2]


def test_a_disabled_intraday_declaration_yields_no_hours():
    assert S.Intraday(enabled=False).hours() == []


def test_the_two_jobs_use_different_labels_and_paths():
    """Installing one must never disturb the other."""
    assert SI._label("daily") != SI._label("intraday")
    assert SI._plist_path("daily") != SI._plist_path("intraday")
    assert SI._unit_name("daily") != SI._unit_name("intraday")


def test_installing_intraday_is_refused_when_it_is_not_declared(monkeypatch):
    monkeypatch.setattr(S, "get_schedule",
                        lambda *a, **k: _sched(intraday=S.Intraday(enabled=False)))
    out = SI.install("intraday")
    assert out["ok"] is False and "intraday schedule is disabled" in out["detail"]


def test_status_reports_both_jobs(monkeypatch):
    monkeypatch.setattr(SI, "detect", lambda: None)
    st = SI.status()
    assert set(st["jobs"]) == set(SI.JOBS)


def test_install_refuses_when_the_schedule_is_disabled(monkeypatch):
    monkeypatch.setattr(S, "get_schedule", lambda *a, **k: S.Schedule(enabled=False))
    out = SI.install()
    assert out["ok"] is False and "disabled" in out["detail"]


def test_install_refuses_when_the_host_has_no_scheduler(monkeypatch):
    monkeypatch.setattr(SI, "detect", lambda: None)
    out = SI.install()
    assert out["ok"] is False and "no user-level scheduler" in out["detail"]


def test_status_reports_the_absence_of_a_scheduler_rather_than_guessing(monkeypatch):
    monkeypatch.setattr(SI, "detect", lambda: None)
    st = SI.status_for("daily")
    assert st["installed"] is False and st["platform"] is None
    assert "neither launchctl nor systemctl" in st["detail"]


def test_status_separates_installed_from_loaded(monkeypatch, tmp_path):
    """A file on disk that launchd never loaded is not a working scheduler,
    and must not be reported as one."""
    plist = tmp_path / "x.plist"
    plist.write_text("<plist/>")
    monkeypatch.setattr(SI, "detect", lambda: "launchd")
    monkeypatch.setattr(SI, "_plist_path", lambda job="daily": plist)

    class R:
        stdout = ""            # launchctl list does not mention the label
    monkeypatch.setattr(SI.subprocess, "run", lambda *a, **k: R())
    st = SI.status_for("daily")
    assert st["installed"] is True and st["loaded"] is False
    assert "not loaded" in st["detail"]
