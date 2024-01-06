from sqlalchemy import create_engine, Column, Integer, Float, BigInteger, Boolean, String, TIMESTAMP, ForeignKey
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

class Futures(Base):
    __tablename__ = 'all_futures'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    exchange = Column(String, unique=True)
    symbol_on_exchange = Column(String, unique=True)
    base_asset = Column(String)
    quote_asset = Column(String)
    expire_at = Column(BigInteger)
    has_buy_sell_data = Column(Boolean)
    is_perpetual = Column(Boolean)
    margined = Column(String)
    oi_lq_vol_denominated_in = Column(String)
    has_long_short_ratio_data = Column(Boolean)
    has_ohlcv_data = Column(Boolean)
    
class Symbol(Base):
    __tablename__ = 'gateio_future'
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))

class GateioOI(Base):
    __tablename__ = 'gateio_oi'
    time = Column(TIMESTAMP, nullable=False)
    symbol_id = Column(Integer, ForeignKey('gateio_future.id'), primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    value = Column(Float, nullable=False)
    update = Column(BigInteger, primary_key=True)

class GateioPrice(Base):
    __tablename__ = 'gateio_price'
    time = Column(TIMESTAMP, nullable=False)
    symbol_id = Column(Integer, ForeignKey('gateio_future.id'), primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    value = Column(Float, nullable=False)
    update = Column(BigInteger, primary_key=True)

class GateioDelta(Base):
    __tablename__ = 'gateio_delta'
    time = Column(TIMESTAMP, nullable=False)
    symbol_id = Column(Integer, ForeignKey('gateio_future.id'), primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    value = Column(Float, nullable=False)
    update = Column(BigInteger, primary_key=True)

if __name__ == '__main__':
    # Example usage
    engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{database_name}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating and adding a new record
    record = Exchange(code='a', name='alpaca')
    session.add(record)
    session.commit()

    # Querying the record
    queried_record = session.query(Exchange).first()
    print(queried_record.code)
