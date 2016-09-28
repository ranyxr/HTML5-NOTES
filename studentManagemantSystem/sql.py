#!/usr/bin/python
#coding=utf-8

import MySQLdb

#打开数据库链接
use = raw_input("用户名:")
passwd = raw_input("密  码:")

db = MySQLdb.connect('localhost',use,passwd,'testdb')

# 创建游标,用来通过sql语句操作具体数据
cursor = db.cursor()

# 通过游标对象执行sql语句

cursor.execute("select version()")


data = cursor.fetchone()

print "Database version :%s"%data

# 创建数据表
cursor.execute("drop table if exists newtab")

sql = "create table newtab(id int not null,name char(20),age int,income float)"

cursor.execute(sql)

sql = "insert into newtab (id,name,age,income) values ('1','mac',20,8.8)"


try:
    cursor.execute(sql)
    db.commit() #数据提交
except:
    db.rollback() #回滚到执行前的状态


db.close()
