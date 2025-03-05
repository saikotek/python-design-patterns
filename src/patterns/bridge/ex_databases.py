"""Bridge Pattern Example

Refined abstractions (Transactional, Logging) of Database for
different (Sqlite, Postgres) database implementations.

To run this example you need to have Docker installed. 
Testcontainers will spin up the real Postgres database in Docker container.
"""
from typing import Protocol
import sqlite3
from psycopg2 import connect
import psycopg2
from testcontainers.postgres import PostgresContainer
from faker import Faker


class DatabaseImplementation(Protocol):
    """Implementor Interface using Protocol."""

    def connect(self) -> None:
        ...

    def execute(self, query: str):
        ...

    def start_transaction(self) -> None:
        ...

    def commit_transaction(self) -> None:
        ...

    def rollback_transaction(self) -> None:
        ...

class SQLiteDatabase:
    """Concrete Implementor for SQLite."""

    def __init__(self, database=':memory:'):
        self.database = database

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def connect(self) -> None:
        self.connection = sqlite3.connect(self.database)
        print("Connected to SQLite database")

    def execute(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def start_transaction(self) -> None:
        self.connection.execute('BEGIN TRANSACTION;')

    def commit_transaction(self) -> None:
        self.connection.commit()

    def rollback_transaction(self) -> None:
        self.connection.rollback()

class PostgreSQLDatabase:
    """Concrete Implementor for PostgreSQL using testcontainers."""

    def __init__(self, image='postgres:16'):
        self.container = PostgresContainer(image)
        self.connection = None

    def __enter__(self):
        self.container.start()
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        self.container.stop()

    def connect(self) -> None:
        self.connection = connect(
            database=self.container.dbname,
            user=self.container.username,
            password=self.container.password,
            host=self.container.get_container_host_ip(),
            port=self.container.get_exposed_port(self.container.port)
        )
        print("Connected to PostgreSQL database running in a Docker container.")

    def execute(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        try:
            result = cursor.fetchall()
            cursor.close()
            return result
        except psycopg2.ProgrammingError as e:
            if e.pgcode == 'P0002':  # No data found, more specific to fetch errors
                print("No results to fetch.")
            cursor.close()
            return None

    def start_transaction(self) -> None:
        self.connection.autocommit = False

    def commit_transaction(self) -> None:
        self.connection.commit()

    def rollback_transaction(self) -> None:
        self.connection.rollback()

class Database:
    """An Abstraction for Database."""

    def __init__(self, implementation: DatabaseImplementation):
        self._implementation = implementation

    def connect(self) -> None:
        self._implementation.connect()

    def execute_query(self, query: str):
        return self._implementation.execute(query)

class LoggingDatabase(Database):
    """Refined Abstraction with logging."""

    def connect(self) -> None:
        print("Connecting to the database...")
        self._implementation.connect()

    def execute_query(self, query: str):
        print(f"Executing query: {query}")
        return self._implementation.execute(query)


class TransactionalDatabase(Database):
    """Refined Abstraction with transaction support."""

    def connect(self) -> None:
        self._implementation.connect()

    def execute_query(self, query: str):
        return self._implementation.execute(query)

    def start_transaction(self) -> None:
        self._implementation.start_transaction()

    def commit(self) -> None:
        self._implementation.commit_transaction()

    def rollback(self) -> None:
        self._implementation.rollback_transaction()


def test_transactional_db(implementation: DatabaseImplementation, fake_data):
    """Tests transactional database functionality."""
    transactional_db = TransactionalDatabase(implementation)
    transactional_db.start_transaction()
    try:
        transactional_db.execute_query("CREATE TABLE people (name TEXT PRIMARY KEY, email TEXT);")
        for i in fake_data:
            transactional_db.execute_query(
                f"INSERT INTO people (name, email) VALUES ('{i['name']}', '{i['email']}');")
        transactional_db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        transactional_db.rollback()

    try:
        result = transactional_db.execute_query("SELECT * FROM people;")
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")


def test_logging_db(implementation: DatabaseImplementation, fake_data):
    """Tests logging database functionality."""
    logging_db = LoggingDatabase(implementation)
    logging_db.connect()
    logging_db.execute_query("CREATE TABLE people (name TEXT PRIMARY KEY, email TEXT);")
    for i in fake_data:
        logging_db.execute_query(f"INSERT INTO people (name, email) VALUES ('{
                                 i['name']}', '{i['email']}');")
    result = logging_db.execute_query("SELECT * FROM people;")
    print(result)


# Example Usage
if __name__ == "__main__":
    faker = Faker()

    fake_data = []

    for _ in range(5):
        fake_data.append(
            {
                "name": faker.name(),
                "email": faker.email()
            }
        )

    print(f"Fake data: {fake_data}")

    print("=" * 50)
    with PostgreSQLDatabase('postgres:16') as implementation:
        test_transactional_db(implementation, fake_data)
    print("=" * 50)
    with SQLiteDatabase(':memory:') as implementation:
        test_transactional_db(implementation, fake_data)
    print("=" * 50)
    with SQLiteDatabase(':memory:') as implementation:
        test_logging_db(implementation, fake_data)
