"""
Memento Design Pattern

Example: Using Memento pattern to save and restore the state of a transactional database.
In this context, the Originator is the Database class, the Memento is the DatabaseMemento class,
and the Caretaker is the TransactionManager class.
"""
from __future__ import annotations
from contextlib import contextmanager
from dataclasses import dataclass, field
import datetime
from typing import Protocol


class Memento(Protocol):
    """Interface for Mementos. Caretracker (TransactionManager) only knows about this interface."""

    @property
    def date(self):
        ...

    def __str__(self) -> str:
        ...

class Database:
    """The Database class is the Originator.

    This class represents a simple key-value store that can save and restore its state using mementos.
    """

    def __init__(self):
        """Initializes the database with an empty dictionary."""
        self._data = {}

    def set(self, key: str, value: any):
        """Sets a key-value pair in the database."""
        print(f"Setting {key} to {value}")
        self._data[key] = value

    def get(self, key: str):
        """Gets the value associated with the given key."""
        return self._data.get(key)

    def __str__(self):
        return f"Current state: {self._data}"

    def save(self) -> Memento:
        """Saves the current state of the database to a memento.
        It's important to copy the actual state, not the reference.
        """
        return self._DatabaseMemento(self._data.copy())

    def restore(self, memento: Memento):
        """Restores the state of the database from a memento.

        Args:
            memento(Memento): The memento from which to restore the state.
        """
        self._data = memento.state

    @dataclass(frozen=True)
    class _DatabaseMemento(Memento):
        """The DatabaseMemento class is the concrete, immutable memento class, encapsulated within the Database class.

        Attributes:
            _state (dict): The state to be saved in the memento.
            _date (datetime): The timestamp when the memento was created.
        """
        _state: dict
        _date: datetime.datetime = field(default_factory=datetime.datetime.now)

        @property
        def state(self) -> dict:
            """Gets the state stored in the memento."""
            return self._state

        @property
        def date(self):
            """Gets the date when the memento was created."""
            return self._date

        def __str__(self):
            return f"[Snapshot @ {self._date}] {self._state}"

class TransactionManager:
    """The TransactionManager class is the Caretaker.

    This class is responsible for managing the database's mementos and handling transactions.
    """

    def __init__(self, database: Database):
        """Initializes the transaction manager with a database instance."""
        self._database = database
        self._memento: Memento = None

    def backup(self):
        """Creates a backup of the current state of the database."""
        memento = self._database.save()
        print(f"Saving backup: {memento}")
        self._memento = memento

    def rollback(self):
        """Restores the database to the last saved state."""
        if not self._memento:
            raise Exception("No mementos to restore.")
        memento = self._memento
        print(f"Rolling back to: {memento}")
        self._database.restore(memento)

    @contextmanager
    def transaction(self):
        """Context manager for handling transactions.

        Back ups the current state of the database, and rolls back if an exception occurs.
        """
        print(f"{'Starting transaction':=^50}")
        try:
            self.backup()
            yield
        except Exception as e:
            print(f"Error during transaction: {e}")
            self.rollback()
            raise
        else:
            print(f"Transaction succeeded.")
        finally:
            print(f"{'Ending transaction':=^50}")


# Example usage
if __name__ == "__main__":
    db = Database()
    tm = TransactionManager(db)

    db.set("a", 1)
    db.set("b", 2)

    # Successful transaction
    try:
        with tm.transaction():
            db.set("a", 10)
            db.set("c", 3)
            print(db)  # Output: Current state: {'a': 10, 'b': 2, 'c': 3}
    except Exception as e:
        print(e)

    # Failed transaction
    try:
        with tm.transaction():
            db.set("b", 20)
            print(db)  # Output: Current state: {'a': 10, 'b': 20, 'c': 3}
            raise Exception("Something went wrong!")  # Simulate an error
    except Exception as e:
        pass

    print(db)  # Output: Current state: {'a': 10, 'b': 2, 'c': 3}  # Rolled back to previous state
