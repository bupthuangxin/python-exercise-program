#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
from html.parser import HTMLParser
import urllib.request
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.text = []

    #处理开始标签，比如<xx>      不需显示调用
    #解析时遇到开始标签调用,如<p class='para'>,参数tag是标签名,这里是'p',attrs为标签所有属性(name,value)列表,这里是[('class','para')]
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for variable, value in attrs:
                if variable == 'href':
                    self.links.append(value)
        if tag == 'p':
            self.text.append('\n\n')
        elif tag == 'br':
            self.text.append('\n')
    #处理开始标签和结束标签
    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.text.append('\n\n')
    #处理结束标签，比如</xx>     不需显示调用
    #遇到结束标签时调用,tag是标签名
    def handle_endtag(self, tag):
        pass
    #处理数据，就是<xx>data</xx>中间的那些数据  不需显示调用
    #遇到标签中间的内容时调用,如<style> p {color: blue; }</style>,参数data为开闭标签间的内容.
    #值得注意的是在形如<div><p>...</p></div>的位置,并不会在div处调用,而是只在p处调用
    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = re.sub('[\n\t\r]+', ' ', text)
            self.text.append(text)
    #处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    def handle_decl(self, decl):
        pass
    #处理注释
    def handle_comment(self, data):
        pass
    #处理形如<?instruction>的东西
    def handle_pi(self, data):
        pass
    #处理特殊字符串，就是以&#开头的，一般是内码表示的字符
    def handle_charref(self, name):
        pass
    #处理一些特殊字符，以&开头的，比如 &nbsp;
    def handle_entityref(self, name):
        pass


# 显式调用的方法
# 1.HTMLParser.feed(data): 参数为需要解析的html字符串,调用后字符串开始被解析
# 2.HTMLParser.getpos(): 返回当前的行号和偏移位置,如(23,5)
# 3.HTMLParser.get_starttag_text(): 返回当前位置最近的开始标签的内容

html = urllib.request.urlopen('https://www.douban.com')
html_code = html.read().decode('utf-8')
html_code = re.sub('<script[^>]*>[\\d\\D]*?</script>', '', html_code)

parser = MyHTMLParser()
parser.feed(html_code)
parser.close()
print(parser.links)
#print(parser.text)
print(''.join(parser.text))
