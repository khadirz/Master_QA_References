/*
13 - Object Types
TypeScript can define the shape of an object.
*/
type User = {
  name: string;
  role: string;
  city: string;
};
const user1: User = {
  name: "Khadir",
  role: "QA Engineer",
  city: "Helsinki",
};
const user2: User = {
  name: "Jaakko",
  role: "CEO",
  city: "Turku",
};
console.log(user1);
console.log(user2);
console.log(user1.name);
console.log(user2.city);
