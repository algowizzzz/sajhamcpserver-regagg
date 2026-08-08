"""The schedule state machine — what makes an empty day readable.

The whole point is the difference between "nothing ran" and "nothing was
supposed to run". Everything else on the Collection page is presentation; this
is the part that can be quietly wrong and mislead someone who is accountable
for the data being current.
"""

from __future__ import annotations

import datetime as _dt

import pytest

from sajha.regagg import schedule as S

TZ = "America/Toronto"


def _sched(**kw) -> S.Schedule:
    base = dict(enabled=True, at="06:00", timezone=TZ,
                days=["mon", "tue", "wed", "thu", "fri"], grace_minutes=90)
    base.update(kw)
    return S.Schedule(**base)


def _at(day: str, hh: int, mm: int = 0) -> _dt.datetime:
    """A UTC instant corresponding to local wall-clock time on `day`."""
    from zoneinfo import ZoneInfo
    local = _dt.datetime.combine(_dt.date.fromisoformat(day),
                                 _dt.time(hh, mm), tzinfo=ZoneInfo(TZ))
    return local.astimezone(_dt.timezone.utc)


SAT = _dt.date(2026, 8, 8)
FRI = _dt.date(2026, 8, 7)
MON = _dt.date(2026, 8, 10)


def test_a_weekend_is_not_a_failure():
    """The case that started this: today is Saturday and the page looked broken."""
    st = _sched().state_for(SAT, ran=0, now=_at("2026-08-08", 14))
    assert st["state"] == S.NOT_SCHEDULED
    assert st["expected"] is False
    assert "schedule" in st["reason"]


def test_a_weekday_with_nothing_recorded_past_grace_is_missed():
    st = _sched().state_for(FRI, ran=0, now=_at("2026-08-07", 9))
    assert st["state"] == S.MISSED
    assert st["expected"] is True
    assert "nothing recorded" in st["reason"]


def test_the_same_day_inside_the_grace_window_is_merely_due():
    """07:00 with a 90-minute grace is late-ish, not late."""
    st = _sched().state_for(FRI, ran=0, now=_at("2026-08-07", 7))
    assert st["state"] == S.DUE
    assert st["due_at"].startswith("2026-08-07T06:00")


def test_before_the_run_time_is_also_due_not_missed():
    st = _sched().state_for(FRI, ran=0, now=_at("2026-08-07", 3))
    assert st["state"] == S.DUE


def test_grace_boundary_is_inclusive_then_flips():
    s = _sched()
    assert s.state_for(FRI, ran=0, now=_at("2026-08-07", 7, 30))["state"] == S.DUE
    assert s.state_for(FRI, ran=0, now=_at("2026-08-07", 7, 31))["state"] == S.MISSED


def test_a_clean_run_on_a_scheduled_day_is_complete():
    st = _sched().state_for(FRI, ran=55, active_sources=55, now=_at("2026-08-07", 9))
    assert st["state"] == S.COMPLETE


@pytest.mark.parametrize("kw,why", [
    ({"ran": 55, "failed": 2, "active_sources": 55}, "failed"),
    ({"ran": 55, "empty": 3, "active_sources": 55}, "returned nothing"),
    ({"ran": 49, "active_sources": 55}, "never started"),
])
def test_partial_says_which_kind_of_partial(kw, why):
    """Three different problems must not collapse into one amber cell."""
    st = _sched().state_for(FRI, now=_at("2026-08-07", 9), **kw)
    assert st["state"] == S.PARTIAL
    assert why in st["reason"]


def test_running_beats_every_other_state():
    st = _sched().state_for(SAT, ran=0, running=4, now=_at("2026-08-08", 14))
    assert st["state"] == S.RUNNING


def test_a_manual_run_on_an_unscheduled_day_still_shows():
    """Someone reran on a Saturday. Hiding that would be a lie of omission."""
    st = _sched().state_for(SAT, ran=6, active_sources=55, now=_at("2026-08-08", 14))
    assert st["state"] == S.COMPLETE
    assert st["expected"] is False
    assert "by hand" in st["reason"]


def test_a_skip_date_behaves_like_a_weekend():
    st = _sched(skip_dates=["2026-08-07"]).state_for(FRI, ran=0,
                                                     now=_at("2026-08-07", 20))
    assert st["state"] == S.NOT_SCHEDULED


def test_next_run_skips_the_weekend():
    nxt = _sched().next_run_at(_at("2026-08-08", 14))
    assert nxt.date() == MON and nxt.hour == 6


def test_next_run_later_today_is_today():
    nxt = _sched().next_run_at(_at("2026-08-07", 3))
    assert nxt.date() == FRI


def test_expected_days_counts_weekdays_only():
    days = _sched().expected_days(_dt.date(2026, 8, 3), _dt.date(2026, 8, 9))
    assert len(days) == 5
    assert SAT not in days


def test_with_no_declaration_nothing_is_ever_late():
    """Silence about the schedule must not become an accusation."""
    off = S.Schedule(enabled=False)
    st = off.state_for(FRI, ran=0, now=_at("2026-08-07", 23))
    assert st["state"] == S.NOT_SCHEDULED
    assert "no schedule declared" in st["reason"]
    assert off.next_run_at(_at("2026-08-07", 9)) is None
    assert off.describe()["note"]


def test_a_missing_or_broken_config_does_not_take_the_page_down(tmp_path):
    assert S.load(tmp_path / "nope.yaml").enabled is False
    bad = tmp_path / "bad.yaml"
    bad.write_text("this: [is: not: valid\n")
    assert S.load(bad).enabled is False


def test_the_shipped_declaration_parses_and_matches_the_documented_intent():
    s = S.load()
    assert s.enabled is True
    assert s.timezone == TZ
    assert set(s.days) == {"mon", "tue", "wed", "thu", "fri"}
    assert s.is_expected(FRI) and not s.is_expected(SAT)


def test_dst_is_handled_by_the_zone_not_by_us():
    """06:00 local stays 06:00 local across the shift — that is why we store a zone."""
    s = _sched()
    before = s.due_at(_dt.date(2026, 3, 6))
    after = s.due_at(_dt.date(2026, 3, 13))
    assert before.hour == after.hour == 6
    assert before.utcoffset() != after.utcoffset()
