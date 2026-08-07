// Shared helpers: a fresh account per run so tests never collide.
const UI = '/api/regagg/ui';

function newUser() {
  const n = Date.now() + '-' + Math.floor(Math.random() * 1e4);
  return { email: `t${n}@bank.test`, password: 'correct-horse-9', name: `Tester ${n}` };
}

async function signup(page, user = newUser()) {
  await page.goto(UI);
  await page.locator('#authGate').waitFor({ state: 'visible' });
  await page.getByText('Create one').click();
  await page.locator('#authName').fill(user.name);
  await page.locator('#authEmail').fill(user.email);
  await page.locator('#authPw').fill(user.password);
  await page.locator('#authGo').click();
  await page.locator('#authGate').waitFor({ state: 'hidden' });
  await page.waitForFunction(() => window.READY !== undefined);
  await page.evaluate(() => window.READY);   // core data loaded
  return user;
}

async function login(page, user) {
  await page.goto(UI);
  await page.locator('#authGate').waitFor({ state: 'visible' });
  await page.locator('#authEmail').fill(user.email);
  await page.locator('#authPw').fill(user.password);
  await page.locator('#authGo').click();
  await page.locator('#authGate').waitFor({ state: 'hidden' });
  await page.evaluate(() => window.READY);
}

module.exports = { UI, newUser, signup, login };
