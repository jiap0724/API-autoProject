from selenium import webdriver
import unittest
from time import sleep
from webPage.HTMLTestReportCN import  HTMLTestRunner


class Demo(unittest.TestCase):

    def setUp(self):
        self.url='http://www.baidu.com'
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get(self.url)

    def test_case1(self):
        self.driver.find_element_by_id('kw').send_keys('python菜鸟教程')
        self.driver.find_element_by_id('su').click()
        sleep(3)


    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    testsuit=unittest.TestSuite()
    testsuit.addTest(Demo('test_case1'))
    # fp=open('report.html','wb')
    # runner = HTMLTestRunnerCN.HTMLTestRunner(
    #     stream=fp,
    #     title='unite test',
    #     description='This demonstrates the report output by HTMLTestRunner.'
    # )
    f = open(".\report.html", 'wb')  # 二进制写格式打开要生成的报告文件
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", runner="卡卡").run(testsuit)
    f.close()
    # runner.run(testsuit)