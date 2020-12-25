import pymongo
from pymongo import MongoClient

# install robomongo or robo3T for Graphical User Interface of MongoDB

myClient = MongoClient()
#client = MongoClient("localhost", 27017)             *Alternate CODE in comments*
#client = MongoClient("mongodb://localhost:27017/")
db = myClient.mydb
#db = myClient["my-database"]

users = db.users
user1 = {"username":"abhishek","password":"123456789","fav_number":2,"hobbies":["python","games","pizza"]}
user_id = users.insert_one(user1).inserted_id
user2 = {"username":"siddharth","password":"123456789","fav_number":2,"hobbies":["python","games","pizza"]}
user_id = users.insert_one(user2).inserted_id