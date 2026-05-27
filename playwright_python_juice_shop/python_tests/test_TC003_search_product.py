import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage


@pytest.mark.ci
@pytest.mark.smoke
def test_search_for_apple_juice(page: Page):
    """
    Test goal:
    Search for Apple Juice in OWASP Juice Shop and verify the result.

    This test uses the HomePage Page Object.
    """

    # STEP 1:
    # Create HomePage object.
    home_page = HomePage(page)

    # STEP 2:
    # Open Juice Shop homepage.
    home_page.open()

    # STEP 3:
    # Verify homepage is loaded.
    home_page.verify_loaded()

    # STEP 4:
    # Search for Apple Juice.
    home_page.search_product("Apple Juice")

    # STEP 5:
    # Verify Apple Juice result is visible.
    home_page.verify_product_result_visible("Apple Juice (1000ml)")