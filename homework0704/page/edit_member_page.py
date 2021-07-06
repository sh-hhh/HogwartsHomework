from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework0704.page.base_page import BasePage


# 编辑成员信息页
class EditMemberPage(BasePage):
    _NAME = (MobileBy.ID, "com.tencent.wework:id/b09")
    _PHONE = (MobileBy.ID, "com.tencent.wework:id/f7y")
    _SAVE = (MobileBy.ID, "com.tencent.wework:id/ad2")
    _FAIL_MSG = (MobileBy.ID, 'com.tencent.wework:id/bg4')
    _CONFIRM_BTN = (MobileBy.XPATH, "//*[@text='确定']")

    _DELETE_MEMBER_BTN = (MobileBy.ANDROID_UIAUTOMATOR,
                       'new UiScrollable(new UiSelector().scrollable(true).\
                       instance(0)).scrollIntoView(new UiSelector().\
                       text("删除成员").instance(0));')

    # 成功添加成员信息
    def edit_member_success(self, name, phone):
        # 输入姓名、手机号
        self.find_and_sendkeys(*self._NAME, name)
        self.find_and_sendkeys(*self._PHONE, phone)
        # 点击保存
        self.find_and_click(*self._SAVE)

        from homework0704.page.add_member_menu_page import AddMemberMenuPage
        return AddMemberMenuPage(self.driver)

    # 添加成员失败
    def edit_member_fail(self, name, phone):
        # 输入姓名、手机号
        self.find_and_sendkeys(*self._NAME, name)
        self.find_and_sendkeys(*self._PHONE, phone)
        # 点击保存
        self.find_and_click(*self._SAVE)
        return self.get_fail_message()

    def get_fail_message(self):
        # 获取错误提示信息，点击确定
        # locator = self.find(*self._FAIL_MSG)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self._FAIL_MSG))
        fail_message = self.find(*self._FAIL_MSG).text
        self.find_and_click(*self._CONFIRM_BTN)
        return fail_message

    # 删除成员
    def delete_member(self):
        # 点击删除、确认
        self.find_and_click(*self._DELETE_MEMBER_BTN)
        self.find_and_click(*self._CONFIRM_BTN)
        from homework0704.page.addresslist_page import AddressListPage
        return AddressListPage(self.driver)