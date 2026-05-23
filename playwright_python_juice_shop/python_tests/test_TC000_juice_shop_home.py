from playwright.sync_api import Page, expect


def test_open_juice_shop_homepage(page: Page):
    # STEP 1:
    # Open the OWASP Juice Shop application.
    page.goto("http://localhost:3000")

    # STEP 2:
    # Close the welcome banner if it appears.
    try:
        page.get_by_label("Close Welcome Banner").click(timeout=3000)
    except Exception:
        print("Welcome banner was not visible, continuing test.")

    # STEP 3:
    # Close the cookie message if it appears.
    try:
        page.get_by_label("dismiss cookie message").click(timeout=3000)
    except Exception:
        print("Cookie message was not visible, continuing test.")

    # STEP 4:
    # Check that the browser title is correct.
    expect(page).to_have_title("OWASP Juice Shop")

    # STEP 5:
    # Check that the product page is visible.
    expect(page.get_by_text("All Products")).to_be_visible()