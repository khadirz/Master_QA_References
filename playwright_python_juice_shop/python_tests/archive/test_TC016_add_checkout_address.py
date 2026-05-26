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
    open_add_new_address_form,
    fill_checkout_address_form,
    submit_checkout_address_form,
    verify_address_in_address_list,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD

@pytest.mark.checkout
@pytest.mark.ci
def test_add_new_address_during_checkout(page: Page):
    """
    Test goal:
    Add Apple Juice to the basket,
    start checkout,
    add a new delivery address,
    and verify that the address appears in the address list.

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
    # Click Checkout.
    click_checkout(page)

    # STEP 10:
    # Verify address selection page.
    verify_address_selection_page(page)

    # STEP 11:
    # Open Add New Address form.
    open_add_new_address_form(page)

    # STEP 12:
    # Fill address form.
    fill_checkout_address_form(
        page,
        country="Finland",
        name="Khadir Test User",
        mobile_number="0501234567",
        zip_code="00100",
        address="Testikatu 1",
        city="Helsinki",
        state="Uusimaa",
    )

    # STEP 13:
    # Submit address form.
    submit_checkout_address_form(page)

    # STEP 14:
    # Verify we are back on address selection page.
    verify_address_selection_page(page)

    # STEP 15:
    # Verify created address is visible in the address list.
    verify_address_in_address_list(
        page,
        address="Testikatu 1",
        city="Helsinki",
        state="Uusimaa",
        zip_code="00100",
    )