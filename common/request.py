import requests
import json
from common import logger
from common.contants import *
import os
# 日志方法
logger = logger.get_logger(__name__,os.path.join(logs_dir, 'request.txt'))

class Request:
    '''请求类'''


    def __init__(self):
        #每次调用函数都会实例化一个会话
        self.session=requests.sessions.session()

    #请求方法
    def request(self,method,url,data=None,cookies=None):#请求方式，请求参数

        method = method.upper()#将字符串转为全部大写
        try:
        # 参数不为空且为字符串类型
            if data is not None and type(data) ==str:
                #字符串转为字典

                data=json.loads(data)
            logger.debug("请求url：{0}".format(url))
            logger.debug("请求method：{0}".format(method))
            logger.debug("请求data：{0}".format(data))
            if  method == 'GET':#get请求方法
                res=self.session.request(method=method,url=url,params=data,cookies=cookies)
            elif method == 'POST':#post请求方法
                res=self.session.request(method=method,url=url,data=data,cookies=cookies)
            else:
                res=None
                logger.error('No -support method')
            logger.debug('请求response：{0}'.format(res.text))
            return res#返回响应结果
        except Exception as e:
            logger.error('请求出错：{0}'.format(e))

if __name__ == '__main__':
    res=Request()
    res=res.request('post','http://test.lemonban.com/futureloan/mvc/api/member/register',
              {"mobilephone":"18999999202","pwd":"123456"})
    print(res.text)
    # from common.do_excel import Do_Excel
    # from common.contants import *
    # cases = Do_Excel(cases_file).read('register')
    # res=Request().request(cases[0].method,cases[0].url,cases[0].param)
    # print(res.text)


