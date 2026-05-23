from playwright.sync_api import Page


def close_startup_popups(page: Page):
    """
    This helper closes optional startup popups in OWASP Juice Shop.

    Why do we need this?
    Juice Shop may show a welcome banner or cookie message.
    If we do not close them, they may block buttons or page content.
    """

    # Try to close the welcome banner.
    # If the banner is not visible, we continue without failing the test.
    try:
        page.get_by_label("Close Welcome Banner").click(timeout=3000)
    except Exception:
        print("Welcome banner was not visible.")

    # Try to close the cookie message.
    # If it is not visible, we continue without failing the test.
    try:
        page.get_by_label("dismiss cookie message").click(timeout=3000)
    except Exception:
        print("Cookie message was not visible.")