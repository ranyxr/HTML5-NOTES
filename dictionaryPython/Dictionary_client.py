#!/usr/bin/python
# coding = utf-8
#online dictionary system

import MySQLdb
import sys
import threading
import os,traceback
from socket import *
from threading import *
from time import sleep

def register(s):
    print ''
    print 'register'
    print ''
    name = raw_input('your name >> ')
    s.send(name)
    password = raw_input('your password >> ')
    s.send(password)
    data = s.recv(1024)
    print data


def login(s):

    print ''
    print 'login'
    print ''
    name = raw_input('your name >> ')
    s.send(name)
    # sleep(0.1)
    password = raw_input('your password >> ')
    s.send(password)
    data = s.recv(1024)
    print data
    if data == 'login successfully':
        user(s,name)

def user(s,name):
    while True:
        print '''

        Welcome,
        1.query 2.history 3.quit

        '''
        num = raw_input('>>')

        if num not in ['1','2','3']:
            print ('input error, you should press 1 or 2 or 3')
            sys.stdin.flush()
            continue
        elif num == '1':
            s.send(num)
            q = raw_input('word: ')
            s.send(q)
            content = s.recv(1024)
            print content

        elif num == '2':
            s.send(num)
            content = s.recv(1024)
            print content
            print ''
            history = s.recv(1024)
            print history

        else:

            print 'goodbye'
            return




def main():
    db = MySQLdb.connect('localhost','root','yxr.1995','Dict')
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('192.168.1.246', 6333))

    while True:
        print '''

        Welcome to online dictionary

        1.register  2.login   3.quit

        '''
        num = raw_input('>>')

        if num not in ['1','2','3']:
            print ('input error, you should press 1 or 2 or 3')
            sys.stdin.flush()
            continue
        elif num == '1':
            sock.send(num)

            register(sock)

        elif num == '2':
            sock.send(num)
            login(sock)
        else:
            db.close()
            print 'goodbye'
            return


if __name__ == "__main__":
    main()
