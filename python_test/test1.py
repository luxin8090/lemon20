# @Time    : 2021/4/14 0014 22:22
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人
'''
1、python中主要数据类型
数字类型：整型：int、浮点型：float、布尔型：bool
字符串 str
字典 dict
列表 list
元组 tuple
集合 set
2、判断数据类型 type()--输出数据的数据类型
num = 10
flo = 99.9999
bo = True
print(type(num))
print(type(flo))
print(type(bo))
3、字符串：用成对的引号括起来的内容 单引号、双引号、三引号
'''
# S1 = 'hello word1'
# S2 = "hello word2"
# S3 = '''hello Word3
#             hello Word3
#                 hello Word3
# '''
# print(S1)
# print(S2)
# print(S3)
'''
4、字符串操作--序列型数据
每一个元素对应一个位置 --索引/下标：从0开始
字符串数值--切片：字符串名【索引头：索引尾：步长】
1.取头不取尾 2.步长默认为1，索引头默认0，索引尾默认最后+1
3.len()：计算长度
5、字符串常用方法
替换replace()
查找元素的位置，获得开始的位置 find() index()
S1 = '自来水来自上海自来水来自海上'
# print(s1[2:5])
# print(s1[:])
# print(s1[::2])
# print(len(s1))

# S2 = S1.replace('上海','北京')
# print(S2)

print(S1.find('上海1'))
5、格式化输出 format --- 占位符{} .format
6、python的常见运算符
1)算数运算符：+ - * / %

'''
name = '夏末'
sex = '男'
age = 18
hobby = '小说、电影'

# print(''' ----{}同学的基本信息
#             name: {}
#             sex: {}
#             age: {}
#             hobby: {}
# '''.format(name,name,sex,age,hobby))
# a = 20
# b = 10
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# s1 = '夏末'
# s2 = '你好'
# print(s1+s2)
# s3 = ''.join((s1,s2))
# print(s3)
# print('夏末你好'*10)
# c = 10
# c += 10
# # c -= 5
# print(c)
# amount = 1000
# print(amount < 10000)
# print(amount > 10000)
# print(amount >= 10000)
# print(amount <= 10000)
# print(amount == 10000)
# print(amount != 10000)
# a1 = 100
# b1 = 200
# print(a1 < 100 or b1 <= 200)
# print(a1 < 100 and b1 <= 200)
# print(not a1 < 100)
#
# str1 = 'hello 夏末'
# print('a' in str1)
'''
课后练习1
'''
# name = 'musne'
# age = 18
# sex = 'nan'
# print('''
#         请输入姓名:{}
#         请输入年龄:{}
#         请输入性别:{}
# '''.format(name,age,sex))
'''
课后练习2
2、现在有字符串:str1 = 'python hello aaa 123123aabb'
1)请取出并打印字符串中的'python'
# # print(len(str1))
# # print(str1[0:6:1])
2）请分别判断'o a' 'he' 'ab' 是否是该字符串的成员
print('o a' in str1)
print('he' in str1)
print('ab' in str1)
3）替换python为“lemon”
# print(str1.replace('python','“lemon”'))
str2 = str1.replace('python','“lemon”')
print(str2)
4）找到aaa的起始位置
# print(str1.index('aaa'))
'''

