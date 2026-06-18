import allure
from playwright.sync_api import Page
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Оформлення замовлення")
class TestCheckout:

    @allure.story("Успішний сценарій")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Повний флоу замовлення: товар → кошик → checkout → завершення")
    def test_happy_path(self, authenticated_page: Page):
        with allure.step("Додати товар у кошик"):
            inventory = InventoryPage(authenticated_page)
            inventory.add_item_to_cart("Sauce Labs Backpack")
            inventory.go_to_cart()

        with allure.step("Перейти до оформлення замовлення"):
            cart = CartPage(authenticated_page)
            cart.proceed_to_checkout()

        with allure.step("Заповнити дані покупця"):
            checkout = CheckoutPage(authenticated_page)
            checkout.fill_customer_info("John", "Doe", "12345")
            checkout.continue_to_step_two()

        with allure.step("Завершити замовлення"):
            checkout.finish_order()

        with allure.step("Перевірити підтвердження замовлення"):
            assert "Thank you for your order" in checkout.get_complete_header()

    @allure.story("Валідація форми")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Порожнє поле First Name викликає помилку валідації")
    def test_checkout_empty_first_name(self, authenticated_page: Page):
        with allure.step("Додати товар у кошик"):
            inventory = InventoryPage(authenticated_page)
            inventory.add_item_to_cart("Sauce Labs Backpack")
            inventory.go_to_cart()

        with allure.step("Перейти до оформлення замовлення"):
            cart = CartPage(authenticated_page)
            cart.proceed_to_checkout()

        with allure.step("Заповнити форму з порожнім First Name"):
            checkout = CheckoutPage(authenticated_page)
            checkout.fill_customer_info("", "Doe", "12345")
            checkout.continue_to_step_two()

        with allure.step("Перевірити повідомлення про помилку"):
            assert checkout.is_error_visible()
            assert "First Name is required" in checkout.get_error_message()

    @allure.story("Валідація форми")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Порожнє поле Last Name викликає помилку валідації")
    def test_checkout_empty_last_name(self, authenticated_page: Page):
        with allure.step("Додати товар у кошик"):
            inventory = InventoryPage(authenticated_page)
            inventory.add_item_to_cart("Sauce Labs Backpack")
            inventory.go_to_cart()

        with allure.step("Перейти до оформлення замовлення"):
            cart = CartPage(authenticated_page)
            cart.proceed_to_checkout()

        with allure.step("Заповнити форму з порожнім Last Name"):
            checkout = CheckoutPage(authenticated_page)
            checkout.fill_customer_info("John", "", "12345")
            checkout.continue_to_step_two()

        with allure.step("Перевірити повідомлення про помилку"):
            assert checkout.is_error_visible()
            assert "Last Name is required" in checkout.get_error_message()

    @allure.story("Валідація форми")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Порожнє поле Postal Code викликає помилку валідації")
    def test_checkout_empty_postal_code(self, authenticated_page: Page):
        with allure.step("Додати товар у кошик"):
            inventory = InventoryPage(authenticated_page)
            inventory.add_item_to_cart("Sauce Labs Backpack")
            inventory.go_to_cart()

        with allure.step("Перейти до оформлення замовлення"):
            cart = CartPage(authenticated_page)
            cart.proceed_to_checkout()

        with allure.step("Заповнити форму з порожнім Postal Code"):
            checkout = CheckoutPage(authenticated_page)
            checkout.fill_customer_info("John", "Doe", "")
            checkout.continue_to_step_two()

        with allure.step("Перевірити повідомлення про помилку"):
            assert checkout.is_error_visible()
            assert "Postal Code is required" in checkout.get_error_message()