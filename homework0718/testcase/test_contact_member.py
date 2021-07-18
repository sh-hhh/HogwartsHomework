import logging

import allure
from faker import Faker
from homework0718.api.api_contact_member import ApiContactMember

@allure.feature("测试通讯录成员管理相关接口")
class TestMember:
    def setup_class(self):
        self.api_contact_member = ApiContactMember()
        self.fake = Faker(locale='zh_CN')

    @allure.title("测试添加成员")
    def test_add_user(self, get_unique_userid):
        logging.info("测试通讯录添加成员信息")
        name = self.fake.name()
        phone = "+86 " + self.fake.phone_number()
        department = [1, 2]
        # globals()["xxx"]方法可以在不同类不同用例之间共用
        globals()["userid"] = get_unique_userid
        result = self.api_contact_member.add_member(globals()["userid"], name, phone, department)
        user_info = self.api_contact_member.get_member(globals()["userid"])
        assert result.json().get("errcode") == 0
        assert user_info.json().get("name") == name

    @allure.title("测试查找成员")
    def test_get_user(self):
        logging.info("测试通讯录查找成员信息")
        result = self.api_contact_member.get_member(globals()["userid"])
        assert result.json().get("errcode") == 0

    @allure.title("测试更新成员")
    def test_update_user(self):
        logging.info("测试通讯录更新成员信息")
        position = self.fake.job()
        result = self.api_contact_member.update_member(globals()["userid"], position=position)
        user_info = self.api_contact_member.get_member(globals()["userid"])
        assert result.json().get("errcode") == 0
        assert user_info.json().get("position") == position

    @allure.title("测试删除成员")
    def test_delete_user(self):
        logging.info("测试通讯录删除成员信息")
        result = self.api_contact_member.delete_member(globals()["userid"])
        user_info = self.api_contact_member.get_member(globals()["userid"])
        assert result.json().get("errcode") == 0
        assert user_info.json().get("errcode") == 60111
