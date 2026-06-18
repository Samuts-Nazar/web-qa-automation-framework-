import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    @allure.step("Відкриття сторінки логіну")
    def open(self):
        self.navigate(self.URL)

    @allure.step("Логін як '{username}'")
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("Отримання тексту повідомлення про помилку")
    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    @allure.step("Перевірка видимості повідомлення про помилку")
    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()