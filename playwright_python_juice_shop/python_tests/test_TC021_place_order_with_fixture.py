import pytest
from playwright.sync_api import Page

from helpers.checkout_helper import place_order
from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
@pytest.mark.ci
def test_place_order_with_checkout_fixture(checkout_order_summary_page: Page):
    """
    Test goal:
    Use checkout_order_summary_page fixture,
    place the order,
    and verify the order confirmation message.

    This test uses the CheckoutPage Page Object for verification.
    """

    page = checkout_order_summary_page

    checkout_page = CheckoutPage(page)

    # STEP 1:
    # Place the order.
    place_order(page)

    # STEP 2:
    # Verify order confirmation page/message.
    checkout_page.verify_order_confirmation_page()