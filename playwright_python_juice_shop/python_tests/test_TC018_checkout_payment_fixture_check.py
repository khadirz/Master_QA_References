import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
@pytest.mark.ci
def test_checkout_payment_fixture_works(checkout_payment_page: Page):
    """
    Test goal:
    Verify that checkout_payment_page fixture works.

    The fixture should leave the browser on the payment page.
    This test uses the CheckoutPage Page Object.
    """

    page = checkout_payment_page

    checkout_page = CheckoutPage(page)

    checkout_page.verify_payment_page()