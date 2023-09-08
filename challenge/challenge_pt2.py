import pymongo as pym
import datetime
import pprint

bank = pym.MongoClient("mongodb+srv://guilhermemroth:<password>@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

db = bank.accounts
collection = db.collection

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

# bulk inserts
new_posts = [{"name": "fiodor",
            "full_name": "Fiódor Mikhailovitch Dostoiévski",
            "CPF": "135798642",
            "address": "Moscou",
            "account": "Savings Account",
            "number": 1342,
            "balance": 643.32},

            {"name": "fiodor",
            "full_name": "Fiódor Mikhailovitch Dostoiévski",
            "CPF": "135798642",
            "address": "Moscou",
            "account": "Savings Account",
            "number": 6853,
            "balance": 0},

            {"name": "gabriel",
            "full_name": "Gabriel José García Márquez",
            "CPF": "246897531",
            "address": "Aracataca",
            "account": "Checking Account",
            "number": 1423,
            "balance": 0},

            {"name": "alexandre",
            "full_name": "Alexandre Dumas",
            "CPF": "975312468",
            "address": "Villers-Cotterêts",
            "account": "Savings Account",
            "number": 1243,
            "balance": 8},

            {"name": "alexandre",
            "full_name": "Alexandre Dumas",
            "CPF": "975312468",
            "address": "Villers-Cotterêts",         
            "account": "Checking Account",
            "number": 7539,
            "balance": 6373.98},

            {"name": "yasunari",
            "full_name": "Yasunari Kawabata",
            "CPF": "864213579",
            "address": "Osaka",
            "number": 1324,
            "balance": 98763.43},

            {"name": "james",
            "full_name": "James Augustine Aloysius Joyce",
            "CPF": "098765432",
            "address": "Rathgar",
            "account": "Checking Account",
            "number": 2431},

            {"name": "dante",
            "full_name": "Dante Alighieri",
            "CPF": "234567890",
            "address": "Florença",
            "account": "Savings Account",
            "number": 4567,
            "balance": 0.56},

            {"name": "dante",
            "full_name": "Dante Alighieri",
            "CPF": "234567890",
            "address": "Florença",
            "account": "Checking Account",
            "number": 2413},

            {"name": "dante",
            "full_name": "Dante Alighieri",
            "CPF": "234567890",
            "address": "Florença",
            "account": "Checking Account",
            "number": 7490,
            "balance": 98},

            {"name": "franz",
            "full_name": "Franz Kafka",
            "CPF": "086315234",
            "address": "Praga",
            "account": "Checking Account",
            "number": 4231,
            "balance": 45.05},

            {"name": "william",
            "full_name": "William Gerald Golding",
            "CPF": "639252047",
            "address": "Newquay",
            "account": "Checking Account",
            "number": 3412,
            "balance": 124324.54},

            {"name": "william",
            "full_name": "William Gerald Golding",
            "CPF": "639252047",
            "address": "Newquay",
            "account": "Savings Account",
            "number": 9373,
            "balance": 0}]

result = clients.insert_many(new_posts)
print(result.inserted_ids)
