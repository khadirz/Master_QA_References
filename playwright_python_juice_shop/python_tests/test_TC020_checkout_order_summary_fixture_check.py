import pytest
from playwright.sync_api import Page
from helpers.checkout_helper import verify_order_summary_page

@pytest.mark.checkout
@pytest.mark.ci
def test_checkout_order_summary_fixture_works(checkout_order_summary_page: Page):
    """
    Test goal:
    Verify that checkout_order_summary_page fixture works.

    The fixture should leave the browser on the order summary page.
    """

    page = checkout_order_summary_page

    verify_order_summary_page(page)