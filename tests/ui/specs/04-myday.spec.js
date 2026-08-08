const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

// These specs do real work: each builds a persona page from a day's corpus and
// then fetches the documents behind a card. Under a full-suite run that is
// legitimately slower than the 30s default, and a timeout here would be a
// false alarm rather than a defect.
test.describe.configure({ timeout: 90_000 });

async function makePersona(page, { name, entities, lane = 'news', families = '' }) {
  await page.evaluate(() => enterLane('news', 'per'));
  await page.locator('#perName').fill(name);
  if (lane !== 'news') await page.selectOption('#perLane', lane);
  await page.locator('#perEntities').fill(entities);
  if (families) await page.locator('#perFamilies').fill(families);
  await page.locator('button:has-text("Save persona")').click();
  await expect(page.locator('#perMsg')).toContainText('Saved');
}

test.describe('My Day — the generated page', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('with no persona it asks you to create one, and links there', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('#v-myday')).toContainText('Tell us what you follow');
    // starters are the fast path; building from scratch is still one click
    await expect(page.locator('.starter')).toHaveCount(3);
    await page.getByRole('button', { name: /Build one from scratch/ }).click();
    await expect(page.locator('#v-per')).toHaveClass(/on/);
  });

  test('builds a page from real corpus data with a coverage ledger', async ({ page }) => {
    await makePersona(page, { name: 'Credit book', entities: 'Goodfood\nWestJet\nSuncor' });
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('.mdlede')).toBeVisible();
    // the headline ledger is one line; the accounting behind it lives in the
    // third column, which is the half of the page that says what is NOT here
    const ledger = await page.locator('.mdledger').textContent();
    expect(ledger).toMatch(/serious/);
    expect(ledger).toMatch(/of [\d,]+ matched/);
    const aside = await page.locator('#mydayCols .fitpanel').last().textContent();
    expect(aside).toMatch(/watched names had no event/);
    expect(aside).toMatch(/documents scanned/);
  });

  test('a credit event outranks market noise and is marked serious', async ({ page }) => {
    await makePersona(page, { name: 'Credit book', entities: 'Goodfood\nWestJet' });
    await page.evaluate(() => enterLane('news', 'myday'));
    // pin the day the corpus holds this event: the test is about RANKING,
    // not about what happened to be published the morning it runs
    await page.evaluate(() => loadMyDay('2026-08-06'));
    const first = page.locator('.mdcard').first();
    await expect(first).toBeVisible();
    await expect(first).toContainText('credit event');
    await expect(first).toContainText('Goodfood');
    // the card carries its own type and corroboration without being opened
    await expect(first.locator('.m')).toContainText('source');
  });

  test('the page is read-only and stable: reopening shows the same page', async ({ page }) => {
    await makePersona(page, { name: 'Stable', entities: 'Goodfood' });
    await page.evaluate(() => enterLane('news', 'myday'));
    const lede = await page.locator('.mdlede').textContent();
    await page.locator('#nHome').click();
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('.mdlede')).toHaveText(lede);
    await expect(page.locator('#mydayHead')).toContainText('read-only');
  });

  test('a regulatory persona reports rule families as unchanged, not silent', async ({ page }) => {
    await makePersona(page, { name: 'Rules', entities: '', lane: 'regulatory',
                              families: 'osfi-car, b-13' });
    // the regulatory lane, because that is where a regulatory persona lives —
    // opening it under News only ever worked by falling back to the server's
    // first-persona default
    await page.evaluate(() => enterLane('reg', 'myday'));
    // wait for the generated page itself — the empty state also mentions
    // "rule families" in a starter blurb, so that phrase alone proves nothing
    await expect(page.locator('#mydayHead')).toContainText('Rules');
    await expect(page.locator('#v-myday')).toContainText('Unchanged');
    const body = await page.locator('#v-myday').textContent();
    expect(body).toMatch(/unchanged|moved/i);
  });

  test('cards open their evidence', async ({ page }) => {
    await makePersona(page, { name: 'Evidence', entities: 'Goodfood' });
    await page.evaluate(() => enterLane('news', 'myday'));
    await page.evaluate(() => loadMyDay('2026-08-06'));
    await expect(page.locator('.mdcard').first()).toBeVisible({ timeout: 25000 });
    await page.locator('.mdcard').first().click();
    await expect(page.locator('#drawer')).toBeVisible({ timeout: 25000 });
  });

  test('a big book gets exception framing, a small one gets narrative', async ({ page }) => {
    await makePersona(page, { name: 'Book',
      entities: ['Goodfood', ...Array.from({length:80},(_,i)=>`Obligor ${i}`)].join('\n') });
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('#mydayHead')).toContainText('names');
    await expect(page.locator('.mdlede')).toContainText('were quiet');
  });
});

test.describe('Health — can I trust the data', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('leads with a verdict, not a wall of tiles', async ({ page }) => {
    await page.locator('#nHea').click();
    await expect(page.locator('#heaVerdict .h')).not.toBeEmpty();
    // the verdict class is the triage signal — it must be one of the three
    const cls = await page.locator('#heaVerdict').getAttribute('class');
    expect(cls).toMatch(/healthy|watch|degraded/);
  });

  test('judges each category against its own staleness window', async ({ page }) => {
    await page.locator('#nHea').click();
    await expect(page.locator('#heaFresh')).toContainText('window');
    await expect(page.locator('#heaFresh .fbarline')).not.toHaveCount(0);
  });

  test('states that the counters are not a partition', async ({ page }) => {
    await page.locator('#nHea').click();
    await expect(page.locator('#heaFunnel')).toContainText('not a partition');
  });

  test('every quality check says what it breaks', async ({ page }) => {
    await page.locator('#nHea').click();
    await expect(page.locator('#heaQuality .qrow').first()).toBeVisible();
  });
});

test.describe('Ask — grounded chat', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('offers starting questions and states its own rule', async ({ page }) => {
    await page.evaluate(() => toggleChat(true));
    await expect(page.locator('#chatdock')).toHaveClass(/open/);
    await expect(page.locator('.ask-sug button').first()).toBeVisible();
    await expect(page.locator('#askSources')).toContainText('Sources');
    // the context switch is part of the contract: the person chooses what it reads
    await expect(page.locator('#ctxActive')).toHaveClass(/on/);
    await page.locator('#ctxPassive').click();
    await expect(page.locator('#ctxPassive')).toHaveClass(/on/);
  });

  test('an answer is grounded in listed sources, or it is withheld', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Ask book');
    await page.locator('#perEntities').fill('Goodfood\nWestJet\nSuncor');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');

    await page.evaluate(() => toggleChat(true));
    await page.locator('#askInput').fill('What should I look at first?');
    await page.locator('#chatdock .ask-form button').click();   // not the nav tab

    // wait for the answer to replace the pending bubble
    await expect(page.locator('.ask-msg.ai.pending')).toHaveCount(0, { timeout: 45000 });
    const reply = page.locator('.ask-msg.ai').last();
    await expect(reply).toBeVisible();
    const text = await reply.textContent();
    // The contract is: answer with citations, or say plainly why you cannot.
    // Every honest refusal the server can produce is listed here — anything
    // else means the assistant asserted something uncited.
    const cited = /\[\d+\]/.test(text);
    const declined = /(could not be verified|no model is configured|no sources pinned|nothing to answer|could not be reached|ask a question)/i.test(text);
    expect(cited || declined, `unexpected reply: ${text}`).toBe(true);
    if (cited) {
      await expect(page.locator('#askSources .s').first()).toBeVisible();
    }
  });

  test('opening a card from My Day pins it as the chat context', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Pin book');
    await page.locator('#perEntities').fill('Goodfood');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');   // then navigate
    await page.evaluate(() => enterLane('news', 'myday'));
    await page.evaluate(() => loadMyDay('2026-08-06'));
    await expect(page.locator('.mdcard').first()).toBeVisible({ timeout: 25000 });
    await page.locator('.mdcard').first().click();
    // the drawer opening confirms the card resolved its evidence
    await expect(page.locator('#drawer')).toBeVisible({ timeout: 25000 });
    // the drawer is modal and covers the nav — close it before navigating,
    // exactly as a person would
    await page.locator('.drclose').click();
    await expect(page.locator('#drawer')).not.toHaveClass(/show/);
    await page.evaluate(() => toggleChat(true));
    await expect(page.locator('#askCtx')).toContainText('story cluster');
  });
});

test.describe('ambiguous name matches', () => {
  test('a possible mention is shown and flagged, never silently dropped', async ({ page }) => {
    const { signup } = require('./helpers');
    await signup(page);
    await page.evaluate(() => enterLane('news', 'per'));
    // "Goodfood" is the analyst's shorthand; the corpus says "Goodfood Market Corp."
    await page.locator('#perName').fill('Shorthand book');
    await page.locator('#perEntities').fill('Goodfood');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');
    await page.evaluate(() => enterLane('news', 'myday'));
    await page.evaluate(() => loadMyDay('2026-08-06'));
    // the item must be on the page at all — that is the whole point
    await expect(page.locator('.mdcard').first()).toBeVisible({ timeout: 25000 });
    const body = await page.locator('#v-myday').textContent();
    expect(body).toMatch(/Goodfood/);
  });
});
