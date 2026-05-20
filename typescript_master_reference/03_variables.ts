/*
03 - Variables
Variables store values.
*/
let nameValue = "Khadir"; // let means the value can be changed later
const country = "Finland"; // const means the value should not be reassigned
let age = 40; // TypeScript understands this is a number
let isTester = true; // TypeScript understands this is a boolean
console.log(nameValue);
console.log(country);
console.log(age);
console.log(isTester);
nameValue = "Jaakko"; // Allowed because nameValue was created with let
console.log(nameValue);
// country = "Sweden"; // This would cause an error because country is const
