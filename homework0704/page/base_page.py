import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: webdriver = None):
        self.driver = driver

    # 查找元素
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 查找元素并点击
    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    # 查找元素并输入
    def find_and_sendkeys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

    def swipe_find(self, text, num=3):
        logging.info('swipe_find')
        '''
        1、添加查找次数
        2、添加 查找文本 的输入参数
        3、添加隐式等待的动态设置
        :param text:
        :param num:
        :return:
        '''
        # 滑动查找元素
        # 优化 隐式等待，提高查找速度
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了 {i} 次，未找到")
