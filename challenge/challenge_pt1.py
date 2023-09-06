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
    account = Column(String(15), default="C/C")
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
        account = [Account(account="C/P", number=1234)]
    )

    fiodor = Client(
        name = "fiodor",
        full_name = "Fiódor Dostoiévsky",
        CPF = "135798642",
        address = "Moscou",
        account = [Account(account="C/P", number=1342),
                   Account(account="C/P", number=6853)]
    )

    gabriel = Client(
        name = "gabriel",
        full_name = "Gabriel García Márquez",
        CPF = "246897531",
        address = "Aracataca",
        account = [Account(account="C/C", number=1423)]
    )

    alexandre = Client(
        name = "alexandre",
        full_name = "Alexandre Dumas",
        CPF = "975312468",
        address = "Villers-Cotterêts",
        account = [Account(account="C/P", number=1243),
                   Account(account="C/C", number=7539)]
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
        account = [Account(number=2413)]
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
                   Account(account="C/P", number=9373)]
    )
    

    # sending to db
    session.add_all([machado, fiodor, gabriel, alexandre, yasunari, james, dante, franz, william])

    session.commit()