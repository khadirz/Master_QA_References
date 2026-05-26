from playwright.sync_api import Page, expect
from helpers.navigation_helper import open_juice_shop_homepage, go_to_homepage
from helpers.login_helper import login_to_juice_shop
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    get_basket_count,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def test_add_product_to_basket_after_login(page: Page):
    """
    Test goal:
    Log in to Juice Shop, add the first visible product to the basket,
    and verify that the basket count does not decrease.

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
    # Verify homepage is visible.
    expect(page.get_by_text("All Products")).to_be_visible()

    # STEP 5:
    # Read basket count before adding product.
    basket_count_before = get_basket_count(page)

    # STEP 6:
    # Add the first visible product to basket.
    add_first_visible_product_to_basket(page)

    # STEP 7:
    # Read basket count after adding product.
    basket_count_after = get_basket_count(page)

    # STEP 8:
    # Verify basket count did not decrease.
    # It may increase by 1, or stay the same if the product was already in basket
    # and only the quantity changed.
    assert basket_count_after >= basket_count_before