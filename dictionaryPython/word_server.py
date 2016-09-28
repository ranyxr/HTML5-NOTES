#! /usr/bin/python
#coding=utf-8

from socket import *
import MySQLdb
from threading import *
import multiprocessing
import re
from time import *

HOST = '192.168.1.247'
PORT = 5857
ADDR = (HOST,PORT)

def register(db,conn):
    user = conn.recv(1024)
    pw = conn.recv(1024)
    cursor = db.cursor()
    sql = "select loginname from users where loginname = '%s'"%user
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        sql1 = "insert into users(loginname,password) values('%s','%s')"%(user,pw)
        try:
            cursor.execute(sql1)
            db.commit()
            conn.send("注册成功！")
            print "注册成功！"
        except:
            conn.send("register error")
            print "register error"
            db.rollback()
        return
    else:
        conn.send("用户名已存在！")
        print "用户名已存在！"
        return

def login(db,conn):
    user = conn.recv(1024)
    pw = conn.recv(1024)
    cursor = db.cursor()
    sql = "select * from users where loginname = '%s' and password = '%s'"%(user,pw)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        if data:
            conn.send("ok")
            return user
        else:
            conn.send("fail")
            return
    except:
        db.rollback()
        return

def select(db,conn,name):
    f = open('dict.txt','r')
    word = conn.recv(1024)
    #print name
    #print word
    p = re.compile(word)
    while True:
        content = f.readline()
        if content == '':
            break
        if p.match(content):
            #print content

            conn.send(content)

            cursor = db.cursor()
            sql = "insert into history values('%s','%s','%s')"%(name,word,ctime())
            try:
                cursor.execute(sql)
                db.commit()
                #print "---"
                return
            except:
                db.rollback()
                continue
        else:
            continue
    return

def history(db,conn,name):
    cursor = db.cursor()
    sql = "select * from history where name = '%s'"%(name)
    cursor.execute(sql)
    for i in cursor.description:
        #print i[0],
        conn.send(i[0])
        sleep(0.1)
    print ""
    rows = cursor.fetchall()
    conn.send(str(len(rows)))
    sleep(0.1)
    for row in rows:
        #print row[0],row[1],row[2]
        conn.send(str(row))
        sleep(0.1)
    return

def main(connfd):
    db = MySQLdb.connect('localhost','root','5560442','word')
    while True:
        data = connfd.recv(1024)
        print "operate :",data
        if data == '1':
            register(db,connfd)
        if data == '2':
            data1 = login(db,connfd)
            while True:
                if data1:
                    data2 = connfd.recv(1024)
                    #print data2
                    if data2 == '1':
                        select(db,connfd,data1)
                    if data2 == '2':
                        history(db,connfd,data1)
                    if data2 == '3':
                        break
        if data == '3':
            break
    return
if __name__ == '__main__':
    s = socket()
    s.bind(ADDR)
    s.listen(10)
    while True:
        try:
            connfd,addr = s.accept()
        except KeyboardInterrupt:
            raise
        except:
            continue
        t = Thread(target = main,args = (connfd,))
        #t.setDarmon(1)
        t.start()
    s.close()
