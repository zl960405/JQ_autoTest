import datetime
import os.path
import time
from selenium import webdriver
from Smoke_testcase.Log.logs import Logger


mylogger = Logger("BasePage").getlog()



class BasePage:

    def __init__(self):
        # 目的在于对类进行实例化时的实例化浏览器对象
        self.driver = self.open_browser()
        self.driver.implicitly_wait(15)

    def open_browser(self):
        """
        通过txt（浏览器类型）启动浏览器
        :param txt:浏览器名称
        :return:
        """
        try:
            # python的放射机制
            txt = None
            driver = getattr(webdriver, txt)()
        except Exception as e:
            print(e)
            driver = webdriver.Chrome()
        return driver

    # def take_screenshot(self):
    #     """截图并保存在根目录的Screenshots文件夹下"""
    #     file_path = os.path.dirname(os.path) + "/Screenshot/"
    #     rq = time.strftime('%y-%m-%d-%H%M',time.localtime(time.time()))
    #     screen_name = file_path + rq + '.png'
    #     self.driver.get_screenshot_as_file(screen_name)
    #
    # def wait_element_visible(self, locator, times=30, poll_frequency=0.5):
    #     """
    #     :param locator: 定位元素
    #     :param times: 等待时间30s
    #     :param poll_frequency: 等待周期
    #     :param doc: 模块名_页面名称_操作名称
    #     :return: NOne
    #     """
    #     mylogger.info(f"等待元素{locator}可见")
    #     try:
    #         # 开始等待时间
    #         time_start = datetime.datetime.now()
    #
    #         WebDriverWait(self.driver, times, poll_frequency).until(
    #             expected_conditions.visibility_of_element_located(locator))
    #         # 结束等待时间
    #         time_end = datetime.datetime.now()
    #         #
    #         time_wait = (time_end - time_start).seconds
    #         mylogger.info(f"元素{locator}可见，等待结束。等待的开始时间：{time_start}，等待的结束时间{time_end}，等待时长为：{time_wait}")
    #     except:
    #         # 捕捉异常
    #         mylogger.exception("等待可见元素失败")
    #         # 截图 元素失败截图
    #         # self.save_screenshot(doc)
    #         raise

    def open(self,url):
        """访问url"""
        # url = "http://pc.tyltxt.com/#/home"  # 访问域名
        self.driver.get(url)

    def get_element(self, locator, value):
        """ 定位方法"""
        return self.driver.find_element(locator, value)
        # return self.driver.find_element(*loc)

    def click(self, locator, value):
        """
        点击操作
        :return
        """
        ele = self.get_element(locator, value)
        ele.click()

    def send_text(self,locator, value, txt):
        """
        操作事件，输入内容
        :param locator: 定位方法
        :param value: 元素
        :param text: 输入文本
        :return:
        """
        ele = self.get_element(locator, value)
        ele.send_keys(txt)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    bg = BasePage()
    bg.open("http://pc.tyltxt.com/#/home")