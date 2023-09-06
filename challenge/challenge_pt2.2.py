import pymongo as pym
import datetime
import pprint

bank = pym.MongoClient("mongodb+srv://guilhermemroth:BtnBHsHjrSOenfgi@cluster0.lhpu10f.mongodb.net/?retryWrites=true&w=majority")

db = bank.accounts
collection = db.test_collection