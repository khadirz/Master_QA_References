from datetime import datetime

import pytest
from playwright.sync_api import Page, expect

from helpers.basket_helper import (
    add_first_visible_product_to_basket,
    open_basket,
    verify_product_in_basket,
)
from helpers.checkout_helper import (
    click_checkout,
    click_continue_to_delivery_method,
    click_continue_to_order_summary,
    click_continue_to_payment,
    fill_checkout_address_form,
    fill_payment_card_form,
    open_add_new_address_form,
    open_add_new_card_form,
    select_first_address,
    select_first_delivery_method,
    select_first_payment_option,
    submit_checkout_address_form,
    submit_payment_card_form,
    verify_address_in_address_list,
    verify_address_selection_page,
    verify_delivery_method_page,
    verify_order_summary_page,
    verify_payment_option_is_selected,
    verify_payment_page,
)
from helpers.login_helper import login_to_juice_shop
from helpers.navigation_helper import go_to_homepage
from helpers.popup_helper import close_startup_popups
from helpers.search_helper import search_product

@pytest.fixture
def fresh_user(page: Page):
    """
    Fixture goal:
    Create a fresh user in Juice Shop and return the email/password.

    Why fixture?
    In CI, Juice Shop starts with a clean database.
    Old users from test_data/users.py may not exist.
    This fixture creates a new user during the test run.
    """

    # STEP 1:
    # Create unique user data.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    email = f"ci_user_{timestamp}@test.com"
    password = "Test12345!"
    security_answer = "Helsinki"

    # STEP 2:
    # Open Juice Shop.
    page.goto("http://localhost:3000")
    page.set_viewport_size({"width": 1600, "height": 1000})

    # STEP 3:
    # Close popups if they appear.
    close_startup_popups(page)

    # STEP 4:
    # Go to Login page.
    page.get_by_role("button", name="Account").click()
    page.get_by_role("menuitem", name="Login").click()

    # STEP 5:
    # Open registration page.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    page.get_by_text("Not yet a customer?").click()

    # STEP 6:
    # Verify registration page is open.
    expect(page.get_by_role("heading", name="User Registration")).to_be_visible()

    # STEP 7:
    # Fill registration form.
    page.locator("#emailControl").fill(email)
    page.locator("#passwordControl").fill(password)
    page.locator("#repeatPasswordControl").fill(password)

    # STEP 8:
    # Select security question.
    page.locator("mat-select").first.click()
    page.locator("mat-option").first.click()

    # STEP 9:
    # Fill security answer.
    page.locator("#securityAnswerControl").fill(security_answer)

    # STEP 10:
    # Submit registration.
    register_button = page.locator("#registerButton")
    expect(register_button).to_be_visible()
    expect(register_button).to_be_enabled()
    register_button.click()

    # STEP 11:
    # Verify registration succeeded and Login page is shown.
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

    # STEP 12:
    # Return user data to the test.
    return {
        "email": email,
        "password": password,
    }

@pytest.fixture
def logged_in_page(page: Page, fresh_user):
    """
    Fixture goal:
    Create a fresh user, log in with that user,
    and return a page that is already logged in.

    Why this is useful:
    Many tests need a logged-in user.
    Instead of repeating signup and login steps in every test,
    we can use this fixture.
    """

    # STEP 1:
    # Get the fresh user data created by the fresh_user fixture.
    email = fresh_user["email"]
    password = fresh_user["password"]

    # STEP 2:
    # The fresh_user fixture leaves the browser on the Login page.
    # Login using the fresh user.
    login_to_juice_shop(
        page,
        email=email,
        password=password
    )

    # STEP 3:
    # Return the logged-in page to the test.
    return page

@pytest.fixture
def product_in_basket_page(logged_in_page: Page):
    """
    Fixture goal:
    Create a fresh user, log in, add Apple Juice to basket,
    open the basket page, and return the page.

    Why this is useful:
    Basket and checkout tests can start from a stable state:
    Apple Juice is already in the basket.
    """

    # STEP 1:
    # Use the page that is already logged in.
    page = logged_in_page

    # STEP 2:
    # Go to homepage.
    go_to_homepage(page)

    # STEP 3:
    # Open Apple Juice search results directly.
    # This is more stable in CI than clicking the search icon and pressing Enter.
    page.goto("http://localhost:3000/#/search?q=Apple%20Juice")

    # STEP 4:
    # Verify search result page is shown.
    expect(page.get_by_text("Search Results - Apple Juice")).to_be_visible(timeout=10000)
    
    # STEP 5:
    # Click the first visible Add to Basket button.
    # After searching Apple Juice, Apple Juice is the first matching product.
    add_to_basket_button = page.get_by_role("button", name="Add to Basket").first

    expect(add_to_basket_button).to_be_visible()
    expect(add_to_basket_button).to_be_enabled()

    # Force click helps in CI when animation or overlay timing interferes.
    add_to_basket_button.click(force=True)

    # STEP 6:
    # Confirm the app accepted the add-to-basket action.
    expect(page.get_by_text("Placed Apple Juice (1000ml) into basket.")).to_be_visible()

    # STEP 7:
    # Wait until basket counter shows 1.
    expect(page.locator(".fa-layers-counter")).to_have_text("1", timeout=10000)

    # STEP 8:
    # Open basket directly.
    # This is more stable than relying on a click on the basket button.
    page.goto("http://localhost:3000/#/basket")

    # STEP 9:
    # Verify basket page is open.
    expect(page.get_by_role("heading", name="Your Basket", exact=False)).to_be_visible()

    # STEP 10:
    # Reload basket page to make sure table data is refreshed.
    page.reload()

    # STEP 11:
    # Verify basket page is still open.
    expect(page.get_by_role("heading", name="Your Basket", exact=False)).to_be_visible()

    # STEP 12:
    # Verify Apple Juice is in basket.
    verify_product_in_basket(page, "Apple Juice (1000ml)")

    # STEP 13:
    # Return the prepared page.
    return page

@pytest.fixture
def checkout_address_page(product_in_basket_page: Page):
    """
    Fixture goal:
    Start from a basket with Apple Juice,
    click Checkout,
    add a new address,
    and return the address selection page.
    """

    page = product_in_basket_page

    click_checkout(page)

    verify_address_selection_page(page)

    open_add_new_address_form(page)

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

    submit_checkout_address_form(page)

    verify_address_selection_page(page)

    verify_address_in_address_list(
        page,
        address="Testikatu 1",
        city="Helsinki",
        state="Uusimaa",
        zip_code="00100",
    )

    return page

@pytest.fixture
def checkout_delivery_page(checkout_address_page: Page):
    """
    Fixture goal:
    Start from the address selection page,
    select the first available address,
    continue to the delivery method page,
    and return the page.
    """

    page = checkout_address_page

    # STEP 1:
    # Select the first available address.
    select_first_address(page)

    # STEP 2:
    # Continue to delivery method page.
    click_continue_to_delivery_method(page)

    # STEP 3:
    # Verify delivery method page is open.
    verify_delivery_method_page(page)

    return page

@pytest.fixture
def checkout_payment_page(checkout_delivery_page: Page):
    """
    Fixture goal:
    Start from the delivery method page,
    select the first available delivery method,
    continue to the payment page,
    and return the page.

    Why this is useful:
    Payment-related tests can start from a stable checkout state.
    """

    page = checkout_delivery_page

    # STEP 1:
    # Select the first available delivery method.
    select_first_delivery_method(page)

    # STEP 2:
    # Continue to payment page.
    click_continue_to_payment(page)

    # STEP 3:
    # Verify payment page is open.
    verify_payment_page(page)

    return page

@pytest.fixture
def checkout_order_summary_page(checkout_payment_page: Page):
    """
    Fixture goal:
    Start from the payment page,
    add/select a payment method,
    continue to the order summary page,
    and return the page.

    Why this is useful:
    Order summary and order confirmation tests can start from a stable checkout state.
    """

    page = checkout_payment_page

    # STEP 1:
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

    # STEP 2:
    # Select first available payment option.
    select_first_payment_option(page)

    # STEP 3:
    # Verify payment option is selected.
    verify_payment_option_is_selected(page)

    # STEP 4:
    # Continue to order summary page.
    click_continue_to_order_summary(page)

    # STEP 5:
    # Verify order summary page is open.
    verify_order_summary_page(page)

    return page