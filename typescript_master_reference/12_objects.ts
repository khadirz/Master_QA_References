/*
12 - Objects
Objects store data as key-value pairs.
Similar idea to Python dictionaries.
*/
const user = {
  name: "Khadir",
  role: "QA Engineer",
  city: "Helsinki",
};
console.log(user);
console.log(user.name); // Dot notation
console.log(user["role"]); // Bracket notation
user.city = "Espoo"; // Update value
console.log(user);
// user.company = "JT Testing"; // Error because company was not defined
