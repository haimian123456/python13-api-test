import pymysql
from common.conf import Conf


class MySql:
    '''数据库类'''

    # 实例化配置类
    conf = Conf()
    # 获取配置类中mysql下的 host
    host = conf.get_str('mysql', 'host')
    # 获取配置类中mysql下的 user
    user = conf.get_str('mysql', 'user')
    # 获取配置类中mysql下的 password
    password = conf.get_str('mysql', 'password')

    def __init__(self):
        # 建立连接
        self.mysql = pymysql.connect(host=self.host, user=self.user, password=self.password)
        # 建立查询页面
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    # 查询sql语句 返回一条符合条件结果 的方法
    def mysql_select_one(self, sql):
        # 执行 sql 语句
        self.cursor.execute(sql)
        # 查看结果
        result = self.cursor.fetchmany()
        return result

        # 查询sql语句 返回所有符合条件结果 的方法

    def mysql_select_all(self, sql):
        # 执行 sql 语句
        self.cursor.execute(sql)
        # 查看结果
        result = self.cursor.fetchall()
        return result




    # 关闭查询页面和数据库连接 的方法
    def mysql_close(self):
        # 关闭查询页面
        self.cursor.close()
        # 关闭数据库连接
        self.mysql.close()


if __name__ == '__main__':
    # host = '47.107.168.87'
    # user = 'futurevistor'
    # password = "123456"
    # # sql语句
    # sql = 'select max(mobilephone) from future.member where mobilephone like "132%%" '
    from common.conf import Conf
    from common.contants import *

    # 实例化 配置类
    conf = Conf()
    # 调用配置类下的 取str类型方法 获取 接口前半段通用url
    # sql = conf.get_str('mysql', 'register_sql')
    test1 = MySql().mysql_select_one("select max(cast(mobilephone as int)) as mobilephone  from future.member ")
    test2 = MySql().mysql_select_one("select id from future.member where mobilephone like '18217245684' ")
    test3 = MySql().mysql_select_one("select max(cast(mobilephone as int))+1  as mobilephone from future.member ")

    print(type(test1),test1)
    print(type(test2),test2)
    print(type(test3), test3)
