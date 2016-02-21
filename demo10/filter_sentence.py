#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
with open('filter_word.txt', 'r') as f:
    data = f.read().split()
text = input('please input sentence:')
for i in data:
    if text.find(i) != -1:
        text = text.replace(i, '*'*len(i))
print(text)
