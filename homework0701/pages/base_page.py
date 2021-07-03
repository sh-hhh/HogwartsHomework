from appium import webdriver


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver
