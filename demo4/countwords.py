#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'

import re

with open('words.txt', 'r') as f:
    data = f.read()
result = re.split(r'[\s\,\.]+', data)
print(result)
print(len(result)-1)

with open('words.txt', 'r') as f:
    # for line in f.readlines():
    #     print(line.strip())
    words = re.findall(r'[a-zA-Z0-9/’]+', f.read())
print(words)
print(len(words))
