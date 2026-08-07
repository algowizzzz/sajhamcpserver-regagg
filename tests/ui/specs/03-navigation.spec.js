const { test, expect } = require('@playwright/test');
const { signup } = require('./helpers');

test.describe('two-level navigation and lane scoping', () => {
  test.beforeEach(async ({ page }) => {
    page.on('pageerror', e => console.log('PAGEERROR:', e.message));
    page.on('console', m => { if (m.type() === 'error') console.log('CONSOLE:', m.text()); });
    page.on('response', r => { if (r.status() >= 400) console.log('HTTP', r.status(), r.url()); });
    await signup(page);
  });

  test('home shows both lane cards with live counts', async ({ page }) => {
    await expect(page.locator('#xhTiles .tile')).toHaveCount(6);
    await expect(page.locator('#xhLanes .lane')).toHaveCount(2);
    await expect(page.locator('#xhLanes')).toContainText('Regulatory Intelligence');
    await expect(page.locator('#xhLanes')).toContainText('Financial News');
  });

  test('entering a lane reveals its subtopics in the lane bar', async ({ page }) => {
    await page.locator('#nNews').click();
    await expect(page.locator('#lanebar')).toBeVisible();
    await expect(page.locator('#laneWho')).toContainText('Financial News');
    await expect(page.locator('#laneTabs button')).toHaveCount(5);
    await page.locator('#nOvw').click();
    await expect(page.locator('#laneWho')).toContainText('Regulatory');
    await expect(page.locator('#laneTabs button')).toHaveCount(6);
  });

  test('shared pages scope to the lane they were entered from', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'brw'));
    await expect(page.locator('#laneScope')).toContainText('financial-news wires only');
    const newsCount = await page.locator('#bCount').textContent();

    await page.evaluate(() => enterLane('reg', 'brw'));
    await expect(page.locator('#laneScope')).toContainText('regulators only');
    const regCount = await page.locator('#bCount').textContent();

    expect(newsCount).not.toEqual(regCount);
    const n = s => Number((s.match(/of ([\d,]+)/) || [])[1].replace(/,/g, ''));
    expect(n(regCount)).toBeGreaterThan(n(newsCount));   // 5,969 vs 603
  });

  test('the coverage tree shows only the current lane\'s regions', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'cov'));
    await expect(page.locator('#tree .rname')).toHaveCount(1);
    await expect(page.locator('#tree .rname')).toContainText('Financial News');
    await page.evaluate(() => enterLane('reg', 'cov'));
    const regions = await page.locator('#tree .rname').allTextContents();
    expect(regions).toContain('Canada');
    expect(regions).not.toContain('Financial News');
  });

  test('pages retitle for their lane', async ({ page }) => {
    await page.evaluate(() => enterLane('news', 'brw'));
    await expect(page.locator('.ptitle[data-t="v-brw"]')).toHaveText('All stories');
    await page.evaluate(() => enterLane('reg', 'brw'));
    await expect(page.locator('.ptitle[data-t="v-brw"]')).toHaveText('Documents');
  });

  test('deep links from charts land filtered, not unfiltered', async ({ page }) => {
    // counts grow as collection runs, so assert the filter WORKED rather than
    // a snapshot number: a filtered view must be a strict subset of everything
    // read the count only after a NEW render — waiting for text that the
    // previous render also matches reads a stale value
    const n = async (prev) => {
      await page.waitForFunction(
        p => Number(document.getElementById('bCount').dataset.render || 0) > p,
        prev ?? 0);
      const t = await page.locator('#bCount').textContent();
      const r = await page.locator('#bCount').getAttribute('data-render');
      return { value: Number((t.match(/of ([\d,]+)/) || [])[1].replace(/,/g, '')),
               render: Number(r) };
    };
    await page.evaluate(() => jumpCorpus(''));
    const all = await n();

    await page.evaluate(() => jumpCorpus('Financial News'));
    await expect(page.locator('#bRegion')).toHaveValue('Financial News');
    const news = await n(all.render);
    expect(news.value).toBeGreaterThan(0);
    expect(news.value).toBeLessThan(all.value);

    await page.evaluate(() => jumpBand('Critical'));
    await expect(page.locator('#bBand')).toHaveValue('Critical');
    const critical = await n(news.render);
    expect(critical.value).toBeGreaterThan(0);
    expect(critical.value).toBeLessThan(all.value);
  });

  test('hash routing deep-links survive a reload', async ({ page }) => {
    await page.goto('/api/regagg/ui#news');
    await expect(page.locator('#v-newslane')).toHaveClass(/on/);
    await expect(page.locator('#xnTiles .tile').first()).toBeVisible();
  });
});
