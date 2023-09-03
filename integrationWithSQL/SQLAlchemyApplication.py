#importando aa bibliotecas e funções
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

class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
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

    def __repr__(self):
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
                 Address(email_address='fdostoievsky@raskolnikov.com')]
    )

    machado = User(
        name='machado',
        full_name='Joaquim Maria Machado de Assis'
        )
    
    # enviando para o BD (persistência de dados)
    session.add_all([guilherme, fiodor, machado])
    
    session.commit()

stmt = select(User).where(User.name.in_(["machado"]))
print('\nRecuperando dados a partir de condição de filtragem.')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando dados a partir de condição de filtragem.')
for address in session.scalars(stmt_address):
    print(address)

print(f'\n{select(User).order_by(User.full_name.desc())}')

stmt_order = select(User).order_by(User.full_name.desc())
print('\nRecuperando dados de maneira ordenada.')
for full_name in session.scalars(stmt_order):
    print(full_name)

stmt_join = select(User.full_name, Address.email_address).join_from(Address, User)
print('\nRecuperando dados a partir de condição de filtragem.')
for result in session.scalars(stmt_join):
    print(result)

# print(select(User.full_name, Address.email_address).join_from(Address, User))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nExecutando statement a partir da connection.')
for result in results:
    print(result)

# print(f"\n{select(func.count('*')).select_from(User)}")

stmt_count = select(func.count('*')).select_from(User)
print('\nRetornando o total de instâncias em User')
for count in session.scalars(stmt_count):
    print(count)
