#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
nums = list(range(100))
print(nums[0:3])
print(nums[:3])
print(nums[-3:])
print(nums[-3:-1])
print(nums[:10:2]) # 10个数里每间隔2取一次
print(nums[::20])
copyNums = nums[:]
print(len(copyNums))

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
# for key in d
# for value in d.values()
# for k, v in d.items()
# for i, value in enumerate([1, 2, 3])
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
print(isinstance(123, Iterable)) # 整数是否可迭代
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)

# 列表生成式
nums = list(range(1, 11))
print(nums)
nums = [x * x for x in range(1, 11)]
print(nums)
nums = [x * x for x in range(1, 11) if x % 2 == 0]
print(nums)
nums = [m + n for m in 'ABC' for n in 'XYZ']
print(nums)
import os
nums = [d for d in os.listdir('.')]
print(nums)
# 练习：输出['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
print([x.lower() for x in L1 if isinstance(x, str)])

# 生成器
# 创建方法一
L = (x * x for x in range(5))
print(L)
for x in L:
	print(x)
# 创建方法二(以斐波那契为例)
def fib(max):
	n, a, b=0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b # 省去了temp临时变量
		n += 1
	return 'done'
g = fib(5) # 用next(g)调用
# 生成器调用for是取不到return值的，需要捕获StopIteration错误
while True:
	try:
		x=next(g)
		print(x)
	except StopIteration as e:
		print('return', e.value)
		break
# 练习：杨辉三角形
# +号可以使数组相连
def trangles():
	L = [1]
	while True:
		yield L
		L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]
n=0
for l in trangles():
	print(l)
	n+=1
	if n==10:
		break

# 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

