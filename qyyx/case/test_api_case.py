import requests
import unittest
import json
import ddt
from ddt import data,unpack,file_data
import yaml
'''
注册分析页面接口
'''
@ddt.ddt
class register(unittest.TestCase):
    def setUp(self):
        # self.huanjing=input('请输入要测试的环境：')
        #
        # if self.huanjing=='正式':
        #     self.host='http://marketing-data.paas.gwm.cn/phqyyxapi/api/operation_analysis'
        # elif self.huanjing=='测试':
        #     self.host='http://phqyyxapi-test.paas.gwm.cn/api/operation_analysis'
        # else:
        #     print('环境错误，无法获取域名！')
        # self.host='http://phqyyxapi-test.paas.gwm.cn/phqyyxapi/api/operation_analysis'
        # self.host = 'http://marketing-data.paas.gwm.cn/phqyyxapi/api/operation_analysis'
        self.host='http://marketing-data-test.paas.gwm.cn/phqyyxapi/api/operation_analysis'

#注册量/率
    @unittest.skip
    def test_001case(self):
        print('注册量/率')
        url='/register_analysis_total'
        r=requests.get(url=self.host+url)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s' % format(r.json()['message']))

#增长量/率
    @unittest.skip
    @data(['2021-01-16','2021-01-23'])
    @unpack
    def test_002case(self,start_time,end_time):
        print('增长量/率')
        url='http://marketing-data-test.paas.gwm.cn/phqyyxapi/api/operation_analysistotal_register?start_time='+start_time+'&end_time='+end_time
        # url='/operation_analysistotal_register?start_time='+start_time+'&end_time='+end_time
        # url='/operation_analysistotal_register?start_time=2020-12-23&end_time=2021-01-22'
        r=requests.get(url=url)
        print('=========================')
        print(url)
        print('=========================')
        if r.status_code==200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s'%format(Exception))

#媒体统计
    @unittest.skip
    def test_003case(self):
        print('媒体统计')
        url='/media_info'
        r=requests.get(url=self.host+url)
        if r.status_code==200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s'%format(Exception))

# 综合榜
    @unittest.skip
    def test_004case(self):
        print('综合榜')
        url='/total_top'
        r = requests.get(url=self.host + url)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s' % format(Exception))

# 增长榜
    @unittest.skip
    @data(['2021-01-15', '2021-01-22'])
    @unpack
    def test_005case(self,start_time,end_time):
        print('增长榜')
        url='/increase_top?start_time='+start_time+'&end_time='+end_time
        r = requests.get(url=self.host + url)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s' % format(Exception))

#综合趋势图
    @unittest.skip
    @data(['2021-01-15', '2020-01-22'])
    @unpack
    def test_006case(self,start_time,end_time):
        print('综合趋势图')
        url='/register_analysis_total_by_data?start_time='+start_time+'&end_time='+end_time
        r = requests.get(url=self.host + url)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s' % format(Exception))

if __name__ == '__main__':
    unittest.main(verbosity=2)
