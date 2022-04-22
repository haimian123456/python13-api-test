import os
# os.path.basename(__file__)#当前文件名
# os.path.realpath(__file__)#当前文件路径，包括文件名
# os.path.abspath(__file__)#当前文件路径，不包括文件名
# os.path.dirname(__file__)#当前文件路径，不包括文件名

'''路径常量'''

#当前文件的上上个文件名
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#文件夹路径
# datas文件夹路径
data_dir=os.path.join(base_dir,'datas')
# reports文件夹路径
reports_dir=os.path.join(base_dir,'reports')
# conf文件夹路径
conf_dir=os.path.join(base_dir,'conf')
# logs文件夹路径
logs_dir=os.path.join(base_dir,'logs')
# testcases文件夹路径
testcases_dir=os.path.join(base_dir,'testcases')
# 路径拼接，
# cases 文件路径
cases_file=os.path.join(data_dir,'前程贷接口测试用例20220405.xlsx')
#conf 文件路径
conf_file=os.path.join(conf_dir,'conf.conf')
conf_url_pro_file=os.path.join(conf_dir,'conf_url_pro.conf')
conf_url_test_file=os.path.join(conf_dir,'conf_url_test.conf')
# print(cases_file)
# print(logs_dir)
# print(conf_file)