#!/usr/bin/python
# coding = utf-8
#online dictionary system

import MySQLdb
import sys
import threading
import socket,os,traceback
from threading import *
import re
from time import ctime

def register(conn,db):
    cursor = db.cursor()
    while True:
        name = conn.recv(1024)
        sql = 'select * from user where name = "%s"'%name
        cursor.execute(sql)
        data = cursor.fetchone()

        if not data:
            break
        else:
            conn.send('the name is already exist')

    password = conn.recv(1024)
    sql = 'insert into user value("%s","%s")'%(name,password)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        conn.send('register failed')
        db.rollback()
        return
    conn.send('register successfully')

def login(conn,db):

    cursor = db.cursor()
    name = conn.recv(1024)
    password = conn.recv(1024)
    sql ='select * from user where name = "%s" and password = "%s"'%(name,password)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        conn.send("soooooooooooorry, your name or password is wrong")
        return
    else:
        conn.send("login successfully")

        while True:
            num = conn.recv(1024)
            if num == '1':
                do_select(db,conn,name)
            elif num == '2':
                do_history(db,conn,name)
            else:
                return

def do_select(db,conn,name):
    f = open('dict.txt','r')
    q = conn.recv(1024)
    p = re.compile(q)
    while True:
        content = f.readline()
        if content == '':
            break;
        if p.match(content):
            conn.send(content)

            cursor = db.cursor()

            sql = 'insert into history values ("%s","%s","%s")'%(name,q,ctime())
            try:
                cursor.execute(sql)
                db.commit()
                return
            except:
                print 'error'
                db.rollback()
                return
            # print 'insert successfully'
        else:
            #conn.send("wrong word")
            continue
    return

def do_history(db,conn,name):
    # print '000000000000000000'
    cursor = db.cursor()
    sql = "select * from history where name = '%s'"%name
    cursor.execute(sql)
    for i in cursor.description:

        conn.send(i[0]+"   ")

    print ""
    rows = cursor.fetchall()
#    conn.send(str(len(rows)))

    for i in rows:

        conn.send(str(i))

    return




def main():
    db = MySQLdb.connect('localhost','root','yxr.1995','Dict')
    host = '192.168.1.246'
    port = 6333
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host,port))
    s.listen(10)


    while True:

        try:
            conn,addr = s.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            num = conn.recv(1024)
            if num == '1':
                threading.Thread(target = register, args = (conn, db)).start()
            else:
                threading.Thread(target = login , args = (conn, db)).start()
        except KeyboardInterrupt:
            raise
        except:
            traceback.print_exc()
            continue


    s.close()

if __name__ == "__main__":
    main()
