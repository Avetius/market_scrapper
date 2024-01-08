from sqlalchemy import create_engine, Column, Integer, Float, BigInteger, Boolean, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2 import sql
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


conn2pg = psycopg2.connect(dbname='postgres', user=user, password=password, host=host)
conn2pg.autocommit = True  # Ensures that the queries will be executed immediately

with conn2pg.cursor() as cursor:
    # Check if the database exists
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), (database_name,))
    if cursor.fetchone() is None:
        print(f"No database {database_name} found")
        # Create a new database
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))

        # Connect to the new database to enable the TimescaleDB extension
        new_db_conn = psycopg2.connect(dbname=database_name, user=user, password=password, host=host)
        new_db_conn.autocommit = True
        with new_db_conn.cursor() as new_db_cursor:
            # Enable TimescaleDB extension
            new_db_cursor.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")
        new_db_conn.close()
conn2pg.close()

conn2cnlz = psycopg2.connect(dbname=database_name, user=user, password=password, host=host)
conn2cnlz.autocommit = True  # Ensures that the queries will be executed immediately

with conn2cnlz.cursor() as cursor:
    cursor.execute("SELECT create_hypertable('gateio_oi', 'update');") # , if_not_exists => TRUE, create_default_indexes => TRUE
    cursor.execute("SELECT create_hypertable('gateio_price', 'update');") # , if_not_exists => TRUE, create_default_indexes => TRUE
    cursor.execute("SELECT create_hypertable('gateio_delta', 'update');") # , if_not_exists => TRUE, create_default_indexes => TRUE


engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{database_name}")
Base.metadata.create_all(engine)

# # Connect to the database and create the TimescaleDB extension
# with engine.connect() as conn:
#     # CREATE EXTENSION IF NOT EXISTS timescaledb
#     # conn.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")
#     # CREATE HYPERTABLES
#     conn.execute("SELECT create_hypertable('gateio_oi', 'update');")
#     conn.execute("SELECT create_hypertable('gateio_price', 'update');")
#     conn.execute("SELECT create_hypertable('gateio_delta', 'update');")


Session = sessionmaker(bind=engine)
session = Session()


# Example usage
if __name__ == '__main__':
    # Creating and adding a new record
    record = Exchange(code='a', name='alpaca')
    session.add(record)
    session.commit()

    # Querying the record
    queried_record = session.query(Exchange).first()
    print(queried_record.code)

