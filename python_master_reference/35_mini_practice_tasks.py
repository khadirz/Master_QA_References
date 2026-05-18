"""
35 - Mini Practice Tasks
Try these tasks yourself.
The solution examples are below each task.
"""

print("=====================================")
# Practice 1:
# Create a variable called course_name and store "Python Basics" inside it.
# Then print it.

# Store the course name in a variable.
course_name = "Python Basics"

print(course_name)

print("=====================================")
# Practice 2:
# Create a function called multiply_numbers that takes two numbers and returns their multiplication.

# Create a function that receives two numbers.
def multiply_numbers(num1, num2):

    # Multiply the two numbers and return the result.
    return num1 * num2


# Call the function with 4 and 5.
print(multiply_numbers(4, 5))

print("=====================================")
# Practice 3:
# Create a class called Product.
# It should have name and price attributes.
# Create two product objects and print their names and prices.

# Create a Product class.
class Product:

    # This method runs automatically when we create a new Product object.
    def __init__(self, name, price):

        # Store the product name inside the object.
        self.name = name

        # Store the product price inside the object.
        self.price = price


# Create the first product object.
product1 = Product("Laptop", 1200)

# Create the second product object.
product2 = Product("Phone", 800)

print(product1.name, product1.price)

print(product2.name, product2.price)

print("=====================================")
# Practice 4:
# Create a LoginPage object and call its methods in the correct order.

# Create a LoginPage class.
class LoginPage:

    # Create a method to open the login page.
    def open_page(self):
        print("Opening login page")

    # Create a method to enter the username.
    def enter_username(self, username):
        print(f"Typing username: {username}")

    # Create a method to enter the password.
    def enter_password(self, password):
        print(f"Typing password: {password}")

    # Create a method to click the login button.
    def click_login(self):
        print("Clicking login button")


# Create a LoginPage object.
login_page = LoginPage()

# Call the login page methods in the correct order.
login_page.open_page()

login_page.enter_username("admin@juice-sh.op")

login_page.enter_password("admin123")

login_page.click_login()