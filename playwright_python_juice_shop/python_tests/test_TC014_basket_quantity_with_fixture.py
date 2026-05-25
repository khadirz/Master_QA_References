from playwright.sync_api import Page, expect


def test_increase_and_decrease_product_quantity_with_fixture(product_in_basket_page: Page):
    """
    Test goal:
    Use product_in_basket_page fixture to start with Apple Juice already in basket.
    Then increase quantity from 1 to 2,
    and decrease it back to 1.

    Why this is CI-friendly:
    The fixture creates a fresh user, logs in,
    adds Apple Juice to basket, and opens the basket page.
    """

    # STEP 1:
    # Use the page prepared by the fixture.
    page = product_in_basket_page

    # STEP 2:
    # Find the basket row containing Apple Juice.
    apple_juice_row = page.locator("mat-row").filter(
        has_text="Apple Juice (1000ml)"
    )

    expect(apple_juice_row).to_be_visible()

    # STEP 3:
    # Find all cells inside the Apple Juice row.
    row_cells = apple_juice_row.locator("mat-cell")

    # STEP 4:
    # Quantity is usually in the third cell, index 2.
    quantity_cell = row_cells.nth(2)

    # Helper function:
    # Read the current quantity from the quantity cell.
    def get_quantity() -> int:
        quantity_text = quantity_cell.inner_text().strip()
        return int(quantity_text)

    # STEP 5:
    # Find all buttons inside the quantity cell.
    quantity_buttons = quantity_cell.locator("button")

    # STEP 6:
    # In this Juice Shop version:
    # first button = decrease quantity
    # last button = increase quantity
    decrease_button = quantity_buttons.first
    increase_button = quantity_buttons.last

    # STEP 7:
    # Normalize quantity to 1.
    # The fixture should already create quantity 1,
    # but this keeps the test stable if the state changes.
    current_quantity = get_quantity()

    while current_quantity > 1:
        expect(decrease_button).to_be_visible()
        expect(decrease_button).to_be_enabled()

        decrease_button.click()

        expected_quantity = current_quantity - 1
        expect(quantity_cell).to_contain_text(str(expected_quantity))

        current_quantity = get_quantity()

    # STEP 8:
    # Verify quantity is now 1.
    assert get_quantity() == 1

    # STEP 9:
    # Increase quantity from 1 to 2.
    expect(increase_button).to_be_visible()
    expect(increase_button).to_be_enabled()

    increase_button.click()

    # STEP 10:
    # Verify quantity increased to 2.
    expect(quantity_cell).to_contain_text("2")
    assert get_quantity() == 2

    # STEP 11:
    # Decrease quantity from 2 back to 1.
    expect(decrease_button).to_be_visible()
    expect(decrease_button).to_be_enabled()

    decrease_button.click()

    # STEP 12:
    # Verify quantity returned to 1.
    expect(quantity_cell).to_contain_text("1")
    assert get_quantity() == 1