#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image # 引入Pillow模块
im = Image.open('test.png') # 打开图像
print(im.format, im.size, im.mode) # 打印信息
im.thumbnail((200,100)) # 设置大小
im.save('thumb.jpg', 'JPEG') # 输出