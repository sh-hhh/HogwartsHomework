import pytest
from calculator import Calculator
import yaml

def get_data():
    with open('data_cacl.yaml') as f:
        datas = yaml.safe_load(f)
        return datas

class Test_Calc():
    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize(['a','b','expect'],get_data()['add']['success'])
    def test_calc_add_success(self,a,b,expect):
        assert expect == round(self.calc.add(a,b),2)

    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data()['add']['fail'])
    def test_calc_add_fail(self,a,b,expect):
        try:
            self.calc.add(a,b)
        except Exception as e:
            assert expect == type(e).__name__

    @pytest.mark.parametrize(['a','b','expect'],get_data()['div']['success'])
    def test_cacl_div_success(self,a,b,expect):
        assert expect == self.calc.div(a,b)

    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data()['div']['fail'])
    def test_cacl_div_fail(self, a, b, expect):
        try:
            self.calc.div(a, b)
        except Exception as e:
            assert expect == type(e).__name__
