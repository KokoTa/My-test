#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 此IO章节都是同步读取


# 读取文本文件
# r:读取文件,w:重新写入文件；with语法可以省去关闭文件的步骤；encoding指定读取时的字符编码，默认为utf-8
with open('F:/Github/Program/My-test/Python/demo/test.txt', 'r', encoding='gbk') as f: 
    print(f.read()) # 一次性全读取

with open('F:/Github/Program/My-test/Python/demo/test.txt', 'r') as f:
    for line in f.readlines(): # 读取所有内容并按行返回
        print(line.strip()) # 把末尾的'\n'删掉

# 读取二进制文件（图片）
# rb:读取二进制文件，rb：重新写入二进制文件
with open('F:/Github/Program/My-test/Python/demo/test.jpg', 'rb') as f:
    print(f.read())

# 写入文本文件
# a:追加写入
with open('F:/Github/Program/My-test/Python/demo/test.txt', 'a', encoding='gbk') as f:
    f.write('Yohoooo~')



# 内存读写->StringIO，只能操作str
from io import StringIO

f = StringIO()
f.write('hello')
print(f.getvalue())

f = StringIO('OK!\nYeah!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#  BytesIO->操作二进制
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())



# 详细路径的操作
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000
# os.path.abspath('.') # 当前目录的绝对路径
# os.path.join(xx, oo) # 连接路径
# os.mkdir(xx) # 创建文件夹
# os.rmdir(xx) # 删除文件夹
# os.path.split(xx) # 拆分路径为两部分，后一部分为最后级别目录或文件
# os.path.splitext(xx) # 同上，后一部分是文件后缀
# os.listdir(xx) # 某文件夹下的所有目录和文件
# os.path.isdir(xx) # 是否是文件夹
# os.path.isfile(xx) # 是否是文件
# os.getcwd() # 获得执行时的绝对路径


# 列出当前目录下的所有目录/.py文件
import os

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 实现 dir -l xx -> 找出xx文件夹下的目录和文件
print([x for x in os.listdir('.')])

# 实现在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出绝对路径。
def searchFile(path, name):
    for x in os.listdir(path):
        if os.path.isdir(x):
            nPath = os.path.join(path, x)
            searchFile(nPath, name)
        else:
            if name in x:
                print(path, x)
    return 0

searchFile(os.getcwd(), 'test.txt')



# 序列化（把变量从内存中变成可存储或传输的过程）
import pickle, os

d = dict(name="KokoTa", age=22, score=100)
print(pickle.dumps(d)) # 把变量转为bytes格式，注意加了s表示读取后返回字符串，不带s表示读取后写入文件
print(pickle.dumps(d))

with open(os.getcwd()+'/test.txt', 'wb') as f:
    pickle.dump(d, f) # 转为二进制数据并写入f

with open(os.getcwd()+'/test.txt', 'rb') as f:
    d = pickle.load(f) # 读取二进制并转为变量
    print(d)



# dict <---> JSON
import json
# dict转为JSON
d = dict(name="AA", age=22, score=100)
print(json.dumps(d))
# JSON转为dict
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))



# python类实例 <---> dict <---> JSON
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student('XX', 23)

# 类实例转JSON
# print(json.dumps(s)) # 报错，不能直接转换，需要有过渡函数转换
def changeToJSON(std):
    return {
        'name': std.name,
        'age': std.age,
    }

print(json.dumps(s, default=changeToJSON))
# 不过这样每次都要写过渡函数
# class实例自带__dict__方法可转换，但若class定义了__slots__则这个方法无效
print(json.dumps(s, default=lambda obj: obj.__dict__))

# JSON转类实例
def changeToClass(d):
    return Student(d['name'], d['age'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=changeToClass)) # 这里是用object_hook