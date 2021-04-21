# @Time    : 2021/4/20 0020 14:07
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人

# 导入selenium 第三方库
from selenium import webdriver
import time
# 启动谷歌浏览器，打开一个网址
driver = webdriver.Chrome()
driver.get('http://erp.lemfix.com/login.html')
driver.implicitly_wait(10)    # 隐形等待，默认等待10s
# 最大化浏览器
# driver.maximize_window()
# # 前进、后退和刷新操作
# time.sleep(2)
# driver.back()   # 返回到上一个页面
# # time.sleep(2)
# driver.forward() # 前进到下一个页面
# # time.sleep(2)
# driver.refresh() # 刷新页面
# 关闭浏览器：
# driver.quit() # 关闭相关联页面
# driver.close() # 关闭当前窗口
# 获取页面元素：并输入正确的用户名和密码，点击登录
driver.find_element_by_id('username').send_keys('13916686542')
driver.find_element_by_id('password').send_keys('lemon123')
driver.find_element_by_id('btnSubmit').click()
# 判断页面登录用户信息是否正常
login_user = driver.find_element_by_xpath('//p').text
# print(login_user)
if login_user == '13916686542':
    print('这个登录用户名是：{}'.format(login_user))
else:
    print('这个登录用户名不正确！')
# 层级定位
# login_user = driver.find_element_by_xpath("//div[@class='pull-left info']/p").text
# login_user = driver.find_element_by_xpath("//div[@class='user-panel']//p").text
# print(login_user)
# if login_user == '13916686542':
#     print('这个登录用户名是：{}'.format(login_user))
# else:
#     print('这个登录用户名不正确！')
# 文本定位
driver.find_element_by_xpath('//span[text()="零售出库"]').click()

# 通过id切换iframe
# driver.switch_to.frame("tabpanel-926970227f-frame")
# 通过xpath切换iframe
driver.switch_to.frame(driver.find_element_by_xpath
                       ('//iframe[@src="/pages/materials/retail_out_list.html"]'))
# 单据编号框，输入806
driver.find_element_by_id('searchNumber').send_keys('806')

# 点击查询按钮进行查询806相关数据
driver.find_element_by_id('searchBtn').click()
time.sleep(2)
# 判断查询出的结果是否与测试用例中的预期结果是否一致
# 前提要先提取数据
# num = driver.find_element_by_xpath('//div[@class="datagrid-cell datagrid-cell-c1-number"]').text
# num = driver.find_element_by_xpath('//td[@field="number"]/div').text
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text

# print(num)
if "806" in num:
    print('查询结果正确！')
else:
    print('查询结果不正确！，用例不通过')