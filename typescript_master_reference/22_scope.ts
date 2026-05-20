/*
22 - Scope
Scope means where a variable can be used.
*/
const globalName = "Khadir";
function showName(): void {
  const localMessage = "Hello";
  console.log(localMessage, globalName);
}
showName();
// console.log(localMessage); // Error because it is local
