"""
Singleton Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).
"""
from __future__ import annotations
import threading
from typing import Optional

class SingletonMeta(type):
    """A thread-safe implementation of the Singleton metaclass.

    This metaclass ensures that a class has only one instance and provides a global point of access to it.
    """
    _instance: Optional[Singleton] = None
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs) -> Singleton:
        """Overrides the __call__ method to control the instantiation of the Singleton class.

        Ensures thread-safe instantiation of the Singleton instance.

        Returns:
            Singleton: The singleton instance of the class.
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    """A Singleton class that ensures only one instance is created in a thread-safe manner."""

    def __init__(self) -> None:
        self.value = None

    def business_logic(self) -> None:
        """A placeholder method for the singleton's business logic."""
        print("Executing business logic.")


# Client code
def singleton_test() -> None:
    singleton = Singleton()
    singleton.value = "Singleton instance value"
    print(f"Singleton value: {singleton.value}")


if __name__ == "__main__":
    # Create multiple threads to test thread-safety of Singleton
    threads = []
    for i in range(10):
        thread = threading.Thread(target=singleton_test)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Check that the singleton instance is the same across threads
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(f"Singleton1 is Singleton2: {singleton1 is singleton2}")  # True
    singleton1.business_logic()  # Executing business logic.
