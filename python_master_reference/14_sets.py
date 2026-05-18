"""
14 - Sets
A set stores only unique values.
"""

unique_numbers = {1, 2, 3, 3, 4}

print(unique_numbers)  # Duplicate 3 appears only once

unique_numbers.add(5)

print(unique_numbers)

unique_numbers.remove(2)

print(unique_numbers)
