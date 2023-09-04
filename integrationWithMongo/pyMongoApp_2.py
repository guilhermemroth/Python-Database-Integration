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

print("\nRetrieving post collection info in an orderly manner")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pym.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {"user_id": 211, "name": "Luke"},
    {"user_id": 212, "name": "Padme"}
]

res = db.profile_user.insert_many(user_profile_user)

collections = db.list_collection_names()

print('\nCollections stored in mongodb')
for collection in collections:
    print(collection)
