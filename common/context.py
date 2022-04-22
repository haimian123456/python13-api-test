import re
from common.conf import Conf
from configparser import *
class Context:
    '''正则表达式 获取类'''

    # 正则表达式 匹配获取方法
    def replace(slef,data):
        #正则表达式
        # . 可以匹配任意单个字符，汉字、字母、符号、数字（注意是单个，就是一个）
        # * 匹配0次或多次
        # ? 最多匹配一次
        # () 表示一个组，通俗的理解就是可以用它来标记一个表达式组的开始和结束
        p='\#\{(.*?)\}'
        # 正则表达式匹配结果不为None时进入循环，反之不进入循环
        while re.search(p,data):
            # 正则表达式对字符串的任意位置进行匹配
            r=re.search(p, data)
            #只返回指定组的内容
            r=r.group(1)
            # rs=re.findall(p,data)
            try:
                # 调用配置配下的取值方法，获取配置中的对应 value值
                v=Conf().get_str('data',r)
            except NoOptionError as e:
                if hasattr(Context,r):
                    v=getattr(Context,r)
                else:
                    print('找不到参数化的值')
                    raise e

            # 查找正则表达式匹配结果，并使用替换内容对目标内容进行替换，count=1 替换一次
            data=re.sub(p,v,data,count=1)
        # 返回替换后的结果
        return data

if __name__ == '__main__':
    data = '{"mobile":"${heihei}","pwd:"${pwd}"}'
    test=Context().replace(data)
    print(test,type(test))