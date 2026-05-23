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


def test_add_new_address_during_checkout(page: Page):
    """
    Test goal:
    Add Apple Juice to the basket, start checkout,
    add a new delivery address,
    and verify that the new address appears in the address list.

    This test teaches:
    1. Checkout navigation
    2. Filling a longer form
    3. Submitting form data
    4. Verifying created data on the page
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
    # Verify Apple Juice is in basket.
    verify_product_in_basket(page, "Apple Juice (1000ml)")

    # STEP 9:
    # Click Checkout button.
    checkout_button = page.get_by_role("button", name="Checkout")
    expect(checkout_button).to_be_visible()
    expect(checkout_button).to_be_enabled()
    checkout_button.click()

    # STEP 10:
    # Verify checkout moved to address selection page.
    expect(page.get_by_text("Select an address")).to_be_visible()

    # STEP 11:
    # Click Add New Address.
    # The visible text is "Add New Address",
    # but the accessible button name is "Add a new address".
    add_new_address_button = page.get_by_role("button", name="Add a new address")

    expect(add_new_address_button).to_be_visible()
    expect(add_new_address_button).to_be_enabled()

    add_new_address_button.click()

    # STEP 12:
    # Verify address form is opened.
    expect(page.get_by_text("Add New Address")).to_be_visible()

    # STEP 13:
    # Fill the address form.
    # We use placeholders because these are visible in the form.
    # Mobile Number must contain digits only, without "+".

    page.get_by_placeholder("Country").fill("Finland")
    page.get_by_placeholder("Name").fill("Khadir Test User")
    page.get_by_placeholder("Mobile Number").fill("0501234567")
    page.get_by_placeholder("ZIP Code").fill("00100")
    page.get_by_placeholder("Address").fill("Testikatu 1")
    page.get_by_placeholder("City").fill("Helsinki")
    page.get_by_placeholder("State").fill("Uusimaa")
    
    # STEP 14:
    # Click Submit.
    submit_button = page.get_by_role("button", name="Submit")
    expect(submit_button).to_be_visible()
    expect(submit_button).to_be_enabled()
    submit_6tg.         button.click()

    # STEP 15:
    # Verify that we are back on the address selection page.
    expect(page.get_by_text("Select an address")).to_be_visible()

    # STEP 16:
    # Verify the created address appears in the address table.
    # The same address may already exist from previous test runs.
    # So we use .first to check that at least one matching address is visible.
    created_address_cell = page.get_by_role(
        "cell",
        name="Testikatu 1, Helsinki, Uusimaa, 00100"
    ).first

    expect(created_address_cell).to_be_visible()