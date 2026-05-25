from playwright.sync_api import Page
from helpers.checkout_helper import verify_delivery_method_page


def test_checkout_delivery_fixture_works(checkout_delivery_page: Page):
    """
    Test goal:
    Verify that checkout_delivery_page fixture works.

    The fixture should leave the browser on the delivery method page.
    """

    page = checkout_delivery_page

    verify_delivery_method_page(page)