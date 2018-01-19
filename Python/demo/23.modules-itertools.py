# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python常用模块 - itertools 模块

# # 迭代无限数字
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#   print(n) # 根本停不下来

# # 迭代无限序列
# cs = itertools.cycle('ABC')
# for c in cs:
#   print(c) # 根本停不下来

# 重复有限次数
import itertools
rp = itertools.repeat('ABC', 3)
for r in rp:
  print(r)

# takewhile -> 从无限中取得有限, 上面无限迭代是因为用了for
natuals = itertools.count(1, 2) # 从1开始，步长为2
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain
# >>> for c in itertools.chain('ABC', 'XYZ'):
# ...     print(c)
# # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# groupby
# >>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
# ...     print(key, list(group))
# ...
# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']

# 练习
import itertools
def pi(N):
  '计算pi的值'
  # step1: 创建一个奇数序列
  odds = itertools.count(1, 2)
  # step2: 取前N项
  ns = itertools.takewhile(lambda x: x<= (2*N-1), odds)
  # step3: 添加正负号并让4除以项，然后求和
  res = 0
  flag = 1
  for n in ns:
    res += (4*flag/n)
    flag = -flag
  # step4: 返回和
  return res

print(pi(10)) # 3.04 < pi(10) < 3.05
print(pi(100)) # 3.13 < pi(100) < 3.14