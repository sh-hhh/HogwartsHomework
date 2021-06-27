import logging

import allure
import yaml
from selenium.webdriver.common.by import By

from homework0627.pages.base_page import BasePage
from homework0627.pages.contact_page import ContactPage

# 首页
class MainPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    @allure.step("跳转到通讯录页面")
    # 跳转到通讯录页面
    def goto_contact(self):
        self.find_ele(*self._CONTACT).click()
        logging.info("跳转到通讯录页面")
        return ContactPage(self.driver)