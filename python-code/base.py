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
#insert one doc
# result = coll.insert_one({"name":"zhaoliu","age":20,"gender":"male"})
# print result
# print result.inserted_id

#insert many docs
# result = coll.insert_many([{"name":"zhang1","age":12,"gender":"female"},{"name":"zhang2","age":13}])
# print "insert many docs ok!"
# print result
# print result.inserted_ids

#update one doc
# result = coll.update_one({"name":"zhang1"},{"$inc":{"age":5}})
# result = coll.update_one({"name":"zhang1"},{"$set":{"gender":"male"}})
# print result.matched_count
# print result.modified_count
# print "update one doc ok!"

#update many docs
# result = coll.update_many({"name":"zhang1"},{"$inc":{"age":5}})
# print result.matched_count
# print result.modified_count
# print "update many docs ok!"

#find doc
# cursor = coll.find({})
# cursor = coll.find({"age":{"$gt":20}})

#and
# cursor = coll.find({"name":"zhang1","age":{"$lt":20}})

#or
# cursor = coll.find({"$or":[{"name":"zhang1"},{"age":13}]})

#sort
# cursor = coll.find({}).sort("age",pymongo.ASCENDING)
# cursor = coll.find({}).sort("age",pymongo.DESCENDING)
# cursor = coll.find({}).sort([("name",pymongo.ASCENDING),("age",pymongo.DESCENDING)])

#limit
# cursor = coll.find({}).limit(2)
# print cursor
# for ret in cursor:
#     print ret

#count
# cursor = coll.find({}).count()
# print cursor

#delete one doc
# result = coll.delete_one({"name":"zhang1"})
# print result.deleted_count
# print "delete one doc ok!"

#delete many docs
result = coll.delete_many({"name":"zhang2"})
print result.deleted_count
print "delete many docs ok!"
