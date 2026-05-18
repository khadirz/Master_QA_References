"""
22 - Error Handling
try/except helps us handle errors safely.
"""

# Try to run this block of code.
# If something goes wrong, Python can handle the error using except.
try:
    # Convert the text "123" into an integer number.
    # This works because "123" is a valid number.
    number = int("123")

    print(number)

# This block runs only if Python cannot convert the text into a number.
except ValueError:
    print("Could not convert text to number")


# Try to run another block of code.
try:
    # Try to divide 10 by 0.
    # This will cause an error because division by zero is not allowed.
    result = 10 / 0

# This block runs only if a division by zero error happens.
except ZeroDivisionError:
    # Print a friendly error message.
    print("You cannot divide by zero")

# The finally block always runs.
# It runs whether there was an error or not.
finally:
    # Print this message every time.
    print("This always runs")