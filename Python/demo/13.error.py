#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误处理
# except可以捕获多个错误，但是如果第二个错误是第一个错误的子集，那么就只能捕获第一个错误
# except...else类似if...else
# try:
#   print('try...')
#   r = 10 / int('2')
#   print('result:', r)
# except ValueError as e:
#   print('ValueError:', e)
# except ZeroDivisionError as e:
#   print('ZeroDivisionError:', e)
# else:
#   print('no error!')
# finally:
#   print('finally...')
# print('END')





# logging模块可以打印或记录错误，并且程序将安全退出
# import logging
# def foo(s):
#   return 10 / int(s)
# def bar(s):
#   return foo(s) * 2
# def main():
#   try:
#     bar('0')
#   except Exception as e:
#     logging.exception(e)
# main()
# print('END')





# 自定义错误
# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
# foo('0')





# 向外抛出错误
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise # 将foo的错误抛出
# bar()





# 调试
# 方法一：assert
# python -O error.py，可以无视断言
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!' # n!=0我就跳过断言
#     return 10 / n
# def main():
#     foo('0')
# main()

# 方法二：logging
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# 方法三：pdb
# python -m pdb error.py启动pdb
# n -> 单步执行
# p x -> 查看变量x
# l -> 查看代码
# q -> 退出pdb
# 以下是测试代码
# s = '0'
# n = int(s)
# print(10 / n)
# 测试完会发现这样太麻烦了
# 我们可以import pdb
# 在想暂停的位置添加pdb.set_trace()
# 然后用命令p查看变量，或者用命令c继续运行
# 不过还是很麻烦= =





# 单元测试
# 测试一个自定义的Dict类
class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("NO attribute %s" % key)

	def __setattr__(self, key, value):
		self[key] = value

# 测试
import unittest
class TestDict(unittest.TestCase):             #所有测试用例类继承的基本类（断言）
    def setUp(self):                           #测试用例执行前的初始化工作
        print('setUp...')
    def tearDown(self):                        #测试用例执行之后的善后工作
        print('tearDown...')
    def test_init(self):                       #测试用Dict生成一个dict实例，然后进行各种判断
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)               #assert*():断言方法
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):             					 #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    def test_attr(self):                       #测试用d.key形式是否成功取到值
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):      #通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']      
    def test_attrerror(self):                  #测试用d.key形式取值，如果没成功，返回的错误为指定错误
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
if __name__ == '__main__':             				 #只能直接运行，通过模块导入时不会运行
    unittest.main()       				 						 #将一个单元测试模块变为可直接运行的测试脚本，寻找在该模块中以“test”命名开头的测试方法，并自动执行他们

# PS：命令行方法 python -m unittest mydict_test