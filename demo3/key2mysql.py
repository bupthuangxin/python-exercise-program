#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'huangxin'
import uuid
import pymysql

class generate_N_keys(object):

    def __init__(self, num):
        self.num = num
        self.list = []

    def generate(self):
        for i in range(200):
            self.list.append(uuid.uuid1())

    def return_list(self):
        return self.list

class connmysql(object):

    def __init__(self, user, passwd, host, port, db):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.db = db

    def accessmysql(self):
        gen = generate_N_keys(200)
        gen.generate()
        keys = gen.return_list()

        conn = pymysql.connect(user=self.user, passwd=self.passwd, host=self.host, port=self.port, db=self.db)
        cursor = conn.cursor()
        cursor.execute('create table user (id int primary key auto_increment, N_key varchar(100))')
        for i in keys:
            cursor.execute('insert into user (N_key) values (%s)', str(i))
        conn.commit()
        cursor.execute('select * from user ')
        values = cursor.fetchall()
        print(values)
        cursor.close()
        conn.close()


if __name__ == "__main__":
    con = connmysql('root', '123456', 'localhost', 3306, 'python')
    con.accessmysql()
