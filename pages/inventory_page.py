import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator("[data-test='inventory-item']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    @allure.step("Отримання кількості товарів на сторінці")
    def get_item_count(self) -> int:
        return self.inventory_items.count()

    @allure.step("Сортування товарів за опцією '{option}'")
    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    @allure.step("Отримання списку назв товарів")
    def get_item_names(self) -> list[str]:
        return self.page.locator("[data-test='inventory-item-name']").all_inner_texts()

    @allure.step("Отримання списку цін товарів")
    def get_item_prices(self) -> list[float]:
        raw = self.page.locator("[data-test='inventory-item-price']").all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

    @allure.step("Додавання товару '{item_name}' у кошик")
    def add_item_to_cart(self, item_name: str):
        item = self.page.locator(
            f"[data-test='inventory-item']:has-text('{item_name}')"
        )
        item.locator("button").click()

    @allure.step("Отримання значення лічильника кошика")
    def get_cart_badge_count(self) -> int:
        return int(self.cart_badge.inner_text())

    @allure.step("Перехід у кошик")
    def go_to_cart(self):
        self.cart_link.click()