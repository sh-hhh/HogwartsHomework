from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest
import allure

from homework0701.common.file_process import get_data

@allure.feature("测试添加成员")
class Test_WeiXin:
    def setup(self):
        desired_cap = {}
        desired_cap['platformName'] = 'android'
        # desired_cap['platformVersion'] = '6.0'
        desired_cap['deviceName'] = 'DLS4C20525007740'
        desired_cap['appPackage'] = 'com.tencent.wework'
        desired_cap['appActivity'] = '.launch.LaunchSplashActivity'
        desired_cap['noReset'] = 'true'
        # desired_cap['skipDeviceInitialization'] = 'true'
        # dontStopAppOnReset=true不会重启app,app打开哪一页就从哪一页开始执行
        desired_cap['dontStopAppOnReset'] = 'true'
        desired_cap['settings[waitForIdleTimeout]'] = 0
        # desired_cap['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @allure.story("添加成员测试用例")
    @allure.title("{name}成员添加成功")
    @pytest.mark.parametrize('name,phone', get_data("add_member")["success"])
    def test_add_member_success(self, name, phone):
        with allure.step("点击通讯录"):
            self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        with allure.step("滑动找到添加成员"):
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).\
                                     instance(0)).scrollIntoView(new UiSelector().\
                                     text("添加成员").instance(0));').click()
        with allure.step("点击手动输入添加"):
            self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        with allure.step("输入姓名、手机号"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b09").send_keys(name)
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f7y").send_keys(phone)
        with allure.step("确认添加"):
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ad2").click()
        with allure.step("返回到通讯录页面"):
            self.driver.back()
            self.driver.back()
        with allure.step("查找通讯录成员列表信息，并断言"):
            sleep(3)
            eles = self.driver.find_elements(MobileBy.XPATH, "//*[@class='android.widget.TextView']")
            name_list = []
            for value in eles:
                name_list.append(value.get_attribute("text"))

            assert name in name_list