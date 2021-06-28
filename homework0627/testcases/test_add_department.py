import allure
import pytest
import logging

from homework0627.pages.main_page import MainPage
from homework0627.common.file_process import get_data


@allure.feature("添加部门测试")
class TestAddDepartment:
    _test_data = get_data("test_data.yml","add_department")

    def setup(self):
        self.main_page = MainPage()

    @allure.story("部门添加成功")
    @allure.title(f"添加部门成功测试用例")
    @pytest.mark.parametrize("department", _test_data['success'])
    def test_add_department_success(self, department):
        result = self.main_page.goto_contact().add_department_success(department).get_departments()
        with allure.step("新增部门后，断言"):
            logging.info("断言新加的部门")
            assert department == result[-1].text

    @allure.story("部门添加失败")
    @allure.title(f"添加部门失败测试用例")
    @pytest.mark.parametrize("department,error", _test_data['fail'])
    def test_add_department_fail(self, department, error):
        result = self.main_page.goto_contact().add_department_fail(department)
        assert error == result
