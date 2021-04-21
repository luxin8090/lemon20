# @Time    : 2021/4/20 0020 21:08
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人

from selenium import webdriver
import time
driver = webdriver.Chrome()   # 初始化
driver.implicitly_wait(10)    # 隐形等待，默认等待10s
# 打开网页
def open_url(url,driver):
    driver.get(url)  # 打开网页
    driver.maximize_window() # 网页最大化
# 登录封装成函数
def login(username,password,driver):
    driver.find_element_by_id('username').send_keys(username)   # 输入用户名
    driver.find_element_by_id('password').send_keys(password)   # 输入密码
    driver.find_element_by_id('btnSubmit').click()              # 点击按钮登录
# 查询零售出库
def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login(username,password,driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    # 通过xpath切换iframe
    driver.switch_to.frame(driver.find_element_by_xpath
                           ('//iframe[@src="/pages/materials/retail_out_list.html"]'))
    # 单据编号框，输入806
    driver.find_element_by_id('searchNumber').send_keys(s_key)
    # 点击查询按钮进行查询806相关数据
    driver.find_element_by_id('searchBtn').click()
    time.sleep(2)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    # print(num)
    return num

