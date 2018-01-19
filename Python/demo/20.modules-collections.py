# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python常用模块 - collections 模块

# namedtuple可以很方便地定义一种数据类型
# 它具备tuple的不变性，又可以根据属性来引用，使用十分方便
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
p = Point(3, 4)
print(p.x, p.y)

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)

# defaultdict，防止key不存在时报错，返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'A'
print(dd['key1'])
print(dd['key2'])

# 保持Key的顺序，可以用OrderedDict
# OrderedDict的Key会按照插入的顺序排列
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # 有序的

# Couter，计数器
from collections import Counter
c = Counter()
for ch in 'programming':
  c[ch] = c[ch] + 1
print(c)