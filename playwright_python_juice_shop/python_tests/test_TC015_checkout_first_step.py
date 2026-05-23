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


def test_checkout_first_step_opens_address_page(page: Page):
    """
    Test goal:
    Add Apple Juice to the basket,
    click Checkout,
    and verify that the checkout/address page opens.

    This test does not complete the full order.
    It only verifies that the user can start checkout.
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
    # Verify Apple Juice is visible in search results.
    expect(page.get_by_text("Apple Juice (1000ml)")).to_be_visible()

    # STEP 6:
    # Add Apple Juice to basket.
    add_first_visible_product_to_basket(page)

    # STEP 7:
    # Open basket page.
    open_basket(page)

    # STEP 8:
    # Verify Apple Juice is in the basket.
    verify_product_in_basket(page, "Apple Juice (1000ml)")

    # STEP 9:
    # Find the Checkout button.
    checkout_button = page.get_by_role("button", name="Checkout")

    # STEP 10:
    # Make sure Checkout button is visible and enabled.
    expect(checkout_button).to_be_visible()
    expect(checkout_button).to_be_enabled()

    # STEP 11:
    # Click Checkout.
    checkout_button.click()

    # STEP 12:
    # Verify that checkout moved to the address selection step.
    # Juice Shop usually shows "Select an address" or similar text.
    expect(page.get_by_text("Select an address")).to_be_visible()