#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建类
class Student(object):
	grade = 1 # 类属性

	# 实例属性
	def __init__(self, name, score): # 第一个参数永远是self，self指向实例本身
		self.__name = name # 私有变量，不可外部访问
		self.score = score

	def printScore(self):
		print('%s: %s' % (self.__name, self.score))

bart = Student('KokoTa', 100)
bart.printScore()
bart.other = 'Greeting'
print(bart.other)
print(bart._Student__name)

print(Student.grade)
print(bart.grade)
bart.grade = 2
print(Student.grade)
print(bart.grade)

# 继承/多态
class NewOne(Student):
	def printScore(self):
		print(self.score)

bart2 = NewOne('KonoTa', 99)
bart2.printScore()

# 判断对象类型
import types
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# dir()获得对象属性和方法
# 可使用getattr(obj, attr, default)、setattr()、hasattr()操作对象状态
# print(dir('ABC'))

# __slots__限制实例属性
# 作用范围仅对当前类的实例，对继承的子类不起作用
class Student(object):
	__slots__ = ('name', 'age')

g = Student()
g.name = 'KokoTa'
g.age = 22
# g.score = 100 报错

# @property：让访问和设置一体化
class Screen(object):
	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		self.__height = value

	@property
	def resolution(self):
		return self.__height * self.__width

bart = Screen()
bart.width = 10
print(bart.width)
bart.height = 20
print(bart.height)
print(bart.resolution)


# 定制类
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
# 其中某个例子
class Chain(object):

  def __init__(self, path=''):
    self._path = path

  def __getattr__(self, path):
    return Chain('%s/%s' % (self._path, path))

  def __call__(self, name):
  	if isinstance(name, str):
  		return Chain('%s/%s' % (self._path, name))

  def __str__(self):
    return self._path

  __repr__ = __str__

# 解析：
# 一开始调用Chain()，本应该调用__str__，但是后面我们访问了status这个属性
# 因此我们调用的是__getattr__，然后我们组合路径后递归调用Chain
# 接下来我们调用user这个函数，注意不是访问属性了，于是我们执行的是__call__，然后组合递归调用Chain
# 以此类推，当执行到list时，后面没有访问其他东西了，所以调用__str__，打印最终路径
print(Chain().status.user('KokoTa').timeline.list)


# 枚举类
from enum import Enum, unique
# 方法一
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value) # 注意value从1开始
# 方法二
@unique # 设定的键和值是唯一的，否则报错
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday(Weekday.Mon))
print(Weekday(1))

# 元类
# 利用type创建class
# type包含三个参数
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def method(self, num):
	return num
NewClass = type('NewClass', (object,), dict(fn=method))
print(NewClass)
print(NewClass())
print(NewClass().fn(100))