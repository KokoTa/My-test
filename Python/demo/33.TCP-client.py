# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
# 循环输入
while True:
  # 输入消息
  data = input().encode('utf-8') # str转bytes
  # 没数据就退出
  if not data:
    break
  # 发送数据
  s.send(data)
  # 接收数据
  print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
print('Close connect')

# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()