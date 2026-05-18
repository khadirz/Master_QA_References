"""
32 - OOP Example for Test Automation: Login Page
This shows how Page Object thinking works.
"""

# Create a class for the Juice Shop login page.
# This class represents one page in the application.
class JuiceShopLoginPage:

    # This method runs automatically when we create a new login page object.
    def __init__(self):

        # Store the login page URL inside the object.
        self.url = "http://localhost:3000/#/login"

    # Create a method to open the login page.
    def open_page(self):

        # In real automation, this would open the browser page.
        print(f"Opening page: {self.url}")

    # Create a method to enter the username or email.
    def enter_username(self, email):

        # In real automation, this would type the email into the email field.
        print(f"Typing '{email}' into the email field")

    # Create a method to enter the password.
    def enter_password(self, password):

        # In real automation, this would type the password into the password field.
        print(f"Typing '{password}' into the password field")

    # Create a method to click the login button.
    def click_login(self):

        # In real automation, this would click the login button.
        print("Clicking the login button")


# Create one login page object from the JuiceShopLoginPage class.
my_login_page = JuiceShopLoginPage()

# Open the login page.
my_login_page.open_page()

# Enter the email address.
my_login_page.enter_username("admin@juice-sh.op")

# Enter the password.
my_login_page.enter_password("admin123")

# Click the login button.
my_login_page.click_login()