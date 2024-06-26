"""
Builder Pattern

Intent: Separate the construction of a complex object from its
representation so that the same construction process 
can create different representations.
"""
from __future__ import annotations
from typing import List, Protocol

class Product:
    """Product represents the complex object under construction."""

    def __init__(self):
        self.parts: List[str] = []

    def add_part(self, part: str) -> None:
        """
        Adds a part to the product.

        Args:
            part (str): The part to be added.
        """
        self.parts.append(part)

    def show(self) -> None:
        """Displays the parts of the product."""
        print("Product parts: " + ", ".join(self.parts))


class Builder(Protocol):
    """Builder defines the abstract interface for creating parts of a Product object."""

    def build_part_a(self) -> None:
        """Builds part A of the product."""
        ...

    def build_part_b(self) -> None:
        """Builds part B of the product."""
        ...

    def get_result(self) -> Product:
        """Returns the final product."""
        ...


class ConcreteBuilder(Builder):
    """ConcreteBuilder constructs and assembles parts of the product by implementing the Builder interface."""

    def __init__(self):
        self.product = Product()

    def build_part_a(self) -> None:
        """Builds part A of the product."""
        self.product.add_part("PartA")

    def build_part_b(self) -> None:
        """Builds part B of the product."""
        self.product.add_part("PartB")

    def get_result(self) -> Product:
        """Returns the final product."""
        return self.product


class Director:
    """Director constructs an object using the Builder interface."""

    def __init__(self, builder: Builder):
        """
        Initializes the director with a builder.

        Args:
            builder (Builder): The builder instance.
        """
        self.builder = builder

    def construct(self) -> None:
        """Constructs the product using the builder."""
        self.builder.build_part_a()
        self.builder.build_part_b()


if __name__ == "__main__":
    """Client code that demonstrates the Builder Design Pattern."""
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_result()
    product.show()
