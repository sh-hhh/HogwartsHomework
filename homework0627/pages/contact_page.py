import logging
import allure
from time import sleep

from homework0627.common.file_process import get_data
from homework0627.pages.base_page import BasePage


# 通讯录页面

class ContactPage(BasePage):
    # _ADD_ICON = ("css", "i.member_colLeft_top_addBtn")
    # _ADD_DEPARTMENT = ("css", "a.js_create_party")
    # _DEPARTMENT_INPUT = ("css", "form.form>div:nth-child(1)>input")
    # _DROPDOWN_DEPART = ("css", ".inputDlg_item>a>span.ww_btn_Dropdown_arrow")
    # _PARENT_DEPART = ("css", ".inputDlg_item:nth-child(3)>div>div>ul>li>a>i")
    # _CONFIRM = ("xpath", '//a[@d_ck="submit"]')
    # _DEPARTMENT_LST = ("css", '.member_colLeft_bottom a:last-child')
    # _ERROR = ("id", "js_tips")

    _contact_page_locator = get_data("element_data.yml","contact_page")

    # 添加部门信息成功
    def add_department_success(self, department):
        with allure.step(f"输入部门信息：{department}，添加成功"):
            sleep(2)
            # self.find_and_click(*self._ADD_ICON)
            # self.find_and_click(*self._ADD_DEPARTMENT)
            # self.find_ele(*self._DEPARTMENT_INPUT).send_keys(department)
            # self.find_and_click(*self._DROPDOWN_DEPART)
            # self.find_and_click(*self._PARENT_DEPART)
            # self.find_and_click(*self._CONFIRM)
            self.find_and_click(*self._contact_page_locator["add_icon"])
            self.find_and_click(*self._contact_page_locator["add_depart"])
            self.find_ele(*self._contact_page_locator["input_depart"]).send_keys(department)
            self.find_and_click(*self._contact_page_locator["btn_choose_depart"])
            self.find_and_click(*self._contact_page_locator["choose_depart"])
            self.find_and_click(*self._contact_page_locator["btn_submit"])
            logging.info("输入部门信息后确定添加")
        return ContactPage(self.driver)

    # 添加部门信息失败
    def add_department_fail(self, department):
        with allure.step("部门信息输入不合法"):
            sleep(2)
            # self.find_and_click(*self._ADD_ICON)
            # self.find_and_click(*self._ADD_DEPARTMENT)
            # self.find_ele(*self._DEPARTMENT_INPUT).send_keys(department)
            # self.find_and_click(*self._DROPDOWN_DEPART)
            # self.find_and_click(*self._PARENT_DEPART)
            # self.find_and_click(*self._CONFIRM)
            self.find_and_click(*self._contact_page_locator["add_icon"])
            self.find_and_click(*self._contact_page_locator["add_depart"])
            self.find_ele(*self._contact_page_locator["input_depart"]).send_keys(department)
            self.find_and_click(*self._contact_page_locator["btn_choose_depart"])
            self.find_and_click(*self._contact_page_locator["choose_depart"])
            self.find_and_click(*self._contact_page_locator["btn_submit"])
            logging.info("输入部门信息不合法，点击确定提示错误信息")
            # error_tip = self.find_ele(*self._ERROR).text
            error_tip = self.find_ele(*self._contact_page_locator["error_tips"]).text
        return error_tip

    def get_departments(self):
        sleep(3)
        # eles = self.find_eles(*self._DEPARTMENT_LST)
        eles = self.find_eles(*self._contact_page_locator["list_depart"])
        logging.info("获取部门信息")
        return eles
