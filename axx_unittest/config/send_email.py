# -*- coding:utf-8 -*-
# @Time : 2021/2/5 18:10
# @Author : jiapeng
# @File : send_email.py
from qyyx.Logs.demolog import *
import smtplib  # 用于建立smtp连接
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # 邮件需要专门的MIME格式
#
# # 1. 编写邮件内容（Email邮件需要专门的MIME格式）
# msg = MIMEText('这是一封测试邮件', 'plain', 'utf-8')  # plain指普通文本格式邮件内容
#
# # 2. 组装Email头（发件人，收件人，主题）
# # msg['From'] = '1016281633@qq.com'  # 发件人
# # msg['To'] = '15210068667@139.com'  # 收件人
# msg['From'] = '15210068667@139.com'  # 发件人
# msg['To'] = '1016281633@qq.com'  # 收件人
# msg['Subject'] = 'Api Test Report'  # 邮件主题
#
# # 3. 连接smtp服务器并发送邮件
# smtp = smtplib.SMTP_SSL('smtp.139.com')  # smtp服务器地址 使用SSL模式
# # smtp.login('1016281633@qq.com', 'exlfvcwyhoosbdfh')  # 发件邮箱的用户名和密码  qq邮箱
# smtp.login('15210068667@139.com', 'cd03f8dc91f123073f00') # 发件邮箱的用户名和密码  139邮箱
# # smtp.sendmail("1016281633@qq.com","15210068667@139.com", msg.as_string())
# smtp.sendmail("15210068667@139.com","1016281633@qq.com", msg.as_string())
# smtp.quit()

def send_email(report_file):
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = '15210068667@139.com'  # 发件人
    msg['To'] = '1016281633@qq.com'  # 收件人
    msg['Subject'] = Header('接口测试报告', 'utf-8')  # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL('smtp.139.com')  # smtp服务器地址 使用SSL模式
        smtp.login('15210068667@139.com', 'cd03f8dc91f123073f00')  # 用户名和密码
        smtp.sendmail("15210068667@139.com", "1016281633@qq.com", msg.as_string())
        # smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
