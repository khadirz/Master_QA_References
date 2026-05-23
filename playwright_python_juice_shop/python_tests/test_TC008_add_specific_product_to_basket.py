from playwright.sync_api import Page, expect
from helpers.navigation_helper import open_juice_shop_homepage, go_to_homepage
from helpers.login_helper import login_to_juice_shop
from helpers.search_helper import search_product
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    get_basket_count,
    verify_product_in_basket,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def test_add_specific_product_to_basket(page: Page):
    """
    Test goal:
    Log in to Juice Shop, search for Apple Juice,
    add Apple Juice to the basket,
    and verify that Apple Juice is visible in the basket.

    This version uses helper functions to keep the test clean.
    """

    # STEP 1:
    # Open Juice Shop homepage.
    open_juice_shop_homepage(page)

    # STEP 2:
    # Log in with shared valid user credentials.
    login_to_juice_shop(
        page,
        email=VALID_USER_EMAIL,
        password=VALID_USER_PASSWORD
    )

    # STEP 3:
    # Go back to homepage after login.
    go_to_homepage(page)

    # STEP 4:
    # Search for Apple Juice.
    search_product(page, "Apple Juice")

    # STEP 5:
    # Verify the specific product is visible in search results.
    expect(page.get_by_text("Apple Juice (1000ml)")).to_be_visible()

    # STEP 6:
    # Read basket count before adding product.
    # Basket may already contain other items, so we compare before and after.
    basket_count_before = get_basket_count(page)

    # STEP 7:
    # Add Apple Juice to basket.
    # Since search result only shows Apple Juice, the first Add to Basket button belongs to it.
    add_first_visible_product_to_basket(page)

    # STEP 8:
    # Read basket count after adding product.
    basket_count_after = get_basket_count(page)

    # STEP 9:
    # Verify basket count did not decrease.
    # It may increase by 1, or stay the same if the same product already existed and quantity changed.
    assert basket_count_after >= basket_count_before

    # STEP 10:
    # Open basket.
    open_basket(page)

    # STEP 11:
    # Verify Apple Juice is listed in basket.
    verify_product_in_basket(page, "Apple Juice (1000ml)")