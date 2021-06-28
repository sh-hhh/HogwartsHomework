import logging

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
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

    def find_ele(self, by, locator):
        by_name = self.find_by_name(by)
        return self.driver.find_element(by_name, locator)

    def find_eles(self, by, locator):
        by_name = self.find_by_name(by)
        return self.driver.find_elements(by_name, locator)

    def find_and_click(self, by, locator):
        by_name = self.find_by_name(by)
        ele = self.find_ele(by_name, locator)
        ele.click()

    def find_by_name(self, by):
        if by == 'id':
            by_name = By.ID
        elif by == 'name':
            by_name = By.NAME
        elif by == 'class':
            by_name = By.CLASS_NAME
        elif by == 'link_txt':
            by_name = By.LINK_TEXT
        elif by == 'partial_link':
            by_name = By.PARTIAL_LINK_TEXT
        elif by == 'tag':
            by_name = By.TAG_NAME
        elif by == 'xpath':
            by_name = By.XPATH
        else:
            by_name = By.CSS_SELECTOR
        return by_name