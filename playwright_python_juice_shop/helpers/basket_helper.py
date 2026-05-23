from playwright.sync_api import Page, expect


def add_first_visible_product_to_basket(page: Page):
    """
    Helper goal:
    Click the first visible Add to Basket button.
    """

    # Find the first Add to Basket button.
    add_to_basket_button = page.get_by_role("button", name="Add to Basket").first

    # Make sure the button is ready.
    expect(add_to_basket_button).to_be_visible()
    expect(add_to_basket_button).to_be_enabled()

    # Click the button.
    add_to_basket_button.click()


def open_basket(page: Page):
    """
    Helper goal:
    Open the shopping basket page.
    """

    # Click the basket button in the top bar.
    page.get_by_role("button", name="Show the shopping cart").click()

    # Verify basket page is open.
    expect(page.get_by_role("heading", name="Your Basket", exact=False)).to_be_visible()


def get_basket_count(page: Page) -> int:
    """
    Helper goal:
    Return the current basket counter as a number.
    """

    # Find the basket counter badge.
    basket_counter = page.locator(".fa-layers-counter")

    # Read the visible text.
    count_text = basket_counter.inner_text()

    # Convert text to integer.
    return int(count_text)


def verify_product_in_basket(page: Page, product_name: str):
    """
    Helper goal:
    Verify that a product is visible in the basket table.
    """

    # Find a table cell containing the product name.
    product_cell = page.locator("mat-cell").filter(has_text=product_name)

    # Verify product is visible.
    expect(product_cell).to_be_visible()


def remove_product_from_basket(page: Page, product_name: str):
    """
    Helper goal:
    Remove a product from the basket table.
    """

    # Find the basket row that contains the product.
    product_row = page.locator("mat-row").filter(has_text=product_name)

    # Verify product row exists before removing.
    expect(product_row).to_be_visible()

    # Find all buttons inside that product row.
    row_buttons = product_row.locator("button")

    # In our Juice Shop version, the last button is the remove/delete button.
    delete_button = row_buttons.last

    # Make sure delete button is ready.
    expect(delete_button).to_be_visible()
    expect(delete_button).to_be_enabled()

    # Click delete/remove.
    delete_button.click()

    # Verify the product row is no longer visible.
    expect(product_row).not_to_be_visible()