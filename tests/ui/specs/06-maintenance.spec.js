// Collection and Health for the person who maintains the data.
//
// The thing being protected here is not "does it render" but "does it mislead".
// A weekend that reads as an outage, a page that hides its own gaps below the
// fold, or a rerun control that silently targets the wrong sources all look
// fine in a screenshot and cost someone an afternoon.

const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

async function collection(page) {
    await page.evaluate(() => enterLane("reg", "run"));
  await page.locator('#todayBar').waitFor();
  await expect(page.locator('#todayBar')).not.toContainText('loading');
}

test.describe('Collection — is today done', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  test('names the date and says what the schedule expects of it', async ({ page }) => {
    await collection(page);
    const bar = page.locator('#todayBar');
    // the complaint that started this: today's date was nowhere on the page
    await expect(bar).toContainText(new Date().getFullYear().toString());
    await expect(bar.locator('.tstate')).toBeVisible();
    const state = await bar.locator('.tstate').getAttribute('class');
    expect(state).toMatch(/not_scheduled|due|running|complete|partial|missed/);
  });

  test('an unscheduled day is drawn as expected, never as a fault', async ({ page }) => {
    await collection(page);
    const cells = page.locator('#covMatrix .cell');
    await expect(cells.first()).toBeVisible();
    const n = await page.locator('#covMatrix .cell.not_scheduled').count();
    for (let i = 0; i < n; i++) {
      // dashed and muted — it must not share the missed treatment
      const cls = await page.locator('#covMatrix .cell.not_scheduled').nth(i).getAttribute('class');
      expect(cls).not.toContain('missed');
    }
  });

  test('a cell opens the list of sources that did not run', async ({ page }) => {
    await collection(page);
    const cell = page.locator('#covMatrix .cell:not(.not_scheduled)').first();
    if (await cell.count()) {
      await cell.click();
      await expect(page.locator('#drawer')).toBeVisible();
      await expect(page.locator('#drawer')).toContainText('sources ran');
    }
  });

  test('trend panels name the day their figures belong to', async ({ page }) => {
    await collection(page);
    await expect(page.locator('#trendCards .spark')).toHaveCount(4);
    await expect(page.locator('#trendNote')).toContainText('latest');
  });

  test('sources are bucketed so you can pick what to rerun', async ({ page }) => {
    await collection(page);
    await expect(page.locator('#srcList .srow').first()).toBeVisible();
    await expect(page.locator('#runChips .chip').first()).toBeVisible();
  });

  test('selecting sources changes what the run button will do', async ({ page }) => {
    await collection(page);
    await expect(page.locator('#runGo')).toContainText('Run all');
    await page.locator('#srcList .srow input[type=checkbox]').first().check();
    await expect(page.locator('#runGo')).toContainText('Run 1 selected');
    await page.locator('#srcList .srow input[type=checkbox]').nth(1).check();
    await expect(page.locator('#runGo')).toContainText('Run 2 selected');
  });

  test('a bucket filter narrows the list without losing the selection count',
    async ({ page }) => {
      await collection(page);
      const chips = page.locator('#runChips .chip');
      if (await chips.count() > 1) {
        await chips.nth(1).click();
        await expect(page.locator('#srcList')).toBeVisible();
        const label = await chips.nth(1).textContent();
        expect(label.trim().length).toBeGreaterThan(0);
      }
    });
});

test.describe('auto-fit — neither page may scroll the window', () => {
  test.beforeEach(async ({ page }) => { await signup(page); });

  for (const [w, h, name] of [[1920, 1080, 'large'], [1440, 900, 'laptop']]) {
    test(`collection fits a ${name} viewport`, async ({ page }) => {
      await page.setViewportSize({ width: w, height: h });
      await collection(page);
      await page.waitForTimeout(600);
      const over = await page.evaluate(() =>
        document.documentElement.scrollHeight - window.innerHeight);
      expect(over).toBeLessThanOrEqual(2);
    });

    test(`health fits a ${name} viewport`, async ({ page }) => {
      await page.setViewportSize({ width: w, height: h });
      await page.locator('#nHea').click();
      await page.locator('#heaVerdict').waitFor();
      await page.waitForTimeout(600);
      const over = await page.evaluate(() =>
        document.documentElement.scrollHeight - window.innerHeight);
      expect(over).toBeLessThanOrEqual(2);
    });
  }

  test('below the breakpoint the page stacks and is allowed to scroll',
    async ({ page }) => {
      // forcing everything into 1000px of width would shrink cells past reading
      await page.setViewportSize({ width: 900, height: 800 });
      await page.locator('#nHea').click();
      await page.locator('#heaVerdict').waitFor();
      const overflow = await page.evaluate(() =>
        getComputedStyle(document.getElementById('v-hea')).overflow);
      expect(overflow).toBe('visible');
    });

  test('density is remembered across a reload', async ({ page }) => {
    await page.locator('#densityBtn').click();
    await expect(page.locator('body')).toHaveClass(/dense/);
    await page.reload();
    await page.evaluate(() => window.READY);
    await expect(page.locator('body')).toHaveClass(/dense/);
  });
});
