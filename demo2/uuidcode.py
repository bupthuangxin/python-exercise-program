#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
import uuid
class generate_N_keys(object):

    def __init__(self, num):
        self.num = num
        self.list = []

    def generate(self):
        for i in range(200):
            self.list.append(uuid.uuid1())

    def return_list(self):
        return self.list

gen = generate_N_keys(200)
gen.generate()
keys = gen.return_list()
print(keys)
print(len(keys))


with open('/Users/huangxin/PycharmProjects/ex/generate_N_keys.txt', 'w') as f:
    for i in keys:
        f.write(str(i)+'\n')