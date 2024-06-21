from contextlib import contextmanager
import datetime
from typing import List, TypeVar, Generic

# Generic type variable
T = TypeVar('T')

# The Memento class is the base class for all mementos
# This class can be generic because we plan to hold the state in a dictionary
class Memento(Generic[T]):
    def __init__(self, state: T):
        self._state = state
        self._date = datetime.datetime.now()

    @property
    def state(self) -> T:
        return self._state
    
    @property
    def date(self):
        return self._date
    
    def __str__(self):
        return f"[Snapshot @ {self._date}] {self._state}"

# The Database class is the Originator
class Database:
    def __init__(self):
        self._data = {}

    def set(self, key: str, value: any):
        print(f"Setting {key} to {value}")
        self._data[key] = value

    def get(self, key: str):
        return self._data.get(key)

    def __str__(self):
        return f"Current state: {self._data}"

    def save(self) -> Memento[dict]:
        return self._DatabaseMemento(self._data.copy())

    def restore(self, memento: Memento[dict]):
        self._data = memento.state

    # The DatabaseMemento class is the concrete memento class
    # It is encapsulated within the Database class
    class _DatabaseMemento(Memento[dict]):
        pass

# The TransactionManager class is the Caretaker
class TransactionManager:
    def __init__(self, database: Database):
        self._database = database
        self._memento: Memento[dict] = None

    def backup(self):
        memento = self._database.save()
        print(f"Saving backup: {memento}")
        self._memento = memento

    def rollback(self):
        if not self._memento:
            raise Exception("No mementos to restore.")
        memento = self._memento
        print(f"Rolling back to: {memento}")
        self._database.restore(memento)

    @contextmanager
    def transaction(self):
        print(f"{'Starting transaction':=^50}")
        try:
            self.backup()
            yield
        except Exception as e:
            print(f"Error during transaction: {e}")
            self.rollback()
            raise
        else:
            # If we reach here, the transaction succeeded.
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
            print(db) # Output: {'a': 10, 'b': 2, 'c': 3}
    except Exception as e:
        print(e)

    # Failed transaction
    try:
        with tm.transaction():
            db.set("b", 20)
            print(db)  # Output: {'a': 10, 'b': 20, 'c': 3}
            raise Exception("Something went wrong!")  # Simulate an error
    except Exception as e:
        pass

    print(db)  # Output: {'a': 10, 'b': 2, 'c': 3}  # Rolled back to previous state
