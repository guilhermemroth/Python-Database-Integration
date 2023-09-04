import pymongo as pym
import datetime
import pprint

cliente = pym.MongoClient("mongodb+srv://guilhermemroth:BtnBHsHjrSOenfgi@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

# creating the db
db = cliente.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "Mike"}))
print(posts.count_documents({"tags": "insert"}))
pprint.pprint(posts.find_one({"tags": "insert"}))