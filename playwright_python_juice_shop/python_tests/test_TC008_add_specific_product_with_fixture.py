import pytest
from playwright.sync_api import Page, expect

from helpers.navigation_helper import go_to_homepage
from helpers.search_helper import search_product
from helpers.basket_helper import add_first_visible_product_to_basket
from pages.basket_page import BasketPage


@pytest.mark.basket
@pytest.mark.ci
def test_add_specific_product_to_basket_with_logged_in_fixture(logged_in_page: Page):
    """
    Test goal:
    Use the logged_in_page fixture to search for Apple Juice,
    add it to basket,
    open the basket,
    and verify that Apple Juice is visible in the basket.

    This test uses the BasketPage Page Object.
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
    add_first_visible_product_to_basket(page)

    # STEP 6:
    # Verify basket counter changed to 1.
    basket_page = BasketPage(page)
    basket_page.verify_basket_count("1")

    # STEP 7:
    # Open basket page.
    basket_page.open()

    # STEP 8:
    # Verify basket page is open.
    basket_page.verify_loaded()

    # STEP 9:
    # Verify Apple Juice is listed in basket.
    basket_page.verify_product_visible("Apple Juice (1000ml)")