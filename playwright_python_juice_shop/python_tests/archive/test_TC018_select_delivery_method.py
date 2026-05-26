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
    select_first_address,
    click_continue_to_delivery_method,
    verify_delivery_method_page,
    select_first_delivery_method,
    click_continue_to_payment,
    verify_payment_page,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD

@pytest.mark.checkout
@pytest.mark.ci
def test_select_delivery_method_and_continue_to_payment(page: Page):
    """
    Test goal:
    Add Apple Juice to the basket,
    start checkout,
    select an address,
    select a delivery method,
    and verify that the payment page opens.

    Precondition:
    The user must already have at least one address.
    TC016 creates an address if needed.
    """

    # STEP 1:
    # Open Juice Shop homepage.
    open_juice_shop_homepage(page)

    # STEP 2:
    # Login with shared valid user.
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
    # Verify Apple Juice is visible in search results.
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
    # Verify address selection page is open.
    verify_address_selection_page(page)

    # STEP 11:
    # Select the first available address.
    select_first_address(page)

    # STEP 12:
    # Continue to delivery method page.
    click_continue_to_delivery_method(page)

    # STEP 13:
    # Verify delivery method page is open.
    verify_delivery_method_page(page)

    # STEP 14:
    # Select the first available delivery method.
    select_first_delivery_method(page)

    # STEP 15:
    # Continue to payment page.
    click_continue_to_payment(page)

    # STEP 16:
    # Verify payment page is open.
    verify_payment_page(page)

def select_first_delivery_method(page: Page):
    """
    Helper goal:
    Select the first available delivery method.
    """

    delivery_radio_button = page.get_by_role("radio").first

    expect(delivery_radio_button).to_be_visible()
    expect(delivery_radio_button).to_be_enabled()

    delivery_radio_button.click()


def click_continue_to_payment(page: Page):
    """
    Helper goal:
    Click Continue after selecting a delivery method.
    """

    continue_button = page.get_by_role(
        "button",
        name="Proceed to delivery method selection"
    )

    expect(continue_button).to_be_visible()
    expect(continue_button).to_be_enabled()

    continue_button.click()


def verify_payment_page(page: Page):
    """
    Helper goal:
    Verify that the payment selection page is open.
    """

    expect(page.get_by_text("My Payment Options")).to_be_visible()