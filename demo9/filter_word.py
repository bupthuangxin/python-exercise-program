#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'

def filter_word(input_words):
    input_words = input_words.split()
    filter_word_list = []
    with open('filter_word.txt', 'r') as f:
        for line in f:
            filter_word_list.append(line.strip())
    if list(set(input_words).intersection(set(filter_word_list))):
        return '请文明用语'
    else:
        return '高雅人士'

input_words = input('Input some words:')
print(filter_word(input_words))