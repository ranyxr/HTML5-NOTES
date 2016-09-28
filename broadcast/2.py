#!/usr/bin/python
#coding=utf-8

from twisted.internet import protocol,reactor
from time import ctime

PORT = 8888

class TSservProtocol(protocol.Protocol):
    def connectionMade(self):                  #重写原来类中的函数在有客户端时被调用
        clnt = self.clnt = self.transport.getPeer().host
        print "...connected from:",clnt
    def dataReceived(self,data):               #与客户端进行网络数据传输时被调用
        self.transport.write('[%s] %s'%(ctime(),data))

factory = protocol.Factory()     #创建protocol工长，每次链接进来产生一个对象
factory.protocol = TSservProtocol # 声明调用执行的类

print "waiting for connection..."
reactor.listenTCP(PORT,factory)  # 进行监听，有客户端链接后创建一个TSserv对象来处理
reactor.run()