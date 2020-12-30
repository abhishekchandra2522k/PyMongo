import datetime
import pymongo
from pymongo import MongoClient

myClient = MongoClient()

db = myClient.mydb

Users = db.users

current_date = datetime.datetime.now()

#print(current_date)

old_date = datetime.datetime(2009,12,29)

#uid = Users.insert_one({"username":"ram", "date":current_date})

# $gt : greater than,  $lt : less than, $lte : less than equal to, $ne : not equal to, $exists : True or False
print(Users.count_documents(filter={"date":{"$gt":old_date}}))

print(Users.count_documents(filter={"date" : {"$exists" : True}}))
print(Users.count_documents(filter={"username" : {"$ne" : "abhishek"}}))

db.users.create_index([("username", pymongo.ASCENDING)])