from datetime import datetime
import pytest
from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups


@pytest.fixture
def fresh_user(page: Page):
    """
    Fixture goal:
    Create a fresh user in Juice Shop and return the email/password.

    Why fixture?
    In CI, Juice Shop starts with a clean database.
    Old users from test_data/users.py may not exist.
    This fixture creates a new user during the test run.
    """

    # STEP 1:
    # Create unique user data.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    email = f"ci_user_{timestamp}@test.com"
    password = "Test12345!"
    security_answer = "Helsinki"

    # STEP 2:
    # Open Juice Shop.
    page.goto("http://localhost:3000")
    page.set_viewport_size({"width": 1600, "height": 1000})

    # STEP 3:
    # Close popups if they appear.
    close_startup_popups(page)

    # STEP 4:
    # Go to Login page.
    page.get_by_role("button", name="Account").click()
    page.get_by_role("menuitem", name="Login").click()

    # STEP 5:
    # Open registration page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    page.get_by_text("Not yet a customer?").click()

    # STEP 6:
    # Verify registration page is open.
    expect(page.get_by_role("heading", name="User Registration")).to_be_visible()

    # STEP 7:
    # Fill registration form.
    page.locator("#emailControl").fill(email)
    page.locator("#passwordControl").fill(password)
    page.locator("#repeatPasswordControl").fill(password)

    # STEP 8:
    # Select security question.
    page.locator("mat-select").first.click()
    page.locator("mat-option").first.click()

    # STEP 9:
    # Fill security answer.
    page.locator("#securityAnswerControl").fill(security_answer)

    # STEP 10:
    # Submit registration.
    register_button = page.locator("#registerButton")
    expect(register_button).to_be_visible()
    expect(register_button).to_be_enabled()
    register_button.click()

    # STEP 11:
    # Verify registration succeeded and Login page is shown.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 12:
    # Return user data to the test.
    return {
        "email": email,
        "password": password,
    }