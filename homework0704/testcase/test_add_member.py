import pytest
from faker import Faker

from homework0704.common.file_process import get_data
from homework0704.page.app import APP


class TestAddMember:

    def setup_class(self):
        self.app = APP()
        fake = Faker(locale='zh_CN')
        self.name = fake.name()
        self.phone = fake.phone_number()

    def setup(self):
        self.main = self.app.start().goto_mainpage()

    def teardown(self):
        # self.app.restart()
        self.app.back(5)

    def teardown_class(self):
        self.app.quit()

    def test_add_member_success(self):
        result = self.main.goto_addresslist_page().goto_add_member_menu_page().hand_input(). \
            edit_member_success(self.name, self.phone).get_succ_message()
        assert "添加成功" == result

    @pytest.mark.parametrize("name,phone,exp_res", get_data("add_member")["fail"])
    def test_add_member_fail(self, name, phone, exp_res):
        result = self.main.goto_addresslist_page().goto_add_member_menu_page().hand_input(). \
            edit_member_fail(name, phone)
        assert result == exp_res

    def test_delete_member(self):
        # name = "李四"
        result = self.main.goto_addresslist_page().goto_contact_detail_page(self.name). \
            goto_contact_detail_setting_page().goto_edit_member_page().delete_member().get_contact_list()
        assert self.name not in result
