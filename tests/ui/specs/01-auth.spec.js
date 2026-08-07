const { test, expect } = require('@playwright/test');
const { UI, newUser, signup, login } = require('./helpers');

test.describe('identity', () => {
  test('the app is gated: no session, no dashboard', async ({ page }) => {
    await page.goto(UI);
    await expect(page.locator('#authGate')).toBeVisible();
    // the dashboard behind it must not be readable
    await expect(page.locator('#xhTiles')).not.toBeVisible();
  });

  test('signup creates an account and lands in the app', async ({ page }) => {
    const user = await signup(page);
    await expect(page.locator('#whoami')).toContainText(user.name);
    await expect(page.locator('#xhTiles .tile').first()).toBeVisible();
  });

  test('a weak password is refused with a reason', async ({ page }) => {
    await page.goto(UI);
    await page.getByText('Create one').click();
    await page.locator('#authEmail').fill(newUser().email);
    await page.locator('#authPw').fill('short');
    await page.locator('#authGo').click();
    await expect(page.locator('#authErr')).toContainText('at least 10 characters');
    await expect(page.locator('#authGate')).toBeVisible();
  });

  test('a duplicate email is refused', async ({ page }) => {
    const user = await signup(page);
    await page.evaluate(() => authLogout());
    await page.waitForLoadState('load');
    await page.locator('#authGate').waitFor({ state: 'visible' });
    await page.getByText('Create one').click();
    await page.locator('#authEmail').fill(user.email);
    await page.locator('#authPw').fill('another-pass-99');
    await page.locator('#authGo').click();
    await expect(page.locator('#authErr')).toContainText('already exists');
  });

  test('wrong password is refused without revealing the account exists', async ({ page }) => {
    const user = await signup(page);
    await page.evaluate(() => authLogout());
    await page.locator('#authGate').waitFor({ state: 'visible' });
    await page.locator('#authEmail').fill(user.email);
    await page.locator('#authPw').fill('definitely-wrong-1');
    await page.locator('#authGo').click();
    await expect(page.locator('#authErr')).toContainText('Email or password is incorrect');
  });

  test('the session survives a reload, and sign-out ends it', async ({ page }) => {
    const user = await signup(page);
    await page.reload();
    await expect(page.locator('#authGate')).toBeHidden();
    await expect(page.locator('#whoami')).toContainText(user.name);
    await page.getByRole('button', { name: 'Sign out' }).click();
    await page.locator('#authGate').waitFor({ state: 'visible' });
  });

  test('the session cookie is httpOnly (not readable by scripts)', async ({ page, context }) => {
    await signup(page);
    const cookies = await context.cookies();
    const session = cookies.find(c => c.name === 'regagg_session');
    expect(session).toBeTruthy();
    expect(session.httpOnly).toBe(true);
    const visible = await page.evaluate(() => document.cookie);
    expect(visible).not.toContain('regagg_session');
  });

  test('login works in a brand-new browser context', async ({ browser }) => {
    const first = await browser.newContext();
    const p1 = await first.newPage();
    const user = await signup(p1);
    await first.close();

    const second = await browser.newContext();   // no cookies
    const p2 = await second.newPage();
    await login(p2, user);
    await expect(p2.locator('#whoami')).toContainText(user.name);
    await second.close();
  });
});
