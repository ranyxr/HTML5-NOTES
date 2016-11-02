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

# cursor = coll.aggregate([{"$group":{"_id":"$name","count":{"$sum":1}}}])
# cursor = coll.aggregate([{"$group":{"_id":"$name","count":{"$sum":"$age"}}}])
# cursor = coll.aggregate([{"$group":{"_id":"$name","count":{"$avg":"$age"}}}])

# cursor = coll.aggregate([{"$match":{"age":{"$gt":20}}},{"$group":{"_id":"$name","count":{"$avg":"$age"}}}])
cursor = coll.aggregate([{"$match":{"age":{"$gt":20}}},{"$sort":{"age":1}}])
print cursor
for ret in cursor:
    print ret
print "aggegate ok!"
