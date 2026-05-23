from playwright.sync_api import Page, expect
from helpers.navigation_helper import open_juice_shop_homepage
from helpers.search_helper import search_product, verify_search_result_title


def test_search_for_non_existing_product(page: Page):
    """
    Test goal:
    Search for a product that does not exist
    and verify that Juice Shop shows 0 results.

    This version uses helper functions to keep the test clean.
    """

    # STEP 1:
    # Open Juice Shop homepage.
    open_juice_shop_homepage(page)

    # STEP 2:
    # Define a product name that should not exist.
    non_existing_product = "NonExistingProduct12345"

    # STEP 3:
    # Search for the non-existing product.
    search_product(page, non_existing_product)

    # STEP 4:
    # Verify the search result title shows our search keyword.
    verify_search_result_title(page, non_existing_product)

    # STEP 5:
    # Verify that the result count shows 0 results.
    # In your Juice Shop version, the pagination text shows "0 of 0".
    expect(page.get_by_text("0 of 0")).to_be_visible()