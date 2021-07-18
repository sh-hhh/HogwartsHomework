import random, string

import pytest


@pytest.fixture()
def get_unique_userid():
    """
    产生一个随机的userid
    :return:
    """
    userid = ""
    num = string.ascii_letters + string.digits
    for i in range(10):
        userid += random.choice(num)
    return userid