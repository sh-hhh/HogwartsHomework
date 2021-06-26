import time

import yaml
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

# 保存数据到文件中
def save_data(datas):
    with open("data.yml","w") as f:
        yaml.dump(datas,f)

# 将文件中的数据读取出来
def get_data():
    with open("data.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas

# 通过复用浏览器，获取并存储cookie
def test_save_cookies():
    opts = webdriver.ChromeOptions()
    # 注意这里的端口要之前Windows命令行输入的端口号保持一致
    opts.debugger_address = 'localhost:9222'
    driver = webdriver.Chrome(options=opts)
    save_data(driver.get_cookies())

@allure.feature("测试企业微信")
class Test_Add_Members():

    def setup(self):
        with allure.step("打开浏览器并输入使用cookie登录企业微信"):
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            # 最大化浏览器，不然会有元素定位不到
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

            cookies = get_data()
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown(self):
        with allure.step("关闭浏览器"):
            self.driver.quit()

    @allure.story("添加企业微信成员信息")
    @allure.title("添加成员测试用例")
    def test_add_member(self):
        with allure.step("进入通讯录tab页"):
            self.driver.find_element(By.ID,"menu_contacts").click()
            self.driver.refresh()  # 不刷新会找不到 添加成员
            time.sleep(3)

        with allure.step("点击添加成员"):
            self.driver.find_elements(By.XPATH, '//a[@class="qui_btn ww_btn js_add_member"]')[1].click()

        with allure.step("输入姓名、别名、账号信息、手机号"):
            self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("洪大力")
            self.driver.find_element(By.XPATH,'//*[@id="memberAdd_english_name"]').send_keys("大力")
            self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys("21061202")
            self.driver.find_element(By.XPATH,'//input[@class="qui_inputText ww_inputText ww_telInput_mainNumber"]').send_keys("18266663333")


        with allure.step("点击保存"):
            # 拉动滚动条到页面底部
            jsCode = "var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(jsCode)
            self.driver.find_elements(By.XPATH,'//a[@class="qui_btn ww_btn js_btn_save"]')[1].click()

        with allure.step("查找页面上新增后的成员进行断言"):
            ele_name = self.driver.find_elements(By.CSS_SELECTOR,'[title="洪大力"]')
            assert len(ele_name) == 1