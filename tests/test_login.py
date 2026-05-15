import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage


class TestLogin:
    """Test suite for the login functionality."""

    def test_successful_login(self, page: Page):
        """Standard user should be redirected to inventory after login."""
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in page.url

    def test_invalid_password(self, page: Page):
        """Wrong password should show an error message."""
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "wrong_password")
        assert login.is_error_visible()
        assert "Username and password do not match" in login.get_error_message()

    def test_locked_out_user(self, page: Page):
        """Locked out user should see a specific error message."""
        login = LoginPage(page)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        assert login.is_error_visible()
        assert "locked out" in login.get_error_message().lower()

    def test_empty_credentials(self, page: Page):
        """Submitting empty form should show a validation error."""
        login = LoginPage(page)
        login.open()
        login.login("", "")
        assert login.is_error_visible()
        assert "Username is required" in login.get_error_message()

    @pytest.mark.parametrize("username, password, expected_error", [
        ("standard_user", "wrong", "Username and password do not match"),
        ("unknown_user", "secret_sauce", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ])
    def test_login_errors_parametrized(self, page: Page, username, password, expected_error):
        """Parametrized check of various invalid credential combinations."""
        login = LoginPage(page)
        login.open()
        login.login(username, password)
        assert login.is_error_visible()
        assert expected_error in login.get_error_message()
