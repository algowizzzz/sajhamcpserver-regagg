const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

test.describe('onboarding and multi-persona', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('a new user is offered starters instead of a blank form', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('.starter')).toHaveCount(3);
    await expect(page.locator('.starter').first()).toContainText('Credit oversight');
  });

  test('a starter prefills a working persona in one click', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'myday'));
    await page.locator('.starter', { hasText: 'Credit oversight' }).click();
    await expect(page.locator('#v-per')).toHaveClass(/on/);
    await expect(page.locator('#perName')).toHaveValue('Credit oversight');
    await expect(page.locator('#perEntities')).toHaveValue(/Goodfood/);
    await expect(page.locator('#perTopics')).toHaveValue(/credit:60/);
    // and it saves straight away — time-to-value is one more click
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('.md-lede')).toBeVisible();
  });

  test('the rules starter produces a regulatory persona', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'myday'));
    await page.locator('.starter', { hasText: 'Rules owner' }).click();
    await expect(page.locator('#perLane')).toHaveValue('regulatory');
    await expect(page.locator('#perFamilies')).toHaveValue(/osfi-car/);
  });

  test('a user with two personas can switch between them on My Day', async ({ page }) => {
    // one of each lane
    await page.locator('#nPer').click();
    await page.locator('#perName').fill('My book');
    await page.locator('#perEntities').fill('Goodfood\nWestJet');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');

    await page.locator('button:has-text("＋ New persona")').click();
    await page.locator('#perName').fill('My second book');
    await page.locator('#perEntities').fill('Meta Platforms, Inc.');
    await page.locator('button:has-text("Save persona")').click();
    await expect(page.locator('#perMsg')).toContainText('Saved');

    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('.md-switch button')).toHaveCount(2);
    const first = await page.locator('.md-head b').textContent();
    await page.locator('.md-switch button').nth(1).click();
    await expect(page.locator('.md-head b')).not.toHaveText(first);
  });

  test('one persona shows no switcher — no controls without a choice', async ({ page }) => {
    await page.locator('#nPer').click();
    await page.locator('#perName').fill('Only one');
    await page.locator('#perEntities').fill('Goodfood');
    await page.locator('button:has-text("Save persona")').click();
    await page.evaluate(() => enterLane('news', 'myday'));
    await expect(page.locator('.md-switch')).toHaveCount(0);
  });
});

test.describe('responsive and resilience', () => {
  test('works on a phone-sized viewport', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await signup(page);
    await expect(page.locator('#v-home')).toHaveClass(/on/);
    // nothing may overflow the viewport horizontally
    const overflow = await page.evaluate(() =>
      document.documentElement.scrollWidth - document.documentElement.clientWidth);
    expect(overflow).toBeLessThanOrEqual(2);
    await page.locator('#nPer').click();
    await expect(page.locator('#perName')).toBeVisible();
  });

  test('a failed API call is reported, not left spinning', async ({ page }) => {
    await signup(page);
    await page.route('**/api/regagg/exec/summary*', r => r.abort());
    await page.locator('#nHome').click();
    await page.evaluate(() => loadHomeExec().catch(() => {}));
    // the panel must not sit on the word "loading" forever
    await page.waitForTimeout(1500);
    const stuck = await page.locator('#xhRegions').textContent();
    expect(stuck).not.toBe('loading…');
  });
});
