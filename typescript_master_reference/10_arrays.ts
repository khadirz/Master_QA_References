/*
10 - Arrays
An array stores multiple values.
*/
const fruits: string[] = ["apple", "banana", "orange"];
console.log(fruits);
console.log(fruits[0]); // First item
fruits.push("mango"); // Add item
console.log(fruits);
const index = fruits.indexOf("banana"); // Find item position
if (index !== -1) {
  fruits.splice(index, 1); // Remove one item
}
console.log(fruits);
console.log(fruits.length); // Count items
fruits[0] = "kiwi"; // Change first item
console.log(fruits);
if (fruits.includes("orange")) {
  console.log("Orange is in the array");
}
