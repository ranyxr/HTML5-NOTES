#! /usr/bin/python
#coding: utf-8

import pymongo

host = "127.0.0.1"
port = 27017

# connect mongod
client = pymongo.MongoClient(host, port);

#connect db
db = client.stu
print "connect stu ok!"

# create or use collection
coll = db.firstClass
print "connect firstClass  ok!"


##aggregate 
#cursor = coll.aggregate([{"$group": {"_id": "$name", "count": {"$sum":1}}}])
#cursor = coll.aggregate([{"$group": {"_id": "$name", "count": {"$sum":"$age"}}}])
#cursor = coll.aggregate([{"$group": {"_id": "$name", "count": {"$avg":"$age"}}}])

#cursor = coll.aggregate([{"$match":{"age": {"$gt": 20}} }, {"$group": {"_id": "$name", "count": {"$avg":"$age"}}}])

cursor = coll.aggregate([{"$match":{"age": {"$gte": 10}} }, { "$sort": {"age": -1}}])

print cursor
for ret in cursor:
    print ret


client.close()
