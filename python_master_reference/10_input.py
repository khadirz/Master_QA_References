"""
10 - Input
input() asks the user to type something.
In automation, we usually avoid input() because tests should run automatically.
"""

user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

print(f"{user_name}, In test automation, we usually pass fixed test data instead of using input().")
