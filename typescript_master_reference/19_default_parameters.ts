/*
19 - Default Parameters
A function can use a default value if no value is provided.
*/
function sayHello(name: string = "Guest"): void {
  console.log(`Hello, ${name}`);
}
sayHello();
sayHello("Khadir");
