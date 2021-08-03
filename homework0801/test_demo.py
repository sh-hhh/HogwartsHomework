import logging

import pytest


@pytest.mark.parametrize('name', ['张三', '李四'])
def test_demo(name):
    print(name)
    logging.info('日志打印：'+name)
