import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from homework0627.pages.base_page import BasePage

# 通讯录页面

class ContactPage(BasePage):
    _ADD_ICON = (By.CSS_SELECTOR, "i.member_colLeft_top_addBtn")
    _ADD_DEPARTMENT = (By.CSS_SELECTOR, "a.js_create_party")
    _DEPARTMENT_INPUT = (By.CSS_SELECTOR, "form.form>div:nth-child(1)>input")
    _DROPDOWN_DEPART = (By.CSS_SELECTOR, ".inputDlg_item>a>span.ww_btn_Dropdown_arrow")
    _PARENT_DEPART = (By.CSS_SELECTOR,  ".inputDlg_item:nth-child(3)>div>div>ul>li>a>i")
    _CONFIRM = (By.LINK_TEXT, "确定")
    _DEPARTMENT_LST = (By.CSS_SELECTOR, '.member_colLeft_bottom a:last-child')

    # 添加部门信息
    def add_department_success(self,department):
        with allure.step(f"输入部门信息：{department}，添加成功"):
            self.find_ele(*self._ADD_ICON).click()
            self.find_ele(*self._ADD_DEPARTMENT).click()
            self.find_ele(*self._DEPARTMENT_INPUT).send_keys(department)
            self.find_ele(*self._DROPDOWN_DEPART).click()
            self.find_ele(*self._PARENT_DEPART).click()
            self.find_ele(*self._CONFIRM).click()
            logging.info("输入部门信息后确定添加")
        return ContactPage(self.driver)

    def get_departments(self):
        sleep(5)
        eles = self.find_eles(*self._DEPARTMENT_LST)
        logging.info("获取部门信息")
        return eles