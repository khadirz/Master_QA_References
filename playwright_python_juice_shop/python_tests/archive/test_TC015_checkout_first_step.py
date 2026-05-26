import pytest
from playwright.sync_api import Page, expect
from helpers.navigation_helper import open_juice_shop_homepage, go_to_homepage
from helpers.login_helper import login_to_juice_shop
from helpers.search_helper import search_product
from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    verify_product_in_basket,
)
from helpers.checkout_helper import (
    click_checkout,
    verify_address_selection_page,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD

@pytest.mark.checkout
@pytest.mark.ci
def test_checkout_first_step_opens_address_page(page: Page):
    """
    Test goal:
    Add Apple Juice to the basket,
    click Checkout,
    and verify that the address selection page opens.

    This version uses checkout helper functions.
    """

    # STEP 1:
    # Open Juice Shop homepage.
    open_juice_shop_homepage(page)

    # STEP 2:
    # Login with valid user.
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
    # Verify Apple Juice is visible.
    expect(page.get_by_text("Apple Juice (1000ml)")).to_be_visible()

    # STEP 6:
    # Add Apple Juice to basket.
    add_first_visible_product_to_basket(page)

    # STEP 7:
    # Open basket.
    open_basket(page)

    # STEP 8:
    # Verify Apple Juice is in basket.
    verify_product_in_basket(page, "Apple Juice (1000ml)")

    # STEP 9:
    # Click Checkout using helper.
    click_checkout(page)

    # STEP 10:
    # Verify address selection page is open using helper.
    verify_address_selection_page(page)