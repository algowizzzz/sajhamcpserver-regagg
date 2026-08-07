# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: 01-auth.spec.js >> identity >> signup creates an account and lands in the app
- Location: specs/01-auth.spec.js:12:3

# Error details

```
Error: expect(locator).toContainText(expected) failed

Locator: locator('#whoami')
Expected substring: "Tester 1786140808894-9906"
Received string:    "Sign out"
Timeout: 7000ms

Call log:
  - Expect "toContainText" with timeout 7000ms
  - waiting for locator('#whoami')
    18 × locator resolved to <span id="whoami">…</span>
       - unexpected value "Sign out"

```

```yaml
- button "Sign out"
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
> 14 |     await expect(page.locator('#whoami')).toContainText(user.name);
     |                                           ^ Error: expect(locator).toContainText(expected) failed
  15 |     // the app opens on Home; the lanes and their pages are one click away
  16 |     await expect(page.locator('#v-home')).toHaveClass(/on/);
  17 |     await expect(page.locator('#xhLanes .lane')).toHaveCount(2);
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