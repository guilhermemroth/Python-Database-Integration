#importando aa bibliotecas e funções
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__():
        return f"User(id={self.id}, name={self.name}, full_name={self.full_name})"

class Address(Base):
    __tablename__ = "address"
    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__():
        return f"Address(id={self.id}, email_address={self.email_address})"
    

# print(User.__tablename__)
# print(Address.__table__)


# conexão com banco de dados

engine = create_engine("sqlite://")

# criando as classes como tabela no BD
Base.metadata.create_all(engine)

# investigando o esquema do BD
insp = inspect(engine)
print(insp.get_table_names())
print(insp.default_schema_name)


with Session(engine) as session:
    guilherme = User(
        name='guilherme',
        full_name='Guilherme Roth',
        address=[Address(email_address='guilhermerth@hotmail.com')]
    )

    fiodor = User(
        name='fiódor',
        full_name='Fiódor Dostoiévsky',
        address=[Address(email_address='fiodor_dost@karamazov.com'),
                 Address(email_address='fdostoievsky@raskólnikov.com')]
    )

    machado = User(
        name='machado',
        full_name='Joaquim Maria Machado de Assis'
        )
    
    # enviando para o BD (persistência de dados)
    session.add_all([guilherme, fiodor, machado])
    
    session.commit()
