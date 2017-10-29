#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数
# map
def normalize(s):
	if isinstance(s, str) != True:
		return
	return s[0].upper() + s[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
# reduce
from functools import reduce
def prod(a, b):
	return a*b
L1 = [3, 5, 7, 9]
L2 = reduce(prod, L1)
print(L2)
# map+reduce
CHAR_TO_FLOAT = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'.': -1}
def strToFloat(s):
	nums = list(map(lambda c: CHAR_TO_FLOAT[c], s)) # 数值数组
	point = 0 # 是否遇到标点符号了
	def toFloat(a, b):
		nonlocal point # 设为非本地变量，因为修改(注意是修改！)同名变量时找的是局部的point，但是局部没有point，所以需引用上级的point
		if b == -1:
			point = 1
			return a # 遇到小数点了，直接返回原值
		if point == 0:
			return a*10+b
		else:
			point = point * 10 #小数点只会遇到一次，但累乘是多次
			return a+b/point
	return reduce(toFloat, nums, 0.0)
print(strToFloat('0'))
print(strToFloat('123.456'))
print(strToFloat('123.45600'))
print(strToFloat('0.1234'))
print(strToFloat('.1234'))
print(strToFloat('120.0034'))
# filter
# 埃氏筛法求素数
def oddIter(): # 构造奇数序列
	n = 1
	while True:
		n += 2
		yield n
def filterNum(n):
	return lambda x: x % n > 0
def preimes():
	yield 2
	it = oddIter() # 初始化
	while True:
		n = next(it) # 返回序列第一个
		yield n
		it = filter(filterNum(n), it) # 构建新序列，这里不要纠结it是生成器，把it当作一个有限长度的数组去理解

for x in preimes():
	if x < 100:
		print (x)
	else:
		break
# 过滤空字符和None
def filterStr(s):
	return s and s.strip()
L1 = ['A', '', 'B', None, 'C', '  ']
L2 = list(filter(filterStr, L1))
print(L2)
# 判断回文数
def palindrome(n):
	return n > 10 and str(n) == str(n)[::-1] # [::-1]取全部，但是是反着取，即反转
output = filter(palindrome, range(1, 100))
print(list(output))
# sorted
# 按名字排序
def sortName(item):
	return item[0]
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L1, key=sortName)
print(L2)
# 成绩高到低排序
def sortValue(item):
	return item[1]
L3 = sorted(L1, key=sortValue, reverse=True)
print(L3)

# 闭包
# 得不到预想结果
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 修正后得到正确结果
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 装饰器
def log(func):
  def wrapper(*args, **kw):
    print('call %s():' % func.__name__)
    return func(*args, **kw)
  return wrapper

@log
def now():
  print('2015-3-25')

now()
# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
# 由于此时now.__name__指向wrapper，所以为了矫正它，需要引入functools.wraps
# 修改后如下：
import functools
def log(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    print('call %s():' % func.__name__)
    return func(*args, **kw)
  return wrapper

# 练习：在函数调用的前后打印出'begin call'和'end call'。同时装饰器可以同时支持单层调用和双层调用
def log(arg=''):
	if isinstance(arg, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('begin call')
				func(arg)
				print('end call')
			return wrapper
		return decorator
	else:
		@functools.wraps(arg)
		def wrapper(*args, **kw):
			print('begin call')
			arg()
			print('end call')
		return wrapper

# test1
@log
def test():
	print('Greeting')

test()
# test2
@log('KokoTa')
def test(name):
	print('Greeting ' + name);

test()


# 偏函数(固定住原函数的部分参数)
int2 = functools.partial(int, base=2)
print(int2('10010'))
# 相当于
# kw = { 'base': 2 }
# int('10010', **kw)

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
# 相当于：
# args = (10, 5, 6, 7)
# max(*args)