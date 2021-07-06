import logging

from appium import webdriver

from homework0704.page.base_page import BasePage
from homework0704.page.main_page import MainPage


class APP(BasePage):

    def start(self):

        if self.driver is None:
            # 启动应用
            logging.info("driver == None 创建driver")
            desired_cap = {
                'platformName': 'android',
                'deviceName': 'DLS4C20525007740',
                'appPackage': 'com.tencent.wework',
                'appActivity': '.launch.LaunchSplashActivity',
                'noReset': 'true',
                'skipDeviceInitialization': 'true',
                'settings[waitForIdleTimeout]': 0
            }

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
            self.driver.implicitly_wait(5)
        else:
            logging.info('driver != None 复用driver')
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def back(self, num):
        for i in range(num):
            self.driver.back()

    def goto_mainpage(self):
        return MainPage(self.driver)
