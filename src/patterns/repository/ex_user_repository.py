"""
Repository Pattern

The Repository pattern is used to decouple the business logic from the data access layer.
It provides an abstraction of data, so that your application can work with a simple
abstraction that has an interface approximating that of a collection.

This pattern allows you to:
1. Centralize the data access logic
2. Provide a substitution point for the unit tests
3. Provide a flexible architecture that can be adapted as the overall design of the application evolves
"""
from typing import Protocol

class User:
    """Represents a user in the system."""
    
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class UserRepository(Protocol):
    """
    Abstract interface for UserRepository.

    This class defines the interface for accessing User data.
    """

    def get(self, id: int) -> User:
        ...

    def add(self, user: User) -> None:
        ...
    
    def update(self, user: User) -> None:
        ...

class InMemoryUserRepository(UserRepository):
    """
    In-memory implementation of UserRepository.

    This class stores users in a dictionary for demonstration purposes.
    """

    def __init__(self):
        self.users = {}

    def get(self, id: int) -> User:
        print(f"Querying in-memory database for user with id {id}")
        return self.users.get(id)

    def add(self, user: User) -> None:
        print(f"Adding user {user.name} to in-memory database")
        self.users[user.id] = user
    
    def update(self, user: User) -> None:
        print(f"Updating user {user.name} in in-memory database")
        self.users[user.id] = user

class SQLUserRepository(UserRepository):
    """Implementation of UserRepository for SQL databases."""

    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        # In a real implementation, we would establish a database connection here

    def get(self, id: int) -> User:
        # In a real implementation, we would query the database
        # For this example, we'll just simulate it
        print(f"Querying SQL database for user with id {id}")
        return User(id, f"User {id}", f"user{id}@example.com")

    def add(self, user: User) -> None:
        # In a real implementation, we would insert into the database
        print(f"Adding user {user.name} to SQL database")

    def update(self, user: User) -> None:
        # In a real implementation, we would update the database
        print(f"Updating user {user.name} in SQL database")

class UserService:
    """Business logic for user operations."""

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, name: str, email: str) -> User:
        """Registers a new user."""
        new_id = self.generate_id()  # This would be more sophisticated in a real app
        user = User(new_id, name, email)
        self.user_repository.add(user)
        return user

    def change_user_email(self, user_id: int, new_email: str) -> User:
        """Changes a user's email."""
        user = self.user_repository.get(user_id)
        user.email = new_email
        self.user_repository.update(user)
        return user

    def generate_id(self) -> int:
        """Generates a new user ID."""
        # This is a simplistic implementation for demonstration purposes
        return 1

def client_code(service: UserService):
    """Client code that uses the UserService."""
    new_user = service.register_user("Bob", "bob@example.com")
    print(f"Registered user: {new_user.name} with email {new_user.email}")

    updated_user = service.change_user_email(new_user.id, "newemail@example.com")
    print(f"Updated user email: {updated_user.email}")
    print(updated_user.name)

# Usage example
if __name__ == "__main__":
    sql_repo = SQLUserRepository("connection_string_here")
    in_memory_repo = InMemoryUserRepository()
    
    client_code(UserService(sql_repo))
    print()
    client_code(UserService(in_memory_repo))    