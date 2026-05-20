/*
11 - Tuples
A tuple is an array with a fixed structure.
*/
const coordinates: [number, number] = [60.17, 24.94]; // latitude, longitude
console.log(coordinates);
console.log(coordinates[0]);
console.log(coordinates[1]);
const userInfo: [string, string, number] = ["Khadir", "QA Engineer", 40];
console.log(userInfo);
// userInfo[2] = "forty"; // Error because index 2 must be a number
