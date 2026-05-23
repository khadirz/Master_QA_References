from playwright.sync_api import Page, expect


def search_product(page: Page, product_name: str):
    """
    Helper goal:
    Search for a product in Juice Shop.

    Example:
    search_product(page, "Apple Juice")
    """

    # Find and click the search icon.
    search_icon = page.locator('mat-icon:has-text("search")').first
    search_icon.click()

    # Find the search textbox.
    search_input = page.get_by_role("textbox")

    # Make sure the search textbox is ready.
    expect(search_input).to_be_visible()
    expect(search_input).to_be_enabled()

    # Type the product name.
    search_input.fill(product_name)

    # Press Enter to run the search.
    search_input.press("Enter")


def verify_search_result_title(page: Page, search_text: str):
    """
    Helper goal:
    Verify that the search result title contains the search text.
    """

    expect(page.get_by_text(f"Search Results - {search_text}")).to_be_visible()