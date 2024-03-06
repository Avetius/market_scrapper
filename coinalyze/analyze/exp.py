from sqlalchemy import create_engine, insert, Column, Integer, Float, BigInteger, Boolean, String, TIMESTAMP, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import insert
from db import create_timescaledb_database
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql import func
from datetime import datetime
from dotenv import load_dotenv
import matplotlib.pyplot as plt
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


def update_to_datetime(arr_of_ms = [1705050113170, 1705050113185]):
    # Convert milliseconds to seconds
    arr_of_ts = []
    for ms in arr_of_ms:        
        timestamp_in_seconds = ms / 1000
        # Convert to a datetime object
        datetime_object = datetime.utcfromtimestamp(timestamp_in_seconds)
        # Format the datetime object as a string
        formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
        # print(formatted_time)
        arr_of_ts.append(formatted_time)

    return arr_of_ts


engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{database_name}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Example usage
if __name__ == '__main__':
    session = Session()

    # Query the data from the gateio_oi table
    query = session.query(GateioOI.update, GateioOI.value).filter(GateioOI.symbol == 'ASTRA_USDT.Y').order_by(GateioOI.update)
    result = query.all()

    print(f"result >>> {len(result)}")
    # Close the session
    session.close()

    # Unpack the result into separate lists for timestamps and values
    update, values = zip(*result)
    upd = update_to_datetime(update)

    # Plot the graph using matplotlib
    plt.plot(upd, values, label='GateioOI Data')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('GateioOI Data Plot')
    plt.legend()
    plt.show()
