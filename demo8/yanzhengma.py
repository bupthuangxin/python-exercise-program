#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
#随机颜色 背景
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)
#随机颜色 字体
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)
#随机字符
def rnfChar():
    return chr(random.randint(65, 90))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('msyh.ttf', 36)
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
#填充文字
for i in range(4):
    draw.text((60*i+10, 10), rnfChar(), font=font, fill=rndColor2())
#模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')