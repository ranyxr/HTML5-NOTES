#!/usr/bin/python
#coding=utf-8

import MySQLdb

db = MySQLdb.connect("localhost","root","123","testdb")

cursor = db.cursor()

try:
    cursor.execute("select * from emp")

    data = cursor.fetchall()

    print "get data:",data

    for i in cursor.description:
        print i[0],

    print ""

    for row in data:
        name = row[0]
        age = row[1]
        sex = row[2]
        num = row[3]

        print "name : %s,age : %d,sex : %s,num : %d"%(name,age,sex,num)

except:
    print "Error : unable to fecth data"

db.close()

