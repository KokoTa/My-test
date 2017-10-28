#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 内置函数：https://docs.python.org/3/library/functions.html#abs

# 空函数（作用：没想好怎么写，但是又想让程序运行不出错的情况下使用）
def nop():
	pass

# 自定义abs
def my_abs(x):
	if not isinstance(x, (int, float)): # 类型检查
		raise TypeError("bad type")
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-20))

# 引入math包后可使用cos/sin
import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny # 多值返回其实就是返回一个tuple

x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)

print(x, y)
print(r)

# ax2 + bx + c = 0的两个解
def quadratic(a, b, c):
	if b*b < 4*a*c:
		raise TypeError("num error")
	else:
		x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
		x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
		return x1, x2

print(quadratic(2, 3, 1))

# 自定义指数函数
def power(x, n=2):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1
	return s

print(power(n = 4, x = 2)) # 乱序传值

# 默认参数必须指向不变对象
def add_end(L=None):
  if L is None:
    L = []
  L.append('END')
  return L

# 可变参数
nums = [1,2,3]
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum

print(calc(2,3,4))
print(calc(*nums))

# 关键词参数
obj = {'A': 1, 'B': 2, 'age': 11}
def person(name, **kw):
	print(name, kw)

person('KokoTa1', p1=obj['A'], p2=obj['B'])
person('KokoTa2', **obj) # 传入的对象是一份深拷贝

# 命名关键词参数(限制关键词参数**kw的名字,见示例中的age)
def person2(name, *nums, age, **kw):
	print(name, nums, age, kw)

person2('KokoTa1', age=12) # 不传age会报错
person2('KokoTa2', *nums, **obj, other=11) # obj里的age被提取出来赋给函数的age

# 总结
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict

# 递归算阶乘
def fact(n):
	if n==1:
		return 1 
	return n * fact(n - 1)

print(fact(5))

# 尾递归优化(然而ptyhon并没有尾递归优化，还是会栈溢出)
def fact2(n, total=1):
	if n == 1:
		return total
	return fact2(n - 1, total * n)

print(fact2(5))

# 汉诺塔(n表示第一个柱子的盘子数)
def move(n, a, b, c):
	if n == 1:
		print('move', a, '-->', c)
	else:
		move(n - 1, a, c, b) # 先执行把n-1个移动到b上这个操作。
		move(1, a, b, c) # 再执行把最下面1个最大的移动到 c 这个操作
		move(n - 1, b, a, c) # 最后执行把n-1个从b上移动到c上这个操作 

move(4, 'A', 'B', 'C')