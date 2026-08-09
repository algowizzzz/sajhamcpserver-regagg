# 08 — Known Issues, War Stories, Roadmap

## Open issues, honestly ranked

| # | Issue | State / path |
|---|---|---|
| 1 | **74% of documents have no publication date** (5,219 of 7,018; 5,120 regulatory) | The single biggest limitation. Any "what changed in the last N days" question silently misses them, and the assistant says so unprompted. Fix: extract dates from document bodies during a backfill pass |
| 2 | **85% have no extraction** (5,969 of 7,018) | No entities, no event type → invisible to entity lookup and to persona watchlists. Fix: `scripts/regagg_extract_backfill.py` over the corpus |
| 3 | **87% of runs have `finished_at < started_at`** (110 of 127) | The poller stamps one batch finish before the per-source starts, so duration is unusable and a slowing collection gives no warning. Fix: stamp per source on completion |
| 4 | 6 runs report `ingested + archived > fetched` | Counters contradict; surfaced on Health rather than hidden |
| 5 | **FederalRegister.gov bot-gates its web host** | Mitigated: API abstracts (64) + metadata stubs (436), `content_source` flagged. Proper fix: GPO govinfo.gov bulk data |
| 6 | **amf_qc 403 bot-block** | 0 docs. Do **not** evade. Path: official contact for IP whitelisting, or a licensed feed |
| 7 | Depth on giant sites (osc ~29k, csa ~6k) | By design: 500/day slices accrue, `--deep` weekly |
| 8 | 6 scanned PDFs have no text layer | Owner decided no OCR (97% extract fine via pypdf) |
| 9 | 10 sources spell out their jurisdiction (`Canada` vs `CA`) | Harmless today — news is grouped by category before jurisdiction is read — but the column feeds region rollups, so it is one refactor from mattering |
| 10 | MAS thin (JS-heavy) | Candidate for a Playwright fetch path; spec'd, unbuilt |
| 11 | SAJHA app ships default credentials; server is localhost-only | **Harden before any non-local exposure** |
| 12 | `reg_trigger_run` gives agents run-start power | Deliberate. Disable the config or scope keys if agents must be read-only |
| 13 | `w-riskgpt` has `reg_trigger_run` enabled | The in-app chat does not (it gets the 10 read-only `corpus_*` tools), but the registered worker does. Drop it from `enabled_tools` if that is not wanted |
| 14 | 31 orphaned tool implementations in `sajha/tools/impl/` | No config → not registered, so they are inert. **Not deleted**: `tools_registry.py` imports `wikipedia_tool` and `yahoo_finance_tool` directly, and the studio imports `sharepoint_tool` |

## War stories — bugs that shaped the code. Do not regress them.

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

## Roadmap, in the order I would do it

1. **Backfill publication dates and extraction** (issues 1–2). Everything
   downstream — "what's new", entity lookup, persona matching — is limited by
   these two, and both are one script away.
2. **Fix run timestamps** (issue 3) so duration becomes a usable signal.
3. **Email digest.** Designed but deliberately unbuilt — see the connectivity
   requirements at the end of this file.
4. **Wire a real `TAVILY_API_KEY`** and re-run the entity sweep so the table
   leaves demo mode.
5. **Move the schedule to cloud scheduling** with a concurrency guard, and keep
   `regagg_schedule.yaml` in step.
6. **Harden auth** before any non-local exposure (issue 11).
7. Playwright fetch path for JS-heavy sources (issue 10).

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
