import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://guilhermemroth:BtnBHsHjrSOenfgi@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

db = cluster['user_data']
collection = db['mongo']

# lets see how we can insert some data

collection.insert_one({"_id":0, "user_name":"Soumi"})
collection.insert_one({"_id":100, "user_name":"Ravi"})


# lets see how we can delete posts

collection.delete_one({"_id":0, "user_name":"Soumi"})


# add mutiple posts together

post1 = {"_id":7, "user_name":"Rami"}
post2 = {"_id":43, "user_name":"Noslen"}
collection.insert_many([post1,post2])

# let's delete the remaining
collection.delete_one({"_id":100, "user_name":"Ravi"})
collection.delete_one({"_id":7, "user_name":"Rami"})
collection.delete_one({"_id":43, "user_name":"Noslen"})