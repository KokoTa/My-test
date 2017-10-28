#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict -> 类似JS对象
d = {}
## d.x = 1 报错
d['x'] = 1
## d[[1]] = 2 key必须是不可变的对象
print(d)
print('x' in d)
print(d.get('x'))
print(d.get('o'))
print(d.get('o', 'No the attr'))
print(d.pop('x'))
print(d)

# set -> 类似JS set过后的数组
s = set([1,2,3])
print(s)
s.add(1)
s.add(4)
print(s)
s.remove(4)
print(s)

# set 交并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)