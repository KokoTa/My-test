# -*- coding: utf-8 -*-

import mysql.connector
con = mysql.connector.connect(user='root', password='123456', database='test')
cursor = con.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Fucker'])
print(cursor.rowcount)
# 执行INSERT等操作后要调用commit()提交事务
con.commit()
cursor.close()

cursor = con.cursor()
cursor.execute('select * from user where id = %s', ('1', ))
values = cursor.fetchall()
print(values)
cursor.close()
con.close()