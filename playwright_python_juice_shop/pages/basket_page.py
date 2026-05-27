from playwright.sync_api import Page, expect


class BasketPage:
    """
    Page Object Model class for the OWASP Juice Shop basket page.
    """

    def __init__(self, page: Page):
        self.page = page
        self.basket_counter = page.locator(".fa-layers-counter")

    def open(self):
        """
        Open basket page directly.
        """

        self.page.goto("http://localhost:3000/#/basket")

    def verify_loaded(self):
        """
        Verify that basket page is open.
        """

        expect(
            self.page.get_by_role("heading", name="Your Basket", exact=False)
        ).to_be_visible()

    def verify_product_visible(self, product_name: str):
        """
        Verify that a product is visible in the basket.
        """

        product_cell = self.page.locator("mat-cell").filter(
            has_text=product_name
        )

        expect(product_cell).to_be_visible()

    def verify_basket_count(self, expected_count: str):
        """
        Verify basket counter value.
        """

        expect(self.basket_counter).to_have_text(expected_count)