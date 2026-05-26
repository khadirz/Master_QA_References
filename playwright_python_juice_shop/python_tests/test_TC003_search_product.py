from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups


def test_search_for_apple_juice(page: Page):
    """
    Test goal:
    Search for Apple Juice in OWASP Juice Shop and verify the result.
    """

    # STEP 1:
    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Close startup popups if they appear.
    close_startup_popups(page)

    # STEP 3:
    # Find the search icon.
    # This looks for a Material icon with text "search".
    search_icon = page.locator('mat-icon:has-text("search")').first

    # STEP 4:
    # Click the search icon.
    # This activates the hidden search textbox.
    search_icon.click()

    # STEP 5:
    # Find the search textbox.
    search_input = page.get_by_role("textbox")

    # STEP 6:
    # After clicking search, the textbox should become visible and enabled.
    expect(search_input).to_be_visible()
    expect(search_input).to_be_enabled()

    # STEP 7:
    # Type the product name.
    search_input.fill("Apple Juice")

    # STEP 8:
    # Press Enter to search.
    search_input.press("Enter")

    # STEP 9:
    # Verify the actual product result is visible.
    # In this Juice Shop version, the product name is exposed as a button inside the product card.
    apple_juice_result = page.get_by_role(
        "button",
        name="Apple Juice (1000ml)",
        exact=True
    )

    expect(apple_juice_result).to_be_visible()