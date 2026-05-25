from playwright.sync_api import Page
from helpers.checkout_helper import verify_payment_page


def test_checkout_payment_fixture_works(checkout_payment_page: Page):
    """
    Test goal:
    Verify that checkout_payment_page fixture works.

    The fixture should leave the browser on the payment page.
    """

    page = checkout_payment_page

    verify_payment_page(page)