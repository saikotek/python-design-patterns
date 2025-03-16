"""
Repository Pattern

Intent: Abstracts data access logic from business logic, providing a collection-like
interface for domain objects.
"""
from typing import Protocol, Optional


class User:
    """Domain entity representing a user."""
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class UserRepository(Protocol):
    """Protocol defining the repository interface."""
    
    def get(self, id: int) -> Optional[User]:
        """Retrieves a user by ID."""
        ...
    
    def add(self, user: User) -> None:
        """Adds a new user."""
        ...
    
    def update(self, user: User) -> None:
        """Updates an existing user."""
        ...
    
    def delete(self, id: int) -> None:
        """Removes a user."""
        ...


class InMemoryUserRepository(UserRepository):
    """In-memory implementation of UserRepository."""
    
    def __init__(self):
        self.users = {}
    
    def get(self, id: int) -> Optional[User]:
        return self.users.get(id)
    
    def add(self, user: User) -> None:
        self.users[user.id] = user
    
    def update(self, user: User) -> None:
        self.users[user.id] = user
    
    def delete(self, id: int) -> None:
        if id in self.users:
            del self.users[id]


class UserService:
    """Business logic using repository abstraction."""
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def register_user(self, name: str, email: str) -> User:
        user = User(id=42, name=name, email=email)
        self.repository.add(user)
        return user


if __name__ == "__main__":
    # Usage example    
    mem_repo = InMemoryUserRepository()
    service = UserService(mem_repo)
    user = service.register_user("Bob", "bob@example.com")
    print(user)  # User(id=42, name='Bob')