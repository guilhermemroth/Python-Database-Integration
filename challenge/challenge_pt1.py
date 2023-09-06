import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    full_name = Column(String(50), nullable=False)
    CPF = Column(String(9), nullable=False)
    address = Column(String(50), nullable=False)

    account = relationship(
        "Account", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, full_name={self.full_name}, CPF={self.CPF}, addres={self.address})"


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(15), default="Checking Account")
    number = Column(Integer, nullable=False)
    id_client = (Column(Integer, ForeignKey("client.id"), nullable=False))

    client = relationship(
        "Client", back_populates="account"
    )

    def __repr__(self):
        return f"Account(id={self.id}, account={self.account}, number={self.number}, )"
    

#print(Account.__tablename__)
#print(Client.__tablename__)

# connecting with db
engine = create_engine("sqlite://")

# creating the classes as tables in the db
Base.metadata.create_all(engine)

# investigating DB schema
insp = inspect(engine)
print(insp.get_table_names())
print(insp.default_schema_name)

with Session(engine) as session:
    machado = Client(
        name = "joaquim",
        full_name = "Joaquim Maria Machado de Assis",
        CPF = "123456789",
        address = "Rio de Janeiro",
        account = [Account(account="Savings Account", number=1234)]
    )

    fiodor = Client(
        name = "fiodor",
        full_name = "Fiódor Dostoiévsky",
        CPF = "135798642",
        address = "Moscou",
        account = [Account(account="Savings Account", number=1342),
                   Account(account="Savings Account", number=6853)]
    )

    gabriel = Client(
        name = "gabriel",
        full_name = "Gabriel García Márquez",
        CPF = "246897531",
        address = "Aracataca",
        account = [Account(account="Checking Account", number=1423)]
    )

    alexandre = Client(
        name = "alexandre",
        full_name = "Alexandre Dumas",
        CPF = "975312468",
        address = "Villers-Cotterêts",
        account = [Account(account="Savings Account", number=1243),
                   Account(account="Checking Account", number=7539)]
    )

    yasunari = Client(
        name = "yasunari",
        full_name = "Yasunari Kawabata",
        CPF = "864213579",
        address = "Osaka",
        account = [Account(number=1324)]
    )

    james = Client(
        name = "james",
        full_name = "James Joyce",
        CPF = "098765432",
        address = "Rathgar",
        account = [Account(number=2431)]
    )

    dante = Client(
        name = "dante",
        full_name = "Dante Alighieri",
        CPF = "234567890",
        address = "Florença",
        account = [Account(number=2413),
                   Account(number=7490),
                   Account(account="Savings Account", number=4567)]
    )

    franz = Client(
        name = "franz",
        full_name = "Franz Kafka",
        CPF = "086315234",
        address = "Praga",
        account = [Account(number=4231)]
    )

    william = Client(
        name = "william",
        full_name = "William Gerald Golding",
        CPF = "639252047",
        address = "Newquay",
        account = [Account(number=3412),
                   Account(account="Savings Account", number=9373)]
    )
    

    # sending to db
    session.add_all([machado, fiodor, gabriel, alexandre, yasunari, james, dante, franz, william])

    session.commit()


stmt_acc = select(Account).where(Account.id_client.in_([2]))
print('\nReturning the account from id_client:\n')
for acc in session.scalars(stmt_acc):
    print(f"{acc}\n")


stmt_count = (select(func.max(Client.full_name)).join(Account, Client.id == Account.id_client).group_by(Client.id).having(func.count() > 1))
print('\nReturning clients with two or more accounts:\n')
for count in session.scalars(stmt_count):
    print(f"{count}\n")


connection = engine.connect()

stmt_join = select(Client.full_name, Account.account, Account.number).join_from(Account, Client)
results = connection.execute(stmt_join).fetchall()
print('\nReturning the full_name from Client table and the account and number from Account table with a join:\n')
for result in results:
    print(f"{result}\n")

