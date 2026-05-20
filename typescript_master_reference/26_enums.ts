/*
26 - Enums
Enum gives names to fixed values.
*/
enum TestStatus {
  Passed = "PASSED",
  Failed = "FAILED",
  Skipped = "SKIPPED",
}
const currentStatus: TestStatus = TestStatus.Passed;
console.log(currentStatus);
if (currentStatus === TestStatus.Passed) {
  console.log("Test passed successfully");
}
