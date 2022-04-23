import unittest
from unittest import TestCase
from ddt import ddt,data
from common.do_excel import Do_Excel
from common.contants import *
from common.request import Request
from common.conf import Conf
from common.mysql import MySql
from common.context import Context
@ddt
class Login_Test(TestCase):
    '''登录测试类'''

    # 实例化excel读取类 打开测试数据excel
    do_excel=Do_Excel(cases_file)
    #定位sheet表单 获取测试数据
    cases= do_excel.read('login')
    #实例化 配置类
    conf=Conf()
    # 调用获取配置类文件中value值方法 获取request请求的前半段url
    conf_vlaue_url=conf.get_str('request','url')
    #实例化数据库类
    mysql=MySql()
    #实例化 正则表达式取值类
    context=Context()

    #初始化测试环境 整个类只执行一次
    @classmethod
    def setUpClass(cls):
        #实例化请求类
        cls.request=Request()

    # 清理测试环境 整个类只执行一次
    @classmethod
    def tearDownClass(cls):
        #关闭请求类 下的session会话
        cls.request.session.close()
        #调用数据库类下的 关闭数据库 方法
        cls.mysql.mysql_close()

    #测试登录方法
    @data(*cases)#测试数据
    def test_login(self,case):#接收测试数据
        #拼接登录接口url
        case_url=os.path.join(self.conf_vlaue_url,case.url)
        # 判断参数中sql是不为空
        if case.sql is not None:
            #调用数据库 类下的查询sql语句 方法 获取数据库中最大手机号+1 得到一个未注册的手机号
            register = self.mysql.mysql_select_one(case.sql)[0][0]
            # 获取 正则表达式 获取类下属性值
            setattr(Context,'register',str(register))
        # 调用正则表达式 获取类下的 正则表达式 匹配获取方法,使用配置中的参数 替换 测试数据中的的参数化值
        case_param = self.context.replace(case.param)
        #调用登录请求
        test_case=self.request.request(case.method,case_url,case_param)
        #断言
        try:
            print('开始执行第{0}条用例:{1}'.format(case.id,case.description))
            #判断期望结果与实际结果是否一致
            self.assertEqual(case.expectedresult,test_case.text)

            print('module:',case.module)
            print('url:', case_url)
            print('param:',case_param)
            #判断期望结果与实际结果一致时，测试通过
            result='pass'
            print('登录成功')
        #判断期望结果与实际结果不一致
        except AssertionError as e:
            # 测试不通过
            print('failed')
            result='failed'
            print('登录失败')
            #抛出 报错
            raise e
        # 不管期望结果与实际结果是否一致都执行此步骤
        finally:
            #调用读取excel类下的写入方法，写回 实际结果和测试结果
            self.do_excel.write(case.id+1,test_case.text,result)
            print('第{0}条用例执行结束'.format(case.id))

if __name__ == '__main__':
    unittest.main()

