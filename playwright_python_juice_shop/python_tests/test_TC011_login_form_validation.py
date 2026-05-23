import pytest
from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def open_login_page(page: Page):
    """
    Helper goal:
    Open Juice Shop login page.

    Why helper?
    TC011 has several validation tests.
    Each test needs to start from the login page.
    """

    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # Make browser window large enough.
    page.set_viewport_size({"width": 1600, "height": 1000})

    # Close startup popups if they appear.
    close_startup_popups(page)

    # Open Account menu.
    page.get_by_role("button", name="Account").click()

    # Click Login from the Account menu.
    page.get_by_role("menuitem", name="Login").click()

    # Verify Login page is visible.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()


@pytest.mark.parametrize(
    "email,password,test_description",
    [
        (
            "",
            "",
            "Empty email and empty password",
        ),
        (
            VALID_USER_EMAIL,
            "",
            "Valid email and empty password",
        ),
        (
            "",
            VALID_USER_PASSWORD,
            "Empty email and valid password",
        ),
    ],
)
def test_login_button_disabled_for_empty_required_fields(
    page: Page,
    email: str,
    password: str,
    test_description: str
):
    """
    Test goal:
    Verify that the Login button stays disabled
    when required fields are empty.
    """

    # Print current scenario.
    print(f"\nRunning scenario: {test_description}")

    # STEP 1:
    # Open Login page.
    open_login_page(page)

    # STEP 2:
    # Locate email and password fields.
    email_field = page.get_by_role(
        "textbox",
        name="Text field for the login email"
    )

    password_field = page.get_by_role(
        "textbox",
        name="Text field for the login password"
    )

    # STEP 3:
    # Fill email if test data contains an email.
    # If email is empty, we leave the field empty.
    if email:
        email_field.fill(email)

    # STEP 4:
    # Fill password if test data contains a password.
    # If password is empty, we leave the field empty.
    if password:
        password_field.fill(password)

    # STEP 5:
    # Locate the Login button.
    login_button = page.locator("#loginButton")

    # STEP 6:
    # Verify the Login button is visible.
    expect(login_button).to_be_visible()

    # STEP 7:
    # Verify the Login button is disabled.
    # This means the form cannot be submitted with missing required fields.
    expect(login_button).to_be_disabled()


def test_invalid_email_format_shows_login_error(page: Page):
    """
    Test goal:
    Verify that login fails when the email format is invalid.

    Important:
    In this Juice Shop version, the Login button still becomes enabled
    even when the email format is invalid.
    So we click Login and verify the error message.
    """

    # STEP 1:
    # Open Login page.
    open_login_page(page)

    # STEP 2:
    # Locate email and password fields.
    email_field = page.get_by_role(
        "textbox",
        name="Text field for the login email"
    )

    password_field = page.get_by_role(
        "textbox",
        name="Text field for the login password"
    )

    # STEP 3:
    # Type an invalid email format.
    email_field.fill("invalid_email_format")

    # STEP 4:
    # Fill password.
    password_field.fill(VALID_USER_PASSWORD)

    # STEP 5:
    # Locate the Login button.
    login_button = page.locator("#loginButton")

    # STEP 6:
    # In this app version, the button is enabled.
    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    # STEP 7:
    # Click Login.
    login_button.click()

    # STEP 8:
    # Verify the app rejects the login attempt.
    expect(page.get_by_text("Invalid email or password.")).to_be_visible()

    # STEP 9:
    # Verify user remains on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()