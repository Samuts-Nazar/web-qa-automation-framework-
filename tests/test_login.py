import allure
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Авторизація")
class TestLogin:

    @allure.story("Успішний логін")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Стандартний юзер потрапляє на інвентар після логіну")
    def test_successful_login(self, page: Page):
        with allure.step("Відкрити сторінку логіну"):
            login = LoginPage(page)
            login.open()

        with allure.step("Залогінитись як standard_user"):
            login.login("standard_user", "secret_sauce")

        with allure.step("Перевірити перехід на сторінку інвентаря"):
            assert "inventory" in page.url

    @allure.story("Невалідні дані")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Неправильний пароль показує помилку")
    def test_invalid_password(self, page: Page):
        with allure.step("Відкрити сторінку логіну"):
            login = LoginPage(page)
            login.open()

        with allure.step("Залогінитись з неправильним паролем"):
            login.login("standard_user", "wrong_password")

        with allure.step("Перевірити повідомлення про помилку"):
            assert login.is_error_visible()
            assert "Username and password do not match" in login.get_error_message()

    @allure.story("Заблокований користувач")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Locked out user бачить відповідне повідомлення")
    def test_locked_out_user(self, page: Page):
        with allure.step("Відкрити сторінку логіну"):
            login = LoginPage(page)
            login.open()

        with allure.step("Залогінитись як locked_out_user"):
            login.login("locked_out_user", "secret_sauce")

        with allure.step("Перевірити повідомлення про блокування"):
            assert login.is_error_visible()
            assert "locked out" in login.get_error_message()

    @allure.story("Валідація форми")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Порожня форма логіну показує помилку валідації")
    def test_empty_credentials(self, page: Page):
        with allure.step("Відкрити сторінку логіну"):
            login = LoginPage(page)
            login.open()

        with allure.step("Відправити порожню форму"):
            login.login("", "")

        with allure.step("Перевірити повідомлення про обов'язкове поле"):
            assert login.is_error_visible()
            assert "Username is required" in login.get_error_message()

    @allure.story("Невалідні дані")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Перевірка помилки логіну: {username} / {password}")
    @pytest.mark.parametrize("username, password, expected_error", [
        ("standard_user", "wrong", "Username and password do not match"),
        ("unknown_user", "secret_sauce", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ])
    def test_login_errors_parametrized(self, page: Page, username, password, expected_error):
        with allure.step("Відкрити сторінку логіну"):
            login = LoginPage(page)
            login.open()

        with allure.step(f"Залогінитись як '{username}' з паролем '{password}'"):
            login.login(username, password)

        with allure.step(f"Перевірити повідомлення про помилку: {expected_error}"):
            assert login.is_error_visible()
            assert expected_error in login.get_error_message()

    @allure.story("Навігація та меню")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC-N-05: Logout перенаправляє на сторінку логіну і очищує сесію")
    def test_logout(self, authenticated_page: Page):
        with allure.step("Перейти на сторінку інвентаря (залогінений юзер)"):
            inventory = InventoryPage(authenticated_page)
            assert "inventory" in authenticated_page.url

        with allure.step("Відкрити бургер-меню"):
            authenticated_page.locator("#react-burger-menu-btn").click()

        with allure.step("Перевірити, що меню відкрилось"):
            assert authenticated_page.locator(".bm-menu").is_visible()

        with allure.step("Натиснути Logout"):
            authenticated_page.locator("#logout_sidebar_link").click()

        with allure.step("Перевірити перехід на сторінку логіну"):
            assert "saucedemo.com" in authenticated_page.url
            login = LoginPage(authenticated_page)
            assert login.login_button.is_visible()

        with allure.step("Перевірити, що сесія очищена (натискання Back не повертає на інвентар)"):
            authenticated_page.go_back()
            assert "saucedemo.com" in authenticated_page.url
            assert login.login_button.is_visible()
