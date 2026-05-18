"""
25 - List Comprehension
A short way to create a new list.
"""

# Create a list of numbers.
numbers = [1, 2, 3, 4, 5]

# Create a new list where each number is multiplied by itself.
squares = [number * number for number in numbers]

print(squares)

# Create a new list that contains only even numbers.
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


"""
Same program but longer way without list comprehension.

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)


even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
"""