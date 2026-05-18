"""
27 - Basic Test-like Assertions
assert checks if something is True.
If it is False, Python raises an error.
"""

# Calculate 5 + 5 and save the result.
actual_result = 5 + 5

# Define what result we expect.
expected_result = 10

# Check if the actual result is equal to the expected result.
# If they are equal, the program continues.
# If they are not equal, Python stops and shows an AssertionError.
assert actual_result == expected_result

print("Assertion passed!")

# Now let's see what happens if the assertion fails.
actual_result_2 = 5 + 5 

expected_result_2= 10 

assert actual_result_2 == expected_result_2 

print("Assertion Failed!")