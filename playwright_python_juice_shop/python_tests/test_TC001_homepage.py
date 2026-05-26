from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups
import pytest

@pytest.mark.smoke
@pytest.mark.ci

def test_homepage_loads_successfully(page: Page):
    """
    Test goal:
    Open OWASP Juice Shop and verify that the homepage is loaded.
    """

    # STEP 1:
    # Open the local Juice Shop application.
    # This assumes Docker Juice Shop is already running on port 3000.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Close welcome and cookie popups if they appear.
    # We moved this logic into a helper function to keep the test clean.
    close_startup_popups(page)

    # STEP 3:
    # Verify that the browser title is correct.
    # This confirms we opened the correct application.
    expect(page).to_have_title("OWASP Juice Shop")

    # STEP 4:
    # Verify that the product section is visible.
    # This confirms the homepage content loaded successfully.
    expect(page.get_by_text("All Products")).to_be_visible()
    