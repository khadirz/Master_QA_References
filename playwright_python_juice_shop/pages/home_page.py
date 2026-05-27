from playwright.sync_api import Page, expect

from helpers.popup_helper import close_startup_popups


class HomePage:
    """
    Page Object Model class for the OWASP Juice Shop homepage.

    This class contains homepage actions and homepage-related checks.
    """

    def __init__(self, page: Page):
        self.page = page
        self.url = "http://localhost:3000"

    def open(self):
        """
        Open the Juice Shop homepage and close startup popups if they appear.
        """

        self.page.goto(self.url)
        close_startup_popups(self.page)

    def verify_loaded(self):
        """
        Verify that the homepage is loaded.
        """

        expect(self.page.get_by_text("All Products")).to_be_visible()

    def search_product(self, product_name: str):
        """
        Search for a product from the homepage.

        Example:
        search_product("Apple Juice")
        """

        search_input = self.page.get_by_role("textbox")

        if not search_input.is_visible():
            search_icon = self.page.locator('mat-icon:has-text("search")').first
            search_icon.click()

        expect(search_input).to_be_visible()
        expect(search_input).to_be_enabled()

        search_input.fill("")
        search_input.fill(product_name)
        search_input.press("Enter")

        expect(
            self.page.get_by_text(f"Search Results - {product_name}")
        ).to_be_visible()

    def verify_product_result_visible(self, product_name: str):
        """
        Verify that a product result is visible on the search results page.
        """

        product_result = self.page.get_by_role(
            "button",
            name=product_name,
            exact=True
        )

        expect(product_result).to_be_visible()