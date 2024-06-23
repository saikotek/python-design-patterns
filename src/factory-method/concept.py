"""
Factory Method Design Pattern

Intent: Lets you create objects without specifying the exact class to create.
This pattern uses factory methods to deal with the problem of creating objects
without having to specify their exact class. Rather than by calling a constructor,
this is done by calling a factory method to create an object.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol

class Product(Protocol):
    """Product declares the interface for the type of object the factory method creates."""

    def operation(self) -> str:
        """Performs an operation."""
        pass

class ConcreteProductA:
    """ConcreteProductA implements the Product interface."""

    def operation(self) -> str:
        """Performs an operation."""
        return "ConcreteProductA operation"

class ConcreteProductB:
    """ConcreteProductB implements the Product interface."""

    def operation(self) -> str:
        """Performs an operation."""
        return "ConcreteProductB operation"

class Creator(ABC):
    """Creator declares the factory method that returns an object of type Product."""

    @abstractmethod
    def factory_method(self) -> Product:
        """Factory method that should be overridden to create a Product."""
        pass

    def some_operation(self) -> str:
        """Performs an operation using the Product."""
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"

class ConcreteCreatorA(Creator):
    """ConcreteCreatorA overrides the factory method to return an instance of ConcreteProductA."""

    def factory_method(self) -> Product:
        """Creates and returns a ConcreteProductA."""
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    """ConcreteCreatorB overrides the factory method to return an instance of ConcreteProductB."""

    def factory_method(self) -> Product:
        """Creates and returns a ConcreteProductB."""
        return ConcreteProductB()


def client_code(creator: Creator) -> None:
    """Client code works with an instance of a Creator subclass."""
    print("Client: I'm not aware of the creator's class, but it still works.")
    print(creator.some_operation())


if __name__ == "__main__":
    print("App: Launched with ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print()

    print("App: Launched with ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
