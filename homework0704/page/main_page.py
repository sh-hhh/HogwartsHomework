from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from homework0704.page.addresslist_page import AddressListPage
from homework0704.page.base_page import BasePage

# 首页
class MainPage(BasePage):
    _ADDRESS_LIST = MobileBy.XPATH, "//*[@text='通讯录']"

    # 跳转到通讯录页面
    def goto_addresslist_page(self):
        # 点击通讯录
        self.find_and_click(*self._ADDRESS_LIST)
        return AddressListPage(self.driver)
