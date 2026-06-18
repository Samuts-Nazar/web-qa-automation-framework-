import allure
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


@allure.feature("Інвентар")
class TestInventory:

    @allure.story("Відображення товарів")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Усі 6 товарів відображаються після логіну")
    def test_all_items_displayed(self, authenticated_page: Page):
        with allure.step("Отримати кількість товарів на сторінці інвентаря"):
            inventory = InventoryPage(authenticated_page)
            count = inventory.get_item_count()

        with allure.step("Перевірити, що відображається 6 товарів"):
            assert count == 6

    @allure.story("Сортування")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортування товарів A→Z дає зростаючий алфавітний порядок")
    def test_sort_name_az(self, authenticated_page: Page):
        with allure.step("Застосувати сортування A→Z"):
            inventory = InventoryPage(authenticated_page)
            inventory.sort_by("az")

        with allure.step("Отримати назви товарів"):
            names = inventory.get_item_names()

        with allure.step("Перевірити зростаючий алфавітний порядок"):
            assert names == sorted(names)

    @allure.story("Сортування")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортування товарів Z→A дає спадаючий алфавітний порядок")
    def test_sort_name_za(self, authenticated_page: Page):
        with allure.step("Застосувати сортування Z→A"):
            inventory = InventoryPage(authenticated_page)
            inventory.sort_by("za")

        with allure.step("Отримати назви товарів"):
            names = inventory.get_item_names()

        with allure.step("Перевірити спадаючий алфавітний порядок"):
            assert names == sorted(names, reverse=True)

    @allure.story("Сортування")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортування за ціною від низької до високої")
    def test_sort_price_low_to_high(self, authenticated_page: Page):
        with allure.step("Застосувати сортування за ціною (low→high)"):
            inventory = InventoryPage(authenticated_page)
            inventory.sort_by("lohi")

        with allure.step("Отримати ціни товарів"):
            prices = inventory.get_item_prices()

        with allure.step("Перевірити зростаючий порядок цін"):
            assert prices == sorted(prices)

    @allure.story("Сортування")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Сортування за ціною від високої до низької")
    def test_sort_price_high_to_low(self, authenticated_page: Page):
        with allure.step("Застосувати сортування за ціною (high→low)"):
            inventory = InventoryPage(authenticated_page)
            inventory.sort_by("hilo")

        with allure.step("Отримати ціни товарів"):
            prices = inventory.get_item_prices()

        with allure.step("Перевірити спадаючий порядок цін"):
            assert prices == sorted(prices, reverse=True)

    @allure.story("Кошик")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Додавання товару збільшує лічильник кошика")
    def test_add_item_updates_cart_badge(self, authenticated_page: Page):
        with allure.step("Додати Sauce Labs Backpack у кошик"):
            inventory = InventoryPage(authenticated_page)
            inventory.add_item_to_cart("Sauce Labs Backpack")

        with allure.step("Перевірити, що лічильник кошика показує 1"):
            assert inventory.get_cart_badge_count() == 1