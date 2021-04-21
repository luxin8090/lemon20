# @Time    : 2021/4/16 0016 16:21
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人

'''
课后练习1
str1 =(11,22,33,'xiamo','夏末''你好',55,66)
print(str1)
list1 =list(str1)
print(list1)
'''
'''
课后练习2
完成任意整数序列的相加 
生成一个整数序列，里面全是数字。求里面所有数字的和
sum1 = 0
for i in range(10):
    sum1 += i
print('相加后总和为:{}'.format(sum1))
'''

'''
课后练习3
3、定义函数：判断一个对象(列表，字典，字符串)的长度是否大于5，
如果大于5 输入true；否则输出false。 --if判断嵌套

'''
# list1 = [11,22,33,'xiamo','hello','夏末','aaa','bbb']
# # print(len(list1))
# count = 0
# for i in list1:
#     count += 1
#     print(count)
#     if count > 5:
#         print("true")
#     else:
#         print("false")


# 需求：判断一下你的工作是否是一个好工作呢？---薪资？
# salary基本薪资+奖金+福利补贴
def good_job(salary,bonus,*args,subsidy=500,**kwargs):
    sum_job = salary + bonus + subsidy
    print('参数salary：{}'.format(salary))
    print('参数bonus：{}'.format(bonus))
    print('参数subsidy：{}'.format(subsidy))
    print('参数*args：{}'.format(args))
    print('参数*kwargs：{}'.format(kwargs))
    for i in args:
        sum_job += i
    # for j in kwargs:   # 方式一：
    #     sum_job += kwargs[j]
    for j in kwargs.values(): # 方式二：
        sum_job += j
    print('工资总和sum_job:{}'.format(sum_job))
    return sum_job
# 调用函数，传参-传入变量的值 --实参
result = good_job(10000,1000,500,200,100,aa=100,bb=200,cc=300)
print(result)
if result > 10000:
    print('这是一个好工作！')
else:
    print('这不是一个好工作')


