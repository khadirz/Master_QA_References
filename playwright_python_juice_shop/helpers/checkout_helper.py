from playwright.sync_api import Page, expect


def click_checkout(page: Page):
    """
    Helper goal:
    Click the Checkout button from the basket page.
    """

    # Find the Checkout button.
    checkout_button = page.get_by_role("button", name="Checkout")

    # Make sure the button is visible and enabled.
    expect(checkout_button).to_be_visible()
    expect(checkout_button).to_be_enabled()

    # Click Checkout.
    checkout_button.click()


def verify_address_selection_page(page: Page):
    """
    Helper goal:
    Verify that the checkout address selection page is open.
    """

    # Juice Shop shows this heading/text on the address selection step.
    expect(page.get_by_text("Select an address")).to_be_visible()


def open_add_new_address_form(page: Page):
    """
    Helper goal:
    Open the Add New Address form.
    """

    # Visible text is "Add New Address",
    # but accessible name is "Add a new address".
    add_new_address_button = page.get_by_role(
        "button",
        name="Add a new address"
    )

    expect(add_new_address_button).to_be_visible()
    expect(add_new_address_button).to_be_enabled()

    add_new_address_button.click()

    # Verify form is opened.
    expect(page.get_by_text("Add New Address")).to_be_visible()


def fill_checkout_address_form(
    page: Page,
    country: str,
    name: str,
    mobile_number: str,
    zip_code: str,
    address: str,
    city: str,
    state: str,
):
    """
    Helper goal:
    Fill the checkout address form.

    Important:
    Mobile number should contain digits only.
    Example: "0501234567"
    """

    page.get_by_placeholder("Country").fill(country)
    page.get_by_placeholder("Name").fill(name)
    page.get_by_placeholder("Mobile Number").fill(mobile_number)
    page.get_by_placeholder("ZIP Code").fill(zip_code)
    page.get_by_placeholder("Address").fill(address)
    page.get_by_placeholder("City").fill(city)
    page.get_by_placeholder("State").fill(state)


def submit_checkout_address_form(page: Page):
    """
    Helper goal:
    Submit the checkout address form.
    """

    submit_button = page.get_by_role("button", name="Submit")

    expect(submit_button).to_be_visible()
    expect(submit_button).to_be_enabled()

    submit_button.click()


def verify_address_in_address_list(
    page: Page,
    address: str,
    city: str,
    state: str,
    zip_code: str,
):
    """
    Helper goal:
    Verify that an address is visible in the address selection table.
    """

    full_address = f"{address}, {city}, {state}, {zip_code}"

    # The same address may exist multiple times from previous test runs.
    # .first means we verify at least one matching address is visible.
    address_cell = page.get_by_role(
        "cell",
        name=full_address
    ).first

    expect(address_cell).to_be_visible()


def select_first_address(page: Page):
    """
    Helper goal:
    Select the first available address in the address selection table.

    Why first address?
    The test user may already have several addresses from previous test runs.
    For this test, we only need any valid address to continue checkout.
    """

    # Find the first radio button in the address list.
    address_radio_button = page.get_by_role("radio").first

    # Make sure the address radio button is visible and enabled.
    expect(address_radio_button).to_be_visible()
    expect(address_radio_button).to_be_enabled()

    # Select the address.
    address_radio_button.click()


def click_continue_to_delivery_method(page: Page):
    """
    Helper goal:
    Click Continue after selecting an address.
    """

    # The visible button text is "Continue",
    # but the accessible name is "Proceed to payment selection".
    continue_button = page.get_by_role(
        "button",
        name="Proceed to payment selection"
    )

    expect(continue_button).to_be_visible()
    expect(continue_button).to_be_enabled()

    continue_button.click()


def verify_delivery_method_page(page: Page):
    """
    Helper goal:
    Verify that the delivery method page is open.
    """

    # Juice Shop usually shows this text after address selection.
    expect(page.get_by_text("Choose a delivery speed")).to_be_visible()

def select_first_delivery_method(page: Page):
    """
    Helper goal:
    Select the first available delivery method.

    Why first delivery method?
    For this test, we only need one valid delivery method
    so that we can continue to the payment step.
    """

    # Find the first delivery method radio button.
    delivery_radio_button = page.get_by_role("radio").first

    # Make sure it is visible and enabled.
    expect(delivery_radio_button).to_be_visible()
    expect(delivery_radio_button).to_be_enabled()

    # Select the delivery method.
    delivery_radio_button.click()


def click_continue_to_payment(page: Page):
    """
    Helper goal:
    Click Continue after selecting a delivery method.
    """

    # The visible text is "Continue",
    # but the accessible name in this Juice Shop page is:
    # "Proceed to delivery method selection".
    continue_button = page.get_by_role(
        "button",
        name="Proceed to delivery method selection"
    )

    # Make sure button is visible and enabled.
    expect(continue_button).to_be_visible()
    expect(continue_button).to_be_enabled()

    # Click Continue.
    continue_button.click()

def verify_payment_page(page: Page):
    """
    Helper goal:
    Verify that the payment selection page is open.
    """

    # Juice Shop usually shows this text on the payment step.
    expect(page.get_by_text("My Payment Options")).to_be_visible()

def open_add_new_card_form(page: Page):
    """
    Helper goal:
    Open the Add New Card form on the payment page.

    Note:
    Juice Shop may show the visible button text as "Add new card".
    """

    # Find Add new card button.
    add_new_card_button = page.get_by_role("button", name="Add new card")

    # Make sure button is visible and enabled.
    expect(add_new_card_button).to_be_visible()
    expect(add_new_card_button).to_be_enabled()

    # Click the button to open card form.
    add_new_card_button.click()


def fill_payment_card_form(
    page: Page,
    card_name: str,
    card_number: str,
    expiry_month: str,
    expiry_year: str,
):
    """
    Helper goal:
    Fill the payment card form.

    Important:
    We scope the text inputs inside the Add new card panel.
    For expiry month and year, this Juice Shop version exposes them as comboboxes.
    """

    # Find the Add new card panel.
    # This avoids accidentally filling the search input in the top menu.
    card_panel = page.locator("mat-expansion-panel").filter(
        has_text="Add a credit or debit card"
    )

    # Find input fields only inside the card panel.
    card_inputs = card_panel.locator("input")

    # First input inside the card panel: card holder name.
    card_inputs.nth(0).fill(card_name)

    # Second input inside the card panel: card number.
    card_inputs.nth(1).fill(card_number)

    # Expiry Month and Expiry Year are dropdown fields.
    # In this Juice Shop version, Playwright sees them as comboboxes.
    expiry_month_dropdown = page.get_by_role("combobox").nth(0)
    expiry_year_dropdown = page.get_by_role("combobox").nth(1)

    # Select expiry month.
    expiry_month_dropdown.select_option(expiry_month)

    # Select expiry year.
    expiry_year_dropdown.select_option(expiry_year)


def submit_payment_card_form(page: Page):
    """
    Helper goal:
    Submit the payment card form.
    """

    # Find Submit button.
    submit_button = page.get_by_role("button", name="Submit")

    # Make sure Submit is visible and enabled.
    expect(submit_button).to_be_visible()
    expect(submit_button).to_be_enabled()

    # Click Submit.
    submit_button.click()


def select_first_payment_option(page: Page):
    """
    Helper goal:
    Select the first available payment option.
    """

    # Find first payment radio button.
    payment_radio_button = page.get_by_role("radio").first

    # Make sure it is visible and enabled.
    expect(payment_radio_button).to_be_visible()
    expect(payment_radio_button).to_be_enabled()

    # Select payment option.
    payment_radio_button.click()


def verify_payment_option_is_selected(page: Page):
    """
    Helper goal:
    Verify that at least one payment option is selected.
    """

    # First radio button should be checked after selecting a payment option.
    payment_radio_button = page.get_by_role("radio").first

    expect(payment_radio_button).to_be_checked()

def click_continue_to_order_summary(page: Page):
    """
    Helper goal:
    Click Continue after selecting a payment method.
    """

    # On the payment page, the visible text is usually "Continue".
    # The accessible name may be different, so we first try the known accessible name.
    continue_button = page.get_by_role(
        "button",
        name="Proceed to review"
    )

    # Make sure the Continue button is visible and enabled.
    expect(continue_button).to_be_visible()
    expect(continue_button).to_be_enabled()

    # Click Continue.
    continue_button.click()


def verify_order_summary_page(page: Page):
    """
    Helper goal:
    Verify that the order summary / review page is open.
    """

    # Juice Shop usually shows this text on the order summary page.
    expect(page.get_by_text("Order Summary")).to_be_visible()

def place_order(page: Page):
    """
    Helper goal:
    Click the Place your order and pay button on the order summary page.
    """

    # The visible button text is "Place your order and pay",
    # but the accessible name is "Complete your purchase".
    place_order_button = page.get_by_role(
        "button",
        name="Complete your purchase"
    )

    # Make sure the button is visible and enabled.
    expect(place_order_button).to_be_visible()
    expect(place_order_button).to_be_enabled()

    # Click Place your order and pay.
    place_order_button.click()


def verify_order_confirmation_page(page: Page):
    """
    Helper goal:
    Verify that the order confirmation page is shown.
    """

    # Juice Shop usually shows a thank you message after placing the order.
    expect(page.get_by_text("Thank you for your purchase!")).to_be_visible()