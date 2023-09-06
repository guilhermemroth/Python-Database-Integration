import pymongo as pym
import datetime
import pprint

bank = pym.MongoClient("mongodb+srv://guilhermemroth:BtnBHsHjrSOenfgi@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

db = bank.accounts
collection = db.test_collection

post = {
    "name": "joaquim",
    "full_name": "Joaquim Maria Machado de Assis",
    "CPF": "123456789",
    "address": "Rio de Janeiro",
    "account": "Savings Account",
    "number": 1234,
    "saldo": 123.45
}

# preparing to submit the info
clients = db.clients
post_id = clients.insert_one(post).inserted_id
print(post_id)

print('\n')
pprint.pprint(db.clients.find_one())
print('\n')