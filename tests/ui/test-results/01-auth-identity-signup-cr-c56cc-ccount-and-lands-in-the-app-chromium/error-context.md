# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: 01-auth.spec.js >> identity >> signup creates an account and lands in the app
- Location: specs/01-auth.spec.js:12:3

# Error details

```
Error: expect(locator).toHaveClass(expected) failed

Locator: locator('#v-myday')
Expected pattern: /on/
Received string:  "view"
Timeout: 7000ms

Call log:
  - Expect "toHaveClass" with timeout 7000ms
  - waiting for locator('#v-myday')
    18 × locator resolved to <div class="view" id="v-myday">…</div>
       - unexpected value "view"

```

```yaml
- text: R Regulatory Intelligence
- button "Home"
- button "🏛️ Regulatory"
- button "📰 Financial News"
- button "Ask"
- button "Personas"
- button "Health"
- text: Window
- combobox "Window":
  - option "7" [selected]
  - option "14"
  - option "30"
- text: Tester 1786137693124-4884
- button "Sign out"
- text: ✓ integrity clean
- button "＋ Add doc"
- button "▶ Run all"
- text: "as of 2026-08-07 live production database Market & Regulatory Intelligence This platform watches two things every day so you don't have to: what financial regulators publish, and what the financial press is reporting. Everything is collected automatically, kept with full history, and ordered by how much it matters to credit risk — not by how recent it is. 👋 New here? Start with one of the two lanes below. Each opens a summary page, and its own menu bar appears at the top with everything inside that lane — the sources it watches, the documents it holds, what changed recently, and how collection is running. Every chart is clickable: clicking a bar takes you to the documents behind it. × 7,018 documents held 30 + 25 regulators + news wires 772 policy PDFs parsed 384 critical-band rules 518 archived versions (audit) 94% collection pass rate Open → 🏛️"
- heading "Regulatory Intelligence" [level=2]
- paragraph: Binding rules, guidance, consultations and enforcement from 30 regulators across Canada, the US, EU & UK, APAC and the standard-setters — versioned, diffed and ranked by materiality.
- text: 5,969 documents 29/30 sources collecting 384 critical band Open → 📰
- heading "Financial News" [level=2]
- paragraph: Top stories from 25 verified financial news wires worldwide, refreshed daily and ranked through a credit-analyst lens — credit events and central banks first, noise last.
- text: 1,049 stories 25/25 wires collecting 338 latest day
- heading "Corpus by coverage area — 7,018 documents" [level=3]
- text: Canada 2,809 United States 1,463 EU & UK 508 APAC 228 International 961 Financial News 1,049 Click any area to browse its documents.
- heading "Regulatory materiality — deterministic score" [level=3]
- text: ⬤Critical 384 ⬤High 264 ⬤Medium 2,062 ⬤Low 3,259 score = doc-type base × regulator tier + topic + deadline proximity + revision size. Click a band to see those documents.
- heading "Where to start" [level=3]
- text: 1 · See what's urgent The highest-priority regulatory documents from the last 7 days, ranked by materiality.
- emphasis: Open the regulatory lane →
- text: 2 · Read this morning's news Today's stories from 25 financial wires, ordered by credit-risk relevance.
- emphasis: Open today's stories →
- text: 3 · Look something up Search the full library by regulator, topic, document type, priority or date.
- emphasis: Browse documents →
- heading "Financial news — daily volume" [level=3]
- text: 5 08-01 19 08-02 48 08-03 139 08-04 230 08-05 270 08-06 338 08-07 Click a day to open that day's ranked story feed.
- heading "Operational footprint" [level=3]
- text: Documents 7,018 Versions on file 7,536 Archived versions 518 Collection runs 127 94% of 127 runs succeeded · +446 documents in the last 1 day · every document carries its source URL and version history.
- button "✕"
```

# Test source

```ts
  1  | const { test, expect } = require('@playwright/test');
  2  | const { UI, newUser, signup, login } = require('./helpers');
  3  | 
  4  | test.describe('identity', () => {
  5  |   test('the app is gated: no session, no dashboard', async ({ page }) => {
  6  |     await page.goto(UI);
  7  |     await expect(page.locator('#authGate')).toBeVisible();
  8  |     // the dashboard behind it must not be readable
  9  |     await expect(page.locator('#xhTiles')).not.toBeVisible();
  10 |   });
  11 | 
  12 |   test('signup creates an account and lands in the app', async ({ page }) => {
  13 |     const user = await signup(page);
  14 |     await expect(page.locator('#whoami')).toContainText(user.name);
  15 |     // a signed-in user lands on their own page, not a generic dashboard
> 16 |     await expect(page.locator('#v-myday')).toHaveClass(/on/);
     |                                            ^ Error: expect(locator).toHaveClass(expected) failed
  17 |     await expect(page.locator('#mydayBody')).toContainText('Tell us what you follow');
  18 |   });
  19 | 
  20 |   test('a weak password is refused with a reason', async ({ page }) => {
  21 |     await page.goto(UI);
  22 |     await page.getByText('Create one').click();
  23 |     await page.locator('#authEmail').fill(newUser().email);
  24 |     await page.locator('#authPw').fill('short');
  25 |     await page.locator('#authGo').click();
  26 |     await expect(page.locator('#authErr')).toContainText('at least 10 characters');
  27 |     await expect(page.locator('#authGate')).toBeVisible();
  28 |   });
  29 | 
  30 |   test('a duplicate email is refused', async ({ page }) => {
  31 |     const user = await signup(page);
  32 |     await page.evaluate(() => authLogout());
  33 |     await page.waitForLoadState('load');
  34 |     await page.locator('#authGate').waitFor({ state: 'visible' });
  35 |     await page.getByText('Create one').click();
  36 |     await page.locator('#authEmail').fill(user.email);
  37 |     await page.locator('#authPw').fill('another-pass-99');
  38 |     await page.locator('#authGo').click();
  39 |     await expect(page.locator('#authErr')).toContainText('already exists');
  40 |   });
  41 | 
  42 |   test('wrong password is refused without revealing the account exists', async ({ page }) => {
  43 |     const user = await signup(page);
  44 |     await page.evaluate(() => authLogout());
  45 |     await page.locator('#authGate').waitFor({ state: 'visible' });
  46 |     await page.locator('#authEmail').fill(user.email);
  47 |     await page.locator('#authPw').fill('definitely-wrong-1');
  48 |     await page.locator('#authGo').click();
  49 |     await expect(page.locator('#authErr')).toContainText('Email or password is incorrect');
  50 |   });
  51 | 
  52 |   test('the session survives a reload, and sign-out ends it', async ({ page }) => {
  53 |     const user = await signup(page);
  54 |     await page.reload();
  55 |     await expect(page.locator('#authGate')).toBeHidden();
  56 |     await expect(page.locator('#whoami')).toContainText(user.name);
  57 |     await page.getByRole('button', { name: 'Sign out' }).click();
  58 |     await page.locator('#authGate').waitFor({ state: 'visible' });
  59 |   });
  60 | 
  61 |   test('the session cookie is httpOnly (not readable by scripts)', async ({ page, context }) => {
  62 |     await signup(page);
  63 |     const cookies = await context.cookies();
  64 |     const session = cookies.find(c => c.name === 'regagg_session');
  65 |     expect(session).toBeTruthy();
  66 |     expect(session.httpOnly).toBe(true);
  67 |     const visible = await page.evaluate(() => document.cookie);
  68 |     expect(visible).not.toContain('regagg_session');
  69 |   });
  70 | 
  71 |   test('login works in a brand-new browser context', async ({ browser }) => {
  72 |     const first = await browser.newContext();
  73 |     const p1 = await first.newPage();
  74 |     const user = await signup(p1);
  75 |     await first.close();
  76 | 
  77 |     const second = await browser.newContext();   // no cookies
  78 |     const p2 = await second.newPage();
  79 |     await login(p2, user);
  80 |     await expect(p2.locator('#whoami')).toContainText(user.name);
  81 |     await second.close();
  82 |   });
  83 | });
  84 | 
```