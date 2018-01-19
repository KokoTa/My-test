# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python常用模块 - base64 模块

import base64
print(base64.b64encode(b'binary\x00string')) # 编码二进制
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw==')) # 解码

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')) # 把字符+和/分别变成-和_
print(base64.urlsafe_b64decode('abcd--__'))

# 处理去掉=的base64解码函数
import base64
def safe_base64_decode(s):
    while len(s)%4: # 补足=直到是4的倍数为止
        s=s+b'='
    return base64.b64decode(s)