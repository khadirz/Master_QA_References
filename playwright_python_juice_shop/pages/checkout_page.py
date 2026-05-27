from playwright.sync_api import Page, expect


class CheckoutPage:
    """
    Page Object Model class for OWASP Juice Shop checkout pages.
    """

    def __init__(self, page: Page):
        self.page = page

    def verify_address_selection_page(self):
        """
        Verify that the address selection page is open.
        """

        expect(
            self.page.get_by_text("Select an address")
        ).to_be_visible()

    def verify_delivery_method_page(self):
        """
        Verify that the delivery method page is open.
        """

        expect(
            self.page.get_by_text("Choose a delivery speed")
        ).to_be_visible()

    def verify_payment_page(self):
        """
        Verify that the payment page is open.
        """

        expect(
            self.page.get_by_text("My Payment Options")
        ).to_be_visible()

    def verify_order_summary_page(self):
        """
        Verify that the order summary page is open.
        """

        expect(
            self.page.get_by_text("Order Summary")
        ).to_be_visible()

    def verify_order_confirmation_page(self):
        """
        Verify that the order confirmation page is shown.
        """

        expect(
            self.page.get_by_text("Thank you for your purchase!")
        ).to_be_visible()