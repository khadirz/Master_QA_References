/*
18 - Functions
A function is a reusable block of code.
*/
function greet(): void {
  console.log("Hello from a function!");
}
greet();

function greetUser(name: string): void {
  console.log(`Hello, ${name}!`);
}
greetUser("Khadir");

function addNumbers(num1: number, num2: number): number {
  const result = num1 + num2;
  return result;
}
const sumResult = addNumbers(5, 7);
console.log(sumResult);

function login(username: string, password: string): void {
  console.log(`Typing username: ${username}`);
  console.log(`Typing password: ${password}`);
  console.log("Clicking login button");
}
login("admin@juice-sh.op", "admin123");
