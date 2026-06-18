import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    URL_STEP_ONE = "https://www.saucedemo.com/checkout-step-one.html"
    URL_STEP_TWO = "https://www.saucedemo.com/checkout-step-two.html"
    URL_COMPLETE = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error_message = page.locator("[data-test='error']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")

    @allure.step("Заповнення даних покупця: {first_name} {last_name}, {postal_code}")
    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    @allure.step("Перехід до кроку 2 (огляд замовлення)")
    def continue_to_step_two(self):
        self.continue_button.click()

    @allure.step("Завершення замовлення (Натискання кнопки Finish)")
    def finish_order(self):
        self.finish_button.click()

    @allure.step("Отримання тексту повідомлення про помилку")
    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    @allure.step("Перевірка видимості повідомлення про помилку")
    def is_error_visible(self) -> bool:
        return self.error_message.is_visible()

    @allure.step("Отримання заголовку підтвердження замовлення")
    def get_complete_header(self) -> str:
        return self.complete_header.inner_text()