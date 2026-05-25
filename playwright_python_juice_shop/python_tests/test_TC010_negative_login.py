import pytest
from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups
from test_data.users import INVALID_USER_EMAIL, INVALID_USER_PASSWORD


@pytest.mark.parametrize(
    "email_type,password_type,test_description",
    [
        (
            "valid",
            "invalid",
            "Valid email with invalid password",
        ),
        (
            "invalid",
            "valid",
            "Invalid email with valid password",
        ),
        (
            "invalid",
            "invalid",
            "Invalid email with invalid password",
        ),
    ],
)
def test_negative_login_combinations(
    page: Page,
    fresh_user,
    email_type: str,
    password_type: str,
    test_description: str,
):
    """
    Test goal:
    Verify that login fails for different negative username/password combinations.

    CI-friendly version:
    The valid user is created during the test run by the fresh_user fixture.
    """

    print(f"\nRunning scenario: {test_description}")

    valid_email = fresh_user["email"]
    valid_password = fresh_user["password"]

    if email_type == "valid":
        email = valid_email
    else:
        email = INVALID_USER_EMAIL

    if password_type == "valid":
        password = valid_password
    else:
        password = INVALID_USER_PASSWORD

    # STEP 1:
    # The fresh_user fixture leaves the browser on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 2:
    # Fill the email field using current test data.
    page.get_by_role(
        "textbox",
        name="Text field for the login email"
    ).fill(email)

    # STEP 3:
    # Fill the password field using current test data.
    page.get_by_role(
        "textbox",
        name="Text field for the login password"
    ).fill(password)

    # STEP 4:
    # Find the Login button by stable ID.
    login_button = page.locator("#loginButton")

    # STEP 5:
    # Verify Login button is visible and enabled.
    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    # STEP 6:
    # Click Login.
    login_button.click()

    # STEP 7:
    # Verify the error message is visible.
    expect(page.get_by_text("Invalid email or password.")).to_be_visible()

    # STEP 8:
    # Verify user remains on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()