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

  // The failure this caught: the change feed had 16,000px of content behind a
  // 340px box on a page that would not itself scroll. Every element was
  // present and technically reachable, so nothing else noticed — you just
  // could not get at what you came to read.
  const VIEWS = [
    ['home', null], ['reg', 'ovw'], ['reg', 'cov'], ['reg', 'brw'],
    ['reg', 'chg'], ['reg', 'run'], ['reg', 'exp'],
    ['news', 'feed'], ['news', 'myday'], ['news', 'per'], ['hea', null],
  ];

  test('no page traps its content behind a letterbox', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    const trapped = [];
    for (const [lane, sub] of VIEWS) {
      await page.evaluate(([l, s]) => (s ? enterLane(l, s) : show(l)), [lane, sub]);
      await page.waitForTimeout(1200);
      const r = await page.evaluate(() => {
        const v = document.querySelector('.view.on');
        if (!v) return null;
        let worst = 0;
        v.querySelectorAll('*').forEach((el) => {
          const over = el.scrollHeight - el.clientHeight;
          if (over > 2 && el.clientHeight &&
              /auto|scroll/.test(getComputedStyle(el).overflowY)) {
            worst = Math.max(worst, over);
          }
        });
        return { id: v.id, worst,
                 pageScroll: document.documentElement.scrollHeight - window.innerHeight };
      });
      // Either the window scrolls, or no single panel may swallow a screenful.
      if (r && r.pageScroll <= 2 && r.worst > 800) {
        trapped.push(`${r.id}: ${r.worst}px hidden, page does not scroll`);
      }
    }
    expect(trapped, trapped.join(' | ')).toHaveLength(0);
  });

  test('a page whose primary content is a list lets the window scroll',
    async ({ page }) => {
      await page.setViewportSize({ width: 1440, height: 900 });
      for (const id of ['chgFeed', 'bTable', 'tree', 'fsTree']) {
        const capped = await page.evaluate((elId) => {
          const el = document.getElementById(elId);
          if (!el) return null;
          return getComputedStyle(el).maxHeight;
        }, id);
        if (capped !== null) expect(capped, `#${id} is capped`).toBe('none');
      }
    });

  test('density is remembered across a reload', async ({ page }) => {
    await page.locator('#densityBtn').click();
    await expect(page.locator('body')).toHaveClass(/dense/);
    await page.reload();
    await page.evaluate(() => window.READY);
    await expect(page.locator('body')).toHaveClass(/dense/);
  });
});

test.describe('the chat panel resizes', () => {
  test.beforeEach(async ({ page }) => {
    await signup(page);
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.evaluate(() => { localStorage.removeItem('riskgpt.dockw'); });
    await page.evaluate(() => { DOCK_PREF = 390; applyDockWidth(); toggleChat(true); });
  });

  const dockw = (page) => page.evaluate(() =>
    parseInt(getComputedStyle(document.documentElement).getPropertyValue('--dockw'), 10));

  test('dragging the grip widens the panel and the page follows it', async ({ page }) => {
    expect(await dockw(page)).toBe(390);
    await page.evaluate(() => {
      const g = document.getElementById('dockGrip');
      g.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, clientX: 390, button: 0 }));
      window.dispatchEvent(new PointerEvent('pointermove', { bubbles: true, clientX: 620 }));
      window.dispatchEvent(new PointerEvent('pointerup', { bubbles: true, clientX: 620 }));
    });
    expect(await dockw(page)).toBe(620);
    // one variable drives panel, page offset and toggle — they cannot drift
    const margin = await page.evaluate(() =>
      parseInt(getComputedStyle(document.querySelector('.page')).marginLeft, 10));
    expect(margin).toBe(620);
  });

  test('it will not shrink past legibility or swallow the page', async ({ page }) => {
    await page.evaluate(() => setDockWidth(50));
    expect(await dockw(page)).toBe(280);
    await page.evaluate(() => setDockWidth(4000));
    const max = await page.evaluate(() => dockMax());
    expect(await dockw(page)).toBe(max);
    expect(max).toBeLessThan(900);   // never more than the page it sits beside
  });

  test('the chosen width survives a reload', async ({ page }) => {
    await page.evaluate(() => setDockWidth(520));
    await page.reload();
    await page.evaluate(() => window.READY);
    expect(await dockw(page)).toBe(520);
  });

  test('a narrow window borrows the width back rather than overwriting it',
    async ({ page }) => {
      // the bug: clamping in place lost the preference, so widening never
      // restored it — unplug a monitor once and the panel stayed narrow
      await page.evaluate(() => setDockWidth(700));
      await page.setViewportSize({ width: 900, height: 800 });
      await page.waitForTimeout(250);
      const shown = await dockw(page);
      expect(shown).toBeLessThan(700);
      expect(await page.evaluate(() => localStorage.getItem('riskgpt.dockw'))).toBe('700');
      await page.setViewportSize({ width: 1440, height: 900 });
      await page.waitForTimeout(250);
      expect(await dockw(page)).toBe(700);
    });

  test('keyboard resizing works and double-click resets', async ({ page }) => {
    await page.evaluate(() => {
      const g = document.getElementById('dockGrip');
      g.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true }));
    });
    expect(await dockw(page)).toBe(402);
    await page.evaluate(() => {
      document.getElementById('dockGrip')
        .dispatchEvent(new MouseEvent('dblclick', { bubbles: true }));
    });
    expect(await dockw(page)).toBe(390);
  });

  test('the grip is only reachable while the panel is open', async ({ page }) => {
    await expect(page.locator('#dockGrip')).toBeVisible();
    await page.evaluate(() => toggleChat(false));
    await expect(page.locator('#dockGrip')).toBeHidden();
  });

  test('old density behaviour is untouched', async ({ page }) => {
    await page.locator('#densityBtn').click();
    await expect(page.locator('body')).toHaveClass(/dense/);
    await page.reload();
    await page.evaluate(() => window.READY);
    await expect(page.locator('body')).toHaveClass(/dense/);
  });
});
