import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.pages.base_page import BasePage


class AddMemberPage(BasePage):
    _NAME = (MobileBy.ID, "com.tencent.wework:id/b09")
    _PHONE = (MobileBy.ID, "com.tencent.wework:id/f7y")
    _ADD_CONFIRM = (MobileBy.ID, "com.tencent.wework:id/ad2")
    _FAIL_MSG = (MobileBy.ID,'com.tencent.wework:id/bg4')
    _CONFIRM_FAIL = (MobileBy.XPATH, "//*[@text='确定']")

    # 添加成员成功
    def add_member_success(self, name, phone):
        from homework0701.pages.add_member_menu_page import AddMemberMenuPage
        with allure.step("输入姓名、手机号"):
            self.driver.find_element(*self._NAME).send_keys(name)
            self.driver.find_element(*self._PHONE).send_keys(phone)
        with allure.step("确认添加"):
            self.driver.find_element(*self._ADD_CONFIRM).click()
        return AddMemberMenuPage(self.driver)

    def add_member_fail(self, name, phone):
        with allure.step("输入姓名、手机号"):
            self.driver.find_element(*self._NAME).send_keys(name)
            self.driver.find_element(*self._PHONE).send_keys(phone)
        with allure.step("确认添加"):
            self.driver.find_element(*self._ADD_CONFIRM).click()
        return self.get_fail_message()

    def get_fail_message(self):
        # 获取错误提示信息，点击确定
        fail_message = self.driver.find_element(*self._FAIL_MSG).text
        self.driver.find_element(*self._CONFIRM_FAIL).click()
        self.driver.back()
        self.driver.back()
        return fail_message
