#!/usr/bin/python

import socket
import sys
import struct

multicast_group = '224.3.29.77'
server_address = ('',10000)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL',group,socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

while True:
    print >>sys.stderr,'\nwaiting to receive message'
    data,address = sock.recvfrom(1024)

    print >>sys.stderr,'received %s bytes from %s'%(data,address)
    print >>sys.stderr,'sending acknowledgement to',address
    sock.sendto('!!!!!!!!!!!!!!!!!!!!!!!!',address)


