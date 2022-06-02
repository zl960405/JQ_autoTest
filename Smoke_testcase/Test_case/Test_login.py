# coding=utf-8
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from Smoke_testcase.Common.BasePage import BasePage
from ddt import ddt,file_data
from Smoke_testcase.Log.logs import Logger

mylog = Logger("Case").getlog()


@ddt()
class Case(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.jq = BasePage()

    def tearDown(self) -> None:
        self.jq.quit()

    @file_data('../data/login_element.yaml')
    def test_login(self, **kwargs):
        self.jq.open(kwargs["url"])
        mylog.info('打开网页')
        self.jq.click(By.XPATH,kwargs['click'])
        mylog.info('点击登录/注册按钮')
        sleep(1.5)
        self.jq.click(By.XPATH,kwargs['locator'])
        mylog.info('点击密码登录按钮')
        sleep(1.5)
        self.jq.send_text(By.XPATH,)
        mylog.info('输入账户')


if __name__ == "__main__":
    unittest.main()

