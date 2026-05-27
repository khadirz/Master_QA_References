from playwright.sync_api import Page, expect


class LoginPage:
    """
    Page Object Model class for the OWASP Juice Shop login page.
    """

    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.get_by_role(
            "textbox",
            name="Text field for the login email"
        )

        self.password_input = page.get_by_role(
            "textbox",
            name="Text field for the login password"
        )

        self.login_button = page.locator("#loginButton")

    def verify_loaded(self):
        """
        Verify that the login page is open.
        """

        expect(
            self.page.get_by_role("heading", name="Login")
        ).to_be_visible()

    def login(self, email: str, password: str):
        """
        Fill email/password and click Login.
        """

        self.verify_loaded()

        self.email_input.fill(email)
        self.password_input.fill(password)

        expect(self.login_button).to_be_visible()
        expect(self.login_button).to_be_enabled()

        self.login_button.click()

    def verify_login_successful(self):
        """
        Verify that login was successful.
        """

        expect(
            self.page.get_by_text("Your Basket")
        ).to_be_visible()