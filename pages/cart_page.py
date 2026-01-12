from pages.base_page import BasePage
from utils.locator_reader import LocatorReader

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LocatorReader("data/locators.xlsx")

    def checkout(self):
        self.click(self.locator.get("cart", "view_bag"))
        self.click(self.locator.get("cart", "checkout"))
