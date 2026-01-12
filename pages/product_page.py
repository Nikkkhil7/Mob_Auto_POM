import time
from pages.base_page import BasePage
from utils.locator_reader import LocatorReader

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LocatorReader("data/locators.xlsx")

    def open_product(self):
        self.click(self.locator.get("product", "product_name"))
        time.sleep(6)  # Adidas Compose UI load

    def add_to_bag(self):
        # 🔥 EXACT WORKING SCROLL
        self.driver.find_element(*self.locator.get("product", "scroll_add_to_bag"))
        self.click(self.locator.get("product", "add_to_bag"))
