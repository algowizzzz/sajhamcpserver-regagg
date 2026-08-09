# 02 — Data, Storage and Schema

## Three stores, three jobs

| Store | Path | Role |
|---|---|---|
| Canonical | `data/web_aggregator/` | the truth: raw bytes, provenance, full version history |
| Projection | `data/markdown/` | agent-consumable mirror of **current only** |
| Index | `data/sajha.db` (`reg_*`) | what exists, what changed, what ran |

The projection is disposable — `projection.resync()` rebuilds it from
canonical. The index is rebuildable from canonical. Canonical is the only thing
you must back up and never lose.

## Canonical layout

```
data/web_aggregator/{source}/
  _state/run_manifests/{run_id}.json          # per-URL log of every run
  current/{doc_type}/{year}/{doc_id}/
    raw.html | raw.pdf                        # original bytes, immutable
    content.md                                # normalised markdown
    meta.json                                 # full provenance
    summary.md                                # LLM slot; often just the title
  archive/{doc_type}/{year}/{doc_id}/{version_ts}/
  staging/                                    # transient; reconcile cleans crashes
```

`meta.json` carries: `doc_id, title, reference_number, source_url, final_url,
fetch_method, content_source (api_abstract|metadata_stub when bot-gated),
content_hash (sha256), version_ts, version_n, ingested_at, run_id, ocr, tags`.

## Projection layout

```
data/markdown/web/{source}/{doc_type}/{doc_id}.md      # HTML-converted
data/markdown/policy/{source}/{doc_type}/{doc_id}.md   # PDF-converted
```

Every file carries YAML frontmatter: `title, regulator, doc_type, status,
source_kind, source_url, published, version`. Maintained write-through at
ingest plus a nightly `resync()` self-heal.

`corpus_index.py` builds its BM25/TF-IDF index from these files, keyed on file
count + newest mtime, so a poll that adds documents is picked up without a
restart. Roughly 4 seconds to index 7,353 documents.

## Database — 15 tables

SQLite in dev, Postgres on-prem. `JSONFlex = JSON().with_variant(JSONB,
"postgresql")` means the same model code runs on both. Postgres DDL lives in
`db/scripts/postgresql/003_regagg_schema.sql`.

### Collection

| Table | Rows | Role |
|---|---|---|
| `reg_regulators` | 55 | the source registry: jurisdiction, connector, `category`, `active`, `staleness_alert_days`, full parsed YAML in `config` |
| `reg_seen_urls` | 7,352 | change detection: url → hash, etag, lastmod, doc_id |
| `reg_documents` | 7,353 | exactly one current row per document |
| `reg_document_versions` | 7,974 | full history; invariant: exactly one `state='current'` per doc |
| `reg_document_tags` | 30,391 | tags with a `source` (config / rule / llm / manual) |
| `reg_document_edges` | 180 | citation graph: implements, supersedes, amends… |
| `reg_pending_edges` | 903 | citations that did not resolve yet; retried nightly |
| `reg_runs` | 157 | every run: counts, status, trigger, operator |
| `reg_watermarks` | 0 | API poller position (unused by current connectors) |

### People and pages

| Table | Rows | Role |
|---|---|---|
| `reg_users` | 3 | login, role |
| `reg_personas` | 12 | the whole persona contract in `config` (JSON) |
| `reg_persona_entities` | 79 | the watchlist, one row per name |
| `reg_persona_versions` | 31 | every saved version of a persona config |
| `reg_page_specs` | 18 | the cached daily page: spec + dossier + ledger |
| `reg_entity_scans` | 12 | one row per persona/day/entity for the entity table |

## Columns worth knowing

**`reg_runs`** — `detected, fetched, ingested, archived, errors`.

> These are **event counters, not a partition.** `fetched <= detected` and
> `errors <= detected` always hold, but `ingested + archived` can exceed
> `fetched` — a document can be created *and* have a version archived in one
> run — and `detected != fetched + errors`. Both are legitimate. Any code that
> presents them as a balancing identity is wrong; `health.funnel()` shows what
> was measured and flags only the real impossibility, `fetched > detected`.

Also: `finished_at < started_at` on runs collected before 2026-08-09 — the
poller stamped one batch finish before the per-source starts. Fixed at source;
`collection._duration_s()` still returns `None` rather than a wrong number for
the historic rows.

**`reg_runs.status`** — `failed` only when nothing landed or >20% errored.
Scattered per-URL errors (regulator-side 404s/429s) stay `success` with an
error count. `success_empty` means it ran and found nothing.

**`reg_documents.materiality_score` / `_band` / `_reason`** — deterministic,
and `_reason` is the audit trail (`final_rule x1.4 (major operating) = 56;
aml_cft +12; new +10`). Every ranked view sorts on this.

**`reg_entity_scans.status`** — `ok | none | error | skipped`. Four different
facts, never a blank cell. `mode` is `live | demo`.

**`reg_personas.config`** — the whole contract in one document:

```json
{
  "scope":        {"sectors": [], "topics": [], "classes": [],
                   "rule_families": ["osfi-car", "b-13"], "regions": []},
  "salience":     {"topic_weights": {"credit": 60}, "serious_threshold": 50},
  "presentation": {"layout": "auto", "max_items": 20},
  "table":        {"columns": "<YAML or JSON text, verbatim as authored>"}
}
```

`table.columns` is stored **verbatim** rather than parsed, so the author's own
YAML and comments come back exactly as written.

## Migrations

There is no Alembic for `reg_*`. `Base.metadata.create_all()` creates missing
tables and `scripts/regagg_migrate.py` adds missing columns:

```bash
./.venv/bin/python -m scripts.regagg_migrate
```

**Run this after any model change, and on the server after every deploy.**
`reg_entity_scans` was added this way; forgetting it produces
`no such table: reg_entity_scans` at request time, not at startup.

## Known data-quality state

Measured 2026-08-09. Surfaced on the Health page, not hidden here.

Backfilled 2026-08-09; the first two were the largest limitations in the system.

| Defect | Count | What it breaks |
|---|---|---|
| documents with no `published_date` | 2,702 of 7,353 (37%) — **was 74%** | any "what changed in the last N days" question misses them. The rest carry no date anywhere we hold |
| documents with no `extraction` | 0 of 7,353 — **was 85%** | resolved; 1,306 documents now name a watchlist company, up from 464 |
| runs with `finished_at < started_at` | 110 of 157 — **was 87%** | historic rows only; fixed at source, so every new run has a usable duration |
| sources with a spelled-out jurisdiction | 10 of 55 | harmless today (news is grouped by category first) but the column feeds region rollups |
| orphaned versions / untitled docs / missing hashes | 0 | — |

The first two are the highest-value backfills available and are the reason the
assistant often says "the corpus does not carry publication dates for these".
