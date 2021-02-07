import yaml
import os

'''
获取yaml文件
'''
class GetYaml():
    def __init__(self, file_path):
        # 判断文件是否存在
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            print('没有找到%s文件路径' % file_path)

        self.data = self.read_yaml()

    def read_yaml(self):
        with open(self.file_path, 'r', encoding='utf-8')as f:
            p = f.read()
            return p

    def get_data(self, key=None):
        result = yaml.load(self.data, Loader=yaml.FullLoader)
        # 判断key是否存在
        if key == None:
            return result
        else:
            return result.get(key)


if __name__ == '__main__':
    read_yaml = GetYaml(r'C:\Users\GW00216719\PycharmProjects\pythonProject1\qyyx\config\time.yml')
    tasecase = read_yaml.get_data('tasecase')
    print(tasecase)