# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# match() 匹配成功返回一个Match对象， 否则返回None
# PS：搜索的字符串用r开头，不然得加/转义
import re

test = '用户输入的字符串'
if re.match(r'用户', test):
  print('OK')
else:
  print('Fail')

# 切分字符串
test = 'a b    c';
print(test.split(' ')) # 错误
print(re.split(r'\s+', test)) # 正确

# 分组
test = '010-12345'
m = re.match(r'^(\d{3})-(\d{3,8})$', test)
print(m.group(0)) # 原始字符串
print(m.group(1)) # 第一个括号匹配的结果
print(m.group(2)) # 同理

# 贪婪匹配
# 默认匹配最多字符
test = '12300'
print(re.match(r'^(\d+)(0*)$', test).groups()) # 第二个括号取不到值，因为被第一个括号匹配完了
# 加?号表示非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', test).groups()) # 非贪婪会根据后面的表达式进行修整

# 编译，类似存储正则表达式，重复利用
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})')
print(re_telephone.match('010-123123').groups())
print(re_telephone.match('010-321321').groups())

# 匹配邮箱
def is_valid_email(address):
  return re.match(r'^[\w\d.]+@\w+.c(om|n)$', address)
# 带名字的邮箱
def name_of_email(address):
  return re.match(r'^<([\w\d\s]+)>[\w\d]*@[\w\d.]+$', address)

print(is_valid_email('asd@qq.com'))
print(name_of_email('<KokoTa>asd@qq.com'))