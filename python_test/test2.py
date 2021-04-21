# @Time    : 2021/4/15 0015 22:04
# @Author  : 夏末
# @FILE    : python_test.py
# @QQ      : 313098754
# @Company ：个人
'''
列表：list【】多个元素逗号隔开
1、列表元素可以任意数据类型
2、序列型数据：有顺序，索引从0开始
1）取值通过下标来取值
2）可以进行切片操作---参考字符串切片来操作
3、列表中的元素可变的:增删改 -- 重点！
4、len()取长度
'''
# list1 = [66,3.1415926,True,'python',[11,22,33,44,55]]
# print(list1)
# print(type(list1))
# print(len(list1))
# 追加操作
# list1.append('xiamo')
# print(list1)
# list1.insert(2,'夏末')
# print(list1)
# 修改操作
# list1[0]=88.88
# print(list1)
# 指定索引值进行删除操作
# list1.pop()
# list1.pop(2)
# print(list1)
# 指定列表中元素值进行删除操作
# list1.remove(66)
# print(list1)
# print(list1)
'''
元组：tuple()
1、元组中元素，可以任意数据类型
2、元祖序列型，有顺序
1）取值通过下标来取值
2）可进行切片操作---参考字符串切片操作
3、元组是不可变的
4、len()
'''
# tu1 = [66,3.1415926,True,'python',[11,22,33,44,55],'夏末']
# print(tu1)
# print(tu1[1])
'''
字典：dict {} 键值对-key：value ==1个元素
1、使用场景：描述一个对象的基本信息，属性-值
2、key：唯一的，不可变的数据，通常使用字符串
3、value：可以任意数据类型
4、字典看一遍的---增删改
5、字典是无序的，没有下标
'''
# 字典定义方式一
# dict1 = {"name":"夏末","age":18,"sex":"男"}
# print(type(dict1))
# print(dict1)
# 字典定义方式二
# dict2 = dict(name='夏末',age=18)
# print(dict2)
# 取值
# print(dict2['name'])
# print(dict2.get('name'))
# print(dict2.keys())
# print(dict2.values())
# print(dict2.items())
# dict2['sex'] = '女'
# print(dict2)
# dict2.pop('sex')
# print(dict2)
'''
集合：set{} {value1,value2,value3}
1、集合中的元素必须不可变，集合本身是可变数据类型
2、无序，集合中的数据是不能重复的
3、集合使用
1）给数据去重
2）用来区分数据是否可变
'''
# set1 = {11,22,33,44,'夏末','xiamo'}
# print(type(set1))
# print(set1)

# list2 = [11,22,33,44,33,22,11,55,66,88]
# set2 = set(list2)
# print(list2)
# print(set2)
# list1 =list(set2)
# print(list1)
'''
python的控制流
1、if elif else 的应用
2、for循环 固定用法：for...in 
3、for 循环加入 break 和 continue 来中断执行

'''
# money = int(input('请输入你毕业后的月薪：'))
# if money >= 15000:
#     print('改善下居住环境！')
# elif money >= 12000:
#     print('换部电脑或者手机！')
# elif money >= 10000:
#     print('去吃顿好的！')
# else:
#     print('自己煮饭')

# str1 = '速成班20期，我们是最棒的！'
# for i in str1:
#     print(i)
#     print('*'*30)

# count=0 # 计数
# str1 = '速成班20期，我们是最棒的！'
# print(len(str1))
# for i in str1:
#     if i == '我':
#         continue
#     print(i)
#     count=count+1
#     print(count)
#     print(('*'*30))
# print(count)
# for i in range(6):
#     print(i)
# a = [1,2,'6','summer'] # 请使用成员运算符判断i是否在这个列表里面
# for i in a:
#     if i == 'i':
#         print(i,":存在列表中")
#         break
#     else:
#         print(i,":不存在列表中")

dict_1 = {"class_id":45,'num':20} # 请判断班级上课人数是否大于5
# 注：num表示课堂人数。如果大于5，输出人数。
num1 = dict_1.get('num')
if num1 > 5:
    print(num1,"人正在上课")
else:
    print("当前上课人数小于5人")
print("当前正在上课：",num1,"人")

# list3 = ['王俊凯','易烊千玺','王源','蔡徐坤','鹿晗','张艺兴']
# # 列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的list中，最后打印最终的列表。
# print(list3)
# dict1 = dict(name='王俊凯',sex='男',age=18,city='北京'),\
#         dict(name='易烊千玺',sex='男',age=18,city='北京'),\
#         dict(name='王源',sex='男',age=18,city='北京'),\
#         dict(name='蔡徐坤',sex='男',age=18,city='北京'),\
#         dict(name='鹿晗',sex='男',age=18,city='北京'),\
#         dict(name='张艺兴',sex='男',age=18,city='北京')
# print(dict1)
# list1 = [dict1]
# print(list1)
