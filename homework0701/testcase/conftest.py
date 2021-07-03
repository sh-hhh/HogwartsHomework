import pytest
from appium import webdriver


@pytest.fixture(scope="class")
def driver_wework():
    desired_cap = {}
    desired_cap['platformName'] = 'android'  # 被测平台
    # desired_cap['platformVersion'] = '6.0'
    desired_cap['deviceName'] = 'DLS4C20525007740'  # 被测设备
    desired_cap['appPackage'] = 'com.tencent.wework'  # 被测应用的包名
    desired_cap['appActivity'] = '.launch.LaunchSplashActivity'  # 被测应用的初始页面
    desired_cap['noReset'] = 'true'  # 每次运行不会清空缓存
    desired_cap['skipDeviceInitialization'] = 'true'  # 跳过初始化步骤
    # dontStopAppOnReset=true不会重启app,app打开哪一页就从哪一页开始执行,适合调试时使用
    # desired_cap['dontStopAppOnReset'] = 'true'
    # desired_cap['automatorName'] = 'UiAutomator2'
    desired_cap['settings[waitForIdleTimeout]'] = 0  # 设备空闲时间，默认10秒，动态页面才需要加

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
