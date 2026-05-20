/*
30 - Async and Await
Many automation actions are asynchronous.
*/
function waitOneSecond(): Promise<string> {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Finished waiting");
    }, 1000);
  });
}

async function runExample(): Promise<void> {
  console.log("Before waiting");
  const result = await waitOneSecond();
  console.log(result);
  console.log("After waiting");
}
runExample();
