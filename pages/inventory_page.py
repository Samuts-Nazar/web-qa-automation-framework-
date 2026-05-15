from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the Sauce Demo inventory (products) page."""

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.inventory_items = page.locator("[data-test='inventory-item']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def get_item_count(self) -> int:
        """Return the number of items visible on the page."""
        return self.inventory_items.count()

    def sort_by(self, option: str):
        """Select a sort option. Available: 'az', 'za', 'lohi', 'hilo'."""
        self.sort_dropdown.select_option(option)

    def get_item_names(self) -> list[str]:
        """Return a list of all visible product names."""
        return self.page.locator("[data-test='inventory-item-name']").all_inner_texts()

    def get_item_prices(self) -> list[float]:
        """Return a list of all visible product prices as floats."""
        raw = self.page.locator("[data-test='inventory-item-price']").all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]

    def add_item_to_cart(self, item_name: str):
        """Add a specific item to the cart by its name."""
        item = self.page.locator(
            f"[data-test='inventory-item']:has-text('{item_name}')"
        )
        item.locator("button").click()

    def get_cart_badge_count(self) -> int:
        """Return the number shown on the cart badge."""
        return int(self.cart_badge.inner_text())

    def go_to_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.cart_link.click()
