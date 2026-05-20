/*
17 - Break and Continue
break stops a loop.
continue skips the current round.
*/
for (let number = 0; number < 10; number++) {
  if (number === 5) {
    break;
  }
  console.log(number);
}
console.log("Second loop");
for (let number = 0; number < 5; number++) {
  if (number === 2) {
    continue;
  }
  console.log(number);
}
