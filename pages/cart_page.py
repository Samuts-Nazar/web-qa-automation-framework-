import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator("[data-test='cart-item']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    @allure.step("Отримання кількості товарів у кошику")
    def get_item_count(self) -> int:
        return self.cart_items.count()

    @allure.step("Отримання списку назв товарів у кошику")
    def get_item_names(self) -> list[str]:
        return self.page.locator("[data-test='inventory-item-name']").all_inner_texts()

    @allure.step("Видалення товару '{item_name}' з кошика")
    def remove_item(self, item_name: str):
        item = self.page.locator(
            f"[data-test='cart-item']:has-text('{item_name}')"
        )
        item.locator("[data-test^='remove']").click()

    @allure.step("Перехід до оформлення замовлення (Натискання кнопки Checkout)")
    def proceed_to_checkout(self):
        self.checkout_button.click()

    @allure.step("Повернення до покупок (Натискання кнопки Continue Shopping)")
    def continue_shopping(self):
        self.continue_shopping_button.click()