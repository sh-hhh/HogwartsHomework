from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from homework0704.page.base_page import BasePage
from homework0704.page.add_member_menu_page import AddMemberMenuPage
from homework0704.page.contact_detail_info_page import ContactDetailInfoPage


# 通讯录页面
class AddressListPage(BasePage):
    _ADD_MEMBER_BTN = (MobileBy.ANDROID_UIAUTOMATOR,
                       'new UiScrollable(new UiSelector().scrollable(true).\
                       instance(0)).scrollIntoView(new UiSelector().\
                       text("添加成员").instance(0));')

    _CONTACT_LIST = (MobileBy.XPATH, "//*[@class='android.widget.TextView']")

    # 跳转到添加成员菜单页面
    def goto_add_member_menu_page(self):
        # 点击添加成员
        self.find_and_click(*self._ADD_MEMBER_BTN)
        return AddMemberMenuPage(self.driver)

    # 进入成员个人信息页
    def goto_contact_detail_page(self,name):
        # 点击成员列表的成员
        # locator = f"//*[@text='{name}']"
        # member_locator = (MobileBy.XPATH, locator)
        # self.find_and_click(*member_locator)
        self.swipe_find(name, num= 6).click()
        return ContactDetailInfoPage(self.driver)

    # 获取通讯录列表信息
    def get_contact_list(self):
        sleep(2)
        eles = self.driver.find_elements(*self._CONTACT_LIST)
        contact_list = []
        for value in eles:
            contact_list.append(value.get_attribute("text"))
        return contact_list
