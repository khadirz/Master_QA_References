from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups


def test_basic_assertions_on_homepage(page: Page):
    """
    Test goal:
    Practice basic Playwright assertions on the Juice Shop homepage.
    """

    # STEP 1:
    # Open the local Juice Shop application.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Close welcome and cookie popups if they appear.
    close_startup_popups(page)

    # STEP 3:
    # Assert that the browser title is exactly "OWASP Juice Shop".
    # This confirms we opened the correct application.
    expect(page).to_have_title("OWASP Juice Shop")

    # STEP 4:
    # Assert that the page URL contains localhost:3000.
    # This confirms we are still on the local Juice Shop site.
    expect(page).to_have_url("http://localhost:3000/#/")

    # STEP 5:
    # Assert that the text "All Products" is visible.
    # This confirms the homepage product area loaded.
    expect(page.get_by_text("All Products")).to_be_visible()

    # STEP 6:
    # Find all product cards on the page.
    # Juice Shop product items are shown inside mat-card elements.
    product_cards = page.locator("mat-card")

    # STEP 7:
    # Assert that the first product card is visible.
    # .first means we use the first matching product card.
    expect(product_cards.first).to_be_visible()

    # STEP 8:
    # Assert that the page contains a known product.
    # This checks that product data is loaded correctly.
    expect(page.get_by_text("Apple Juice (1000ml)")).to_be_visible()

    # STEP 9:
    # Assert that the Apple Juice product card contains the price.
    # This is a more specific content check.
    expect(page.get_by_text("1.99¤").first).to_be_visible()