import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_cookie(cookie_data):
    with open("data.yml","w") as f:
        yaml.dump(cookie_data,f)

# 通过复用浏览器，获取并存储cookie
def test_save_cookies():
    opts = webdriver.ChromeOptions()
    # 注意这里的端口要之前Windows命令行输入的端口号保持一致
    opts.debugger_address = 'localhost:9222'
    driver = webdriver.Chrome(options=opts)
    get_cookie(driver.get_cookies())


class Test_Add_Members():
    # 用cookie登录，添加成员
    def test_add_member(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        # 最大化浏览器，不然会有元素定位不到
        driver.maximize_window()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

        with open("data.yml", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get("https://work.weixin.qq.com/wework_admin/frame")

        driver.find_element(By.ID,"menu_contacts").click()
        driver.find_element(By.XPATH,"//*[@id=\"js_contacts49\"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]").click()
        driver.find_element(By.XPATH,"//*[@id=\"username\"]").send_keys("洪大力")
        driver.find_element(By.XPATH,"//*[@id=\"memberAdd_english_name\"]").send_keys("大力")
        driver.find_element(By.XPATH, "//*[@id=\"memberAdd_acctid\"]").send_keys("21061201")

        target = driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > a.qui_btn ww_btn js_btn_save")
        # 拉动滚动条，直到最下面的保存按钮出现，这样才能定位到这个元素
        driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()