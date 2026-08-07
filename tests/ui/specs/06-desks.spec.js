const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

async function makeDesk(page, name, entities, weights) {
  await page.locator('#nPer').click();
  await page.locator('button:has-text("＋ New persona")').click();
  await page.locator('#perName').fill(name);
  await page.locator('#perEntities').fill(entities);
  if (weights) await page.locator('#perTopics').fill(weights);
  await page.locator('button:has-text("Save persona")').click();
  await expect(page.locator('#perMsg')).toContainText('Saved');
}

test.describe('desk dashboard', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('with no personas it explains itself instead of showing an empty grid', async ({ page }) => {
    await page.locator('#nDsk').click();
    await expect(page.locator('#desksBody')).toContainText('No desks yet');
  });

  test('shows one card per desk with counts and the collection window', async ({ page }) => {
    await makeDesk(page, 'Credit book', 'Goodfood\nWestJet\nSuncor', 'credit:70');
    await makeDesk(page, 'Equity book', 'Meta Platforms, Inc.\nApple Inc.', 'guidance:70');
    await page.locator('#nDsk').click();
    await expect(page.locator('.dk')).toHaveCount(2);
    await expect(page.locator('.dk-hero')).toContainText('2 desks');
    await expect(page.locator('.dk-hero .win')).toContainText('days of collection');
    // every card states its watchlist size and what it scanned
    await expect(page.locator('.dk').first()).toContainText('names watched');
    await expect(page.locator('.dk').first()).toContainText('documents scanned');
  });

  test('a desk with nothing says so rather than showing a blank card', async ({ page }) => {
    await makeDesk(page, 'Nothing here', 'Zzz Nonexistent Holdings Plc');
    await page.locator('#nDsk').click();
    await expect(page.locator('.dk')).toContainText('Nothing to report');
    await expect(page.locator('.dk')).toContainText('documents\n            checked');
  });

  test('urgent desks sort first', async ({ page }) => {
    await makeDesk(page, 'AAA quiet desk', 'Zzz Nonexistent Holdings Plc');
    await makeDesk(page, 'ZZZ busy desk', 'Meta Platforms, Inc.\nApple Inc.\nAlphabet Inc.',
                   'guidance:70, deal:60');
    await page.locator('#nDsk').click();
    await expect(page.locator('.dk')).toHaveCount(2);      // wait for the grid
    const names = await page.locator('.dk h4').allTextContents();
    // alphabetically AAA would be first; urgency must win over the name
    expect(names[0]).toContain('ZZZ busy desk');
  });

  test('clicking a desk opens that desk\'s page', async ({ page }) => {
    await makeDesk(page, 'Credit book', 'Goodfood\nWestJet');
    await makeDesk(page, 'Equity book', 'Meta Platforms, Inc.');
    await page.locator('#nDsk').click();
    await page.locator('.dk', { hasText: 'Equity book' }).click();
    await expect(page.locator('#v-myday')).toHaveClass(/on/);
    await expect(page.locator('.md-head b')).toHaveText('Equity book');
  });

  test('the window is stated, never implied', async ({ page }) => {
    await makeDesk(page, 'Any', 'Goodfood');
    await page.locator('#nDsk').click();
    const win = await page.locator('.dk-hero .win').textContent();
    expect(win).toMatch(/\d+ days? of collection/);
    expect(win).toMatch(/[\d,]+ stories/);
    expect(win).toContain('read-only');
  });
});
