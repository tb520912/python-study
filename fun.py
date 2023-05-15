"""
函数
必须先定义 再使用
定义：
def 函数名（参数）:
    函数体

调用 函数名（参数）
"""
from functools import reduce

# def fn(a, b):
#     """
#     求和
#     :param a:
#     :param b:
#     :return:
#     """
#     return a + b
#
#
# print(fn(1, 2))
#
# help(fn)
#
#
# def fn2():
#     print("无参")
#
#
# # fn2(1, 2)  # 无参函数调用时不能传参
#
#
# def line():
#     print("-" *20)
#
#
# def big(n):
#     for i in range(n):
#         line()
#
#
# big(20)

"""
变量作用域
"""

# a = 10


# def fn():
#     global a  # 函数体中声明全局变量
#     a = 100
#     print(a)
#     return 1, 2  # 默认是元组类型
#
#
# print(a)
# fn()
# print(type(fn()))  # <class 'tuple'>

"""
参数：
位置参数： 实参和形参个数必须一致 并且顺序相同
关键字参数： 声明时和位置参数一致。调用时 将参数通过 键=值 的方式进行传递 fn(name = "zs",age = 10)
        注意：不论声明还是调用，如果有位置参数，则位置参数必须放在关键字参数前。关键字参数不存在前后顺序
缺省参数： 所有位置参数必须出现在默认参数前
不定参数： *args 元组接收位置参数  **args 字典接收关键字参数
"""

# def fn(name, age, gender="nan"):
#     print(f'name={name},age = {age}, gender = {gender}')
#
#
# fn("zs", age = 10)

# def fn(name, age, *args):  # 默认以元组形式接收
#     print(name)
#     print(age)
#     print(args)
#
# fn("zs", 18, 1)
# fn(1,2,3)

# def fn(name, age, **args):  # 默认以元组形式接收
#     print(name)
#     print(age)
#     print(args)
#
# fn("zs", 18, key=1)
# fn(1,2,key=3)

"""
拆包
字典的拆包是取出key
"""
# tuple1 = (100, 110)
# a, b = tuple1
# print(a)  # 100
# print(b)  # 110
#
# dict1 = {
#     "name": 'zs',
#     "age": 20
# }
# # c, d = dict1
# # print(c)   # name
# # print(d)  # age
#
# c, d = dict1.values()
# print(c)   # zs
# print(d)  # 20


"""
交换变量值
"""
# a, b = 1, 2
# b, a = a, b
# print(a)  # 2
# print(b)  # 1


"""
引用
"""
# a = 1
# b = a
# print(id(a))  # 140728445625128
# print(id(b))  # 140728445625128

# a = 1
# b = 1
# print(id(a))  # 140728445625128
# print(id(b))  # 140728445625128

# a = [1, 2]
# b = [1, 2]
# print(id(a))  # 2107572508544
# print(id(b))  # 2107574765632
# a.append(3)
# print(id(a))  # 2159393331072


# a = [1, 2]
# def fn(a):
#     print(id(a))
#     a.append(3)
#     print(a)
#
# print(a)  # [1,2]
# print(id(a))  # 1803863152512
# fn(a)  # 1803863152512
# print(a)  # [1,2,3]


# a = 10
# print(id(a))
#
#
# def fn(a):
#     print(id(a))
#     a = 20
#
# fn(a)
# print(a)

"""
lambda
当函数体只有一行 并返回时，可使用lambda进行简化
lambda 参数: 函数体
"""
# def fn(c):
#     c(10)
#
# fn(lambda a: print(a))


"""
newList = map(fn, list)
reduce(fn, list) fn两个参，第一个是上一次迭代的计算结果，第二个是当前迭代的值
filter(fn, list) 过滤序列中不符合条件的元素
"""
list1 = [1, 2, 3]
newList = map(lambda x: x * 2, list1)
print(newList)  # <map object at 0x000002282D715570>
print(list(newList))  # [2, 4, 6]

sum = reduce(lambda s, a: s + a, list1)
print(sum)  # 6

list2 = [i for i in range(10)]
newList2 = filter(lambda x: x % 2 == 0, list2)
print(newList2)  # <filter object at 0x0000021789AC6200>
print(list(newList2))  # [0, 2, 4, 6, 8]




