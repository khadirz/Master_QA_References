from playwright.sync_api import Page, expect
from helpers.navigation_helper import go_to_homepage
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    get_basket_count,
)


def test_add_product_with_logged_in_fixture(logged_in_page: Page):
    """
    Test goal:
    Verify that the logged_in_page fixture works.

    Flow:
    1. Fixture creates a fresh user
    2. Fixture logs in
    3. Test adds a product to basket
    4. Test verifies basket count is not decreased
    """

    # STEP 1:
    # Use the logged-in page from the fixture.
    page = logged_in_page

    # STEP 2:
    # Go to homepage after login.
    go_to_homepage(page)

    # STEP 3:
    # Verify homepage is visible.
    expect(page.get_by_text("All Products")).to_be_visible()

    # STEP 4:
    # Read basket count before adding product.
    basket_count_before = get_basket_count(page)

    # STEP 5:
    # Add first visible product to basket.
    add_first_visible_product_to_basket(page)

    # STEP 6:
    # Read basket count after adding product.
    basket_count_after = get_basket_count(page)

    # STEP 7:
    # Verify basket count did not decrease.
    assert basket_count_after >= basket_count_before