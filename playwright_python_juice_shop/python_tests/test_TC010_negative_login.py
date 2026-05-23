import pytest
from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups
from test_data.users import (
    VALID_USER_EMAIL,
    VALID_USER_PASSWORD,
    INVALID_USER_EMAIL,
    INVALID_USER_PASSWORD,
)


@pytest.mark.parametrize(
    "email,password,test_description",
    [
        (
            VALID_USER_EMAIL,
            INVALID_USER_PASSWORD,
            "Valid email with invalid password",
        ),
        (
            INVALID_USER_EMAIL,
            VALID_USER_PASSWORD,
            "Invalid email with valid password",
        ),
        (
            INVALID_USER_EMAIL,
            INVALID_USER_PASSWORD,
            "Invalid email with invalid password",
        ),
    ],
)
def test_negative_login_combinations(page: Page, email: str, password: str, test_description: str):
    """
    Test goal:
    Verify that login fails for different negative username/password combinations.
    """

    # STEP 1:
    # Print the current scenario.
    # This is visible only when pytest is run with -s.
    print(f"\nRunning scenario: {test_description}")

    # STEP 2:
    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # STEP 3:
    # Make browser window large enough.
    page.set_viewport_size({"width": 1600, "height": 1000})

    # STEP 4:
    # Close welcome and cookie popups if they appear.
    close_startup_popups(page)

    # STEP 5:
    # Open the Account menu.
    page.get_by_role("button", name="Account").click()

    # STEP 6:
    # Click Login from the Account menu.
    page.get_by_role("menuitem", name="Login").click()

    # STEP 7:
    # Verify that the Login page is open.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 8:
    # Fill the email field using current test data.
    page.get_by_role(
        "textbox",
        name="Text field for the login email"
    ).fill(email)

    # STEP 9:
    # Fill the password field using current test data.
    page.get_by_role(
        "textbox",
        name="Text field for the login password"
    ).fill(password)

    # STEP 10:
    # Find the Login button by stable ID.
    login_button = page.locator("#loginButton")

    # STEP 11:
    # Verify Login button is visible and enabled.
    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    # STEP 12:
    # Click Login.
    login_button.click()

    # STEP 13:
    # Verify the error message is visible.
    expect(page.get_by_text("Invalid email or password.")).to_be_visible()

    # STEP 14:
    # Verify user remains on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()