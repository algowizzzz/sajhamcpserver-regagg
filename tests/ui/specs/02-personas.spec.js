const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

test.describe('personas', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('creates a persona and persists it across a reload', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Credit Oversight');
    await page.locator('#perEntities').fill('Goodfood,consumer\nWestJet,airlines\nSuncor,energy');
    await page.locator('#perTopics').fill('credit:60, ccr:50');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');
    await expect(page.locator('#perList .pitem')).toContainText('Credit Oversight');
    await expect(page.locator('#perList .pitem')).toContainText('3 names');

    await page.reload();
    await page.evaluate(() => enterLane('news', 'per'));
    await expect(page.locator('#perList .pitem').first()).toContainText('Credit Oversight');
  });

  test('layout is DERIVED from scope, not chosen: few names -> narrative', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Energy beat');
    await page.locator('#perEntities').fill('Suncor\nCenovus');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perList .pitem').first()).toContainText('narrative first');
  });

  test('a 1,000-name book flips the layout to exception-first', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Big book');
    const names = Array.from({ length: 1000 }, (_, i) => `Obligor ${i}`).join('\n');
    await page.locator('#perEntities').fill(names);
    await expect(page.locator('#perPreview')).toContainText('exception first');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('1,000 names');
    await expect(page.locator('#perList .pitem').first()).toContainText('exception first');
  });

  test('rule families flip a regulatory persona to change-first', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Rules owner');
    await page.selectOption('#perLane', 'regulatory');
    await page.locator('#perFamilies').fill('osfi-car, b-13, fincen-aml');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perList .pitem').first()).toContainText('change first');
    await expect(page.locator('#perList .pitem').first()).toContainText('regulatory');
  });

  test('editing bumps the version (the audit trail)', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Versioned');
    await page.locator('#perEntities').fill('AlphaCorp');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('v1');
    await page.locator('#perEntities').fill('AlphaCorp\nBetaCorp');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('v2');
    await expect(page.locator('#perMsg')).toContainText('2 names');
  });

  test('duplicate names in the paste are collapsed', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Dupes');
    await page.locator('#perEntities').fill('Goodfood\ngoodfood\nGOODFOOD\nWestJet');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('2 names');
  });

  test('personas are private to their owner', async ({ browser, page }) => {
    await page.evaluate(() => enterLane('news', 'per'));
    await page.locator('#perName').fill('Private book');
    await page.locator('#perEntities').fill('SecretCo');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');

    const other = await browser.newContext();
    const p2 = await other.newPage();
    await signup(p2);
    await p2.evaluate(() => enterLane('news', 'per'));
    await expect(p2.locator('#perList')).not.toContainText('Private book');
    await other.close();
  });
});
