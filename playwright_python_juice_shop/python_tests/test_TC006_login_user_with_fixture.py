from playwright.sync_api import Page, expect
from helpers.login_helper import login_to_juice_shop


def test_login_with_fresh_user(page: Page, fresh_user):
    """
    Test goal:
    Create a fresh user using a fixture,
    then log in with that user.

    This is CI-friendly because it does not depend on old saved test data.
    """

    # STEP 1:
    # Get user data from the fixture.
    email = fresh_user["email"]
    password = fresh_user["password"]

    # STEP 2:
    # The fresh_user fixture leaves us on the Login page.
    # So we can use the login helper directly.
    login_to_juice_shop(
        page,
        email=email,
        password=password
    )

    # STEP 3:
    # Verify login succeeded.
    expect(page.get_by_text("Your Basket")).to_be_visible()