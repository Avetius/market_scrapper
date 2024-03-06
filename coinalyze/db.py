import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("POSTGRES_HOST")
database_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

print(f"host >>> {host}")
print(f"database_name >>> {database_name}")
print(f"user >>> {user}")
print(f"password >>> {password}")

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
    conn.close()

    conn = psycopg2.connect(dbname=database_name, user=user, password=password, host=host)
    conn.autocommit = True  # Ensures that the queries will be executed immediately

    conn.close()


if __name__ == '__main__':
    # Example usage
    create_timescaledb_database(database_name, user, password, host)