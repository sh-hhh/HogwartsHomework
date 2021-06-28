import logging
import allure

from homework0627.pages.base_page import BasePage
from homework0627.pages.contact_page import ContactPage
from homework0627.common.file_process import get_data

# 首页
class MainPage(BasePage):
    # _CONTACT = ("id", "menu_contacts")
    _main_page_locator = get_data("element_data.yml","main_page")

    @allure.step("跳转到通讯录页面")
    # 跳转到通讯录页面
    def goto_contact(self):

        self.find_and_click(*self._main_page_locator["contact_menu"])
        logging.info("跳转到通讯录页面")
        return ContactPage(self.driver)