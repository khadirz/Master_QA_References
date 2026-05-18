"""
33 - Common Python Naming Style
Python has common naming conventions.
"""

# Variable names usually use snake_case.
# snake_case means lowercase words separated by underscore.
user_email = "admin@juice-sh.op"

# Function names also usually use snake_case.
def click_button():

    print("Button clicked")


# Class names usually use PascalCase.
# PascalCase means each word starts with a capital letter.
class LoginPage:

    # pass means do nothing for now.
    # It is used when Python needs some code here, but we want to leave it empty.
    pass


# Call the click_button function.
click_button()

# Create an object from the LoginPage class.
page = LoginPage()

print(user_email)