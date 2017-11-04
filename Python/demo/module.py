#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这里是模块注释'

import sys # 引入sys模块

__author__ = "KokoTa"

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello')
	elif len(args) == 2:
		print('Hello %s' % args[1]) # args[0]为文件名,即09.module.py
	else:
		print('Too many args')

if __name__ == '__main__': # 使用命令行时调用test
	test()