from playwright.sync_api import Page
from helpers.checkout_helper import (
    place_order,
    verify_order_confirmation_page,
)


def test_place_order_with_checkout_fixture(checkout_order_summary_page: Page):
    """
    Test goal:
    Use checkout_order_summary_page fixture,
    place the order,
    and verify the order confirmation message.

    Why this is CI-friendly:
    The fixture creates a fresh user and prepares the full checkout state.
    The test only focuses on placing the order and checking confirmation.
    """

    # STEP 1:
    # Use the page prepared by the fixture.
    page = checkout_order_summary_page

    # STEP 2:
    # Place the order.
    place_order(page)

    # STEP 3:
    # Verify order confirmation page/message.
    verify_order_confirmation_page(page)