# 这是一个示例 Python 脚本。

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
