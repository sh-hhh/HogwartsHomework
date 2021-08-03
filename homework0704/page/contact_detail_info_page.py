from appium.webdriver.common.mobileby import MobileBy

from homework0704.page.base_page import BasePage

from homework0704.page.contact_detail_setting_page import ContactDetailSettingPage


# 个人信息页面
class ContactDetailInfoPage(BasePage):
    _ICON_INFO = (MobileBy.ID, "com.tencent.wework:id/hc9")

    # 进入个人信息设置页面
    def goto_contact_detail_setting_page(self):
        # 点击右上角的icon
        self.find_and_click(*self._ICON_INFO)
        return ContactDetailSettingPage(self.driver)
