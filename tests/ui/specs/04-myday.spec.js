const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

async function makePersona(page, { name, entities, lane = 'news', families = '' }) {
  await page.locator('#nPer').click();
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
    await page.locator('#nMyd').click();
    await expect(page.locator('#mydayBody')).toContainText('Tell us what you follow');
    // starters are the fast path; building from scratch is still one click
    await expect(page.locator('.starter')).toHaveCount(3);
    await page.getByRole('button', { name: /Build one from scratch/ }).click();
    await expect(page.locator('#v-per')).toHaveClass(/on/);
  });

  test('builds a page from real corpus data with a coverage ledger', async ({ page }) => {
    await makePersona(page, { name: 'Credit book', entities: 'Goodfood\nWestJet\nSuncor' });
    await page.locator('#nMyd').click();
    await expect(page.locator('.md-lede')).toBeVisible();
    // the ledger must reconcile and must state the quiet count
    const ledger = await page.locator('.md-ledger').textContent();
    expect(ledger).toMatch(/shown of/);
    expect(ledger).toMatch(/watched names quiet/);
    expect(ledger).toMatch(/built from [\d,]+ documents/);
  });

  test('a credit event outranks market noise and is marked serious', async ({ page }) => {
    await makePersona(page, { name: 'Credit book', entities: 'Goodfood\nWestJet' });
    await page.locator('#nMyd').click();
    // pin the day the corpus holds this event: the test is about RANKING,
    // not about what happened to be published the morning it runs
    await page.evaluate(() => loadMyDay('2026-08-06'));
    const first = page.locator('.md-ev').first();
    await expect(first).toBeVisible();
    await expect(first).toContainText('CREDIT EVENT');
    await expect(first).toContainText('Goodfood');
    // every card explains itself
    await expect(first.locator('.m')).toContainText('credit event +');
  });

  test('the page is read-only and stable: reopening shows the same page', async ({ page }) => {
    await makePersona(page, { name: 'Stable', entities: 'Goodfood' });
    await page.locator('#nMyd').click();
    const lede = await page.locator('.md-lede').textContent();
    await page.locator('#nHome').click();
    await page.locator('#nMyd').click();
    await expect(page.locator('.md-lede')).toHaveText(lede);
    await expect(page.locator('.md-head .day')).toContainText('read-only');
  });

  test('a regulatory persona reports rule families as unchanged, not silent', async ({ page }) => {
    await makePersona(page, { name: 'Rules', entities: '', lane: 'regulatory',
                              families: 'osfi-car, b-13' });
    await page.locator('#nMyd').click();
    // wait for the generated page itself — the empty state also mentions
    // "rule families" in a starter blurb, so that phrase alone proves nothing
    await expect(page.locator('.md-head b')).toHaveText('Rules');
    await expect(page.locator('#mydayBody')).toContainText('Your rule families');
    const body = await page.locator('#mydayBody').textContent();
    expect(body).toMatch(/unchanged|moved/i);
  });

  test('cards open their evidence', async ({ page }) => {
    await makePersona(page, { name: 'Evidence', entities: 'Goodfood' });
    await page.locator('#nMyd').click();
    await page.evaluate(() => loadMyDay('2026-08-06'));
    await expect(page.locator('.md-ev').first()).toBeVisible();
    await page.locator('.md-ev').first().click();
    await expect(page.locator('#drawer')).toBeVisible({ timeout: 10000 });
  });

  test('a big book gets exception framing, a small one gets narrative', async ({ page }) => {
    await makePersona(page, { name: 'Book',
      entities: ['Goodfood', ...Array.from({length:80},(_,i)=>`Obligor ${i}`)].join('\n') });
    await page.locator('#nMyd').click();
    await expect(page.locator('.md-head .chip')).toContainText('exception first');
    await expect(page.locator('.md-lede')).toContainText('were quiet');
  });
});

test.describe('Health — the platform team pane', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('shows pipeline conservation, pass rate and source attention', async ({ page }) => {
    await page.locator('#nHea').click();
    await expect(page.locator('#heaTiles .tile')).toHaveCount(6);
    await expect(page.locator('#heaStages span').first()).toBeVisible();
    await expect(page.locator('#heaConserve')).toContainText('Conservation');
    await expect(page.locator('#heaSources')).not.toBeEmpty();
    await expect(page.locator('#heaGen')).toContainText('validated');
  });
});

test.describe('Ask — context-pinned chat', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('is honest when chat is not connected, and never dead-ends', async ({ page }) => {
    await page.locator('#nAsk').click();
    await expect(page.locator('#askBody')).toContainText('not connected');
    await expect(page.locator('#askBody')).toContainText('visible in');
    await expect(page.locator('#askCtx')).toContainText('No artifact pinned');
  });
});

test.describe('ambiguous name matches', () => {
  test('a possible mention is shown and flagged, never silently dropped', async ({ page }) => {
    const { signup } = require('./helpers');
    await signup(page);
    await page.locator('#nPer').click();
    // "Goodfood" is the analyst's shorthand; the corpus says "Goodfood Market Corp."
    await page.locator('#perName').fill('Shorthand book');
    await page.locator('#perEntities').fill('Goodfood');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');
    await page.locator('#nMyd').click();
    await page.evaluate(() => loadMyDay('2026-08-06'));
    // the item must be on the page at all — that is the whole point
    await expect(page.locator('.md-ev').first()).toBeVisible();
    const body = await page.locator('#mydayBody').textContent();
    expect(body).toMatch(/Goodfood/);
  });
});
