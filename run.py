# @Time    : 2021/4/20 0020 21:45
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人

from selenium import webdriver   # 引入第三方库
from test_data import test_data  # 调用参数
from python_web import test2     # 引入函数

driver = webdriver.Chrome()   # 初始化
driver.implicitly_wait(10)    # 隐形等待，默认等待10s
# 取出传参的实参
url = test_data.url['url']
username = test_data.user_info['username']
password = test_data.user_info['password']
s_key = test_data.s_key['s_key']
print(url,username,password,s_key)
# 调用查询函数，传参
result_num = test2.search_key(url=url,driver=driver,username=username,password=password,s_key=s_key)
if s_key in result_num:
    print('查询结果正确！')
else:
    print("查询结果错误，用例结果不通过！")