import pytest
import allure

from homework0701.common.file_process import get_data
from homework0701.pages.main_page import MainPage


@allure.feature("测试添加成员")
class Test_WeiXin:

    _test_data = get_data("add_member")

    @allure.story("添加成员成功测试用例")
    @allure.title("{name}成员添加成功")
    @pytest.mark.parametrize('name,phone', _test_data["success"])
    def test_add_member_success(self, driver_wework, name, phone):
        result = MainPage(driver_wework).click_contact().click_add_member().click_add_member_with_input(). \
            add_member_success(name, phone).click_back_to_contact_page().get_member_list()
        assert name in result

    @allure.story("添加成员失败测试用例")
    @allure.title("{name}成员添加失败")
    @pytest.mark.parametrize('name,phone,err_msg', _test_data["fail"])
    def test_add_member_fail(self, driver_wework, name, phone,err_msg):
        result = MainPage(driver_wework).click_contact().click_add_member().click_add_member_with_input().\
            add_member_fail(name,phone)
        assert err_msg == result