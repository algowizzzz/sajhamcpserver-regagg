# How to add a test

## Python

```python
def test_a_category_that_did_not_run_is_missed_even_when_the_other_did(wired):
    """The bug that made reliability report zero missed runs.

    News collecting on Friday must not make it look like regulatory did too.
    """
```

Two conventions that matter more than they look:

**Name the behaviour, not the function.** `test_sweep_budget` tells you nothing
when it fails at 2am. `test_the_budget_stops_the_sweep_and_names_what_it_missed`
tells you what was promised.

**When a test comes from a bug, say so in the docstring.** The intent is the
thing that gets lost in a refactor, and a docstring naming the original failure
stops someone "simplifying" the guard away.

### Fixtures

| Fixture | Gives you |
|---|---|
| `session` | in-memory SQLite with only the `reg_*` tables |
| `storage` | tmp-dir corpus storage |
| `seed_regulator(id, jurisdiction, connector)` | a source row |
| `corpus` | two enriched, cross-referenced documents + wired runtime |

A fixture that needs the runtime must wire and unwire it:

```python
runtime.set_providers(session=lambda: session, storage=lambda: storage)
yield
runtime.set_providers(session=lambda: None)      # or the next test inherits it
```

### Testing a generated surface

Never call a live model. Inject a fake and assert the **validation**:

```python
class Echo:
    def complete(self, system, user, **kw):
        return json.dumps({"order": [...], "note": "..."})

def test_a_note_with_an_invented_figure_is_withheld():
    out = F.rank_by_prompt(ITEMS, "x", client=Echo(note="Totals $947 million."))
    assert out["note"] is None
    assert "947" in out["reason"]
    assert out["ranked"] is True        # the order survives; they fail separately
```

What is being protected is that a bad model output cannot reach the screen —
not that a good one is pretty.

## Browser

```js
test('an unscheduled day is drawn as expected, never as a fault', async ({ page }) => {
  await collection(page);
  const n = await page.locator('#covMatrix .cell.not_scheduled').count();
  for (let i = 0; i < n; i++) {
    const cls = await page.locator('#covMatrix .cell.not_scheduled').nth(i)
      .getAttribute('class');
    expect(cls).not.toContain('missed');
  }
});
```

`await signup(page)` in `beforeEach` gives a fresh account. Navigate with
`page.evaluate(() => enterLane('reg', 'run'))` rather than clicking through —
the lane bar is dynamic and clicking is slower and flakier.

For rendering that depends on model output, seed the thread directly:

```js
await page.evaluate((m) => { ASKTHREAD.length = 0; ASKTHREAD.push(m);
                             toggleChat(true); renderAsk(); }, msg);
```

That tests the rendering, which is what you changed, rather than the model.

## Prove a regression test is not vacuous

**Always.** A test written after the fix may pass on the broken code too.

Re-create the bug and confirm the test fires:

```python
bad = src.replace('      </div></div>\n    <div id="ovwHead"',
                  '      </div></div></div>\n    <div id="ovwHead"', 1)
# → both markup tests fail. Now it is a real guard.
```

Or in the live page:

```js
el.style.maxHeight = '340px';   // re-impose the old cap
// → 16,238px hidden, page frozen, the letterbox check fires
```

## Traps that have cost time here

| Trap | What happens |
|---|---|
| Nested quantifiers in a regex | catastrophic backtracking on long non-matching input; it hung a page render, not just a test |
| Testing the matcher without watching the clock | a correct fix was 80× slower and looked like UI flakiness |
| `cp` of a live SQLite file | torn page → `database disk image is malformed` |
| Thread-locals for DB sessions | do not propagate into FastAPI's threadpool; pool exhaustion |
| Two components sharing a CSS class | strict-mode locator resolves to 2 elements |
| Asserting on a cached page | My Day caches per persona per day; use `refresh=true` |
| Percentages against the wrong population | a run-level defect over the document count read as 1.6% instead of 87% |

## Before you commit

```bash
./.venv/bin/python -m pytest tests/regagg -q     # 377 passed
bash tests/ui/run_suite.sh                       # 76 passed
```

Both, if you touched `sajha/regagg/` or the dashboard. Update
`testing/03_RESULTS.md` when the counts change.
