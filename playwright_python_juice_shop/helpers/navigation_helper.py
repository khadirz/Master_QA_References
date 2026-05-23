from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups


def open_juice_shop_homepage(page: Page):
    """
    Helper goal:
    Open OWASP Juice Shop homepage and prepare the browser.

    This helper does common startup actions:
    1. Open the app
    2. Set browser size
    3. Close startup popups
    4. Verify homepage is loaded
    """

    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # Make browser window large enough.
    page.set_viewport_size({"width": 1600, "height": 1000})

    # Close welcome and cookie popups if they appear.
    close_startup_popups(page)

    # Verify homepage is loaded.
    expect(page.get_by_text("All Products")).to_be_visible()


def go_to_homepage(page: Page):
    """
    Helper goal:
    Go back to Juice Shop homepage.
    """

    # Open homepage route directly.
    page.goto("http://localhost:3000/#/")

    # Verify homepage is visible.
    expect(page.get_by_text("All Products")).to_be_visible()