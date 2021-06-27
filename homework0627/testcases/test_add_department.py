import allure
import pytest
import logging
from homework0627.pages.main_page import MainPage

@allure.feature("添加部门测试")
class TestAddDepartment:
    def setup(self):
        self.main_page = MainPage()


    @allure.story("部门添加成功")
    @allure.title(f"添加部门成功测试用例")
    @pytest.mark.parametrize("department",["测试部","销售部"])
    def test_add_department(self,department):
        result = self.main_page.goto_contact().add_department_success(department).get_departments()
        with allure.step("新增部门后，断言"):
            logging.info("断言新加的部门")
            assert department == result[-1].text
