from pages.base_page import BasePage
from utils.locator_reader import LocatorReader

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LocatorReader("data/locators.xlsx")

    def open_sneakers(self):
        self.click(self.locator.get("home", "main_category"))
        self.click(self.locator.get("home", "sneakers"))
