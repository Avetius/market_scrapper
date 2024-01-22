from sqlalchemy import create_engine, insert, Column, Integer, Float, BigInteger, Boolean, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import insert
from db import create_timescaledb_database
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import func
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv("POSTGRES_HOST")
user = os.getenv("POSTGRES_USER")
database_name = os.getenv("POSTGRES_DB")
password = os.getenv("POSTGRES_PASSWORD")

create_timescaledb_database(database_name, user, password, host)
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
    exchange = Column(String)
    symbol_on_exchange = Column(String)
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
    exchange_code = Column(String, ForeignKey('exchange.code'))

class GateioOI(Base):
    __tablename__ = 'gateio_oi'
    time = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    symbol = Column(String, ForeignKey('gateio_future.symbol'), primary_key=True)
    value = Column(Float, nullable=False)
    update = Column(BigInteger, primary_key=True)

class GateioPrice(Base):
    __tablename__ = 'gateio_price'
    time = Column(TIMESTAMP, nullable=False)
    symbol = Column(String, ForeignKey('gateio_future.symbol'), primary_key=True)
    value = Column(Float, nullable=False)
    update = Column(BigInteger, primary_key=True)

class GateioDelta(Base):
    __tablename__ = 'gateio_delta'
    time = Column(TIMESTAMP, nullable=False)
    symbol_name = Column(String, ForeignKey('gateio_future.symbol'), primary_key=True)
    value = Column(Float, nullable=False)
    update = Column(BigInteger, primary_key=True)


engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{database_name}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Example usage
if __name__ == '__main__':
    session = Session()
    insert_stmt = insert(Exchange).values(
        code='a',
        name='alpaca'
    )

    # Execute the statement
    session.execute(insert_stmt)
    session.commit()
    # Creating and adding a new record
    # record = Exchange(code='a', name='alpaca')
    # session.add(record)
    # session.commit()

    # Querying the record
    queried_record = session.query(Exchange).first()
    print(queried_record.code)

