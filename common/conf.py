from configparser import ConfigParser
from common.contants import *


class Conf:
    '''配置类'''

    # 初始化函数
    def __init__(self):
        self.conf = ConfigParser()  # 创建对象，配置文件类
        self.conf.read(conf_file, encoding='utf-8')  # 相当于open()方法 打开文件
        # 获取配置文件开关 值
        conf_value = self.conf.getboolean('switch', 'open')

        if conf_value == True:
            # 判断配置文件开关值为 True,使用test环境配置文件
            self.conf.read(conf_url_test_file, encoding='utf-8')
        else:
            # 判断配置文件开关值不为 True,使用pro环境配置文件
            self.conf.read(conf_url_pro_file, encoding='utf-8')

    # 取str类型
    def get_str(self, section, optian):
        return self.conf.get(section, optian)

    # 取int类型
    def get_int(self, section, optian):
        return self.conf.getint(section, optian)

    # 取float类型
    def get_float(self, section, optian):
        return self.conf.getfloat(section, optian)

    # 取boolean类型
    def get_boolean(self, section, optian):
        return self.conf.getboolean(section, optian)

    #  读取出来的值都是字符串，使用eval（）对值去进行处理 ，获取字符串中数据原始类型
    def get_all(self, section, optian):
        value = eval(self.conf.get(section, optian))
        return value


if __name__ == '__main__':
    conf = Conf()
    conf_value = conf.get_str('re', 'mobilephone')
    print(type(conf_value), conf_value)