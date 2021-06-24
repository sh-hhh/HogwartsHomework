import os
import sys
import pytest

sys.path.insert(0,os.path.dirname(os.getcwd())) #设置当前运行代码文件所在的目录为一级目录
from code.calculator import Calculator


@pytest.fixture()
def get_calc():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("计算结束")