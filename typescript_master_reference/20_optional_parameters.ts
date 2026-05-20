/*
20 - Optional Parameters
The ? means the parameter is optional.
*/
function createUser(name: string, role?: string): void {
  console.log(`Name: ${name}`);
  if (role) {
    console.log(`Role: ${role}`);
  } else {
    console.log("Role was not provided");
  }
}
createUser("Khadir", "QA Engineer");
createUser("Jaakko");
