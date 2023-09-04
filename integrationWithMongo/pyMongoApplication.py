import pymongo as pym
import datetime
import pprint

cliente = pym.MongoClient("mongodb+srv://guilhermemroth:BtnBHsHjrSOenfgi@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

# creating the db
db = cliente.test
collection = db.test_collection

# definition of the info that makes up the doc
post = {
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparing to submit the info
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# print(f"\n{db.posts.find_one()}\n")

print('\n')
pprint.pprint(db.posts.find_one())
print('\n')

# bulk inserts
new_posts = [{
    "author": "Mike",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()
},
             {
    "author": "Joao",
    "text": "Post from Joao. New post available",
    "title": "Mongo is fun",
    "date": datetime.datetime(2009, 7, 13, 12, 54, 34)
             }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print('\n')
pprint.pprint(db.posts.find_one({"author": "Joao"}))
print('\n')

print('\n Documents in the collection posts')
for post in posts.find():
    pprint.pprint(post)
    print('\n')
    