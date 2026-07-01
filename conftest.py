import pytest
from playwright.sync_api import sync_playwright, Browser, Page

from pages.login_page import LoginPage


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_URL = "https://www.saucedemo.com"
STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


# ---------------------------------------------------------------------------
# Browser fixture — one browser instance per test session
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def browser():
    """Launch a Chromium browser once for the whole test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


# ---------------------------------------------------------------------------
# Page fixture — fresh page for every test
# ---------------------------------------------------------------------------

@pytest.fixture
def page(browser: Browser) -> Page:
    """Create a new browser page (tab) for each test and close it after."""
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()
    yield page
    context.close()


# ---------------------------------------------------------------------------
# Authenticated page fixture — already logged in as standard_user
# ---------------------------------------------------------------------------

@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Return a page that is already logged in as standard_user."""
    login = LoginPage(page)
    login.open()
    login.login(STANDARD_USER, PASSWORD)
    page.wait_for_url("**/inventory.html")
    return page


# --------------------------------------------------------------------------
# Screenshot on failure
# --------------------------------------------------------------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach a screenshot to the report when a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page") or item.funcargs.get("authenticated_page")
        if page:
            screenshot_path = f"screenshots/{item.nodeid.replace('/', '_').replace('::', '_')}.png"
            import os
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=screenshot_path)
