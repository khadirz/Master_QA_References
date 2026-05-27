import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
@pytest.mark.ci
def test_checkout_order_summary_fixture_works(checkout_order_summary_page: Page):
    """
    Test goal:
    Verify that checkout_order_summary_page fixture works.

    The fixture should leave the browser on the order summary page.
    This test uses the CheckoutPage Page Object.
    """

    page = checkout_order_summary_page

    checkout_page = CheckoutPage(page)

    checkout_page.verify_order_summary_page()