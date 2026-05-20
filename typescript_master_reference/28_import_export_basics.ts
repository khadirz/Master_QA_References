/*
28 - Import and Export Basics
In real projects, code is usually split into files.

helpers.ts:
export function sayHello(name: string): void {
  console.log(`Hello, ${name}`);
}

main.ts:
import { sayHello } from "./helpers";
sayHello("Khadir");
*/
console.log("Import/export is used to share code between files.");
