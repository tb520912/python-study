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

f = open('test.txt', "r")
# # 读取全部内容
# print(f.read(10))
# 读取文件 只能是读取模式
# aaaaa
# bbbb
# # 读取一行
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# # 读取多行
print(f.readlines())
# 关闭
f.close()