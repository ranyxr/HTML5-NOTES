#! /usr/bin/python
#coding=utf-8

from socket import *
import MySQLdb
from threading import *
import multiprocessing
from time import sleep

HOST = '192.168.1.247'
PORT = 5857
ADDR = (HOST,PORT)

def register(s,username,password):
    if username:
        s.send(username)
        sleep(0.1)
        if password:
            s.send(password)
        else:
            return
    else:
        return
    data = s.recv(1024)
    print data
    return

def login(s,username,password):
    if username:
        s.send(username)
        sleep(0.1)
        if password:
            s.send(password)
        else:
            return
    else:
        return
    data = s.recv(1024)
    return data

def select(s,word):
    s.send(word)
    data1 = s.recv(1024)
    print data1
    return

def history(s):
    for i in range(3):
        data1 = s.recv(1024)
        print data1+'   ',
    print ""
    num = s.recv(1024)
    for i in range(int(num)):
        data2 = s.recv(1024)
        print data2
    return

def main(s):
    s.connect(ADDR)
    while True:
        print "---1.register---"
        print "---2.login------"
        print "---3.quit-------"
        operate = raw_input("输入操作对应的数字：")
        if operate == '1':
            s.send(operate)
            username = raw_input("输入用户名：")
            password = raw_input("输入密码：")
            register(s,username,password)
        if operate == '2':
            s.send(operate)
            username = raw_input("输入用户名：")
            password = raw_input("输入密码：")
            data = login(s,username,password)
            if data == 'ok':
                while True:
                    print "---1.select---"
                    print "---2.history---"
                    print "---3.quit---"
                    op = raw_input("输入对应操作的数字：")
                    if op == '1':
                        s.send(op)
                        word = raw_input("输入要查询的单词：")
                        select(s,word)
                    if op == '2':
                        s.send(op)
                        print op
                        history(s)
                    if op == '3':
                        break
            else:
                print "登陆失败！"
                continue
        if operate == '3':
            break




if __name__ == '__main__':

    s = socket()
    main(s)
