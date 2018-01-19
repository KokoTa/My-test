# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python常用模块 - contextlib 模块

# @contextmanager -> 上下文管理
# demo1
from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

# demo2
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")


# @closing -> 把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page: # urlopen没有上下文，我们可以用closing把它改成有上下文，然后就可以像读取文件一样读取它了
    for line in page:
        print(line)

print(urlopen('https://www.python.org')) # 返回一个对象，读取需要用read()方法