from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups
from helpers.login_helper import login_to_juice_shop


def test_add_first_product_to_basket_after_login(page: Page):
    """
    Test goal:
    Login, add the first visible product to the basket,
    and verify that the basket count changes.
    """

    # STEP 1:
    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Make browser large so product buttons are easier to see.
    page.set_viewport_size({"width": 1600, "height": 1000})

    # STEP 3:
    # Close startup popups if they appear.
    close_startup_popups(page)

    # STEP 4:
    # Login to Juice Shop.
    # These are commonly used Juice Shop demo credentials.
    login_to_juice_shop(
        page,
        email="admin@juice-sh.op",
        password="admin123"
    )

    # STEP 5:
    # Go back to homepage after login.
    page.goto("http://localhost:3000/#/")

    # STEP 6:
    # Verify product page is visible.
    expect(page.get_by_text("All Products")).to_be_visible()

    # STEP 7:
    # Find the first Add to Basket button.
    add_to_basket_button = page.get_by_role("button", name="Add to Basket").first

    # STEP 8:
    # Confirm the button is visible.
    expect(add_to_basket_button).to_be_visible()

    # STEP 9:
    # Click Add to Basket.
    add_to_basket_button.click()

    # STEP 10:
    # Verify basket count changed to 1.
    expect(page.locator(".fa-layers-counter")).to_have_text("1")