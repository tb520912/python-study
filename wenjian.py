"""
文件操作
"""
"""
基本步骤
1.打开文件
2.读写文件
3.关闭文件
方法：
open(name[,mode[,buffering]])
name:文件名
mode:打开模式
buffering:缓冲区大小
"""
# # 打开文件
# f = open('test.txt', "w")
# print("文件名：", f.name)
# # 写入文件
# f.write("hello world")
# # 关闭文件
# f.close()

# # 读取文件
# 如果文件不存在则报错
# f = open('test.txt', "r")
# # # 读取全部内容
# print(f.read())
# # # 读取一行
# print(f.readline())
# # # 读取多行
# print(f.readlines())
# # # 关闭文件
# f.close()

# 追加 如果文件不存在则创建
# f = open('test.txt', "a")
# f.write("hello world")
# f.close()

# 写入 如果文件不存在则创建
# f = open('test1.txt', "w")
# f.write("hello world")
# f.close()

# 省略模式 默认为r
# f = open('test.txt')
# print(f.read())
# # f.write("hello world")
# f.close()

# f = open('test.txt', "r")
# # # 读取全部内容
# # print(f.read(10))
# # 读取文件 只能是读取模式
# # aaaaa
# # bbbb
# # # 读取一行
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # # 读取多行
# print(f.readlines())
# # 关闭
# f.close()


# f = open('test.txt', "r+")
# # r+ 可读可写，指针在开头 用新内容覆盖旧内容
# # f = open('test.txt', "w+")
# # w+ 可读可写，指针在开头 用新内容覆盖旧内容，这里我们只执行了读取，所有文件的内容为空，所以读取不到内容
# print(f.readline())
#
# f.write("hello world")
# f.close()

"""
seek(偏移量,起始位置) 用于移动文件指针到指定位置
0 开头
1 当前位置
2 文件末尾
目标：
 1, r 改变文件指针的位置，改变读取数据开始位置或把指针放到文件末尾
 2, a 改变文件指针的位置，做到读取数据

"""
"""
tell() 用于获取文件指针的位置
"""
# f = open('test.txt', "r")
# # 移动指针到文件末尾
# print(f.tell())
# f.seek(0, 2)
# print(f.readline())  # 读取不到内容
# print(f.tell())
# # 移动指针到文件开头
# # f.seek(0, 0)
# f.close()

# 移到某个位置
# f = open('test.txt', "r")
# f.seek(5, 0)
# print(f.readlines())  # ['\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee'] \n算两个偏移量
# f.close()

# f = open('test.txt', "a+")
# print(f.tell())
# print(f.read())
# f.seek(0, 0)
# print(f.tell())
# print(f.readline())
# f.close()


# 文件备份
# 1， 用户输入要备份的文件名
# 2， 处理文件名
# 3， 备份文件写入
# 4， 关闭文件

# f = open('test.txt', "r")
# old_name = f.name
# print(old_name)
# # 处理文件名
# # 1，找到文件名中的点 最后一个点
# index = old_name.rfind(".")
# if index < 0:
#     print("文件名错误")
#     exit()
# # 2，分割文件名
# c = old_name[:index], old_name[index:]
#
# # 3，拼接文件名
#
# print(c)
# new_name = "[备份].".join(c)
# new_f = open(new_name, "w")
# # new_f.write(f.read())
# # 字节读取 1024字节 循环写入
# while True:
#     content = f.read(1024)
#     if len(content) == 0:
#         break
#     new_f.write(content)
# f.close()
# new_f.close()

"""
OS模块
1，重命名
2，删除
3，目录操作
"""
import os;
# os.rename("test.txt", "test1.txt")
# os.remove("test1.txt")  # 系统找不到指定的文件。: 'test1.txt'  删除 文件必须存在
# os.mkdir("test")  # 已经存在的 不能创建 [WinError 183] 当文件已存在时，无法创建该文件。: 'test'
# os.mkdir('test/test1/test2')  # 不能同时创建多级目录
# print(os.getcwd())  # D:\Python\code\demo1 获取当前文件的绝对路径
# os.mkdir("aa")

# 在aa目录下创建bb目录 先切换到aa目录 再创建bb目录
# os.chdir("aa")  # 切换目录
# os.mkdir("bb")

# print(os.listdir())  # 获取当前目录下的所有文件和目录
# print(os.listdir("aa"))  # 获取aa目录下的所有文件和目录

# 重命名文件夹 不能跨级重命名 需要先切换到目录下
# os.chdir("aa")
# os.rename("bb", "bbbb")

os.chdir("aa")
os.removedirs("bbbb")