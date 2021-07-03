from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.pages.add_member_page import AddMemberPage
from homework0701.pages.base_page import BasePage


class AddMemberMenuPage(BasePage):
    _HAND_ADD = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _BACK_BTN = (MobileBy.ID, "com.tencent.wework:id/hbs")

    # 选择手动输入添加，天转到添加成员页面
    def click_add_member_with_input(self):
        with allure.step("点击手动输入添加"):
            self.find_and_click(*self._HAND_ADD)
        return AddMemberPage(self.driver)

    def click_back_to_contact_page(self):
        from homework0701.pages.contact_page import ContactPage
        with allure.step("返回通讯录页面"):
            sleep(3)
            self.find_and_click(*self._BACK_BTN)
        return ContactPage(self.driver)
