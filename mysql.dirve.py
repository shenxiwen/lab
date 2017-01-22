#!/usr/bin/env python
import mysql.connector
conn = mysql.connector.connect(user='test',password='test',database='test',host='192.168.1.20')
cursor = conn.cursor()
cursor.execute('create table user2 (id varchar(20) primary key , name varchar(20))')
cursor.execute('insert into user2 (id,name) values (%s,%s)',['1','sxw'])
cursor.rowcount

conn.commit()
cursor.close()

