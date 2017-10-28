#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for in
for x in list(range(5)):
	print(x)

# while
sum = 0
n = 99
while n > 0:
	sum += n
	n -= 2
print(sum)

# break
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n += 1
print('END')

# continue
n = 0
while n < 10:
	n += 1
	if n % 2 == 0:
		continue
	print(n)