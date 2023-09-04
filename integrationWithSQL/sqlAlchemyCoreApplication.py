# importando as bibliotecas
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData(schema='teste')

user = Table(
    'user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(40), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
)

print('\nInfo da tabela user_prefers:')
print(user_prefs.primary_key)
print(user_prefs.constraints)

for table in metadata_obj.sorted_tables:
    print(f"\n{table}")

# metadata_obj.create_all(engine)

metadata_bd_obj = MetaData(schema='bank')

financial_info = Table(
    'financial_info', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

print('\nInfo da tabela financial_info:')
print(financial_info.primary_key)
print(financial_info.constraints)

for table in metadata_bd_obj.sorted_tables:
    print(f"\n{table}\n")
