"""When collection was expected to run — and therefore when it didn't.

The scheduler is external: a host cron or cloud task calls the daily poll. The
app only ever sees runs that happened, so an empty day is ambiguous — a quiet
Saturday and a dead scheduler look identical. For anyone accountable for
freshness that is the worst thing a dashboard can be.

Declaring the schedule (``config/regagg_schedule.yaml``) makes absence
readable. Every day resolves to exactly one state:

    not_scheduled   a weekend, a holiday, or the feature is off — expected,
                    and never rendered as a fault
    complete        every active source produced a clean run
    partial         it ran, but some sources failed or returned nothing
    running         in flight right now
    due             expected later today, still inside the grace window
    missed          expected, the grace window has passed, nothing recorded

Nothing here triggers anything. It is a declaration the UI reads, which is
also why it can drift: if the cron entry changes and this file does not, the
missed count climbs and says so.
"""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

CONFIG_PATH = Path("config/regagg_schedule.yaml")

_DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

NOT_SCHEDULED = "not_scheduled"
COMPLETE = "complete"
PARTIAL = "partial"
RUNNING = "running"
DUE = "due"
MISSED = "missed"


@dataclass(frozen=True)
class Intraday:
    """The news-lane poll. Independent of the daily job by design: fresh wires
    and a full corpus sweep are different jobs on different clocks."""

    enabled: bool = False
    every_hours: int = 3
    start: str = "07:00"
    end: str = "19:00"
    days: Sequence[str] = field(default_factory=lambda: list(_DAYS[:5]))

    def hours(self) -> List[int]:
        """The hours it fires, host-local. Empty when disabled."""
        if not self.enabled:
            return []
        try:
            s = int(str(self.start).split(":")[0])
            e = int(str(self.end).split(":")[0])
        except (ValueError, TypeError):
            s, e = 7, 19
        step = max(1, min(int(self.every_hours or 3), 12))
        return list(range(s, e + 1, step))


@dataclass(frozen=True)
class Schedule:
    """A declared expectation. Absent config means "we make no claim"."""

    enabled: bool = False
    at: str = "06:00"
    timezone: str = "UTC"
    days: Sequence[str] = field(default_factory=lambda: list(_DAYS[:5]))
    grace_minutes: int = 90
    skip_dates: Sequence[str] = field(default_factory=tuple)
    intraday: Intraday = field(default_factory=Intraday)

    # ── zone / time helpers ─────────────────────────────────────────────────

    @property
    def zone(self) -> _dt.tzinfo:
        try:
            return ZoneInfo(self.timezone)
        except (ZoneInfoNotFoundError, ValueError):
            return _dt.timezone.utc

    @property
    def at_time(self) -> _dt.time:
        try:
            hh, mm = str(self.at).split(":")[:2]
            return _dt.time(int(hh), int(mm))
        except (ValueError, TypeError):
            return _dt.time(6, 0)

    def local_now(self, now: Optional[_dt.datetime] = None) -> _dt.datetime:
        now = now or _dt.datetime.now(_dt.timezone.utc)
        if now.tzinfo is None:
            now = now.replace(tzinfo=_dt.timezone.utc)
        return now.astimezone(self.zone)

    # ── expectation ─────────────────────────────────────────────────────────

    def is_expected(self, day: _dt.date) -> bool:
        """Was a run due on this calendar day at all?"""
        if not self.enabled:
            return False
        if day.isoformat() in set(self.skip_dates or ()):
            return False
        return _DAYS[day.weekday()] in {d.lower() for d in self.days}

    def due_at(self, day: _dt.date) -> Optional[_dt.datetime]:
        """The moment a run becomes due on `day`, in the declared zone."""
        if not self.is_expected(day):
            return None
        return _dt.datetime.combine(day, self.at_time, tzinfo=self.zone)

    def deadline(self, day: _dt.date) -> Optional[_dt.datetime]:
        """After this, silence is a missed run rather than a pending one."""
        due = self.due_at(day)
        return None if due is None else due + _dt.timedelta(minutes=self.grace_minutes)

    def next_run_at(self, now: Optional[_dt.datetime] = None) -> Optional[_dt.datetime]:
        """The next moment a run is due, looking up to a fortnight ahead."""
        if not self.enabled:
            return None
        local = self.local_now(now)
        for offset in range(0, 15):
            day = (local + _dt.timedelta(days=offset)).date()
            due = self.due_at(day)
            if due is not None and due > local:
                return due
        return None

    def expected_days(self, start: _dt.date, end: _dt.date) -> List[_dt.date]:
        """Every day in [start, end] on which a run was due."""
        out, day = [], start
        while day <= end:
            if self.is_expected(day):
                out.append(day)
            day += _dt.timedelta(days=1)
        return out

    # ── the state machine ───────────────────────────────────────────────────

    def state_for(self, day: _dt.date, *, ran: int = 0, failed: int = 0,
                  empty: int = 0, active_sources: int = 0, running: int = 0,
                  now: Optional[_dt.datetime] = None) -> Dict:
        """What to show for one day, and why.

        `ran` counts sources with any run recorded for the day; `failed` and
        `empty` are subsets of it. The reason string is returned alongside the
        state so the UI never has to re-derive it — and so the two can't drift.
        """
        local = self.local_now(now)
        expected = self.is_expected(day)

        if running:
            return {"state": RUNNING, "expected": expected, "ran": ran,
                    "failed": failed, "empty": empty, "running": running,
                    "reason": f"{running} source(s) collecting now"}

        if not expected:
            # A run that happened anyway (a manual rerun) is still worth showing.
            if ran:
                return {"state": PARTIAL if (failed or empty) else COMPLETE,
                        "expected": False, "ran": ran, "failed": failed,
                        "empty": empty, "running": 0,
                        "reason": "not scheduled today — this was run by hand"}
            why = "outside the declared schedule" if self.enabled \
                else "no schedule declared, so nothing is expected"
            return {"state": NOT_SCHEDULED, "expected": False, "ran": 0,
                    "failed": 0, "empty": 0, "running": 0, "reason": why}

        if ran:
            if failed:
                return {"state": PARTIAL, "expected": True, "ran": ran,
                        "failed": failed, "empty": empty, "running": 0,
                        "reason": f"{failed} source(s) failed"}
            if empty:
                return {"state": PARTIAL, "expected": True, "ran": ran,
                        "failed": 0, "empty": empty, "running": 0,
                        "reason": f"{empty} source(s) returned nothing"}
            if active_sources and ran < active_sources:
                return {"state": PARTIAL, "expected": True, "ran": ran,
                        "failed": 0, "empty": 0, "running": 0,
                        "reason": f"{active_sources - ran} source(s) never started"}
            return {"state": COMPLETE, "expected": True, "ran": ran,
                    "failed": 0, "empty": 0, "running": 0,
                    "reason": "every source reported cleanly"}

        deadline = self.deadline(day)
        if deadline is not None and local <= deadline:
            due = self.due_at(day)
            return {"state": DUE, "expected": True, "ran": 0, "failed": 0,
                    "empty": 0, "running": 0,
                    "due_at": due.isoformat() if due else None,
                    "reason": f"due {self.at} {self.timezone}"}

        return {"state": MISSED, "expected": True, "ran": 0, "failed": 0,
                "empty": 0, "running": 0,
                "reason": f"expected {self.at} {self.timezone}, nothing recorded"}

    def describe(self, now: Optional[_dt.datetime] = None) -> Dict:
        """The declaration itself, for the UI to show and for humans to check."""
        nxt = self.next_run_at(now)
        return {"enabled": self.enabled, "at": self.at, "timezone": self.timezone,
                "intraday": {"enabled": self.intraday.enabled,
                             "every_hours": self.intraday.every_hours,
                             "between": [self.intraday.start, self.intraday.end],
                             "days": list(self.intraday.days),
                             "hours": self.intraday.hours()},
                "days": list(self.days), "grace_minutes": self.grace_minutes,
                "skip_dates": list(self.skip_dates or ()),
                "next_run_at": nxt.isoformat() if nxt else None,
                "source": str(CONFIG_PATH),
                "note": None if self.enabled else
                        "No schedule is declared, so no run can be called late. "
                        "Declare one in config/regagg_schedule.yaml to see "
                        "missed runs."}


def load(path: Optional[Path] = None) -> Schedule:
    """Read the declaration. A missing or broken file is not an outage.

    Falling back to a disabled schedule keeps every page working and simply
    stops it claiming anything about lateness — which is the honest answer
    when nobody has said when collection ought to run.
    """
    p = Path(path or CONFIG_PATH)
    if not p.exists():
        return Schedule(enabled=False)
    try:
        import yaml
        raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001 — a bad file must not take the page down
        return Schedule(enabled=False)
    if not isinstance(raw, dict):
        return Schedule(enabled=False)
    days = raw.get("days") or _DAYS[:5]
    if isinstance(days, str):
        days = [d.strip() for d in days.split(",") if d.strip()]
    skip = raw.get("skip_dates") or []
    intra_raw = raw.get("intraday") or {}
    between = intra_raw.get("between") or ["07:00", "19:00"]
    idays = intra_raw.get("days") or days
    intraday = Intraday(
        enabled=bool(intra_raw.get("enabled", False)),
        every_hours=int(intra_raw.get("every_hours", 3) or 3),
        start=str(between[0] if len(between) > 0 else "07:00"),
        end=str(between[1] if len(between) > 1 else "19:00"),
        days=[str(d).lower()[:3] for d in idays],
    )
    return Schedule(
        intraday=intraday,
        enabled=bool(raw.get("enabled", False)),
        at=str(raw.get("at", "06:00")),
        timezone=str(raw.get("timezone", "UTC")),
        days=[str(d).lower()[:3] for d in days],
        grace_minutes=int(raw.get("grace_minutes", 90) or 0),
        skip_dates=[str(d) for d in skip],
    )


_CACHE: Optional[Schedule] = None
_CACHE_MTIME: float = 0.0


def get_schedule(path: Optional[Path] = None) -> Schedule:
    """Cached, but reloaded when the file changes — editing it takes effect."""
    global _CACHE, _CACHE_MTIME
    p = Path(path or CONFIG_PATH)
    try:
        mtime = p.stat().st_mtime
    except OSError:
        mtime = 0.0
    if _CACHE is None or mtime != _CACHE_MTIME:
        _CACHE = load(p)
        _CACHE_MTIME = mtime
    return _CACHE
