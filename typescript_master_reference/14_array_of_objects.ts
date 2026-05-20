/*
14 - Array of Objects
Useful when we have many users, products, or test data rows.
*/
type User = {
  name: string;
  role: string;
  city: string;
};
const users: User[] = [
  { name: "Khadir", role: "QA Engineer", city: "Helsinki" },
  { name: "Jaakko", role: "CEO", city: "Turku" },
];
console.log(users);
console.log(users[0].name);
console.log(users[1].name);
for (const user of users) {
  console.log("-----");
  console.log(user.name);
  console.log(user.role);
  console.log(user.city);
}
