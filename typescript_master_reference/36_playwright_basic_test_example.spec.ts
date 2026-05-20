/*
36 - Playwright Basic Test Example
This is a real-looking Playwright test example.

To run this in a real project:
npm init playwright@latest
npx playwright test
*/
import { test, expect } from "@playwright/test";

test("open Juice Shop login page", async ({ page }) => {
  await page.goto("http://localhost:3000/#/login");
  await expect(page).toHaveURL(/login/);
});

test("type login credentials", async ({ page }) => {
  await page.goto("http://localhost:3000/#/login");
  await page.locator("#email").fill("admin@juice-sh.op");
  await page.locator("#password").fill("admin123");
  await page.locator("#loginButton").click();
});
