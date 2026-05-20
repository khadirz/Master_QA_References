/*
27 - Error Handling
try/catch helps us handle errors safely.
*/
try {
  const jsonText = '{"name": "Khadir"}';
  const user = JSON.parse(jsonText);
  console.log(user.name);
} catch (error) {
  console.log("Could not parse JSON");
}
try {
  throw new Error("Something went wrong");
} catch (error) {
  console.log("Error was handled");
}
