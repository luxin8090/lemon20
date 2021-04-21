# @Time    : 2021/4/19 0019 23:58
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人
from python_test.test6 import read_data,api_fun,wirte_result
def execute_fun(filename,sheetname):
    cases = read_data(filename,sheetname)
    # print(cases)
    for case in cases:     # 依次去访问cases中的元素，保存到定义的变量case中
        # print(case)
        case_id = case['case_id']
        url = case['url']  # 字典通过key取值
        data = eval(case['data'])
        # print(case_id,url,data)
        # print(type(data))
        # print('*'*50)
        # 获取期望结果code、msg
        expect = eval(case['expect'])
        expect_code = expect['code']
        expect_msg = expect['msg']
        print('预期结果code为：{},msg为：{}'.format(expect_code,expect_msg))

        # 执行读取接口测试
        real_result = api_fun(url=url,data=data)
        # print(real_result)

        # # 获取实际结果code、msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print('实际结果code为：{},msg为：{}'.format(real_code,real_msg))
        print('*' * 50)
        # 断言：预期vs实际结果
        if real_code == expect_code and real_msg == expect_msg:
            print('第{}条测试用例执行通过！'.format(case_id))
            final_re = 'Passed'
        else:
            print('第{}条测试用例执行不通过！'.format(case_id))
            final_re = 'Failed'
        print('*'*50)
        # 执行写入接口测试
        wirte_result(filename,sheetname,case_id+1,8,final_re)
#调用接口执行函数
# execute_fun('D:\\yeshen\\Pycharm-Workspace\\xiamotest\\test_data\\test_case_api.xlsx','register') # 调用注册
execute_fun('D:\\Dqcb-git\\lemon20\\test_data\\test_case_api.xlsx','register')      # 调用注册