from playwright.sync_api import Page
from helpers.basket_helper import verify_product_in_basket


def test_product_in_basket_fixture_works(product_in_basket_page: Page):
    """
    Test goal:
    Verify that product_in_basket_page fixture works.

    The fixture should leave the browser on the basket page
    with Apple Juice already added.
    """

    page = product_in_basket_page

    verify_product_in_basket(page, "Apple Juice (1000ml)")