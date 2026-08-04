# 04 — Known Issues, War Stories, Roadmap

## Open issues (honest, prioritized)
| # | Issue | State / suggested path |
|---|---|---|
| 1 | **FederalRegister.gov bot-gates its whole web host** — full text unavailable from this IP | Mitigated: API abstracts (64 docs) + metadata stubs (436), `content_source` flagged in provenance; full text retried every daily run. **Proper fix: switch full-text source to GPO govinfo.gov bulk data (official, sanctioned, free) — see roadmap #1** |
| 2 | **amf_qc (AMF Québec) 403 bot-block** | 0 docs. Do NOT evade. Path: official contact for IP whitelisting, or a licensed data feed |
| 3 | Depth on giant sites (osc ~29k, csa ~6k, fincen slow) | By design: daily 500/doc slices accrue; `--deep` weekly. Watch coverage % on Coverage page |
| 4 | 6 scanned PDFs have no text layer (`ocr=true`) | Owner decided: no OCR (97% extract fine via pypdf). Revisit only if scanned volume grows |
| 5 | Excerpts are first-paragraph text, not summaries | By design until owner's LLM layer writes summary.md (swap is one line in queries_ui/_excerpt) |
| 6 | MAS thin (JS-heavy site) | Listing-based config verified but yields little; candidate for Playwright fetch (spec'd, unbuilt) |
| 7 | SAJHA app default creds admin/admin123; server localhost-only | MUST harden before any non-local exposure |
| 8 | reg_trigger_run gives agents run-start power | Deliberate; disable the tool config or scope keys if agents must be read-only |

## War stories (bugs that shaped the code — don't regress them)
1. **doc_id from content-hash breaks versioning** (spec bug): a revision became a
   *new* doc. Fix: identity = reference number → URL-hash; content hash is only
   the change signal. (`ids.stable_doc_id`)
2. **Filter-after-LIMIT**: institution-filtered Changes returned empty because
   newer rows crowded the fetch window. Filter in SQL first. (regression test)
3. **DB pool exhaustion**: one leaked session per API call + 5s polling = hung
   endpoints. Thread-scoped sessions in runtime.wire_from_app.
4. **PDF by extension is a lie**: .pdf URLs served HTML error pages → pypdf
   noise. Detect by %PDF magic bytes.
5. **Bot-block pages stored as content**: FederalRegister block notice became
   538 docs' "content". Guard: `_looks_bot_blocked` + API fallback chain.
6. **3.8MB sitemap hang** (HKMA): resolution ran 78min with zero output.
   Guards: 8MB byte cap + 30-child index cap, logged truncation.
7. **Anonymous tools/call**: fixing a None-session crash accidentally enabled
   unauthenticated execution; then key allowlists turned out never enforced on
   /mcp. Both closed in api_routes; keep the verification matrix in tests.
8. **Demo seed data polluting real corpus**: purge synthetic fixtures the
   moment real data arrives; never let them mix silently.

## Roadmap (highest-leverage next builds)
1. **govinfo.gov bulk-data connector for Federal Register full text** —
   replaces abstracts/stubs with sanctioned full text. New api provider
   adapter, ~a day.
2. **LLM enrichment activation** (owner's layer): fill summary.md, taxonomy
   topic tags, doc_type reclassification (corpus is 90% "announcement" —
   rule-based typing is URL-pattern-limited), date extraction → deadlines feed.
3. **Expected inventories beyond OSFI** (`config/regulators/_inventories/`):
   EBA RTS register, FCA handbook index, APRA standards list → provable
   completeness per regulator.
4. **Simple-mode overview page** for first-time users (see UX proposal in
   BUILD_LOG session notes): one hero strip + one plain table; move ops detail
   behind drill-ins.
5. **Playwright fetch path** for JS-heavy sites (MAS, some NYDFS pages) —
   spec'd in original TRD, config field `fetch: playwright` already parses.
6. **Postgres flip** when concurrency demands (DDL ready; engine switch in
   application.yml; pg_trgm improves reference resolution).
7. Weekly digest email/Teams webhook from reg_changes (spec FR-9 alerting).
