from playwright.sync_api import Page
from helpers.checkout_helper import verify_address_selection_page


def test_checkout_address_fixture_works(checkout_address_page: Page):
    """
    Test goal:
    Verify that checkout_address_page fixture works.

    The fixture should leave the browser on the address selection page
    with one address already created.
    """

    page = checkout_address_page

    verify_address_selection_page(page)