#! /usr/bin/python
#coding:utf-8

import pymongo

host = "192.168.1.247"
port = 27017

# connect mongod
client = pymongo.MongoClient(host,port)
print "connect datebase ok!"
#connect db
db = client.stu
print "connect stu ok!"
#create or use collection
coll = db.first
print "connect collection ok!"

#create one index
index_name = coll.create_index([("name",pymongo.ASCENDING),("age",pymongo.DESCENDING)])
print index_name
print "create index ok!"

#drop one index
coll.drop_index(index_name)
print "drop index ok!"
client.close()
