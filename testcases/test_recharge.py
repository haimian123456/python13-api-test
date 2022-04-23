import unittest
from unittest import TestCase
from common.do_excel import Do_Excel
from common.contants import *
from common.request import Request
from ddt import ddt, data
from common.conf import Conf
from common.mysql import MySql
from common.context import Context
import json


@ddt
class Recharge_Test(TestCase):
    '''注册测试类'''

    # 实例化 excel读写类
    do_excel = Do_Excel(cases_file)
    # 调用 excel读写类下的excel读取方法
    cases = do_excel.read('recharge')
    # 实例化 配置类
    conf = Conf()
    # 调用配置类下的 取str类型方法 获取 接口前半段通用url
    conf_value_url = conf.get_str('request', 'url')
    # 调用配置类下的 取str类型方法 获取mysql下的 sql
    leaveamount_sql = conf.get_str('mysql', 'recharge_leaveamount_sql')
    # 实例化 数据库 类
    mysql = MySql()
    # 实例化 正则表达式取值类
    context = Context()

    # 初始化测试环境 执行每一条用例的时候都会执行 对象方法
    def setup(self):
        pass

    # 清理测试环境 执行每一条用例的时候都会执行 对象方法
    def teardown(self):
        pass

    # 初始化测试环境 整个类中只运行一次 类方法
    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 实例化请求类

    # 清理测试环境  整个类中只运行一次 类方法
    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭请求类下的session会话
        cls.mysql.mysql_close()  # 关闭数据库连接

    @data(*cases)  # 测试数据
    def test_recharge(self, case):  # 测试 注册类 方法
        # 拼接  注册接口
        case_url = os.path.join(self.conf_value_url, case.url)
        case_param=json.loads(case.param)
        # 判断参数中sql是不为空
        if case.sql is not None and '未注册手机号' in case.description :
            # 调用数据库 类下的查询sql语句 方法 获取数据库中最大手机号+1 得到一个未注册的手机号
            register=self.mysql.mysql_select_one(case.sql)[0][0]
            # 获取 正则表达式 获取类下属性值
            setattr(Context,'register',str(register))
        #判断用例是否 未正常充值
        elif '正常充值' in case.description :
            # 调用数据库 类下的查询sql语句 方法 获取充值前的账户金额
            leaveamount = self.mysql.mysql_select_one(self.leaveamount_sql)[0][0]
            #充值成功后的账户金额=将充值前的账户金额+即将成功充值的金额
            case_leaveamount = float(leaveamount) + float(case_param['amount'])
            # 获取 正则表达式 获取类下属性值
            setattr(Context, 'case_leaveamount', str(case_leaveamount))
        # 调用正则表达式 获取类下的 正则表达式 匹配获取方法,使用配置中的参数 替换 测试数据中的的参数化值
        case_param=self.context.replace(case.param)

        # 将测试期望结果 由字符串类型转为字典类型
        case_expectedresult = json.loads(case.expectedresult)

        # 判断测试用例==登录已过期 重新请求
        if case.description == '登录已过期':
            test_case = self.request.request(case.method, case_url, case_param)
        else:
            # 调用 注册接口 请求方法
            test_case = self.request.request(case.method, case_url, case_param)
        try:
            print('开始执行第{0}个测试用例：{1}'.format(case.id, case.description))
            print('module:', case.module)
            print('url:', case_url)
            print('param:', case_param)

            # 判断期望结果中的 msg =='充值成功'
            if case_expectedresult['msg'] == '充值成功':
                # 将测试实际结果 由字符串类型转为字典类型
                test_case_text = json.loads(test_case.text)
                # 判断期望status 与实际status 是否一致
                self.assertEqual(case_expectedresult['status'], test_case_text['status'])
                # 判断期望code 与实际code 是否一致
                self.assertEqual(case_expectedresult['code'], test_case_text['code'])
                # 判断期望msg 与实际msg 是否一致
                self.assertEqual(case_expectedresult['msg'], test_case_text['msg'])
                # 判断期望mobilephone 与实际mobilephone 是否一致
                self.assertEqual(self.conf.get_str('data','user'), test_case_text['data']['mobilephone'])
                # 判断期望 充值后金额 与 实际充值后金额 是否一致
                self.assertEqual(case_leaveamount, float(test_case_text['data']['leaveamount']))
            else:
                # 断言 判断期望结果和请求实际结果是否一致
                self.assertEqual(case.expectedresult, test_case.text)

            # 期望结果和请求实际结果一致
            result = 'pass'
            print('充值用例测试成功')
        except AssertionError as e:
            # 期望结果和请求实际结果不一致
            result = 'failed'
            print('充值用例测试失败')
            raise e  # 返回报错信息
        finally:
            # 不管期望结果和请求实际结果是否一致 都写入 实际结果和 测试结果
            self.do_excel.write(case.id + 1, test_case.text, result)
            print('第{0}个测试用例执行结束'.format(case.id))


if __name__ == '__main__':
    unittest.main()
    #
    # 1，设计配置文件，完成配置文件类的封装，将接口请求URL和数据库信息放到配置文件中进行管理。
    # 2，思考如何实现投资接口？
    #
    # 1》如何实现投资人测试数据的参数化？（类比注册手机号码的实现？）
    #
    # 2》参数化后的投资人，管理员，借款人这些基础数据放到哪里管理？
    #
    # 3》如何在自动化用例中特换这些参数化数据？
    #
    # 4》如何实现投资接口中对于标的ID的依赖？ （温馨提示可以使用global全局变量）
