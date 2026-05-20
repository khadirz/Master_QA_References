/*
29 - Basic Test-like Assertions
In real test tools, we use expect/assert.
Here we create a simple check manually.
*/
const actualResult = 5 + 5;
const expectedResult = 10;
if (actualResult !== expectedResult) {
  throw new Error("Test failed: result is not correct");
}
console.log("Assertion passed!");
