#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# input()返回字符串，需要用int()转为整数
age = int(input('Input your age：'))
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

# 计算BMI
height = float(input('Input your height：'))
weight = float(input('Input your weight：'))
BMI = weight / (height**2)
print(BMI)
if BMI < 18.5:
    print('过轻')
elif BMI <= 25:
    print('正常')
elif BMI <= 28:
    print('过重')
elif BMI <= 32:
    print('肥胖')
else:
    print('严重肥胖')