import pytest
import allure
import logging
import yaml

def get_data():
    with open('../data/data_cacl.yaml') as f:
        datas = yaml.safe_load(f)
        return datas

@allure.feature("计算加法、除法测试")
class Test_Calc():

    @allure.story("加法成功的测试用例")
    @allure.title("{a}+{b}是否等于{expect}")
    @pytest.mark.parametrize(['a','b','expect'],get_data()['add']['success'])
    def test_calc_add_success(self,a,b,expect,get_calc):
        logging.info(f'计算{a}+{b},结果为{expect}')
        assert expect == round(get_calc.add(a,b),2)

    @allure.story("加法失败的测试用例")
    @allure.title("{a}+{b}是否等于{expect}")
    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data()['add']['fail'])
    def test_calc_add_fail(self,a,b,expect,get_calc):
        try:
            get_calc.add(a,b)
        except Exception as e:
            logging.info(f"失败，错误信息{e}")
            assert expect == type(e).__name__

    @allure.story("除法成功的测试用例")
    @allure.title("{a}/{b}是否等于{expect}")
    @pytest.mark.parametrize(['a','b','expect'],get_data()['div']['success'])
    def test_cacl_div_success(self,a,b,expect,get_calc):
        logging.info(f'计算{a}/{b},结果为{expect}')
        assert expect == get_calc.div(a,b)

    @allure.story("除法失败的测试用例")
    @allure.title("{a}/{b}是否等于{expect}")
    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data()['div']['fail'])
    def test_cacl_div_fail(self, a, b, expect,get_calc):
        try:
            get_calc.div(a, b)
        except Exception as e:
            logging.info(f"失败，错误信息{e}")
            assert expect == type(e).__name__