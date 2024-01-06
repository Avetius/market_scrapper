import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("POSTGRES_HOST")
database_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

# print(f"host >>> {host}")
# print(f"database_name >>> {database_name}")
# print(f"user >>> {user}")
# print(f"password >>> {password}")

def create_timescaledb_database(database_name, user, password, host):
    # Connect to the default database (usually 'postgres')
    conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host)
    conn.autocommit = True  # Ensures that the queries will be executed immediately

    with conn.cursor() as cursor:
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

    with conn.cursor() as cursor:
        # Create the exchange table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS exchange (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                code VARCHAR NOT NULL
            );
        """)
        # Convert the exchange table to a hypertable, if not already a hypertable
        # cursor.execute("SELECT create_hypertable('exchange', 'code') ON CONFLICT DO NOTHING;")

        # Create the future table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS future (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR NOT NULL,
                exchange VARCHAR NOT NULL,
                symbol_on_exchange VARCHAR NOT NULL,
                base_asset VARCHAR NOT NULL,
                quote_asset VARCHAR NOT NULL,
                expire_at BIGINT,
                has_buy_sell_data BOOLEAN NOT NULL,
                is_perpetual BOOLEAN NOT NULL,
                margined VARCHAR NOT NULL,
                oi_lq_vol_denominated_in VARCHAR NOT NULL,
                has_long_short_ratio_data BOOLEAN NOT NULL,
                has_ohlcv_data BOOLEAN NOT NULL
            );
        """)

        # Convert the future table to a hypertable, if not already a hypertable
        # cursor.execute("SELECT create_hypertable('future', 'exchange') ON CONFLICT DO NOTHING;")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS all_futures (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR NOT NULL,
                exchange VARCHAR NOT NULL,
                symbol_on_exchange VARCHAR NOT NULL,
                base_asset VARCHAR NOT NULL,
                quote_asset VARCHAR NOT NULL,
                expire_at BIGINT,
                has_buy_sell_data BOOLEAN NOT NULL,
                is_perpetual BOOLEAN NOT NULL,
                margined VARCHAR NOT NULL,
                oi_lq_vol_denominated_in VARCHAR NOT NULL,
                has_long_short_ratio_data BOOLEAN NOT NULL,
                has_ohlcv_data BOOLEAN NOT NULL
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateio_future (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR NOT NULL,
                exchange_id INTEGER REFERENCES gateio_future(id)
            );
        """)

        # Convert the future table to a hypertable, if not already a hypertable
        # cursor.execute("SELECT create_hypertable('gateio_future', 'exchange_id')") #  ON CONFLICT DO NOTHING;

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateio_oi (
                id SERIAL PRIMARY KEY,
                symbol_id INTEGER REFERENCES gateio_future(id),
                symbol VARCHAR NOT NULL,
                value FLOAT NOT NULL,
                update BIGINT NOT NULL
            );
        """)

        # Convert the future table to a hypertable, if not already a hypertable
        cursor.execute("SELECT create_hypertable('gateio_oi', 'update')")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateio_price (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR NOT NULL,
                value FLOAT NOT NULL,
                update BIGINT NOT NULL
            );
        """)

        # Convert the future table to a hypertable, if not already a hypertable
        cursor.execute("SELECT create_hypertable('gateio_price', 'update')")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gateio_delta (
                id SERIAL PRIMARY KEY,
                symbol_id INTEGER REFERENCES gateio_future(id),
                symbol VARCHAR NOT NULL,
                value FLOAT NOT NULL,
                update BIGINT NOT NULL
            );
        """)

        # Convert the future table to a hypertable, if not already a hypertable
        cursor.execute("SELECT create_hypertable('gateio_delta', 'update')")

    conn.close()



if __name__ == '__main__':
    # Example usage
    create_timescaledb_database(database_name, user, password, host)