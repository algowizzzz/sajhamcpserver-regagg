"""Install the collection job on this host, from the declared schedule.

`config/regagg_schedule.yaml` says when collection is *expected*. Something has
to actually make it happen, and until now that was a cron line somebody typed
on some machine. On this host there was no cron line at all — the runs labelled
`trigger=schedule` were launched by hand, and the Health page was counting
missed runs against a promise no process was keeping.

This module closes that loop. The unit is **generated from the declaration**,
so the two cannot drift: change the YAML, reinstall, and the job matches. There
is no field anywhere for a raw cron string, deliberately — a second place to
write the schedule is a second place for it to be wrong.

Two things it refuses to hide:

**Timezones.** launchd has no concept of one; it fires in host-local time.
systemd can carry `Timezone=` but not every version honours it the same way. So
the declared time is *converted* to host-local at render time and the
conversion is reported. A declaration of 06:00 America/Toronto on a machine set
to America/Chicago installs as 05:00 local, and the status says so.

**Whether it is really there.** `status()` asks the operating system, not a
database flag. An installed-but-unloaded job and a job that was never installed
are different answers.

Everything is user-level: no sudo, no system paths, and uninstall is one call.
"""

from __future__ import annotations

import datetime as _dt
import os
import platform
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional
from zoneinfo import ZoneInfo

from sajha.regagg import schedule as _sched

LABEL = "com.riskgpt.regagg.daily"
LABEL_INTRADAY = "com.riskgpt.regagg.intraday"
SYSTEMD_UNIT = "riskgpt-collect"
SYSTEMD_UNIT_INTRADAY = "riskgpt-news"

# Two jobs, deliberately independent. The daily pass re-enriches the whole
# corpus; the intraday one collects the news lane and skips the sweep. Putting
# them on one timer would mean either wasting the sweep six times a day or
# leaving the wires a day stale.
JOBS = ("daily", "intraday")
_DAY_NUM = {"sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6}
_SYSTEMD_DAY = {"mon": "Mon", "tue": "Tue", "wed": "Wed", "thu": "Thu",
                "fri": "Fri", "sat": "Sat", "sun": "Sun"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _python() -> str:
    """The interpreter the job should use — the venv's, not whatever is on PATH.

    A launchd agent runs with a minimal environment; `python3` there is the
    system one, which has none of this project's dependencies.
    """
    venv = repo_root() / ".venv" / "bin" / "python"
    return str(venv if venv.exists() else Path(sys.executable))


def host_timezone() -> str:
    try:
        link = os.readlink("/etc/localtime")
        if "zoneinfo/" in link:
            return link.split("zoneinfo/", 1)[1]
    except OSError:
        pass
    return _dt.datetime.now().astimezone().tzname() or "local"


def detect() -> Optional[str]:
    """Which init system can hold a user-level timer here."""
    if platform.system() == "Darwin" and shutil.which("launchctl"):
        return "launchd"
    if shutil.which("systemctl"):
        return "systemd"
    return None


# ── the timezone conversion ─────────────────────────────────────────────────

def local_time_for(sched: _sched.Schedule) -> Dict:
    """The declared wall-clock time, expressed in this host's local time.

    Neither init system will do this for us reliably, and getting it wrong is
    a silent one-hour error that only shows up as a run arriving late.
    """
    host_tz_name = host_timezone()
    try:
        host_tz = ZoneInfo(host_tz_name)
    except Exception:  # noqa: BLE001
        host_tz = _dt.datetime.now().astimezone().tzinfo

    # a concrete near-future date, so DST is resolved rather than assumed
    today = _dt.datetime.now(sched.zone).date()
    declared = _dt.datetime.combine(today, sched.at_time, tzinfo=sched.zone)
    local = declared.astimezone(host_tz)
    shifted = (local.hour, local.minute) != (declared.hour, declared.minute)
    day_shift = (local.date() - declared.date()).days

    return {
        "declared": f"{sched.at} {sched.timezone}",
        "host_timezone": host_tz_name,
        "local_hour": local.hour, "local_minute": local.minute,
        "local": f"{local.hour:02d}:{local.minute:02d}",
        "shifted": shifted, "day_shift": day_shift,
        "note": (f"{sched.at} {sched.timezone} is {local.hour:02d}:{local.minute:02d} "
                 f"on this host ({host_tz_name})" if shifted else
                 f"host clock is {host_tz_name}; no conversion needed"),
    }


# ── rendering ───────────────────────────────────────────────────────────────

def _command(job: str = "daily") -> List[str]:
    script = "regagg_news_poll.py" if job == "intraday" else "regagg_daily_poll.py"
    return [_python(), str(repo_root() / "scripts" / script)]


def launchd_plist(sched: _sched.Schedule, job: str = "daily") -> bytes:
    if job == "intraday":
        iv = sched.intraday
        # already host-local: the intraday window is expressed in wall-clock
        # hours on the machine that runs it, not in the declared zone
        intervals = [{"Weekday": _DAY_NUM[d], "Hour": h, "Minute": 0}
                     for d in iv.days if d in _DAY_NUM for h in iv.hours()]
        log = repo_root() / "logs" / "regagg_news.log"
        label = LABEL_INTRADAY
    else:
        tl = local_time_for(sched)
        intervals = [{"Weekday": _DAY_NUM[d], "Hour": tl["local_hour"],
                      "Minute": tl["local_minute"]}
                     for d in sched.days if d in _DAY_NUM]
        log = repo_root() / "logs" / "regagg_scheduled.log"
        label = LABEL
    return plistlib.dumps({
        "Label": label,
        "ProgramArguments": _command(job),
        "WorkingDirectory": str(repo_root()),
        "StartCalendarInterval": intervals,
        "StandardOutPath": str(log),
        "StandardErrorPath": str(log),
        # a laptop asleep at 06:00 should still collect when it wakes
        "RunAtLoad": False,
        "EnvironmentVariables": {
            k: v for k, v in {
                "DEEPSEEK_API_KEY": os.getenv("DEEPSEEK_API_KEY", ""),
                "REGAGG_SECRET": os.getenv("REGAGG_SECRET", ""),
                "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY", ""),
            }.items() if v
        },
    })


def systemd_units(sched: _sched.Schedule, job: str = "daily") -> Dict[str, str]:
    if job == "intraday":
        iv = sched.intraday
        days = ",".join(_SYSTEMD_DAY[d] for d in iv.days if d in _SYSTEMD_DAY)
        hours = ",".join(f"{h:02d}" for h in iv.hours())
        log = repo_root() / "logs" / "regagg_news.log"
        return {
            f"{SYSTEMD_UNIT_INTRADAY}.service": f"""[Unit]
Description=riskGPT intraday news poll

[Service]
Type=oneshot
WorkingDirectory={repo_root()}
ExecStart={' '.join(_command('intraday'))}
StandardOutput=append:{log}
StandardError=append:{log}
""",
            f"{SYSTEMD_UNIT_INTRADAY}.timer": f"""[Unit]
Description=riskGPT intraday news poll (every {iv.every_hours}h, {iv.start}-{iv.end})

[Timer]
OnCalendar={days} {hours}:00:00
Persistent=false

[Install]
WantedBy=timers.target
""",
        }
    tl = local_time_for(sched)
    days = ",".join(_SYSTEMD_DAY[d] for d in sched.days if d in _SYSTEMD_DAY)
    log = repo_root() / "logs" / "regagg_scheduled.log"
    service = f"""[Unit]
Description=riskGPT daily collection

[Service]
Type=oneshot
WorkingDirectory={repo_root()}
ExecStart={' '.join(_command())}
StandardOutput=append:{log}
StandardError=append:{log}
"""
    timer = f"""[Unit]
Description=riskGPT daily collection ({tl['declared']})

[Timer]
OnCalendar={days} {tl['local']:s}:00
Persistent=true

[Install]
WantedBy=timers.target
"""
    return {f"{SYSTEMD_UNIT}.service": service, f"{SYSTEMD_UNIT}.timer": timer}


# ── paths ───────────────────────────────────────────────────────────────────

def _label(job: str) -> str:
    return LABEL_INTRADAY if job == "intraday" else LABEL


def _unit_name(job: str) -> str:
    return SYSTEMD_UNIT_INTRADAY if job == "intraday" else SYSTEMD_UNIT


def _plist_path(job: str = "daily") -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{_label(job)}.plist"


def _systemd_dir() -> Path:
    return Path.home() / ".config" / "systemd" / "user"


# ── status ──────────────────────────────────────────────────────────────────

def status_for(job: str = "daily") -> Dict:
    """Ask the operating system, not a flag in our own database."""
    sched = _sched.get_schedule()
    kind = detect()
    declared_on = sched.enabled if job == "daily" else sched.intraday.enabled
    out: Dict = {
        "job": job, "declared_enabled": declared_on,
        "platform": kind,
        "declared": sched.describe(),
        "timing": local_time_for(sched) if sched.enabled else None,
        "installed": False, "loaded": False, "unit_path": None,
        "next_fire": None, "detail": "",
    }
    if kind is None:
        out["detail"] = ("no user-level scheduler on this host "
                         "(neither launchctl nor systemctl)")
        return out

    if kind == "launchd":
        p = _plist_path(job)
        out["unit_path"] = str(p)
        out["installed"] = p.exists()
        if out["installed"]:
            r = subprocess.run(["launchctl", "list"], capture_output=True, text=True)
            out["loaded"] = _label(job) in (r.stdout or "")
            out["detail"] = ("installed and loaded" if out["loaded"]
                             else "the file is there but launchd has not loaded it")
        else:
            out["detail"] = "not installed on this host"
        return out

    d, unit = _systemd_dir(), _unit_name(job)
    out["unit_path"] = str(d / f"{unit}.timer")
    out["installed"] = (d / f"{unit}.timer").exists()
    if out["installed"]:
        r = subprocess.run(["systemctl", "--user", "is-active",
                            f"{unit}.timer"], capture_output=True, text=True)
        out["loaded"] = (r.stdout or "").strip() == "active"
        nx = subprocess.run(["systemctl", "--user", "list-timers", "--no-pager",
                             f"{unit}.timer"], capture_output=True, text=True)
        out["next_fire"] = (nx.stdout or "").strip().splitlines()[1:2] or None
        out["detail"] = "installed and active" if out["loaded"] else \
                        "installed but the timer is not active"
    else:
        out["detail"] = "not installed on this host"
    return out


# ── install / uninstall ─────────────────────────────────────────────────────

def status() -> Dict:
    """Both jobs, so the page can show them side by side."""
    return {"jobs": {j: status_for(j) for j in JOBS}, "platform": detect()}


def install(job: str = "daily") -> Dict:
    """Write the unit and load it. Idempotent: reinstalling replaces."""
    sched = _sched.get_schedule()
    on = sched.enabled if job == "daily" else sched.intraday.enabled
    if not on:
        return {"ok": False, "job": job,
                "detail": f"the {job} schedule is disabled in "
                          "config/regagg_schedule.yaml — nothing to install"}
    kind = detect()
    if kind is None:
        return {"ok": False, "detail": "no user-level scheduler on this host"}

    (repo_root() / "logs").mkdir(exist_ok=True)
    tl = local_time_for(sched)

    if kind == "launchd":
        p = _plist_path(job)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(launchd_plist(sched, job))
        subprocess.run(["launchctl", "unload", str(p)],
                       capture_output=True, text=True)      # replace cleanly
        r = subprocess.run(["launchctl", "load", str(p)],
                           capture_output=True, text=True)
        ok = r.returncode == 0
        return {"ok": ok, "platform": kind, "job": job,
                "unit_path": str(p), "timing": tl,
                "detail": (f"installed — fires {tl['local']} local on "
                           f"{', '.join(sched.days)}" if ok
                           else (r.stderr or "launchctl load failed").strip()[:200])}

    d = _systemd_dir()
    d.mkdir(parents=True, exist_ok=True)
    for name, body in systemd_units(sched, job).items():
        (d / name).write_text(body)
    subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True)
    unit = _unit_name(job)
    r = subprocess.run(["systemctl", "--user", "enable", "--now",
                        f"{unit}.timer"], capture_output=True, text=True)
    ok = r.returncode == 0
    return {"ok": ok, "platform": kind, "job": job,
            "unit_path": str(d / f"{unit}.timer"),
            "timing": tl,
            "detail": (f"installed — fires {tl['local']} local on "
                       f"{', '.join(sched.days)}" if ok
                       else (r.stderr or "systemctl enable failed").strip()[:200])}


def uninstall(job: str = "daily") -> Dict:
    kind = detect()
    if kind == "launchd":
        p = _plist_path(job)
        if not p.exists():
            return {"ok": True, "detail": "was not installed"}
        subprocess.run(["launchctl", "unload", str(p)], capture_output=True)
        p.unlink()
        return {"ok": True, "detail": "removed"}
    if kind == "systemd":
        d, unit = _systemd_dir(), _unit_name(job)
        subprocess.run(["systemctl", "--user", "disable", "--now",
                        f"{unit}.timer"], capture_output=True)
        for name in (f"{unit}.timer", f"{unit}.service"):
            (d / name).unlink(missing_ok=True)
        subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True)
        return {"ok": True, "detail": "removed"}
    return {"ok": False, "detail": "no user-level scheduler on this host"}
