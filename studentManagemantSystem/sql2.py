#!/usr/bin/python
#coding=utf-8

import MySQLdb

db = MySQLdb.connect("localhost","root","123","testdb")

cursor = db.cursor()

#sql = "update emp set sex = 'm' where name = 'lisi'"
sql = "update emp set age = age + 1 where sex = 'm'"

try:
    cursor.execute(sql)
    db.commit()
except:
    print "Error : failed update"
    db.rollback()

sql = "delete from emp where age > 20"

try:
    cursor.execute(sql)
    db.commit()
except:
    print "failed update"
    db.rollback()

db.close()

