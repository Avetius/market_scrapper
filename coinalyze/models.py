from sqlalchemy import create_engine, Column, Integer, Float, BigInteger, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("POSTGRES_HOST")
database_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

Base = declarative_base()

class Exchange(Base):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    code = Column(String, unique=True)

class Symbol(Base):
    __tablename__ = 'symbol'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))

class OI(Base):
    __tablename__ = 'oi'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbol.id'))
    value = Column(Float)
    update = Column(BigInteger)

class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbol.id'))
    value = Column(Float)
    update = Column(BigInteger)

class Delta(Base):
    __tablename__ = 'delta'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbol.id'))
    value = Column(Float)
    update = Column(BigInteger)


if __name__ == '__main__':
    # Example usage
    engine = create_engine(f"postgres://{user}:{password}@{host}:5432/coinalyze")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating and adding a new record
    record = MyModel(large_number=12345678901234567890)
    session.add(record)
    session.commit()

    # Querying the record
    queried_record = session.query(MyModel).first()
    print(queried_record.large_number)
