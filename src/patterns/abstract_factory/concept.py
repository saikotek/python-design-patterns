"""
Abstract Factory Pattern

Intent: Lets you create families of related objects without specifying their
concrete implementations.
"""
from typing import Protocol


class AbstractProductA(Protocol):
    """Protocol declaring an interface of a product A."""

    def method_a(self) -> None:
        ...

class AbstractProductB(Protocol):
    """Protocol declaring an interface of a product B."""

    def method_b(self) -> None:
        ...

class AbstractFactory(Protocol):
    """Protocol declaring an interface of an abstract factory.

    This factory will create a family of related products A and B.
    """

    def create_product_a(self) -> AbstractProductA:
        ...

    def create_product_b(self) -> AbstractProductB:
        ...

class ConcreteProductA1(AbstractProductA):
    """Concrete implementation of Product A1."""

    def method_a(self) -> None:
        print("The result of the product A1.")

class ConcreteProductA2(AbstractProductA):
    """Concrete implementation of Product A2."""

    def method_a(self) -> None:
        print("The result of the product A2.")

class ConcreteProductB1(AbstractProductB):
    """Concrete implementation of Product B1."""

    def method_b(self) -> None:
        print("The result of the product B1.")

class ConcreteProductB2(AbstractProductB):
    """Concrete implementation of Product B2."""

    def method_b(self) -> None:
        print("The result of the product B2.")

class ConcreteFactory1(AbstractFactory):
    """Concrete factory that creates the family of products A1 and B1."""

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    """Concrete factory that creates the family of products A2 and B2."""

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """Client code that uses the abstract factory to create products.

    Args:
        factory (AbstractFactory): The abstract factory used to create products.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    product_a.method_a()
    product_b.method_b()


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\nClient: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
