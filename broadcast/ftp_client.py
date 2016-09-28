#!/usr/bin/python
#coding=utf-8

from socket import *
from time import ctime,sleep
import sys
import os

class FtpClient:

    BUFSIZE = 1024
    def __init__(self,serveraddr):
        self.serveraddr = serveraddr

    def do_list(self):
        data = "L"
        sockfd = socket(AF_INET,SOCK_STREAM,0)
        sockfd.connect(self.serveraddr)

        sockfd.send(data)
        data = sockfd.recv(self.BUFSIZE)

        if data[0:2] == "OK":
            while True:
                data = sockfd.recv(self.BUFSIZE)
                if not data:
                    break
                print("%s"%data)
        else:
            print("list error!")
            sockfd.close()
            return
        
        print("list OK!")
        return

    def do_get(self,filename):
        fd = open(filename,'wb')
        data = "G " + filename

        sockfd = socket(AF_INET,SOCK_STREAM,0)
        sockfd.connect(self.serveraddr)
        sockfd.send(data)
        data = sockfd.recv(self.BUFSIZE)

        if data[0:2] == "OK":
            while True:
                data = sockfd.recv(self.BUFSIZE)
                if not data:
                    break
                fd.write(data)
        else:
            print("get %s fail!"%filename)
            sockfd.close()
            fd.close()
            return
        
        print("get %s OK!"%filename)
        sockfd.close()
        fd.close()
        return      

    def do_put(self,filename):
        fd = open(filename,'rb')
        data = "P " + filename

        sockfd = socket(AF_INET,SOCK_STREAM,0)
        sockfd.connect(self.serveraddr)

        sockfd.send(data)
        data = sockfd.recv(self.BUFSIZE)

        if data[0:2] == "OK":
            while True:
                data = fd.readline()
                if not data:
                    break
                data = sockfd.send(data)
                sleep(0.1)
            fd.close()
        else:
            print("put %s fail!"%filename)
            sockfd.close()
            fd.close()
            return
        
        print("put %s OK!"%filename)
        sockfd.close()
        fd.close()
        return      
        

def main():
    if len(sys.argv) < 3:
        print "Input valid arg"
        sys.exit(0)
   
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    ftp = FtpClient(ADDR)
    
    while True:
        print("----------command-------------------")
        print("-----------list---------------------")
        print("-----------get filename-------------")
        print("-----------put filename-------------")
        print("------------quit--------------------")
        print("Input command >>")

        data = raw_input()

        if data[0] == 'l':
            ftp.do_list()
        elif data[0] == 'g':
            ftp.do_get(data[4:])
        elif data[0] == 'p':
            ftp.do_put(data[4:])
        elif data[0] == 'q':
            sys.exit(0)
        else:
            continue
    
    sys.exit(0)

if __name__ == '__main__':
    main()

        
