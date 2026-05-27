import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
@pytest.mark.ci
def test_checkout_delivery_fixture_works(checkout_delivery_page: Page):
    """
    Test goal:
    Verify that checkout_delivery_page fixture works.

    The fixture should leave the browser on the delivery method page.
    This test uses the CheckoutPage Page Object.
    """

    page = checkout_delivery_page

    checkout_page = CheckoutPage(page)

    checkout_page.verify_delivery_method_page()