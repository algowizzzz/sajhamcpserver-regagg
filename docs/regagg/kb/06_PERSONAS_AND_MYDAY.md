# 06 — Personas, My Day, and the Entity Table

## What a persona is

One object with four parts, stored in `reg_personas.config` plus
`reg_persona_entities` rows.

| Part | Meaning |
|---|---|
| `lane` | `news` or `regulatory` — decides which documents it can **ever** see |
| entities | the watchlist, one `reg_persona_entities` row per name |
| `scope.rule_families` | e.g. `osfi-car`, `b-13`, `fincen-aml` |
| `salience` | `topic_weights` + `serious_threshold` |
| `table.columns` | the entity table's extra columns, YAML or JSON, stored verbatim |

The lane filter is absolute: a news persona never sees a regulator's document
and vice versa (`dossier.py`, the `category` comparison).

## How a persona shapes its page

`personas.derive_layout()` — **the user never picks a layout**:

| Persona shape | Layout | Effect |
|---|---|---|
| ≥ 50 entities (`BOOK_THRESHOLD`) | `exception_first` | only names with events, plus a quiet count |
| has rule families | `change_first` | what moved leads the page |
| otherwise | `narrative_first` | prose storyline |

## Regulatory differs from news in five ways

**1. It matches two things.** News matches entity names only. Regulatory also
matches rule families — `b-13` hits a document whose text says "b 13" *or whose
reference number is B-13*. That second path is why a rules owner catches a
guideline whose prose never names their family.

**2. A rule hit is worth a flat +25** on the score. That is the mechanism that
floats rule changes above everything else.

**3. There is a safety net only regulatory personas get.** If a regulatory
persona declares no rule families and nothing else matched, a document still
enters scope when its materiality band is Critical or High. A news persona has
no such fallback: no watchlist match means no card.

**4. It reports silence as a finding.** A `rule_state` section lists every
watched family and which moved. When none did, the page says *"Unchanged:
osfi-car · b-13 · fincen-aml — checked against 12 documents"*. "We looked and
nothing moved" and "we didn't look" are different facts.

**5. Previews come from the document body**, skipping letterhead — see the
excerpt extractor below. News previews are the publisher's own feed summary and
nothing else.

## The dossier — what goes on a page, and why

`dossier.build_dossier()` is the deterministic selector. For each candidate
document it computes:

```
score = topic_weight(event_type)
      + jurisdiction bonus
      + severity signals
      + corroboration (multiple sources)
      + 25 if a watched rule family matched
      + 0.2 × materiality
```

and a human-readable `why`: `credit event +55; 2 sources +10; watched rule
(b-13) +25`. Every card can explain itself without an LLM.

It also produces the **ledger**, which is conserved: `scanned, matched, shown,
suppressed_below_floor, suppressed_overflow, quiet_entities,
entities_with_events, entities_possible`. Nothing may vanish without appearing
in a counter — there is a test.

### Three-tier entity matching

`matching.WatchlistMatcher` returns `(name, confidence, reason)` where
confidence is **confirmed / possible / none**. Ambiguity is a first-class
outcome: a possible match is shown flagged as *"possible mention — verify"*,
never silently dropped and never asserted.

Rules in order: exact/alias → acronym → squashed-equal (spacing) → token-prefix
→ distinctive-word. Acronyms require 3+ core tokens and 3+ letters, so
"Goodfood Market Corp." does not become "GM" and match General Motors.

> Recall was 68% with one false positive before this rewrite — "Meta", "Uber",
> "AMD", "JP Morgan" silently missed while "Apple Hospitality REIT" matched
> "Apple Inc.". `test_entity_recall.py` now pins 100% recall on 22 name
> variants and zero false confirmations on 8 confusable pairs.
>
> The first version was also 80× too slow (a 4-second suite became 5.5 minutes)
> because it scanned the whole watchlist twice per lookup. Candidate indexes by
> first token and name-head fixed it. **If you touch the matcher, watch the
> suite's wall clock** — it was the symptom that looked like UI flakiness.

## My Day

Built once per persona per day, cached in `reg_page_specs`, read-only.
`GET /myday?refresh=true` rebuilds.

`myday.compose_template()` produces the deterministic spec; the LLM composer
may replace it, and `validate_spec()` checks coverage, citations and numbers
before it renders. A failed validation falls back to the template and the page
says `fallback_reason`.

### The focus bar

The one place a user's free text touches a generated page, so the split is
strict:

- **Entities and sources filter, in code.** Deterministic, and the view reports
  what each clause removed: `kept 4 of 16 · 12 came from another source`.
- **The prompt only reorders and narrates.** It cannot introduce a document
  that did not match. Its note is validated and withheld if it invents a
  figure. An order naming an unknown card voids the ranking.

A focused view is **ephemeral** and never overwrites the cached page — the
daily page is a record and someone may already have acted on it. It is labelled
"filtered by you, not the generated page" with an exit back.

## The entity table

`entity_table.py` + `tavily.py` + `table_schema.py`.

One row per watched name, whatever the outcome. 500 entities → 500 rows.
Every name ends in exactly one recorded state:

| Status | Meaning |
|---|---|
| `ok` | news found |
| `none` | searched, nothing published in the window |
| `error` | the search failed — retryable, and visible |
| `skipped` | the sweep hit its budget before reaching this name |
| `pending` | not searched yet |

Three things keep it affordable and honest:

- **Cached per persona/day/entity.** A re-run fills only the gaps; opening the
  page never spends. `error` rows are retried by the next sweep, `none` rows
  are not — an error is a gap, "no news" is an answer.
- **A hard budget**, checked before each call, with the remainder marked
  `skipped` rather than the sweep pretending it finished.
- **Cost shown before the click.** At 500 names a daily sweep is roughly
  15,000 Tavily credits/month, about **$120** at basic depth.

### Columns the desk declares

```yaml
columns:
  - name: event
    label: Event
    values: [major, minor, none]
    describe: major if it could move the credit on its own
  - name: rating_impact
    values: [negative, neutral, positive, unclear]
  - name: note
    type: text
    max_chars: 120
```

The model fills them from the snippet alone; every answer is then **coerced
against the declared set**. Case and surrounding punctuation are forgiven;
nothing else is. `"major event"` becomes `unknown`, not `major` — a near-miss
is still a miss, and silently mapping it would make the column look reliable
while quietly deciding what the model meant. An analyst is going to sort and
filter on it.

Reserved names (`entity, title, snippet, url, source, published, status`)
cannot be redefined. A broken schema reports why rather than vanishing.

### Demo mode

Without `TAVILY_API_KEY` the sweep uses `DemoNews` — deterministic per
(name, day), ~45% coverage so it looks like a real book, and **marked at every
level**: `demo` on each hit, `mode='demo'` on the row, and an undismissable
banner on the page.

> The pre-existing `sajha/tools/impl/tavily_tool_refactored.py` also has a demo
> mode, but an *unlabelled* one — invented results return through the same
> shape as real ones and nothing downstream can tell. That path is deliberately
> not used here.

## The excerpt extractor

`excerpt.py` gives each card the opening of its own document.

**News**: the publisher's feed summary, which is all that is stored. Where a
feed carries none, the card shows nothing rather than repeating its headline.

**Regulatory**: plenty of text, almost none of it useful at the top — the first
300 characters of an OSFI guideline is `255 Albert Street, Ottawa`. Paragraphs
are *scored for how much they read like prose* rather than matched against a
list of known letterheads, because every regulator has its own. A labelled
`Subject:` beats a guess.

Coverage on the real corpus: **83% of news, 76% of regulatory**. The rest
genuinely have no prose to show.

> The obvious regex for "six words then a full stop" nests two quantifiers and
> backtracks catastrophically on long paragraphs that never match — which
> regulatory PDFs supply in quantity. It hung on a 4,000-word input. It is a
> linear scan now, with a test that fails if it ever takes a second.
