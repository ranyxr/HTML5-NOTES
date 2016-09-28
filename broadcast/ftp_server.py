#!/usr/bin/python
#coding=utf-8

from socket import *
from time import sleep
import sys
import os

class FtpServer:

    BUFSIZE = 1024
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        filelist = os.listdir('.')

        if filelist == None:
            self.sockfd.send('FAIL')
            return
        self.sockfd.send('OK')

        for filename in filelist:
            if filename[0] != '.' and os.path.isfile(filename):
                self.sockfd.send(filename)
            sleep(0.1)
        print("list OK!")
        return


    def do_get(self,filename):
        try:
            fd = open(filename,'rb')
        except:
            self.sockfd.send('FAIL')
        
        self.sockfd.send('OK')

        while True:
            data = fd.readline()
            if not data:
                break
            self.sockfd.send(data)
            sleep(0.1)
        fd.close()
        print("get OK!")
        return
        

    def do_put(self,filename):
        try:
            fd = open(filename,'wb')
        except:
            self.sockfd.send('FAIL')
        
        self.sockfd.send('OK')

        while True:
            data = self.sockfd.recv(self.BUFSIZE)
            if not data:
                break
            fd.write(data)
        fd.close()
        print("put OK!")
        return
        

def main():
    if len(sys.argv) < 3:
            print ("Input valid arg")
            sys.exit(0)

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    BUFSIZE = 1024
    ADDR = (HOST,PORT)

    sockfd = socket(AF_INET,SOCK_STREAM,0)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    while True:
        connfd,addr = sockfd.accept()
        print("Connected from:",addr)

        data = connfd.recv(BUFSIZE)

        ftp = FtpServer(connfd)

        print(">>>>>",data)

        if data[0] == 'L':
            ftp.do_list()

        if data[0] == 'G':
            ftp.do_get(data[2:])

        if data[0] == 'P':
            ftp.do_put(data[2:])

        connfd.close()

    sys.exit(0)

if __name__ == '__main__':
    main()