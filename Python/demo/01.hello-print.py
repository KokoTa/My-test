#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# input your name
# name = input("Please input your name：");
# print("Hello", name);

# print string
print('I\'m OK');
print('\\\t\\');
print(r'\\\t\\'); # 不转义
print('''Hello
	Hello
	Hello''');
print(10 / 3);
print(10 // 3);
print(ord('A'));
print(chr(65));
print('\u4e2d\u6587');
print(b'ABC'); # bytes的每个字符都只占用一个字节
print('中文'.encode('utf-8')); # 将中文转为以utf-8编码的bytes
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));
print(len('中文'.encode('utf-8'))); # 1中文 = 3字节

# print string2 代码结尾有木有分号都可以
s1 = 72;
s2 = 85;
r = ((85-72)/72)*100;
print('%s %.1f' % ('成绩提升的百分点：', r));
