from playwright.sync_api import Page, expect
from helpers.navigation_helper import go_to_homepage
from helpers.search_helper import search_product
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    verify_product_in_basket,
)


def test_add_specific_product_to_basket_with_logged_in_fixture(logged_in_page: Page):
    """
    Test goal:
    Use the logged_in_page fixture to search for Apple Juice,
    add it to basket,
    open the basket,
    and verify that Apple Juice is visible in the basket.

    Why this is CI-friendly:
    The logged_in_page fixture creates a fresh user and logs in during the test run.
    So the test does not depend on old local test data.
    """

    # STEP 1:
    # Use the page that is already logged in by the fixture.
    page = logged_in_page

    # STEP 2:
    # Go to homepage after login.
    go_to_homepage(page)

    # STEP 3:
    # Search for Apple Juice.
    search_product(page, "Apple Juice")

    # STEP 4:
    # Verify search result page is shown.
    expect(page.get_by_text("Search Results - Apple Juice")).to_be_visible()

    # STEP 5:
    # Add the first visible product to basket.
    # In Juice Shop search results, Apple Juice appears as the first result.
    # This avoids fragile locators that behave differently locally and in CI.
    add_first_visible_product_to_basket(page)

    # STEP 6:
    # Open basket.
    open_basket(page)

    # STEP 7:
    # Verify Apple Juice is listed in basket.
    # This confirms that the product added was Apple Juice.
    verify_product_in_basket(page, "Apple Juice (1000ml)")