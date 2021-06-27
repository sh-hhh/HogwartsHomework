import logging

import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            with allure.step("复用浏览器，打开首页"):
                opt = webdriver.ChromeOptions()
                opt.debugger_address = "127.0.0.1:9222"
                self.driver = webdriver.Chrome(options=opt)
                self.driver.implicitly_wait(10)
                self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
                logging.info("复用浏览器，打开首页")
        else:
            self.driver = base_driver

    def find_ele(self,by,locator):
        return self.driver.find_element(by,locator)

    def find_eles(self,by,locator):
        return self.driver.find_elements(by, locator)