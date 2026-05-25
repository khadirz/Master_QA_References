import pytest
from playwright.sync_api import Page, expect
from test_data.users import INVALID_USER_PASSWORD


@pytest.mark.parametrize(
    "email_value,password_value,test_description",
    [
        (
            "",
            "",
            "Empty email and empty password",
        ),
        (
            "valid_email",
            "",
            "Valid email and empty password",
        ),
        (
            "",
            "valid_password",
            "Empty email and valid password",
        ),
    ],
)
def test_login_button_disabled_for_empty_required_fields(
    page: Page,
    fresh_user,
    email_value: str,
    password_value: str,
    test_description: str,
):
    """
    Test goal:
    Verify that the Login button stays disabled
    when required fields are empty.

    CI-friendly version:
    The valid email/password come from the fresh_user fixture.
    """

    print(f"\nRunning scenario: {test_description}")

    # STEP 1:
    # Get fresh user data created during this test run.
    valid_email = fresh_user["email"]
    valid_password = fresh_user["password"]

    # STEP 2:
    # The fresh_user fixture leaves the browser on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 3:
    # Locate email and password fields.
    email_field = page.get_by_role(
        "textbox",
        name="Text field for the login email"
    )

    password_field = page.get_by_role(
        "textbox",
        name="Text field for the login password"
    )

    # STEP 4:
    # Decide what email value to use.
    if email_value == "valid_email":
        email = valid_email
    else:
        email = email_value

    # STEP 5:
    # Decide what password value to use.
    if password_value == "valid_password":
        password = valid_password
    else:
        password = password_value

    # STEP 6:
    # Fill email if value is not empty.
    if email:
        email_field.fill(email)

    # STEP 7:
    # Fill password if value is not empty.
    if password:
        password_field.fill(password)

    # STEP 8:
    # Locate Login button.
    login_button = page.locator("#loginButton")

    # STEP 9:
    # Verify Login button is visible.
    expect(login_button).to_be_visible()

    # STEP 10:
    # Verify Login button is disabled.
    expect(login_button).to_be_disabled()


def test_invalid_email_format_shows_login_error(page: Page, fresh_user):
    """
    Test goal:
    Verify that login fails when the email format is invalid.

    CI-friendly version:
    The password comes from the fresh_user fixture.
    """

    # STEP 1:
    # Get fresh user password.
    valid_password = fresh_user["password"]

    # STEP 2:
    # The fresh_user fixture leaves the browser on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 3:
    # Locate email and password fields.
    email_field = page.get_by_role(
        "textbox",
        name="Text field for the login email"
    )

    password_field = page.get_by_role(
        "textbox",
        name="Text field for the login password"
    )

    # STEP 4:
    # Type an invalid email format.
    email_field.fill("invalid_email_format")

    # STEP 5:
    # Fill password.
    password_field.fill(valid_password)

    # STEP 6:
    # Locate the Login button.
    login_button = page.locator("#loginButton")

    # STEP 7:
    # In this Juice Shop version, the button becomes enabled.
    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()

    # STEP 8:
    # Click Login.
    login_button.click()

    # STEP 9:
    # Verify the app rejects the login attempt.
    expect(page.get_by_text("Invalid email or password.")).to_be_visible()

    # STEP 10:
    # Verify user remains on the Login page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()