"""
Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance. One instance per each subclass (if any).
"""
from __future__ import annotations
from typing import Optional


class SingletonMeta(type):
    """A metaclass for creating Singleton classes.

    This metaclass ensures that a class has only one instance and provides a global point of access to it.
    """
    _instance: Optional[Singleton] = None

    def __call__(cls, *args, **kwargs) -> Singleton:
        """Overrides the __call__ method to control the instantiation of the Singleton class.

        If an instance of the class does not exist, it creates one. Otherwise, it returns the existing instance.

        Returns:
            Singleton: The singleton instance of the class.
        """
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    """A Singleton class that can have only one instance."""

    def __init__(self) -> None:
        self.value = None

    def business_logic(self) -> None:
        """A placeholder method for the singleton's business logic."""
        print("Executing business logic.")


# Client code
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    singleton1.value = "Singleton instance value"

    print(f"Singleton1 value: {singleton1.value}")  # Singleton instance value
    print(f"Singleton2 value: {singleton2.value}")  # Singleton instance value
    print(f"Singleton1 is Singleton2: {singleton1 is singleton2}")  # True

    singleton1.business_logic()  # Executing business logic.
