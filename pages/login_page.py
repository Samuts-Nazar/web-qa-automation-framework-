from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the Sauce Demo login page."""

    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        """Navigate to the login page."""
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        """Fill credentials and submit the login form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """Return the text of the error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Return True if the error message is visible."""
        return self.error_message.is_visible()
