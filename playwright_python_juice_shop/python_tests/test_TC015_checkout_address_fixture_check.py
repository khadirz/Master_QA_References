import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


@pytest.mark.checkout
@pytest.mark.ci
def test_checkout_address_fixture_works(checkout_address_page: Page):
    """
    Test goal:
    Verify that checkout_address_page fixture works.

    The fixture should leave the browser on the address selection page.
    This test uses the CheckoutPage Page Object.
    """

    page = checkout_address_page

    checkout_page = CheckoutPage(page)

    checkout_page.verify_address_selection_page()