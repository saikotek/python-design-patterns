"""
Repository Pattern with SQLite

An example of the Repository pattern using SQLite in-memory database.
"""
from typing import Protocol, Optional
import sqlite3

class User:
    """Represents a user in the system."""
    
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class UserRepository(Protocol):
    """
    Abstract interface for UserRepository.
    """
    def get(self, id: int) -> Optional[User]:
        ...

    def add(self, user: User) -> None:
        ...
    
    def update(self, user: User) -> None:
        ...


class SQLiteUserRepository:
    """Implementation of UserRepository using SQLite database."""

    def __init__(self, db_path=":memory:"):
        """Initialize with in-memory database."""
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_table()
    
    def _create_table(self):
        """Create the users table."""
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT
        )
        ''')
        self.conn.commit()

    def get(self, id: int) -> Optional[User]:
        """Get user by ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (id,))
        row = cursor.fetchone()
        
        if row:
            return User(row['id'], row['name'], row['email'])
        return None

    def add(self, user: User) -> None:
        """Add a new user."""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )
        self.conn.commit()
        # Update the user's ID with the auto-generated one
        user.id = cursor.lastrowid

    def update(self, user: User) -> None:
        """Update an existing user."""
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (user.name, user.email, user.id)
        )
        self.conn.commit()
    
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()


class InMemoryUserRepository:
    """In-memory implementation of UserRepository."""

    def __init__(self):
        self.users = {}
        self.next_id = 1

    def get(self, id: int) -> Optional[User]:
        """Get user by ID."""
        return self.users.get(id)

    def add(self, user: User) -> None:
        """Add a new user."""
        # Assign ID if not present
        if user.id <= 0:
            user.id = self.next_id
            self.next_id += 1
        self.users[user.id] = user
    
    def update(self, user: User) -> None:
        """Update an existing user."""
        self.users[user.id] = user


class UserService:
    """Business logic for user operations."""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, name: str, email: str) -> User:
        """Registers a new user."""
        # Create user with temporary ID
        user = User(0, name, email)
        self.user_repository.add(user)
        return user

    def change_email(self, user_id: int, new_email: str) -> Optional[User]:
        """Changes a user's email."""
        user = self.user_repository.get(user_id)
        if user:
            user.email = new_email
            self.user_repository.update(user)
            return user
        return None


def client_code(service: UserService):
    """Client code that uses the UserService doesn't know the underlying repository implementation details."""
    # Register new users
    alice = service.register_user("Alice", "alice@example.com")
    print(f"Registered: {alice}")
    
    bob = service.register_user("Bob", "bob@example.com")
    print(f"Registered: {bob}")
    
    # Update a user's email
    updated_user = service.change_email(alice.id, "alice.new@example.com")
    if updated_user:
        print(f"Updated email: {updated_user}")


if __name__ == "__main__":
    # Using SQLite repository
    print("=== Using SQLite Repository ===")
    sqlite_repo = SQLiteUserRepository()
    sql_service = UserService(sqlite_repo)
    client_code(sql_service)
    sqlite_repo.close()
    
    print("\n=== Using In-Memory Repository ===")
    memory_repo = InMemoryUserRepository()
    memory_service = UserService(memory_repo)
    client_code(memory_service)