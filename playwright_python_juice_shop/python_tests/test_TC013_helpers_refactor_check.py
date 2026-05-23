from playwright.sync_api import Page, expect
from helpers.navigation_helper import open_juice_shop_homepage, go_to_homepage
from helpers.login_helper import login_to_juice_shop
from helpers.search_helper import search_product
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    verify_product_in_basket,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def test_helpers_can_add_specific_product_to_basket(page: Page):
    """
    Test goal:
    Use the new helper functions to perform a real user flow.

    Flow:
    1. Open Juice Shop
    2. Login
    3. Search Apple Juice
    4. Add product to basket
    5. Open basket
    6. Verify Apple Juice is in basket
    """

    # STEP 1:
    # Open Juice Shop homepage using helper.
    open_juice_shop_homepage(page)

    # STEP 2:
    # Login using existing login helper.
    login_to_juice_shop(
        page,
        email=VALID_USER_EMAIL,
        password=VALID_USER_PASSWORD
    )

    # STEP 3:
    # Go back to homepage after login.
    go_to_homepage(page)

    # STEP 4:
    # Search for Apple Juice using helper.
    search_product(page, "Apple Juice")

    # STEP 5:
    # Verify the specific product is visible.
    expect(page.get_by_text("Apple Juice (1000ml)")).to_be_visible()

    # STEP 6:
    # Add the first visible product to basket.
    # Because search result only shows Apple Juice, this adds Apple Juice.
    add_first_visible_product_to_basket(page)

    # STEP 7:
    # Open basket using helper.
    open_basket(page)

    # STEP 8:
    # Verify product is in basket using helper.
    verify_product_in_basket(page, "Apple Juice (1000ml)")