import allure
from appium.webdriver.common.mobileby import MobileBy

from homework0701.pages.base_page import BasePage
from homework0701.pages.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (MobileBy.XPATH, "//*[@text='通讯录']")

    # 从默认的消息页跳转到通讯录
    def click_contact(self):
        with allure.step("点击通讯录"):
            self.driver.find_element(*self._CONTACT).click()
        return ContactPage(self.driver)