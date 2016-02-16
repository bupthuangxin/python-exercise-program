#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
from PIL import Image, ImageDraw, ImageFont

def add_num_to_img(image_path, sign):
    img = Image.open(image_path)
    width, height = img.size

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("msyh.ttf", min(width//8, height//8))

    w_font, h_font = draw.textsize(sign, font)

    draw.text((width - w_font, 0), sign, fill='red', font=font)
    img.save('newimg.jpg')

if __name__ == "__main__":
    add_num_to_img('0.jpg', '20')
    print('finish the img...')