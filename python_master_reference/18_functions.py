"""
18 - Functions
A function is a reusable block of code.
"""

def greet():
    print("Hello from a function!")

greet()


def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Khadir")


def add_numbers(num1, num2):
    result = num1 + num2
    return result

sum_result = add_numbers(5, 7)

print(sum_result)


def login(username, password):
    print(f"Typing username: {username}")
    print(f"Typing password: {password}")
    print("Clicking login button")

login("admin@juice-sh.op", "admin123")
