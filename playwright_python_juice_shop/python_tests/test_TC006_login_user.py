from playwright.sync_api import Page, expect
from helpers.popup_helper import close_startup_popups
from helpers.login_helper import login_to_juice_shop
from test_data.users import VALID_USER_EMAIL, VALID_USER_PASSWORD


def test_login_existing_user(page: Page):
    """
    Test goal:
    Log in to OWASP Juice Shop with an existing user
    and verify that the basket is visible.
    """

    # STEP 1:
    # Open Juice Shop.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Make browser window large.
    page.set_viewport_size({"width": 1600, "height": 1000})

    # STEP 3:
    # Close popups if they appear.
    close_startup_popups(page)

    # STEP 4:
    # Log in with an existing user.
    # This user must already exist in Juice Shop.
    login_to_juice_shop(
        page,
        email=VALID_USER_EMAIL,
        password=VALID_USER_PASSWORD
    )

    # STEP 5:
    # Verify that Your Basket is visible after login.
    expect(page.get_by_text("Your Basket")).to_be_visible()