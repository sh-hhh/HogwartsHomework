from appium import webdriver


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_and_click(self,by,locator):
        element = self.driver.find_element(by, locator)
        element.click()
        return element