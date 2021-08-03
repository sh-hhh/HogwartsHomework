from appium.webdriver.common.mobileby import MobileBy

from homework0704.page.base_page import BasePage


# 成员详情设置页面
class ContactDetailSettingPage(BasePage):
    _EDIT_MEMBER = (MobileBy.XPATH, "//*[@text='编辑成员']")

    # 跳转到编辑成员页面
    def goto_edit_member_page(self):
        # 点击编辑成员
        self.find_and_click(*self._EDIT_MEMBER)
        from homework0704.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)
