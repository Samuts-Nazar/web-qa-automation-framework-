from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for the Sauce Demo checkout flow (step one and step two)."""

    URL_STEP_ONE = "https://www.saucedemo.com/checkout-step-one.html"
    URL_STEP_TWO = "https://www.saucedemo.com/checkout-step-two.html"
    URL_COMPLETE = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Step one — customer info
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error_message = page.locator("[data-test='error']")
        # Step two — order summary
        self.finish_button = page.locator("[data-test='finish']")
        # Complete
        self.complete_header = page.locator("[data-test='complete-header']")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        """Fill in the customer information form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_step_two(self):
        """Click Continue to proceed to order summary."""
        self.continue_button.click()

    def finish_order(self):
        """Click Finish to complete the order."""
        self.finish_button.click()

    def get_error_message(self) -> str:
        """Return the text of the validation error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Return True if the error message is visible."""
        return self.error_message.is_visible()

    def get_complete_header(self) -> str:
        """Return the confirmation header text on the complete page."""
        return self.complete_header.inner_text()
