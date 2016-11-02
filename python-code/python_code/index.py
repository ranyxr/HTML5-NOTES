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


## create_index
#index_name = coll.create_index("name")
index_name = coll.create_index([("name", pymongo.ASCENDING), ("age",
    pymongo.DESCENDING)])

print index_name
print "create_index ok!"


## drop_index
#coll.drop_index(index_name)
coll.drop_index([("name", pymongo.ASCENDING),("age", pymongo.DESCENDING)])

print "drop_index ok!"





client.close()
