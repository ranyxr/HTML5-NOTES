#!/usr/bin/python
#coding = utf-8

import socket
import struct
import sys
from time import sleep

message = '1'
#message = '2'

multicast_group = ('224.3.329.77',10000)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.settimeout(3)

ttl = struct.pack('b',1)
sock.setsockopt(socket.IPPROTO_TP,socket.IP_MULTICAST_TTL,ttl)

try:
    while True:
        sleep(2)
        sent = sock.sendto(message,multicast_group)

        print >>sys.stderr,'waiting to receive'
        try:
            data,server = sock.recvfrom(16)
        except socket.timeout:
            print >>sys.stderr,'timed out, no more responses'
            break
        else:
            print >>sys.stderr,'received "%s" from %s'%(data,server)

finally:
    print >>sys.stderr,'closing socket'
    sock.close()
