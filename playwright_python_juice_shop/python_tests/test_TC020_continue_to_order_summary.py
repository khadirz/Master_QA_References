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
    open_add_new_card_form,
    fill_payment_card_form,
    submit_payment_card_form,
    select_first_payment_option,
    verify_payment_option_is_selected,
    click_continue_to_order_summary,
    verify_order_summary_page,
)
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def test_continue_from_payment_to_order_summary(page: Page):
    """
    Test goal:
    Add Apple Juice to basket,
    go through checkout until payment page,
    select a payment method,
    click Continue,
    and verify that the order summary page opens.

    This test does not place the order yet.
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
    # Verify address selection page.
    verify_address_selection_page(page)

    # STEP 11:
    # Select first available address.
    select_first_address(page)

    # STEP 12:
    # Continue to delivery method page.
    click_continue_to_delivery_method(page)

    # STEP 13:
    # Verify delivery method page.
    verify_delivery_method_page(page)

    # STEP 14:
    # Select first delivery method.
    select_first_delivery_method(page)

    # STEP 15:
    # Continue to payment page.
    click_continue_to_payment(page)

    # STEP 16:
    # Verify payment page.
    verify_payment_page(page)

    # STEP 17:
    # If no payment option exists, add a fake test card.
    payment_options_count = page.get_by_role("radio").count()

    if payment_options_count == 0:
        open_add_new_card_form(page)

        fill_payment_card_form(
            page,
            card_name="Khadir Test Card",
            card_number="4111111111111111",
            expiry_month="12",
            expiry_year="2080",
        )

        submit_payment_card_form(page)
        verify_payment_page(page)

    # STEP 18:
    # Select first available payment option.
    select_first_payment_option(page)

    # STEP 19:
    # Verify payment option is selected.
    verify_payment_option_is_selected(page)

    # STEP 20:
    # Continue to order summary page.
    click_continue_to_order_summary(page)

    # STEP 21:
    # Verify order summary page is open.
    verify_order_summary_page(page)