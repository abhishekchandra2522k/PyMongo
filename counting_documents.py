import pymongo
from pymongo import MongoClient

myClient = MongoClient()

db = myClient.mydb

Users = db.users

# new syntax to get count with filter
print(Users.count_documents(filter={}))

# old version to get count with find()
# print(Users.find({"username":"abhishek"}).count())