import allure
from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Перейти за URL: {url}")
    def navigate(self, url: str):
        self.page.goto(url)

    @allure.step("Отримати заголовок сторінки")
    def get_title(self) -> str:
        return self.page.title()

    @allure.step("Дочекатись URL: {url}")
    def wait_for_url(self, url: str):
        self.page.wait_for_url(url)