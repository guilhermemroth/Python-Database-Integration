import pymongo as pym
import datetime
import pprint

bank = pym.MongoClient("mongodb+srv://guilhermemroth:BtnBHsHjrSOenfgi@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

db = bank.accounts
clients = db.clients


print("Returning all the clients\n")
for post in clients.find():
    pprint.pprint(post)
    print("\n")

print("Returning the count of items:\n")
print(clients.count_documents({}))
print("\n")
print(clients.count_documents({"name": "fiodor"}))
print("\n")
print(clients.count_documents({"name": "dante"}))
print("\n")

print("Returning formated\n")
pprint.pprint(clients.find_one({"address": "Rio de Janeiro"}))

print("\nReturning sorted:\n")
for post in clients.find({}).sort("balance"):
    pprint.pprint(post)
    print("\n")