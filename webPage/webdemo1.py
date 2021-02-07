from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
# 打开chrome 进入百度
driver.get('http://www.baidu.com')
sleep(3)
# 查询软件测试
driver.find_element_by_id('kw').send_keys('python菜鸟教程')
sleep(3)
# 点击百度一下按钮
driver.find_element_by_id('su').click()
sleep(3)
# 点击python菜鸟教程网址
driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()
sleep(3)
# 关闭浏览器
driver.quit()
