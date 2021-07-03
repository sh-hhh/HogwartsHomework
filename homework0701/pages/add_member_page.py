import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.pages.base_page import BasePage


class AddMemberPage(BasePage):
    # 添加成员成功
    def add_member_success(self, name, phone):
        from homework0701.pages.add_member_menu_page import AddMemberMenuPage
        with allure.step("输入姓名、手机号"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b09").send_keys(name)
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f7y").send_keys(phone)
        with allure.step("确认添加"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ad2").click()
        return AddMemberMenuPage(self.driver)

    def add_member_fail(self, name, phone):
        with allure.step("输入姓名、手机号"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b09").send_keys(name)
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f7y").send_keys(phone)
        with allure.step("确认添加"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ad2").click()
        return self.get_fail_message()

    def get_fail_message(self):
        # 获取错误提示信息，点击确定
        fail_message = self.driver.find_element(MobileBy.ID,
                                                'com.tencent.wework:id/bg4').text
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        return fail_message
