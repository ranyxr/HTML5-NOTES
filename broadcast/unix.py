#!/usr/bin/python

import socket
import sys

sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
server_address = './test'  #本地套接字通讯是设置的不是IP而是一个文件

print >>sys.stderr,'connection to %s'%server_address

try:
    sock.connect(server_address)
except socket.error,msg:
    print >>sys.stderr,msg
    sys.exit(1)

try:
    message = 'This is the message.It will be repeated'
    print >>sys.stderr,'sending "%s"'%message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr,'received "%s"'%data
finally:
    print >>sys.stderr,'closing socket'
    sock.close()