from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups


def test_homepage_basic_locators(page: Page):
    """
    Test goal:
    Practice different locator types on the Juice Shop homepage.
    """

    # STEP 1:
    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Close startup popups if they appear.
    close_startup_popups(page)

    # STEP 3:
    # Find text on the page.
    # This checks that the text "All Products" is visible.
    expect(page.get_by_text("All Products")).to_be_visible()

    # STEP 4:
    # Find the search icon.
    # Juice Shop uses a Material icon with the text "search".
    search_icon = page.locator('mat-icon:has-text("search")')

    # In Python Playwright, .first is a property, not a function.
    # search_icon.first is the correct way to access the first element. Do not use parentheses.
    expect(search_icon.first).to_be_visible()

    # STEP 5:
    # Find product cards by CSS.
    # Juice Shop uses mat-card elements for products.
    product_cards = page.locator("mat-card")

    # Again, use .first without parentheses.
    expect(product_cards.first).to_be_visible()