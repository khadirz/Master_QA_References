from playwright.sync_api import Page, expect
from helpers.navigation_helper import open_juice_shop_homepage, go_to_homepage
from helpers.login_helper import login_to_juice_shop
from helpers.search_helper import search_product
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    verify_product_in_basket,
    remove_product_from_basket,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def test_remove_product_from_basket(page: Page):
    """
    Test goal:
    Log in, add Apple Juice to the basket,
    open the basket, remove Apple Juice,
    and verify that Apple Juice is removed.

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
    # Add Apple Juice to basket.
    # Since search result only shows Apple Juice, the first Add to Basket button belongs to it.
    add_first_visible_product_to_basket(page)

    # STEP 7:
    # Open basket.
    open_basket(page)

    # STEP 8:
    # Verify Apple Juice is in basket before removing it.
    verify_product_in_basket(page, "Apple Juice (1000ml)")

    # STEP 9:
    # Remove Apple Juice from basket.
    remove_product_from_basket(page, "Apple Juice (1000ml)")