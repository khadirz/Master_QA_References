from playwright.sync_api import Page, expect


def login_to_juice_shop(page: Page, email: str, password: str):
    """
    Helper goal:
    Log in to OWASP Juice Shop with the given email and password.

    Why helper?
    Login is needed in several tests, so we keep the login steps in one reusable place.
    """

    # STEP 1:
    # Click the Account button in the top menu.
    page.get_by_role("button", name="Account").click()

    # STEP 2:
    # Click the Login option from the account menu.
    page.get_by_role("menuitem", name="Login").click()

    # STEP 3:
    # Verify that the Login page is opened.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 4:
    # Fill the email field.
    page.get_by_role(
        "textbox",
        name="Text field for the login email"
    ).fill(email)

    # STEP 5:
    # Fill the password field.
    page.get_by_role(
        "textbox",
        name="Text field for the login password"
    ).fill(password)

    # STEP 6:
    # Find the login button by ID.
    # This is more stable than using button text.
    login_button = page.locator("#loginButton")

    # STEP 7:
    # Make sure the login button is visible.
    expect(login_button).to_be_visible()

    # STEP 8:
    # Make sure the login button is enabled.
    # If this fails, email/password fields may be empty or invalid.
    expect(login_button).to_be_enabled()

    # STEP 9:
    # Click the login button.
    login_button.click()

    # STEP 10:
    # Verify that login was successful.
    # After login, Your Basket should be visible.
    expect(page.get_by_text("Your Basket")).to_be_visible()