import unittest
from qyyx.Logs.demolog import *
from qyyx.HTMLTestReportCN import HTMLTestRunner
from qyyx.Sendemail.send_email import send_email

logging.info('测试开始')
suite=unittest.defaultTestLoader.discover('./case')
# suite=unittest.TestSuite()
# suite.addTest(test_demo1('test_query'))
f = open("./report/report11.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="XXXXX项目接口测试报告",description="全员自动化1期api测试",tester='贾鹏').run(suite)
f.close()
send_email('./report/report.html')
logging.info('测试结束')
