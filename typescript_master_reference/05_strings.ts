/*
05 - Strings
String means text.
*/
const firstName = "Khadir";
const lastName = "Zavareh";
const fullName = firstName + " " + lastName; // Join strings
console.log(fullName);
const message = `My name is ${firstName}.`; // Template literal
console.log(message);
const sentence = "TypeScript is useful for test automation.";
console.log(sentence.toUpperCase()); // Uppercase
console.log(sentence.toLowerCase()); // Lowercase
console.log(sentence.replace("TypeScript", "Playwright")); // Replace text
console.log(sentence.length); // Count characters
console.log(sentence[0]); // First character
console.log(sentence.slice(0, 10)); // Characters from index 0 to 9
