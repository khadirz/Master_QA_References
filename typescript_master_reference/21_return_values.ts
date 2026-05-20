/*
21 - Return Values
return sends a value back to where the function was called.
*/
function calculateTotal(price: number, quantity: number): number {
  return price * quantity;
}
const total = calculateTotal(25, 3);
console.log(total);

function isAdult(age: number): boolean {
  return age >= 18;
}
console.log(isAdult(20));
console.log(isAdult(15));
