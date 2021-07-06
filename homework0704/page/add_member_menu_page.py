from appium.webdriver.common.mobileby import MobileBy
from homework0704.page.base_page import BasePage
from homework0704.page.edit_member_page import EditMemberPage


# 添加成员方式选择 菜单页面
class AddMemberMenuPage(BasePage):
    _HAND_ADD = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    # 手工输入添加
    def hand_input(self):
        # 点击手工输入添加
        self.find_and_click(*self._HAND_ADD)
        return EditMemberPage(self.driver)

    # 获取提示信息
    def get_succ_message(self):
        result = self.get_toast_text()
        return result
