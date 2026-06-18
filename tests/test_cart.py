import allure
from pages.cart_page import CartPage


@allure.feature("Кошик")
@allure.story("Відображення товару")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC-C01: Доданий товар відображається в кошику")
def test_cart_displays_added_item(authenticated_page):
    with allure.step("Перейти на сторінку інвентаря"):
        authenticated_page.goto("/inventory.html")

    with allure.step("Додати Sauce Labs Backpack у кошик"):
        authenticated_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    with allure.step("Перейти у кошик"):
        authenticated_page.goto("/cart.html")

    with allure.step("Перевірити, що товар присутній у кошику"):
        cart = CartPage(authenticated_page)
        assert "Sauce Labs Backpack" in cart.get_item_names()


@allure.feature("Кошик")
@allure.story("Видалення товару")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC-C02: Після Remove товар зникає з кошика")
def test_cart_remove_item(authenticated_page):
    with allure.step("Перейти на сторінку інвентаря"):
        authenticated_page.goto("/inventory.html")

    with allure.step("Додати Sauce Labs Backpack у кошик"):
        authenticated_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    with allure.step("Перейти у кошик"):
        authenticated_page.goto("/cart.html")

    with allure.step("Видалити товар з кошика"):
        authenticated_page.locator("[data-test='remove-sauce-labs-backpack']").click()

    with allure.step("Перевірити, що кошик порожній"):
        cart = CartPage(authenticated_page)
        assert cart.get_item_count() == 0


@allure.feature("Кошик")
@allure.story("Навігація")
@allure.severity(allure.severity_level.MINOR)
@allure.title("TC-C03: Continue Shopping повертає на інвентар")
def test_cart_continue_shopping(authenticated_page):
    with allure.step("Перейти у кошик"):
        authenticated_page.goto("/cart.html")

    with allure.step("Натиснути Continue Shopping"):
        authenticated_page.locator("[data-test='continue-shopping']").click()

    with allure.step("Перевірити перехід на сторінку інвентаря"):
        assert "inventory.html" in authenticated_page.url


@allure.feature("Кошик")
@allure.story("Оформлення замовлення")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC-C04: Checkout переводить на оформлення")
def test_cart_proceed_to_checkout(authenticated_page):
    with allure.step("Перейти на сторінку інвентаря"):
        authenticated_page.goto("/inventory.html")

    with allure.step("Додати Sauce Labs Backpack у кошик"):
        authenticated_page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    with allure.step("Перейти у кошик"):
        authenticated_page.goto("/cart.html")

    with allure.step("Натиснути Checkout"):
        authenticated_page.locator("[data-test='checkout']").click()

    with allure.step("Перевірити перехід на сторінку оформлення замовлення"):
        assert "checkout-step-one.html" in authenticated_page.url