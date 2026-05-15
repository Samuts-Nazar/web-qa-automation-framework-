from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


class TestInventory:
    """Test suite for the inventory (products) page."""

    def test_all_items_displayed(self, authenticated_page: Page):
        """All 6 products should be visible after login."""
        inventory = InventoryPage(authenticated_page)
        assert inventory.get_item_count() == 6

    def test_sort_name_az(self, authenticated_page: Page):
        """Products sorted A→Z should be in ascending alphabetical order."""
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("az")
        names = inventory.get_item_names()
        assert names == sorted(names)

    def test_sort_name_za(self, authenticated_page: Page):
        """Products sorted Z→A should be in descending alphabetical order."""
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("za")
        names = inventory.get_item_names()
        assert names == sorted(names, reverse=True)

    def test_sort_price_low_to_high(self, authenticated_page: Page):
        """Products sorted by price low→high should be in ascending order."""
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("lohi")
        prices = inventory.get_item_prices()
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self, authenticated_page: Page):
        """Products sorted by price high→low should be in descending order."""
        inventory = InventoryPage(authenticated_page)
        inventory.sort_by("hilo")
        prices = inventory.get_item_prices()
        assert prices == sorted(prices, reverse=True)

    def test_add_item_updates_cart_badge(self, authenticated_page: Page):
        """Adding a product should increment the cart badge counter."""
        inventory = InventoryPage(authenticated_page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        assert inventory.get_cart_badge_count() == 1
