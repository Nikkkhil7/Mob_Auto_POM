import openpyxl
from appium.webdriver.common.appiumby import AppiumBy

class LocatorReader:
    def __init__(self, file_path):
        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active

    def get(self, page, name):
        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            page_name, locator_name, by, value = row
            if page_name == page and locator_name == name:
                if by == "XPATH":
                    return (AppiumBy.XPATH, value)
                if by == "ID":
                    return (AppiumBy.ID, value)
                if by == "ANDROID_UIAUTOMATOR":
                    return (AppiumBy.ANDROID_UIAUTOMATOR, value)

        raise Exception(f"Locator not found: {page}.{name}")
