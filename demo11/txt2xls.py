#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
import json
import xlwt3

def txt_to_xls(txt_file):
    with open(txt_file, 'r') as f:
        file_content = json.load(f, encoding='utf-8')
        xls_workbook = xlwt3.Workbook(encoding='utf-8')
        #创建表单
        xls_sheet = xls_workbook.add_sheet('student')
        for i in range(len(file_content)):
            #写入行序号
            xls_sheet.write(i, 0, i+1)
            json_data = file_content[str(i+1)]
            for j in range(len(json_data)):
                xls_sheet.write(i, j+1, json_data[j])
        xls_workbook.save('student.xls')

if __name__ == '__main__':
    txt_to_xls('student.txt')
