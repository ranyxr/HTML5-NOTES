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


'''
# insert on doc
result = coll.insert_one({"name":"wangqi", "age": 22, "gender": "male"})
print "insert_one ok!"
print result
print result.inserted_id
'''


'''
#insert many docs
result = coll.insert_many([{"name":"wangba", "age": 2, "gender": "female"},
    {"name":"wangjiu", "age": 3, "gender": "male"}])
print "insert_many ok!"
print result.inserted_ids
'''




'''
# update one doc
# $set, $inc, $push, $pushAll =====>   "$set"
#result = coll.update_one({"name": "wangba"}, {"$inc": {"age": 10}})
#result = coll.update_one({"name": "wangba"}, {"$set": {"gender": "male"}})

result = coll.update_one({"name": "lisi"}, {"$pushAll": {"hobby":["read", "write"]}})
print result.matched_count
print result.modified_count
print "update_one ok"
'''


'''
#update_many  docs
result = coll.update_many({"name": "wangba"}, {"$inc": {"age": 10}})
print result.matched_count
print result.modified_count
print "update_many ok"
'''

'''

# find doc
#cursor = coll.find({})
#cursor = coll.find({"age": {"$gt": 20}})

# and condition
#cursor = coll.find({"name":"wangba", "age": {"$gt": 30}})

#or 
#cursor = coll.find({"$or":[{"name":"lisi"},{"age":{"gt": 40}}]})

# and, or
#cursor = coll.find({"gender": "female", "$or":[{"name":"lisi"},{"age":{"gt": 40}}]})


#sort 
#cursor = coll.find({"name":"wangba", "age": {"$gt": 30}}).sort("age",
#        pymongo.DESCENDING)

#cursor = coll.find({"name":"wangba", "age": {"$gt": 30}}).sort([
#    ("age", pymongo.ASCENDING),("name", pymongo.DESCENDING)])

#limit number
#cursor = coll.find({"name":"wangba", "age": {"$gt": 30}}).limit(2)

#count number
cursor = coll.find({"name":"wangba", "age": {"$gt": 30}}).count()
print cursor

'''


'''
#delete_one
result = coll.delete_one({"name": "wangba"})
print result.deleted_count
print "delete_one ok"
'''


#delete_many 
result = coll.delete_many({"name": "wangba"})
print result.deleted_count
print "delete_many ok"





# close connect
client.close()

