import json
import unittest
import requests
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

    @unittest.skip
    def test_001case(self):
        print('注册量/率')
        # url='/register_analysis_info?high_level=reg_rate,3,75.7'
        url='/register_analysis_info?start_time=2021-01-16&end_time=2021-01-23'
        r=requests.get(url=self.host+url)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s' % format(r.json()['message']))

    # download
    @unittest.skip
    def test_002case(self):
        url='/register_analysis/download'
        r = requests.get(url=self.host + url)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        else:
            print(r.status_code)
            print('报错信息: %s' % format(r.json()['message']))

if __name__ == '__main__':
    unittest.main(verbosity=2)

