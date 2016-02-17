#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
import os
from PIL import Image

iphone_width = 200
iphone_height = 1000

def imgiphone5(path):
    files = os.listdir(path)
    for img in files:
        if img.endswith(('.jpg', '.bmp', '.png')):
            im = Image.open(path+img)
            width, height = im.size
            if iphone_width < width or iphone_height < height:
                if iphone_width < width:
                    im.thumbnail((iphone_width, height))
                if iphone_height < height:
                    im.thumbnail((width, iphone_height))
            im.save('new'+img)

imgiphone5('/Users/huangxin/PycharmProjects/ex/img/')