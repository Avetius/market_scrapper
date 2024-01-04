from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

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
    update = Column(DateTime)
    
class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbol.id'))
    value = Column(Float)
    update = Column(DateTime)

class Delta(Base):
    __tablename__ = 'delta'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbol.id'))
    value = Column(Float)
    update = Column(DateTime)