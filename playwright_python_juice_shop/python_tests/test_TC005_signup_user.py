from datetime import datetime
from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups


def test_signup_new_user(page: Page):
    """
    Test goal:
    Create a new user account in OWASP Juice Shop.

    Important:
    This test creates a new random email every time.
    The email is printed in the terminal so we can use it in the login test.
    """

    # STEP 1:
    # Create a unique email using the current date and time.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    email = f"test_user_{timestamp}@test.com"

    # STEP 2:
    # Define password and security answer.
    password = "Test12345!"
    security_answer = "Helsinki"

    # STEP 3:
    # Print the user early.
    # This way, even if registration fails later, we still see what data was used.
    print("\nCreated user email:", email)
    print("Created user password:", password)

    # STEP 4:
    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # STEP 5:
    # Make browser large enough.
    page.set_viewport_size({"width": 1600, "height": 1000})

    # STEP 6:
    # Close welcome and cookie popups if they appear.
    close_startup_popups(page)

    # STEP 7:
    # Open the Account menu.
    page.get_by_role("button", name="Account").click()

    # STEP 8:
    # Click Login because the registration link is on the Login page.
    page.get_by_role("menuitem", name="Login").click()

    # STEP 9:
    # Verify that the Login page is open.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 10:
    # Click the registration link.
    page.get_by_text("Not yet a customer?").click()

    # STEP 11:
    # Verify that the User Registration page is open.
    expect(page.get_by_role("heading", name="User Registration")).to_be_visible()

    # STEP 12:
    # Fill email field.
    page.locator("#emailControl").fill(email)

    # STEP 13:
    # Fill password field.
    page.locator("#passwordControl").fill(password)

    # STEP 14:
    # Fill repeat password field.
    page.locator("#repeatPasswordControl").fill(password)

    # STEP 15:
    # Open the security question dropdown.
    page.locator("mat-select").first.click()

    # STEP 16:
    # Select the first available security question.
    page.locator("mat-option").first.click()

    # STEP 17:
    # Fill security answer.
    page.locator("#securityAnswerControl").fill(security_answer)

    # STEP 18:
    # Find the Register button by stable ID.
    register_button = page.locator("#registerButton")

    # STEP 19:
    # Make sure the Register button is visible and enabled.
    expect(register_button).to_be_visible()
    expect(register_button).to_be_enabled()

    # STEP 20:
    # Click Register.
    register_button.click()

    # STEP 21:
    # Verify registration was successful.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 22:
    # Print again after successful registration.
    print("\nSIGNUP SUCCESSFUL")
    print("Use this email in TC006:", email)
    print("Use this password in TC006:", password)