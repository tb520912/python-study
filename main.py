# 这是一个示例 Python 脚本。
# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 14:44
# @Author  : sunnysabde
# @Site    :
# @File    : main
# @Software: PyCharm
# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


"""
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
"""
import random

"""
数据类型
"""
"""
# <class 'int'>
print(type(11))
# <class 'float'>
print(type(11.11))
# <class 'bool'>
print(type(True))
# <class 'NoneType'>
print(type(None))
# <class 'str'>
print(type('hello world'))
# <class 'list'> 列表
print(type([1, 2, 3, 4, 5]))
# <class 'tuple'> 元组
print(type((1, 2, 3, 4, 5)))
# <class 'set'> 集合
print(type({1, 2, 3, 4, 5}))
# <class 'dict'> 字典
print(type({'name': 'sunny', 'age': 18}))
"""

"""
输出 
print()
格式化输出：
%d 整数
%03d 整数，不足三位补0
%f 浮点数
%.2f 浮点数，保留两位小数
"""

"""
print("int: %d" % 11)  # 11
print("int: %03d" % 11)  # 011
print("float: %f" % 11.11)  # 11.110000
print("float: %.2f" % 11.11111)  # 11.11
print(f'字符串 {11}', end="\t")  # 字符串 11 \t 制表符，一个tab 四个空格
name = "张三"
print(f'姓名：{name}')  # 姓名：张三
print("hello \nworld")  # hello world
"""

"""
输入
input()
参数是提示信息
返回值用变量接收，是用户输入的内容
程序执行到input时 等待用户输入，输入完成后才会继续向下执行
input接收到的数据类型都是字符串
"""
"""
name = input("请输入姓名：")
print(f'姓名：{name}')
"""

"""
类型转换
"""
# age = "18"
# print(type(age))  # <class 'str'>
# age = int(age)
# print(type(age))  # <class 'int'>

# aa = input("请输入年龄：")
# print(type(aa))  # <class 'str'>
# print(type(int(aa)))  # <class 'int'>
# print(type(float(aa)))  # <class 'float'>
# print(type(bool(aa)))  # <class 'bool'>
# bb = tuple(aa)
# print(bb)
# print(type(bb))  # <class 'str'>
# cc = list(aa)
# print(cc)
# print(type(cc))  # <class 'str'>
"""
t1 = (1,2,3)
print(type(t1))
print(list(t1))
print(type(list(t1)))
str1 = "1"
str2 = "1.1"
str3 = "(1,2,3)"
str4 = "[1,2,3]"
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
print(type(eval(str1)))  # <class 'int'>
print(type(eval(str2)))  # <class 'float'>
print(type(eval(str3)))  # <class 'tuple'>
print(type(eval(str4)))  # <class 'list'>
"""

"""
运算符
"""
"""
# a = 10
# b = "3"
# print(a + b)  # 报错 TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 多个变量赋值
a, b, c = 1,2,3
print(a, b, c)  # 1 2 3
b > 1 and print("b大于1")  # b大于1
b > 2 and print("b大于1")  # 不输出
"""

"""
语句
"""
"""
# if
格式
if 条件:
    代码块
elif 条件:
    代码块
else:
    代码块


age = 18
if age > 18:
    print("成年人")
elif age == 18:
    print("刚好成年")
else:
    print("未成年人")
"""
"""
三目运算符
格式
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""
# a = 2
# b = 1
# c = a if a > b else b
# print(c)

"""
循环 
for
格式
for 变量 in 序列: #序列 可迭代对象 例如：字符串、列表、元组、字典、集合
"""
# age = 10  # 'int' object is not iterable
# age = "10"  # 0 1
# age = (1,2,3)  # 1 2 3
# age = {1, 2, 3}  # 1 2 3
# for i in age:
#     print(i)

"""
循环和else
格式
for 变量 in 序列:
    代码块
else:
    代码块
当循环正常执行完成后执行else
当循环被break打断后不执行else

"""



"""
字符串
下标
切片
    选取方向必须和步长方向一致，否则无法选取
常用方法
find() 查找指定字符串，找到返回下标，找不到返回-1;参数：子串，开始下标，结束下标；返回值：子串首位下标 从左往右查找
rfind() 查找指定字符串，找到返回下标，找不到返回-1;参数：子串，开始下标，结束下标；返回值：子串首位下标 从右往左查找
index() 查找指定字符串，找到返回下标，找不到报错；参数：子串，开始下标，结束下标；返回值：可以找到 则返回子串首位下标 否则异常 从左往右查找
rindex() 查找指定字符串，找到返回下标，找不到报错；参数：子串，开始下标，结束下标；返回值：可以找到 则返回子串首位下标 否则异常 从右往左查找

count() 统计指定字符串出现的次数；参数：子串，开始下标，结束下标；返回值：子串出现的次数
replace() 替换字符串；参数：旧子串，新子串，替换次数；返回值：替换后的字符串 默认全部替换
split() 分割字符串；参数：分割符，分割次数；返回值：分割后的列表
join() 合并列表中的字符串数据为一个大字符串；参数：分隔符；返回值：合并后的字符串
capitalize() 将字符串第一个字符转换为大写,其余全部变小写；参数：无；返回值：字符串
lower() 将字符串中的大写转换为小写；参数：无；返回值：字符串
upper() 将字符串中的小写转换为大写；参数：无；返回值：字符串
lstrip() 删除字符串左侧空白字符；参数：无；返回值：字符串
rstrip() 删除字符串右侧空白字符；参数：无；返回值：字符串
strip() 删除字符串两侧空白字符；参数：无；返回值：字符串
startswith() 判断字符串是否以指定子串开头；参数：子串，开始下标，结束下标；返回值：布尔值
endswith() 判断字符串是否以指定子串结尾；参数：子串，开始下标，结束下标；返回值：布尔值
isalpha() 判断字符串是否全是字母；参数：无；返回值：布尔值
isdigit() 判断字符串是否全是数字；参数：无；返回值：布尔值
isalnum() 判断字符串是否全是字母或数字；参数：无；返回值：布尔值
isspace() 判断字符串是否全是空白字符；参数：无；返回值：布尔值
title() 将字符串中的每个单词首字母大写；参数：无；返回值：字符串
len() 计算字符串的长度；参数：无；返回值：字符串长度
ljust() 指定字符串长度，内容靠左边，不足的位置用指定字符填充，默认空格；参数：长度，填充字符；返回值：字符串
rjust() 指定字符串长度，内容靠右边，不足的位置用指定字符填充，默认空格；参数：长度，填充字符；返回值：字符串
center() 指定字符串长度，内容居中，不足的位置用指定字符填充，默认空格；参数：长度，填充字符；返回值：字符串
"""
# a = "hello World"
# 下标
# print(a[0])  # h
# 切片
# 语法：字符串[开始下标:结束下标:步长]
# 从开始下标开始截取到结束下标之前，步长是1
# 步长是负数，从右往左截取
# 步长是正数，从左往右截取
# 步长是0，报错
# 步长：是连续截取还是隔一个截取 1 连续；2 隔一个，3 隔两个。。。
# print(a[0:5])  # hello
# print(a[0:5:2])  # hlo
# print(a[0:5:0])  # 报错
# print(a[0:5:-1])  # 无输出
# print(a[5:0:-1])  # olleh
# print(a[5:0:-2])  # olh
# print(a[5:0:2])  # 无输出
# print(a[5:0:-3])  # oe
# print(a[5::-1])  # olleh
# print(a[5::1])  # world
# print(a[5::2])  # wold
# print(a[5::3])  # wl
# print(a[5::0])  # 报错
# print(a[5:0])  # 无输出
# print(a[0:-1:1])  # hello worl
# print(a[-1:-10:-1])  # dlrow ol
# print(a[-1:-10:-1])  # 无输出

# print(a.find("l"))  # 2
# print(a.find("l", 3, 5))  # 3
# print(a.find("c"))
# print(a.rfind("l"))  # 9
# print(a.rfind("l", 3, 5))  # 3
# print(a.rfind("c"))  # -1
# print(a.index("l"))  # 2
# print(a.index("l", 3, 5))  # 3
# print(a.index("c"))  # 报错
# print(a.rindex("l"))  # 9
# print(a.rindex("l", 3, 5))  # 3
# 和切片不同。查找时查找的字符串不论是从左向右 还是右往左。子串的首位下标都是从左往右数。并子串只有和左向右的切片一样，是连续的才能找到
# print(a.rfind("lro"))
# print(a.rfind("orl"))
# print(a.find("lro"))
# print(a.find("orl"))
# print("========")
# print(a.count("l"))  # 3
# print(a.capitalize())
# print(a)
# print(a.lower())
# print(a.upper())
# print("======")
# print(a.ljust(20, "*"))
# print(a.rjust(3, "*"))
# print(a.center(20, "*"))

# a = [1, 2, 3]
# b = (1, 2, 3)
# c = {1, 2, 3}
# print(type(a))
# print(type(b))
# print(type(c))
# d = "hello"
# print(len(d))
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# a.insert(3, b)
# print(a)
# del(b[3])
# print(b)
# a1 = [1,2,3]
# a2 = a1.copy()
# print(a2)
# a1[0] = 100
# print(a2)
# print(a1)

# ta = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
# c = [[], [], []]
# for i in ta:
#     y = random.randint(0, 2)
#     # 判断c[y]是否已满 每个元素最多3个
#     if len(c[y]) < 3:
#         c[y].append(i)
#     else:
#         # 随机找一个不满的列表
#         while True:
#             y = random.randint(0, 2)
#             if len(c[y]) < 3:
#                 c[y].append(i)
#                 break
# print(c)

"""
元组
1.元组是不可变的，不能增删改
2.元组中的元素可以是任意类型
3.元组中的元素可以重复
4.元组中的元素是有序的

如果元组中只有一个元素，那么这个元素后面必须加逗号，否则会被认为是其他类型
加逗号的才知道是元组，否则只认为是元素用括号包裹了
"""
c = (1, 2, 3)
print(c)
# c[0] = 100  # 'tuple' object does not support item assignment
print(c)
d = (1,)  # <class 'tuple'>
f = (1)  # <class 'int'>
print(type(d))
print(type(f))

'''
按 Shift+F10 执行或将其替换为您的代码。
按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
'''
"""
按 Shift+F10 执行或将其替换为您的代码。
按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
"""
"""
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
"""

"""
变量
内存地址的别名，用来存储数据的
定义 变量名 = 值
"""

# age = 18
# print(type(age))  # aaa 单行注释如果和代码同行，则至少需要两个空格去分隔
# age = "zhansan"
# print(type(age))
# a = 10
# f = 10.3
# print('name=%s, age = %d, float = %f.' %(age, a, f))
# print("%s is %d years old." %('Horace', 20))

"""
公共操作
+
支持字符串 列表 元组
* 复制 字符串 列表 元组 与整数相乘 
in 元素是否存在 字符串 列表 元组 字典
not in 元素是否不存在 字符串 列表 元组 字典
"""
str1 = "hello"
str2 = "world"

list1 = [1,2]
list2 = [3,4]

tuop1 = (1, 2)
tuop2 = (3, 4)

# print(str1 + str2)  # helloworld
# print(list1 + list2)  # [1, 2, 3, 4]
# print(tuop1 + tuop2)  # (1, 2, 3, 4)

dict1 = {"name": 'zs',"mw": "a"}
dict22 = {"age": 18}
# print(dict1 + dict2)  #  unsupported operand type(s) for +: 'dict' and 'dict'

# print(str1 * 2)  # hellohello
# print(list1 * 3)  # [1, 2, 1, 2, 1, 2]
# print(tuop1 * 4)  # (1, 2, 1, 2, 1, 2, 1, 2)
# print("o" in str1)  # True
# print("w" in str1)  # False
# print("===")
# print("o" not in str1)  # False
# print("w" not in str1)  # True
# print("====list")
# print(1 in list1)  # True
# print(8 in list1)  # False
# print("====")
# print(1 not in list1)  # False
# print(8 not in list1)  # True
# print("====tuop")
# print(1 in tuop1)  # True
# print(8 in tuop1)  # False
# print("====")
# print(1 not in tuop1)  # False
# print(8 not in tuop1)  # True
# print("====dict")
# print("name" in dict1)  # True
# print("pw" in dict1)  # False
# print("====")
# print("name" not in dict1)  # False
# print("pw" not in dict1)  # True

"""
方法
len() 计算容器中元素个数
del / del() 删除
max() 返回容器中元素最大值。按照首字符的ASCII码值进行比较
min() 返回容器中元素最小值
range(start, end step) 生成从start到end的数字，步长为step。供for循环使用
enumerate() 函数用于将一个可遍历的数据对象（列表 元组 或字符串）组合成一个索引序列，同时列出数据和下标，一般在for中使用
"""
# print(len(str1))  # 5
# print(len(list1))  # 2
# print(len(tuop1))  # 2
# print(len(dict1))  # 1

# print(max(str1))  # o
# print(max(list1))  # 2
# print(max(tuop1))  # 2
# print(max(dict1))  # name
# print(max([1, 2, 3, 38, 35]))  # 38

# list = ['a', 'b', 'c', 'e']
# for index, char in enumerate(list):
#     print(f"{index}---{char}")
    #  0---a
    # 1---b
    # 2---c
    # 3---e

"""容器类型转换"""
# print(tuple(list))  # ('a', 'b', 'c', 'e')

"""列表推导式"""
# list = [i for i in range(10)]
# print(list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = [i for i in range(10) if i % 2 == 0]
# print(list2)  # [0, 2, 4, 6, 8]

"""字典推导式"""
keys = ["name", "age", "gender", "sex"]
vs = ["zs", 18, "男"]
dict = {keys[i]: vs[i] for i in range(min(len(keys), len(vs)))}
print(dict)  # {'name': 'zs', 'age': 18, 'gender': '男'}

"""提取字典数据"""
counts = {"a": 100, "b": 30, "c": 155}
newCounts = {key: value for key, value in counts.items() if value > 50}
print(newCounts)  # {'a': 100, 'c': 155}

"""集合推导式"""
set1 = {i*2 for i in range(10)}
print(set1)
