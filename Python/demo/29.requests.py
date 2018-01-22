# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# GET
import requests
r = requests.get('https://www.douban.com', params={'q': 'python', 'cat': '1001'}, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.status_code)
print(r.url)
print(r.encoding)
print(r.headers)
print(r.cookies)
# print(r.text) # 返回文本
# print(r.content) # 返回bytes对象
# print(r.json) # 返回json



# POST
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# 传JSON
# r = requests.post(url, json={...})
# 传cookie
# r = requests.post(url, cookies={...})
# 传文件
# upload_files = {'file': open('report.xls', 'rb')} # 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
# r = requests.post(url, files=upload_files)
# 超时
# r = requests.get(url, timeout=2.5)
