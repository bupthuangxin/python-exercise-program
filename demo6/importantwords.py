#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
import os, re
from collections import Counter
#找到该路径下的所有文件
def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path + '/' + fp
        if os.path.isfile(fppath):
            files.append(fppath)
        elif os.path.isdir(fppath):
            files += get_files(fppath)
    return files

#去除的词
stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']

#找到每个词出现的次数
def get_important_words(files):
    worddict = {}
    for filename in files:
        if filename.endswith('.txt'):
            with open(filename, 'r') as f:
                data = f.read()
                words = re.findall(r'[a-zA-Z0-9/’]+', data)
                for word in words:
                    if word not in stop_word:
                        worddict[word] = worddict[word] + 1 if word in worddict else 1
    worddict = sorted(worddict.items(), key=lambda x: x[1], reverse=True)
    return worddict


filess = get_files('/Users/huangxin/PycharmProjects/ex/words')
worddict = get_important_words(filess)

#可能出现多个最多次数
maxnum = 1
for i in range(len(worddict) - 1):
    if worddict[i][1] == worddict[i+1][1]:
        maxnum += 1
    else:
        break
for i in range(maxnum):
    print(worddict[i])
