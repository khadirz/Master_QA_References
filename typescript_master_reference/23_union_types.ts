/*
23 - Union Types
Union type means a variable can accept more than one type.
*/
let userId: string | number;
userId = "ABC123";
console.log(userId);
userId = 123;
console.log(userId);

function printId(id: string | number): void {
  console.log(`ID is: ${id}`);
}
printId("USER-1");
printId(1001);
