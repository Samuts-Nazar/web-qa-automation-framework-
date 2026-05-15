from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    """Test suite for the checkout flow."""

    def test_happy_path(self, authenticated_page: Page):
        """Full order flow: add item → cart → checkout → complete."""
        # Add item
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        # Proceed to checkout
        cart = CartPage(authenticated_page)
        cart.proceed_to_checkout()

        # Fill in customer info
        checkout = CheckoutPage(authenticated_page)
        checkout.fill_customer_info("John", "Doe", "12345")
        checkout.continue_to_step_two()

        # Finish order
        checkout.finish_order()

        assert "Thank you for your order" in checkout.get_complete_header()

    def test_checkout_empty_first_name(self, authenticated_page: Page):
        """Empty first name should trigger a validation error."""
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(authenticated_page)
        checkout.fill_customer_info("", "Doe", "12345")
        checkout.continue_to_step_two()

        assert checkout.is_error_visible()
        assert "First Name is required" in checkout.get_error_message()

    def test_checkout_empty_last_name(self, authenticated_page: Page):
        """Empty last name should trigger a validation error."""
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(authenticated_page)
        checkout.fill_customer_info("John", "", "12345")
        checkout.continue_to_step_two()

        assert checkout.is_error_visible()
        assert "Last Name is required" in checkout.get_error_message()

    def test_checkout_empty_postal_code(self, authenticated_page: Page):
        """Empty postal code should trigger a validation error."""
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()

        cart = CartPage(authenticated_page)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(authenticated_page)
        checkout.fill_customer_info("John", "Doe", "")
        checkout.continue_to_step_two()

        assert checkout.is_error_visible()
        assert "Postal Code is required" in checkout.get_error_message()
