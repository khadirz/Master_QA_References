"""
11 - Lists
A list stores multiple values.
Lists can be changed.
"""

fruits = ["apple", "banana", "orange"]

print(fruits)

print(fruits[0])  # First item

fruits.append("mango")  # Add item

print(fruits)

fruits.remove("banana")  # Remove item

print(fruits)

print(len(fruits))  # Count items

fruits[0] = "kiwi"  # Change first item

print(fruits)

if "orange" in fruits:
    print("Orange is in the list")
