from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the Sauce Demo cart page."""

    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator("[data-test='cart-item']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def get_item_count(self) -> int:
        """Return the number of items in the cart."""
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        """Return a list of item names in the cart."""
        return self.page.locator("[data-test='inventory-item-name']").all_inner_texts()

    def remove_item(self, item_name: str):
        """Remove a specific item from the cart by its name."""
        item = self.page.locator(
            f"[data-test='cart-item']:has-text('{item_name}')"
        )
        item.locator("[data-test^='remove']").click()

    def proceed_to_checkout(self):
        """Click the Checkout button."""
        self.checkout_button.click()

    def continue_shopping(self):
        """Click Continue Shopping to go back to the inventory."""
        self.continue_shopping_button.click()