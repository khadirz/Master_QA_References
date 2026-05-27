import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.ci
def test_login_with_fresh_user(page: Page, fresh_user):
    """
    Test goal:
    Create a fresh user using a fixture,
    then log in with that user.

    This test uses the LoginPage Page Object.
    """

    # STEP 1:
    # Get user data from the fixture.
    email = fresh_user["email"]
    password = fresh_user["password"]

    # STEP 2:
    # The fresh_user fixture leaves us on the Login page.
    login_page = LoginPage(page)

    # STEP 3:
    # Login with fresh user.
    login_page.login(
        email=email,
        password=password
    )

    # STEP 4:
    # Verify login succeeded.
    login_page.verify_login_successful()