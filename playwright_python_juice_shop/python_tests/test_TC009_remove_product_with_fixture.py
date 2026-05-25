from playwright.sync_api import Page, expect
from helpers.navigation_helper import go_to_homepage
from helpers.search_helper import search_product
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    verify_product_in_basket,
    remove_product_from_basket,
)


def test_remove_product_from_basket_with_logged_in_fixture(logged_in_page: Page):
    """
    Test goal:
    Use the logged_in_page fixture to add Apple Juice to basket,
    remove it from the basket,
    and verify that it is removed.

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
    # After searching Apple Juice, the first result should be Apple Juice.
    add_first_visible_product_to_basket(page)

    # STEP 6:
    # Wait until basket counter shows 1.
    expect(page.locator(".fa-layers-counter")).to_have_text("1")

    # STEP 7:
    # Open basket.
    open_basket(page)

    # STEP 8:
    # Reload basket page to make sure basket table data is refreshed.
    page.reload()

    # STEP 9:
    # Verify basket page is still open.
    expect(page.get_by_role("heading", name="Your Basket", exact=False)).to_be_visible()

    # STEP 10:
    # Verify Apple Juice is in basket before removing it.
    verify_product_in_basket(page, "Apple Juice (1000ml)")

    # STEP 11:
    # Remove Apple Juice from basket.
    remove_product_from_basket(page, "Apple Juice (1000ml)")