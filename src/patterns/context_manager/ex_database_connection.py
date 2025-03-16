"""
Python Context Manager Protocol for Database Connections
This demonstrates using Python's ContextManager protocol for a simple database connection.
"""
from typing import ContextManager, Optional, Type
from types import TracebackType
import sqlite3


class DatabaseConnection(ContextManager[sqlite3.Connection]):
    """
    A database connection manager that implements the ContextManager protocol.
    """
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None
        
    def __enter__(self) -> sqlite3.Connection:
        """
        Open and return a database connection.
        """
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
        
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> bool:
        """
        Close the database connection when exiting the context.
        """
        if self.connection:
            if exc_type is None:
                print("No exception occurred, commit changes")
                self.connection.commit()
            else:
                print("An exception occurred, rollback changes")
                self.connection.rollback()
            
            self.connection.close()
            print("Database connection closed")
        return False  # Propagate exceptions


if __name__ == "__main__":
    # In-memory database for demonstration
    DB_PATH = ":memory:"
    
    # Use the context manager to handle the connection
    with DatabaseConnection(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # Create a table
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        
        # Insert data
        cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
        
        # Query data
        cursor.execute("SELECT id, name FROM users")
        for user_id, name in cursor.fetchall():
            print(f"User {user_id}: {name}")
    
    # The connection is automatically closed when exiting the with block
    
    print("\nExample with exception handling:")
    try:
        with DatabaseConnection(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nonexistent_table")  # This will cause an error
    except sqlite3.OperationalError as e:
        print(f"Caught database error: {e}")
        print("Connection was still properly closed by the context manager")