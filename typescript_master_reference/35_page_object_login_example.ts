/*
35 - Page Object Example: Login Page
This is similar to what we use in Playwright automation.
*/
class JuiceShopLoginPage {
  url: string;

  constructor() {
    this.url = "http://localhost:3000/#/login";
  }

  openPage(): void {
    console.log(`Opening page: ${this.url}`);
  }

  enterUsername(email: string): void {
    console.log(`Typing '${email}' into the email field`);
  }

  enterPassword(password: string): void {
    console.log(`Typing '${password}' into the password field`);
  }

  clickLogin(): void {
    console.log("Clicking the login button");
  }
}

const myLoginPage = new JuiceShopLoginPage();
myLoginPage.openPage();
myLoginPage.enterUsername("admin@juice-sh.op");
myLoginPage.enterPassword("admin123");
myLoginPage.clickLogin();
