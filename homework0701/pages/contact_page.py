from time import sleep

import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.pages.add_member_menu_page import AddMemberMenuPage
from homework0701.pages.base_page import BasePage


class ContactPage(BasePage):
    _ADD_MEMBER_BTN = (MobileBy.ANDROID_UIAUTOMATOR,
                       'new UiScrollable(new UiSelector().scrollable(true).\
                       instance(0)).scrollIntoView(new UiSelector().\
                       text("添加成员").instance(0));')
    _MEMBER_LIST = (MobileBy.XPATH, "//*[@class='android.widget.TextView']")

    # 点击添加成员，跳转到添加成员方式选择页面
    def click_add_member(self):
        with allure.step("滑动找到添加成员"):
            self.driver.find_element(*self._ADD_MEMBER_BTN).click()
        return AddMemberMenuPage(self.driver)

    def get_member_list(self):
        with allure.step("查找通讯录成员列表信息，并断言"):
            sleep(3)
            eles = self.driver.find_elements(*self._MEMBER_LIST)
            name_list = []
            for value in eles:
                name_list.append(value.get_attribute("text"))
        return name_list
