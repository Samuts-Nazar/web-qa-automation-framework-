from playwright.sync_api import Page

def test_raw_login(page: Page):
    # 1. Перейди на сайт https://www.saucedemo.com/
    
    # 2. Знайди поле Username (використовуй локатор "[data-test='username']") і введи "standard_user"
    
    # 3. Знайди поле Password (локатор "[data-test='password']") і введи "secret_sauce"
    
    # 4. Знайди кнопку Login (локатор "[data-test='login-button']") і клікни по ній
    
    # 5. Перевір (через assert), що поточний URL сторінки дорівнює "https://www.saucedemo.com/inventory.html"
    pass