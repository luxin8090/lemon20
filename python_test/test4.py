# @Time    : 2021/4/17 0017 00:44
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人

import requests # 导入第三方库
import jsonpath # 导入第三方库
# 注册接口
# url_reg = 'http://8.129.91.152:8766/futureloan/member/register' # 请求地址
# data_reg = {"mobile_phone": "18633332221", "pwd": "lemon666","type":"1","reg_name":"xiam"}# 请求正文
# headers_reg = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} # 请求头
# res_reg = requests.post(url=url_reg,json=data_reg,headers=headers_reg).json()  # 调用post方法，返回值
# print(res_reg.headers)       # 获取响应头
# print(res_reg.status_code) # 获取响应码
# print(res_reg.text)        # 获取文本信息，自动解码
# print(res_reg.json())      # 获取响应正文为json格式
# print(res_reg.content)     # 获取二进制内容，需要手动解码

# 登录接口
# url_login='http://8.129.91.152:8766/futureloan/member/login'
# data_login={ "mobile_phone": "18633332221","pwd": "lemon666"}
# headers_login = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'}
# res_login = requests.post(url=url_login,json=data_login,headers=headers_login).json()
# print(res_login)

# 充值接口
# 从登录获取token和member_id
# token = res_login['data']['token_info']['token']
# member_id = res_login['data']['id']
# # print(token)
# # print(member_id)
# url_rec = 'http://8.129.91.152:8766/futureloan/member/recharge'
# data_rec = {"member_id": member_id,"amount": "10000"}
# headers_rec={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json',
# 'Authorization':'Bearer'+' '+ token}
# res_rec = requests.post(url=url_rec,json=data_rec,headers=headers_rec).json()
# print(res_rec)

# token = jsonpath.jsonpath(res_login,'$..token')[0] # [0]为list列表数据取值
# member_id = jsonpath.jsonpath(res_login,'$..id')[0]
# print(token,member_id)
# url_rec = 'http://8.129.91.152:8766/futureloan/member/recharge'
# data_rec = {"member_id": member_id,"amount": "10000"}
# headers_rec={'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json',
# 'Authorization':'Bearer'+' '+ token}
# res_rec = requests.post(url=url_rec,json=data_rec,headers=headers_rec).json()
# print(res_rec)

# 封装函数
# def api_fun(url,data):  # 定义函数
#     # url_login = 'http://8.129.91.152:8766/futureloan/member/login'  # 请求地址
#     # data_login = {"mobile_phone": "18633332221", "pwd": "lemon666"} # 请求正文
#     headers = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json'} # 请求头
#     result = requests.post(url=url, json=data, headers=headers).json()
#     return result

#调用api_fun()  注册
# url_reg ='http://8.129.91.152:8766/futureloan/member/register'
# data_reg ={"mobile_phone": "18633332223", "pwd": "lemon666","type":"1","reg_name":"xiaomo"}
# res_reg = api_fun(url=url_reg,data=data_reg)
# print(res_reg)
#调用api_fun()  登录
# url_login ='http://8.129.91.152:8766/futureloan/member/login'
# # data_login ={"mobile_phone": "18633332223", "pwd": "lemon666"}
# # res_login = api_fun(url=url_login,data=data_login)
# # print(res_login)
# 调用api_fun()  充值

# 补充面试题：访问baidu接口请求 通过火狐浏览器的值访问baidu用的是get请求
# headers_baidu = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
# url_baidu = 'https://www.baidu.com/'
# res = requests.get(url=url_baidu,headers=headers_baidu)
# # print(res.text)
# print(res.content.decode('utf8'))

