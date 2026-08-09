# 03 — The UI, page by page

One file: `sajha/regagg/ui_dashboard.html`, served at `GET /api/regagg/ui`,
read from disk per request. No build step, no CDN. Edit and reload.

## Navigation is two levels

**Top bar — four tabs only:** Home · Regulatory · Financial News · Health.
The top bar carries the *lane*, not the page.

**Lane bar — the pages inside that lane:**

| | Regulatory | Financial News |
|---|---|---|
| | Overview | Overview |
| | My Day | My Day |
| | Entity table | Entity table |
| | **Regulators** | **Wires** |
| | Documents | Today's stories |
| | What changed | All stories |
| | Collection | Collection |
| | Files | Personas |
| | Personas | |

**Regulators and Wires are the same view** (`v-cov`), retitled per lane.
**Files** (`v-exp`) is regulatory-only — the news lane stores headline plus a
one-line summary, so a file explorer over it would show nothing worth auditing.

The four-layer mental model: **Wires/Regulators** = where it comes from →
**Collection** = whether it arrived → **Documents/All stories** = what we hold
→ **Files** = the bytes on disk, for audit.

## The layout system

Two families, deliberately different:

**`.fitpage`** — claims the viewport, panels scroll internally, the window
never scrolls. Used by Collection, Health, My Day, Entity table: maintenance
pages you scan rather than read.

```css
.fitpage { height: calc(100dvh - var(--chrome)); }
.fitpanel { display:flex; flex-direction:column; min-height:0; }
.fitbody  { flex:1; min-height:0; overflow:auto; }
```

Three details that are easy to get wrong and were:
- `dvh` not `vh` — mobile browser chrome clips the last panel otherwise.
- `min-height:0` on every flex child — without it a child refuses to shrink
  below its content and pushes the page taller than the screen.
- Below 1100px `.fitpage` reverts to `height:auto` and the page scrolls, rather
  than shrinking cells past reading.

**`.mainlist`** — the primary content of a reading page flows at full height
and the *window* scrolls. Used by the change feed, document table, coverage
tree, file tree, top-stories list.

> This distinction exists because capping every long list at 340px put 16,238px
> of the change feed behind a letterbox on a page that would not itself scroll.
> Everything was technically reachable and no test noticed. The rule now:
> **a page's primary content scrolls with the page; side panels cap.**
> There is a regression test that walks all eleven views and fails if any holds
> more than a screenful in a panel while the window will not scroll.

Side panels use `.scrollbox`, sized against the viewport
(`clamp(200px, 100dvh - 380px, 560px)`) rather than a fixed height, with a
persistent thin scrollbar because macOS hides overlay scrollbars until you
scroll and a bounded panel otherwise reads as clipped.

## Home

Two lane cards with live counts, a corpus-by-coverage-area chart, the
materiality band breakdown, and a "where to start" strip. Every chart is
clickable through to the documents behind it.

## Regulatory / Financial News overview

Hero tiles, deepest holdings, corpus by document type, materiality bands,
change tracking. The news overview additionally shows the credit-analyst
ranking lens and daily volume.

## My Day — three columns

The persona's daily briefing. Built once per persona per day, cached read-only
in `reg_page_specs`, so everyone who opens it sees the same page.

```
[persona ▾] [12 names] [date · generated · model · read-only]   [3 serious · 13 watch · 11 quiet · 16 of 338 matched]
[Focus: a question ……………] [+ entity] [+ source] [Focus]
[ narrative — two lines, click to expand ]
┌ Serious ────────┬ Watch ──────────┬ Not on this page ─┐
│ card + preview  │ card + preview  │ rule families     │
│ card + preview  │ …               │ what was excluded │
└─────────────────┴─────────────────┴───────────────────┘
```

Design decisions worth keeping:
- **A dropdown, not chips.** A control that shows every option permanently is
  worth it when you compare them; you do not compare personas.
- **One ledger line, not five tiles.** The interesting figure is the ratio, so
  "16 of 338 matched" replaces two separate tiles.
- **Three columns** because the page is triaged in three moves: act on it, read
  it before Monday, note that it happened. Stacked, Watch began below the fold
  on every screen.
- **Every card carries a preview** so the click is a choice, not the only way
  to find out what happened.
- **The third column is the reassurance half** — what was checked and set
  aside, plus the rule-family verdict for a regulatory persona.

### The focus bar

Entities and sources **filter deterministically in code**; the prompt only
**reorders and narrates**. A focused view is ephemeral, labelled as a filter
rather than the daily page, and never overwrites the cache. See
`06_PERSONAS_AND_MYDAY.md`.

## Entity table

One row per watched name — 500 entities produce 500 rows, including the ones
with nothing to report, because those are the evidence that the sweep looked.

Columns: entity · headline + snippet · source · **the persona's own declared
columns** · status. Status is `ok | none | error | skipped | pending`.

Reading the table spends nothing; it serves cache. **Run sweep** is the only
thing that calls out, and it shows the credit count before the click. Without
`TAVILY_API_KEY` the sweep produces labelled demo rows and the page shows an
undismissable banner.

## Collection

The page for the person accountable for the data being current.

- **Today bar** — the date in words, and one of six schedule states:
  `not scheduled · due · running · complete · partial · missed`, with the next
  run time. This is the page's whole reason for existing: a weekend and a dead
  scheduler used to look identical.
- **Coverage matrix** — category × 7 days. A gap the schedule never promised is
  dashed and muted, never red. Click a cell for the sources that did not run,
  with a button to run exactly those.
- **Volume** — four sparklines, labelled with the day they belong to (on a
  Saturday the latest figures are Friday's, and saying "today" would be a lie).
- **Run and rerun** — sources bucketed `failed / stale / silent / never`,
  multi-select, per-row rerun, date and cap.
- **What arrived** — per source, against that source's own 7-day average.
- **Live queue** — appears for scheduled and manual runs alike.

`silent` is the important bucket: those runs are green, so nothing else on the
page complains, and the data quietly ages out.

## Health

Organised around one question: can I trust what is in here.

- **Verdict banner** — one sentence, deliberately blunt. A page that is always
  green stops being read.
- **Freshness** — each category against its own window (news 3d, regulatory
  14d). Judging both by one number would either cry wolf about regulators or
  say nothing about wires.
- **Collection funnel** — as measured, with the note that the counters are not
  a partition, and a count of runs whose numbers contradict each other.
- **Schedule reliability** — per category, never pooled. Pooling let the news
  wires mask regulatory sitting dark for three days.
- **Needs attention** — ranked by how long the data has been wrong, with inline
  rerun.
- **Data quality** — defects in what we already hold. Every row states which
  capability it breaks, because a count with no consequence gets scrolled past.

## The chat dock

A collapsible left panel, resizable by dragging its right edge (280px to
min(760px, 62vw)), double-click to reset, arrow keys when focused. The width is
a stored preference held separately from the width currently displayable, so
narrowing the window borrows it back and widening restores it.

- **Page context: Active / Passive.** Active tells the assistant what the person
  is looking at; passive tells it to ignore the screen.
- **Sources live inside the answer bubble** — a row of chips under the text,
  title first, publisher as caption, opening the article in a new tab.
  Citations in the prose are superscript numbers matching the chips.

## Density toggle

The `▤` button in the header toggles compact rows, remembered per browser.

## Design language

Neutral bank palette, `--blue #0f5aa9` for accent only. Status is pill + icon +
text, never colour alone. Tabular numerals for counts. Progressive disclosure
(region → source → document). Every count is clickable to its evidence. Show
denominators — "X of Y", not a bare success.
