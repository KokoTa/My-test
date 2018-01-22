# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 缩放
from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')



# 模糊
from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')



# 生成子母验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def randomChar():
  return chr(random.randint(65, 90))

# 随机颜色1
def randomColor():
  return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def randomColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 240
height = 60
# 验证码画布大小和颜色
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充像素
for x in range(width):
  for y in range(height):
    draw.point((x, y), fill=randomColor())
# 输出文字
for t in range(4):
  # 60*4 = 240 = width 每个字占据的宽度， 10 距离左边界距离
  # 10 距离上边界距离
  draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')