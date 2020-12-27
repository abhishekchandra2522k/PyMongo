import pymongo
from pymongo import MongoClient

# install robomongo or robo3T for Graphical User Interface of MongoDB

myClient = MongoClient()
#client = MongoClient("localhost", 27017)             *Alternate CODE in comments*
#client = MongoClient("mongodb://localhost:27017/")
db = myClient.mydb
#db = myClient["my-database"]

users = [{"username":"first", "password":"secure"}, {"username":"abhishek","password":"verysecure"}]

Users = db.users

inserted = Users.insert_many(users)

print(inserted.inserted_ids)