"""Collection and Health — the claims a maintainer would act on.

These pages exist to be trusted at a glance, which makes a plausible-but-wrong
number worse than a blank. Each test below pins a way the pages could mislead
someone who is accountable for the data being current.
"""

from __future__ import annotations

import datetime as _dt

import pytest

from sajha.regagg import collection as C
from sajha.regagg import health as H
from sajha.regagg import schedule as S
from sajha.regagg.models import Run

FRI = _dt.date(2026, 8, 7)
SAT = _dt.date(2026, 8, 8)


def _now(day: str, hh: int = 12) -> _dt.datetime:
    return _dt.datetime.combine(_dt.date.fromisoformat(day), _dt.time(hh),
                                tzinfo=_dt.timezone.utc)


@pytest.fixture()
def wired(session, storage, seed_regulator):
    """Two regulators and two wires, so category behaviour is observable."""
    seed_regulator("osfi", "CA", "sitemap_diff")
    seed_regulator("fintrac", "CA", "sitemap_diff")
    seed_regulator("wsj", "US", "sitemap_diff")
    seed_regulator("nikkei", "JP", "sitemap_diff")
    from sajha.regagg.models import Regulator
    for rid in ("wsj", "nikkei"):
        r = session.get(Regulator, rid)
        r.category = "news"
        r.staleness_alert_days = 3
    session.commit()
    from sajha.regagg import runtime
    runtime.set_providers(session=lambda: session, storage=lambda: storage)
    yield session
    runtime.set_providers(session=lambda: None)


def _run(session, rid, day, *, status="success", detected=10, fetched=10,
         ingested=5, archived=0, errors=0):
    session.add(Run(run_id=f"{rid}-{day}-{status}-{ingested}", regulator_id=rid,
                    logical_date=_dt.date.fromisoformat(day), trigger="schedule",
                    status=status, detected=detected, fetched=fetched,
                    ingested=ingested, archived=archived, errors=errors,
                    started_at=_now(day, 6), finished_at=_now(day, 7)))
    session.commit()


# ── the coverage matrix ─────────────────────────────────────────────────────

def test_a_weekend_cell_is_not_a_failure(wired):
    m = C.coverage_matrix(wired, days=2, now=_now("2026-08-08"))
    sat = [c for c in m["rows"][0]["cells"] if c["date"] == "2026-08-08"][0]
    assert sat["state"] == S.NOT_SCHEDULED
    assert sat["expected"] is False


def test_a_category_that_did_not_run_is_missed_even_when_the_other_did(wired):
    """The bug that made reliability report zero missed runs.

    News collecting on Friday must not make it look like regulatory did too.
    """
    _run(wired, "wsj", "2026-08-07")
    _run(wired, "nikkei", "2026-08-07")
    m = C.coverage_matrix(wired, days=1, now=_now("2026-08-07", 20))
    by = {r["key"]: r["cells"][0] for r in m["rows"]}
    assert by["news"]["state"] in (S.COMPLETE, S.PARTIAL)
    assert by["regulatory"]["state"] == S.MISSED


def test_a_cell_names_who_is_missing(wired):
    _run(wired, "osfi", "2026-08-07")
    m = C.coverage_matrix(wired, days=1, now=_now("2026-08-07", 20))
    reg = [r for r in m["rows"] if r["key"] == "regulatory"][0]["cells"][0]
    assert reg["missing"] == ["fintrac"]


def test_a_rerun_clears_an_earlier_failure_for_the_same_day(wired):
    """Otherwise a source stays red all day after you have already fixed it."""
    _run(wired, "osfi", "2026-08-07", status="failed", errors=3, ingested=0)
    _run(wired, "osfi", "2026-08-07", status="success", ingested=7)
    m = C.coverage_matrix(wired, days=1, now=_now("2026-08-07", 20))
    reg = [r for r in m["rows"] if r["key"] == "regulatory"][0]["cells"][0]
    assert reg["failed"] == 0


# ── the today bar ───────────────────────────────────────────────────────────

def test_the_bar_never_claims_complete_over_a_partial_day(wired):
    """25 of 55 sources is not a completed collection, whatever the label says."""
    _run(wired, "wsj", "2026-08-07")
    bar = C.today_bar(wired, now=_now("2026-08-08"))
    assert "last_complete" not in bar
    la = bar["last_activity"]
    assert la["sources"] == 1 and la["total"] == 4


def test_duration_is_omitted_rather_than_wrong(wired):
    """87% of real runs finish before they start; a 0s duration reads as speed."""
    wired.add(Run(run_id="bad", regulator_id="osfi", logical_date=FRI,
                  trigger="schedule", status="success", detected=1, fetched=1,
                  ingested=1, archived=0, errors=0,
                  started_at=_now("2026-08-07", 7),
                  finished_at=_now("2026-08-07", 6)))
    wired.commit()
    assert C.today_bar(wired, now=_now("2026-08-08"))["last_activity"]["duration_s"] is None


def test_the_bar_reports_each_category_separately(wired):
    _run(wired, "wsj", "2026-08-07")
    cats = {c["key"]: c for c in C.today_bar(wired, now=_now("2026-08-08"))["by_category"]}
    assert cats["news"]["days_ago"] == 1
    assert cats["regulatory"]["last_run"] is None


# ── rerun candidates ────────────────────────────────────────────────────────

def test_a_source_that_succeeds_but_returns_nothing_is_flagged(wired):
    """The failure that looks like health — green runs, ageing data."""
    for day in ("2026-08-05", "2026-08-06", "2026-08-07"):
        _run(wired, "osfi", day, status="success", ingested=0, archived=0)
    rows = {r["regulator_id"]: r for r in C.candidates(wired, now=_now("2026-08-07", 20))["sources"]}
    assert rows["osfi"]["bucket"] == "silent"


def test_never_run_is_its_own_bucket_not_stale(wired):
    rows = {r["regulator_id"]: r for r in C.candidates(wired, now=_now("2026-08-08"))["sources"]}
    assert rows["fintrac"]["bucket"] == "never"
    assert rows["fintrac"]["days_stale"] is None


def test_consecutive_failures_are_counted(wired):
    _run(wired, "osfi", "2026-08-06", status="failed", errors=2, ingested=0)
    _run(wired, "osfi", "2026-08-07", status="failed", errors=1, ingested=0)
    rows = {r["regulator_id"]: r for r in C.candidates(wired, now=_now("2026-08-07", 20))["sources"]}
    assert rows["osfi"]["bucket"] == "failed"
    assert rows["osfi"]["fail_streak"] == 2


def test_each_category_is_judged_against_its_own_window(wired):
    """A wire silent 5 days is broken; a regulator silent 5 days is Tuesday."""
    _run(wired, "osfi", "2026-08-02")
    _run(wired, "wsj", "2026-08-02")
    rows = {r["regulator_id"]: r for r in C.candidates(wired, now=_now("2026-08-08"))["sources"]}
    assert rows["osfi"]["window_days"] == 14 and rows["osfi"]["bucket"] == "ok"
    assert rows["wsj"]["window_days"] == 3 and rows["wsj"]["bucket"] == "stale"


# ── health ──────────────────────────────────────────────────────────────────

def test_reliability_and_the_matrix_cannot_disagree(wired):
    """They read the same state machine, so a day is missed in both or neither."""
    _run(wired, "wsj", "2026-08-07")
    _run(wired, "nikkei", "2026-08-07")
    rel = H.reliability(wired, now=_now("2026-08-07", 20))
    by_cat = {c["key"]: c for c in rel["by_category"]}
    assert "2026-08-07" in by_cat["regulatory"]["missed"]
    assert "2026-08-07" not in by_cat["news"]["missed"]

    m = C.coverage_matrix(wired, days=1, now=_now("2026-08-07", 20))
    cells = {r["key"]: r["cells"][0]["state"] for r in m["rows"]}
    assert (cells["regulatory"] == S.MISSED) is ("2026-08-07" in by_cat["regulatory"]["missed"])


def test_nothing_is_late_before_the_first_run_ever_recorded(wired):
    """Without a floor, every weekday of prehistory reports as a missed run."""
    _run(wired, "osfi", "2026-08-07")
    rel = H.reliability(wired, days=365, now=_now("2026-08-07", 20))
    assert rel["since"] == "2026-08-07"
    assert rel["expected_days"] == 1


def test_the_funnel_reports_what_holds_and_does_not_invent_an_identity(wired):
    """detected/fetched/ingested are event counters, not a partition."""
    _run(wired, "osfi", "2026-08-07", detected=100, fetched=80, ingested=50,
         archived=40, errors=5)
    f = H.funnel(wired, day=FRI, now=_now("2026-08-07", 20))
    assert f["holds"]["fetched_le_detected"] is True
    assert f["not_fetched"] == 20
    assert f["unchanged"] == 0            # clamped, never negative
    # ingested + archived exceeds fetched here, and that is LEGITIMATE: one
    # document can be created and have a version archived in the same run.
    # Flagging it manufactured a defect and sent someone to reconcile clean data.
    assert f["inconsistent_count"] == 0


def test_only_a_real_impossibility_is_flagged(wired):
    """You cannot fetch more than you detected. That one is a genuine defect."""
    _run(wired, "osfi", "2026-08-07", detected=10, fetched=99, ingested=1)
    f = H.funnel(wired, day=FRI, now=_now("2026-08-07", 20))
    assert f["inconsistent_count"] == 1
    assert "fetched exceeds detected" in f["inconsistent_runs"][0]["why"]


def test_quality_percentages_use_the_right_population(wired):
    """A run-level defect divided by the document count reads as ~nothing."""
    q = H.quality(wired)
    by = {c["key"]: c for c in q["checks"]}
    assert by["run_timestamps_inverted"]["of"] == by["run_timestamps_inverted"].get("of")
    assert by["no_published_date"]["of"] == q["documents"]
    assert by["jurisdiction_vocabulary"]["of"] == 4      # sources, not documents


def test_every_quality_check_says_what_it_breaks(wired):
    """A count with no consequence attached gets scrolled past."""
    for c in H.quality(wired)["checks"]:
        assert c["breaks"], f"{c['key']} has no stated consequence"


def test_the_verdict_is_healthy_only_when_nothing_is_outstanding(wired):
    _run(wired, "osfi", "2026-08-07")
    _run(wired, "fintrac", "2026-08-07")
    _run(wired, "wsj", "2026-08-07")
    _run(wired, "nikkei", "2026-08-07")
    v = H.overview(wired, now=_now("2026-08-07", 20))["verdict"]
    assert v["level"] in ("healthy", "watch", "degraded")
    if v["level"] == "healthy":
        assert not v["points"]


# ── run status: nothing new is not a failure ────────────────────────────────

def _manifest(**kw):
    from sajha.regagg.events import RunManifest
    base = dict(run_id="r", regulator_id="x", logical_date="2026-08-09",
                trigger="rerun")
    base.update(kw)
    return RunManifest(**base).finalize()


def test_finding_nothing_new_is_not_a_failure_just_because_a_link_was_dead():
    """fintrac fetched 198 documents, found nothing new — correct, it had
    ingested them an hour earlier — and went RED over two 404s in 889 URLs.
    'Nothing changed today' is the most common healthy outcome there is."""
    m = _manifest(detected=889, fetched=198, ingested=0, errors=2)
    assert m.status == "success_empty"


def test_one_unreachable_pdf_does_not_fail_a_run(  ):
    """hkma: 17 detected, one PDF on a different host unreachable."""
    assert _manifest(detected=17, fetched=16, ingested=0, errors=1).status == "success_empty"


def test_a_systemically_throttled_run_still_fails():
    """finra: 141 HTTP 429s out of 369 detected. 38% is a real fault."""
    m = _manifest(detected=369, fetched=61, ingested=15, errors=142)
    assert m.status == "failed"


def test_a_run_that_fetched_nothing_at_all_fails():
    assert _manifest(detected=50, fetched=0, ingested=0, errors=50).status == "failed"


def test_detecting_things_and_fetching_none_of_them_is_fine_without_errors():
    """The lastmod fast path: everything was already held, so nothing was
    re-fetched. That must not read as a collapsed fetch."""
    assert _manifest(detected=100, fetched=0, ingested=0, errors=0).status == "success_empty"


def test_documents_landing_is_success_even_with_scattered_errors():
    assert _manifest(detected=100, fetched=90, ingested=40, errors=10).status == "success"


# ── orphaned runs ───────────────────────────────────────────────────────────

def test_a_killed_run_is_closed_rather_than_running_forever(session, seed_regulator,
                                                            monkeypatch):
    """A row is written as `running` before the work starts. Kill the process
    and nothing ever closes it — osc showed as in flight for good."""
    import datetime as dt
    from sajha.regagg import collection as C
    from sajha.regagg.models import Run

    monkeypatch.setattr(C.subprocess, "run", lambda *a, **k: type("R", (), {"stdout": ""})())
    seed_regulator("osc", "CA", "sitemap_diff")
    session.add(Run(run_id="stuck", regulator_id="osc", logical_date=dt.date(2026, 8, 9),
                    trigger="rerun", status="running",
                    started_at=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None) - dt.timedelta(hours=4)))
    session.commit()

    assert C.reap_orphaned_runs(session) == ["stuck"]
    row = session.get(Run, "stuck")
    assert row.status == "failed"
    # we do not know when it died; claiming a zero-second run would be a lie
    assert row.finished_at is None


def test_a_run_still_inside_its_grace_period_is_left_alone(session, seed_regulator,
                                                           monkeypatch):
    import datetime as dt
    from sajha.regagg import collection as C
    from sajha.regagg.models import Run

    monkeypatch.setattr(C.subprocess, "run", lambda *a, **k: type("R", (), {"stdout": ""})())
    seed_regulator("osc", "CA", "sitemap_diff")
    session.add(Run(run_id="young", regulator_id="osc", logical_date=dt.date(2026, 8, 9),
                    trigger="rerun", status="running",
                    started_at=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None) - dt.timedelta(minutes=5)))
    session.commit()
    assert C.reap_orphaned_runs(session) == []
    assert session.get(Run, "young").status == "running"


def test_a_live_ingest_process_stops_the_sweep_entirely(session, seed_regulator,
                                                        monkeypatch):
    """A genuinely long run must never be cut off mid-flight."""
    import datetime as dt
    from sajha.regagg import collection as C
    from sajha.regagg.models import Run

    monkeypatch.setattr(C.subprocess, "run",
                        lambda *a, **k: type("R", (), {"stdout": "4242\n"})())
    seed_regulator("osc", "CA", "sitemap_diff")
    session.add(Run(run_id="long", regulator_id="osc", logical_date=dt.date(2026, 8, 9),
                    trigger="rerun", status="running",
                    started_at=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None) - dt.timedelta(hours=9)))
    session.commit()
    assert C.reap_orphaned_runs(session) == []
    assert session.get(Run, "long").status == "running"


# ── a scattered error is not a failed run ───────────────────────────────────

def test_a_successful_run_with_a_dead_link_is_not_a_failure(wired):
    """Found live. `_is_failed` was `status == 'failed' OR errors > 0`, so a
    single 404 on the regulator's side made a green run count as red.

    iosco and nydfs had NO failed run in their entire history and both sat in
    the Failed bucket with a "consecutive failures" streak, because every run
    carried one dead link.
    """
    for day in ("2026-08-05", "2026-08-06", "2026-08-07"):
        _run(wired, "osfi", day, status="success", ingested=9, errors=1)
    rows = {r["regulator_id"]: r
            for r in C.candidates(wired, now=_now("2026-08-07", 20))["sources"]}
    assert rows["osfi"]["bucket"] == "ok"
    assert rows["osfi"]["fail_streak"] == 0
    assert rows["osfi"]["last_clean"] == "2026-08-07"


def test_the_streak_counts_failed_runs_not_imperfect_ones(wired):
    _run(wired, "osfi", "2026-08-05", status="success", ingested=5, errors=7)
    _run(wired, "osfi", "2026-08-06", status="failed", ingested=0, errors=9)
    _run(wired, "osfi", "2026-08-07", status="failed", ingested=0, errors=9)
    rows = {r["regulator_id"]: r
            for r in C.candidates(wired, now=_now("2026-08-07", 20))["sources"]}
    assert rows["osfi"]["fail_streak"] == 2          # not 3


def test_the_matrix_does_not_paint_a_cell_red_for_a_dead_link(wired):
    _run(wired, "osfi", "2026-08-07", status="success", ingested=4, errors=2)
    _run(wired, "fintrac", "2026-08-07", status="success", ingested=4, errors=0)
    m = C.coverage_matrix(wired, days=1, now=_now("2026-08-07", 20))
    reg = [r for r in m["rows"] if r["key"] == "regulatory"][0]["cells"][0]
    assert reg["failed"] == 0


def test_the_run_pass_rate_measures_passes_not_perfection(wired):
    """The Health headline read 83%. It was counting runs with zero errors —
    a different quantity wearing the same label."""
    for day in ("2026-08-05", "2026-08-06", "2026-08-07"):
        _run(wired, "osfi", day, status="success", ingested=3, errors=4)
    rel = H.reliability(wired, now=_now("2026-08-07", 20))
    assert rel["pass_rate"] == 100.0
