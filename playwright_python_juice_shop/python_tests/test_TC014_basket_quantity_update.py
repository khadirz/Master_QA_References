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


def test_increase_and_decrease_product_quantity_in_basket(page: Page):
    """
    Test goal:
    Add Apple Juice to the basket,
    set its quantity to 1,
    increase it to 2,
    then decrease it back to 1.

    Why we normalize quantity first:
    The basket may already contain Apple Juice from previous tests.
    So the quantity may start as 2, 3, 4, or 5.
    To make the test stable, we first reduce it to 1.
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
    # Find the basket row containing Apple Juice.
    apple_juice_row = page.locator("mat-row").filter(has_text="Apple Juice (1000ml)")
    expect(apple_juice_row).to_be_visible()

    # STEP 10:
    # Find all cells inside the Apple Juice row.
    row_cells = apple_juice_row.locator("mat-cell")

    # STEP 11:
    # Quantity is usually in the third cell, index 2.
    quantity_cell = row_cells.nth(2)

    # Helper function:
    # Read the current quantity from the quantity cell.
    def get_quantity() -> int:
        quantity_text = quantity_cell.inner_text().strip()
        return int(quantity_text)

    # STEP 12:
    # Find all buttons inside the quantity cell.
    quantity_buttons = quantity_cell.locator("button")

    # STEP 13:
    # In this Juice Shop version:
    # first button = decrease quantity
    # last button = increase quantity
    decrease_button = quantity_buttons.first
    increase_button = quantity_buttons.last

    # STEP 14:
    # Normalize quantity to 1.
    # If quantity is already 1, this loop will not run.
    # If quantity is 2, 3, 4, or 5, we decrease it until it becomes 1.
    current_quantity = get_quantity()

    while current_quantity > 1:
        expect(decrease_button).to_be_visible()
        expect(decrease_button).to_be_enabled()

        decrease_button.click()

        expected_quantity = current_quantity - 1
        expect(quantity_cell).to_contain_text(str(expected_quantity))

        current_quantity = get_quantity()

    # STEP 15:
    # Verify quantity is now 1 before testing increase/decrease.
    assert get_quantity() == 1

    # STEP 16:
    # Click increase quantity.
    expect(increase_button).to_be_visible()
    expect(increase_button).to_be_enabled()

    increase_button.click()

    # STEP 17:
    # Verify quantity increased from 1 to 2.
    expect(quantity_cell).to_contain_text("2")
    assert get_quantity() == 2

    # STEP 18:
    # Click decrease quantity.
    expect(decrease_button).to_be_visible()
    expect(decrease_button).to_be_enabled()

    decrease_button.click()

    # STEP 19:
    # Verify quantity decreased from 2 back to 1.
    expect(quantity_cell).to_contain_text("1")
    assert get_quantity() == 1