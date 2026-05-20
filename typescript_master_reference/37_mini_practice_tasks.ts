/*
37 - Mini Practice Tasks
Try these tasks yourself.
Solution examples are below each task.
*/

// Practice 1
const courseName = "TypeScript Basics";
console.log(courseName);

// Practice 2
function multiplyNumbers(num1: number, num2: number): number {
  return num1 * num2;
}
console.log(multiplyNumbers(4, 5));

// Practice 3
type Product = {
  name: string;
  price: number;
};

const product1: Product = { name: "Laptop", price: 1200 };
const product2: Product = { name: "Phone", price: 800 };

console.log(product1.name, product1.price);
console.log(product2.name, product2.price);

// Practice 4
class LoginPage {
  openPage(): void {
    console.log("Opening login page");
  }

  enterUsername(username: string): void {
    console.log(`Typing username: ${username}`);
  }

  enterPassword(password: string): void {
    console.log(`Typing password: ${password}`);
  }

  clickLogin(): void {
    console.log("Clicking login button");
  }
}

const loginPage = new LoginPage();
loginPage.openPage();
loginPage.enterUsername("admin@juice-sh.op");
loginPage.enterPassword("admin123");
loginPage.clickLogin();
