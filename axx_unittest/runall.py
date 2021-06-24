import unittest
from axx_unittest.Logs.demolog import *
from axx_unittest.HTMLTestReportCN import HTMLTestRunner
from axx_unittest.config.send_email import send_email

logging.info('测试开始')
suite=unittest.defaultTestLoader.discover('./case')# 遍历当前目录及子包中所有test_*.py中所有unittest用例
f = open("./report/report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="爱学习接口测试报告",description="ToC商城api测试",tester='贾鹏').run(suite)
f.close()
send_email('./report/report.html')
logging.info('测试结束')
