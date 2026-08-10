# 08 — Known Issues, War Stories, Roadmap

## Open issues, honestly ranked

| # | Issue | State / path |
|---|---|---|
| 1 | ~~74% of documents have no publication date~~ | **Improved 2026-08-09: 26% → 65% dated.** `scripts/regagg_backfill_dates.py` recovered 2,747 of 5,219 (932 from URL paths, 1,815 from document text), each tagged `date:url` or `date:text` so an inferred date is distinguishable from a collected one. The remaining 2,472 carry no date anywhere we hold |
| 2 | ~~85% have no extraction~~ | **Fixed 2026-08-09: 15% → 100%.** All 7,353 documents extracted; 1,306 now name a watchlist company, up from 464. The first pass lost its work to a SQLite lock held by a concurrent collection run — the script batches its commits and retries a lock now |
| 3 | ~~87% of runs finish before they start~~ | **Fixed 2026-08-09.** `pipeline.run_regulator` stamped `finished_at` from the caller's fleet-wide `now`; it now records the real completion moment. Historic rows keep the bad values — duration is reported only for runs collected after the fix |
| 4 | ~~6 runs with contradictory counters~~ | **Resolved 2026-08-09 — the check was wrong, not the data.** `ingested` and `archived` are event counters and one document can be created and have a version archived in the same run. All six were legitimate. Health now flags only the real impossibility, `fetched > detected` |
| 5 | **FederalRegister.gov bot-gates its web host** | Mitigated: API abstracts (64) + metadata stubs (436), `content_source` flagged. Proper fix: GPO govinfo.gov bulk data |
| 6 | **amf_qc 403 bot-block** | 0 docs. Do **not** evade. Path: official contact for IP whitelisting, or a licensed feed |
| 7 | Depth on giant sites (osc ~29k, csa ~6k) | By design: 500/day slices accrue, `--deep` weekly |
| 8 | 6 scanned PDFs have no text layer | Owner decided no OCR (97% extract fine via pypdf) |
| 9 | 10 sources spell out their jurisdiction (`Canada` vs `CA`) | Harmless today — news is grouped by category before jurisdiction is read — but the column feeds region rollups, so it is one refactor from mattering |
| 10 | MAS thin (JS-heavy) | Candidate for a Playwright fetch path; spec'd, unbuilt |
| 11 | **Server binds `0.0.0.0` with the shipped admin account present** | Verified 2026-08-09; the KB previously claimed localhost-only and was wrong. Surfaced on Health as a high-severity check. Bind to 127.0.0.1, change the password, add TLS |
| 12 | `reg_trigger_run` gives agents run-start power | Deliberate. Disable the config or scope keys if agents must be read-only |
| 13 | `w-riskgpt` has `reg_trigger_run` enabled | The in-app chat does not (it gets the 10 read-only `corpus_*` tools), but the registered worker does. Drop it from `enabled_tools` if that is not wanted |
| 14 | 31 orphaned tool implementations in `sajha/tools/impl/` | No config → not registered, so they are inert. **Not deleted**: `tools_registry.py` imports `wikipedia_tool` and `yahoo_finance_tool` directly, and the studio imports `sharepoint_tool` |
| 15 | **A rerun for a past date silently collects today** | `spawn_ingest` accepts `logical_date` and drops it — `regagg_ingest_live.py` has no `--date` and calls `date.today()`. So the coverage matrix's "▶ Run these N" for a missed day writes rows dated today and the gap stays open. Fix: add `--date` and thread it through |
| 16 | **One source rerun costs a whole-corpus enrichment sweep** | `regagg_ingest_live.py` ends with `for doc in session.query(Document).all()`, so a single-source rerun took ~6 minutes against 7.4k documents. This is *why* the queue coalesces instead of spawning per source. Fix: scope the sweep to the sources in the run |
| 17 | Rerun from the UI is uncapped | The Health page's Rerun sends no `max_docs`, so a giant source (osc ~29k detected) can hold the queue for 30+ minutes. The Collection page has a cap field; the Health button should default to one |

## War stories — bugs that shaped the code. Do not regress them.

**0. Nine Rerun clicks, one run, nine "started" messages.** `spawn_ingest`
refuses a second concurrent fleet (SQLite has one writer) and returns
`{"started": false, "reason": ...}`. `/rerun` handed that straight back as
`{"queued": result}`, and the dashboard tested `d.queued === false` — against a
*dict*, which is never `=== false`. So eight of nine clicks were dropped and
all nine reported success. The refusal was correct at every layer except the
one an operator could see. A second copy of the bug lived in `runScope`, which
toasted "Run queued" on `r.ok` alone — the HTTP status, 200 for a refusal too.

Fixed by `sajha/regagg/runqueue.py`: a click now **joins a queue** and each
source carries `queued → running → done/failed`, polled from `/rerun/queue` and
drawn on the button itself. Pending ids are **coalesced into one batch** rather
than run as N processes — `regagg_ingest_live.py` ends with an enrichment sweep
over the whole corpus, so eight processes would mean eight sweeps contending
for one writer (see story 12). Outcomes are read back out of `reg_runs`, so a
source the runner never recorded is failed, not assumed done.

*The lesson, which is story 3 wearing different clothes:* the guard was right,
the server was honest, and the operator still could not see it. A refusal that
cannot reach the screen is indistinguishable from no refusal at all.

**1. Entity matching was 68% recall with a false positive.**
"Meta", "Uber", "AMD", "JP Morgan" silently missed; "Apple Hospitality REIT"
matched "Apple Inc.". Rewritten as three-tier confidence. Ambiguity is now a
first-class outcome rather than a coin flip.

**2. The fix was 80× too slow.** The suite went from 4s to 5.5 minutes because
the matcher scanned the whole watchlist twice per lookup — 12,000 comparisons
per story against 6,000 names. Candidate indexes fixed it. It had also been
misdiagnosed as UI test flakiness.

**3. A stray `</div>` closed `.page` early.** Two sections rendered on *all
four* tabs — ~1,400px of phantom scroll. Every element existed and every
endpoint answered, so no functional test noticed. `test_dashboard_markup.py`
now asserts balance and view containment directly.

**4. `el.className = ""` stripped `scrollbox`.** Clearing the `empty`
placeholder class also removed the layout class, so the change feed grew to
66,000px instead of scrolling in 340px.

**5. Capping every list at 340px trapped the content.** 16,238px of change feed
behind a letterbox on a page that would not itself scroll. Led to the
`mainlist` / `scrollbox` split and a test that walks all eleven views.

**6. The Health page claimed an identity the data does not support.**
"detected = ingested + deduped + cap-dropped + errors, checked every run by the
reconciler" — measured, it does not hold. The funnel now shows what was
measured and reports the contradictory runs.

**7. Reliability contradicted the coverage matrix on the same screen.** Pooling
both categories let the news wires mask regulatory sitting dark for three days.
Now computed per category, from the same state machine as the matrix.

**8. `corpus_changes` accepted a filter and ignored it.** The worker asked for
OSFI, got fedreg and news, and reconstructed the answer by hand. Led to
schema-driven argument validation across all 22 tools.

**9. Chat showed sources the answer did not use.** Built from every doc_id the
tools returned, then truncated — the model cited four documents and none were
in the twelve shown.

**10. A nested-quantifier regex backtracked catastrophically.** "Six words then
a full stop" hung on a 4,000-word paragraph. It would have hung a page render,
not just a test.

**11. `cp` of a live SQLite file produced a malformed database.** Two UI suites
running concurrently captured a torn page. Backups use the `.backup` API now.

**12. Thread-locals do not propagate into FastAPI's threadpool.** Sessions are
contextvar-scoped; the earlier version exhausted the connection pool.

**13. `doc_id` from a content hash breaks versioning** (a spec bug): a revision
became a new document. `doc_id` is derived from the URL.

**14. Filter in SQL before LIMIT.** Shipped once; there is a test.

**15. The declared schedule was never installed anywhere.** There was no
crontab and no launchd agent on the host at all — the runs labelled
`trigger=schedule` had been launched by hand, and the Health page was counting
missed runs against a promise no process was keeping. A declaration is not a
scheduler; `scheduler_install.py` now generates the job *from* the declaration
so they cannot disagree.

**16. launchd has no timezones.** `StartCalendarInterval` fires in host-local
time. The declared 06:00 America/Toronto on a Chicago machine would have run an
hour late, silently and forever. The time is converted at render, and the panel
states the conversion.

**17. Two writers, one SQLite file.** An extraction backfill and a collection
run at the same time: the run held the write lock, the backfill's single
end-of-pass commit failed with "database is locked", and ten minutes of paid
LLM calls were lost. The extraction had all succeeded — only the write died.
The script commits every 200 rows and retries a lock now.

**18. A check that manufactured a defect.** Health flagged six runs as having
"contradictory counters" because `ingested + archived > fetched`. All six were
legitimate: those are event counters, and one document can be created and have
a version archived in the same run. The check would have sent someone to
reconcile clean data. Only `fetched > detected` is a real impossibility.

**19. "Run all" on a lane page ran the whole fleet.** It sent `scope:"all"`
with no filter, so the Regulatory page's button re-polled all 25 news wires.
A control on a lane page reads as lane-scoped.

## Roadmap

**Done 2026-08-09** — the first three entries of the previous roadmap:
extraction 15% → 100%, publication dates 26% → 63%, run timestamps fixed at
source, and the scheduler installed from the UI on this host.

### Blocked on someone with credentials

| # | Item | What it needs |
|---|---|---|
| 1 | **Email digest** | Azure AD app registration with `Mail.Send` (application, admin-consented), sender mailbox, send time and timezone, recipients. **And `CLAUDE.md` amended** — it currently forbids the engine from sending email outright, which contradicts the intent |
| 2 | **Live entity table** | `TAVILY_API_KEY`. Until then the sweep produces labelled demo rows. ~$120/month at 500 names, basic depth |

### Buildable

| # | Item | Why |
|---|---|---|
| 3 | **Harden auth** (issue 11) | binds `0.0.0.0` with the shipped admin account — do this before the host is reachable from anywhere but a laptop |
| 4 | Cloud scheduling with a concurrency guard | the launchd/systemd job is per-host; keep `regagg_schedule.yaml` as the single declaration either way |
| 5 | Recover more publication dates | 2,702 documents still have none. The next tranche needs per-source rules, since the generic recogniser has taken what it safely can |
| 6 | Playwright fetch path (issue 10) | for JS-heavy sources like MAS |
| 7 | Untangle the 31 orphaned tool implementations (issue 14) | `tools_registry.py` and the studio import several directly |

### Operational, not code

- **Do not run two writers against SQLite.** A collection run holding the write
  lock cost the extraction backfill ten minutes of paid LLM calls before the
  script learned to commit in batches. Postgres removes the constraint.
- **Keep `config/regagg_schedule.yaml` and the installed job in step.** They
  cannot drift while the job is installed from the UI, because the unit is
  generated from the declaration — but a hand-edited crontab elsewhere can.

## The email digest — what it needs before it can be built

Nothing has been implemented. The blockers, in order:

**Outlook, one of two paths.** Microsoft Graph is the one a bank's security
team will accept: an Azure AD app registration with the `Mail.Send`
**application** permission (not delegated — nobody is logged in on a cron run),
admin-consented. Needs `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`,
`AZURE_CLIENT_SECRET`, and the sender mailbox. Outbound HTTPS to
`login.microsoftonline.com` and `graph.microsoft.com`; no inbound. SMTP via
`smtp.office365.com:587` works but needs SMTP AUTH per mailbox and a password,
and breaks under MFA — basic auth is being retired across Exchange Online.

**A separate schedule** from collection, so a collection outage does not
silently mean no email. Needs the send time, weekdays and timezone, and a
decision on whether a quiet day still sends. Recommendation: always send, with
the subject saying "nothing material" — a digest that only arrives on bad days
trains people to panic, and its absence is ambiguous.

**Recipients.** `reg_users` has an email but nothing that says "send me the
digest". Needs per-persona subscription with a real unsubscribe, and a decision
on whether desks share a distribution list.

**Content.** My Day as HTML — Outlook's renderer needs table-based layout and
inline styles, so it is a separate template, not the web page. Entity table as
`.xlsx` (analysts will pivot it); `openpyxl` is the dependency.

**Two safety requirements before the first live send:** a dry-run mode that
writes the rendered email to disk, and a hard allowlist of recipient domains. A
bug in a digest loop that mails 500 people is not recoverable by fixing the bug.

**And amend `CLAUDE.md` first.** It currently states the engine must *never*
send email or outreach. That rule was written for the SEO side but is stated
absolutely — the guardrail and the intent must not contradict each other.
