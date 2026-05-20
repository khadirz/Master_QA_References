/*
24 - Type Aliases
type lets us create our own type names.
*/
type LoginStatus = "success" | "failed" | "locked";
let statusValue: LoginStatus = "success";
console.log(statusValue);
statusValue = "failed";
console.log(statusValue);
// statusValue = "unknown"; // Error
