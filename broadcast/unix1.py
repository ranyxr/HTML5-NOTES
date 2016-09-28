#!/usr/bin/python

import socket
import sys
import os

server_address = './test'

#首先确保这个文件不能存在，只是用于本地套接字的通信，如果已经存在则不可以了
try:
    os.unlink(server_address)  # 用于删除一个文件
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

print >>sys.stderr,'starting up on %s'%server_address
sock.bind(server_address)
sock.listen(5)

while True:
    print >>sys.stderr,'waiting for a connection'
    connection,client_address = sock.accept()
    try:
        print >>sys.stderr,'connection from',client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr,'received "%s"'%data
            if data:
                print >>sys.stderr,'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr,'no data from',client_address
                break
    finally:
        connection.close()
