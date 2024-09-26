"""
Bridge Pattern

Intent: Decouple an abstraction from its implementation so that the two can vary inde-
pendently.
"""
from __future__ import annotations

class Implementor:
    """Implementor defines the interface for implementation classes."""

    def operation_impl(self):
        """Performs an operation."""
        pass


class ConcreteImplementorA(Implementor):
    """ConcreteImplementorA implements the Implementor interface."""

    def operation_impl(self):
        """Performs an operation specific to ConcreteImplementorA."""
        return "ConcreteImplementorA operation"


class ConcreteImplementorB(Implementor):
    """ConcreteImplementorB implements the Implementor interface."""

    def operation_impl(self):
        """Performs an operation specific to ConcreteImplementorB."""
        return "ConcreteImplementorB operation"


class Abstraction:
    """Abstraction defines the abstraction's interface and maintains a reference to an Implementor object."""

    def __init__(self, implementor: Implementor):
        """
        Initializes the abstraction with an implementor.

        Args:
            implementor (Implementor): The implementor instance.
        """
        self._implementor = implementor

    def operation(self):
        """Performs an operation."""
        return self._implementor.operation_impl()


class RefinedAbstraction(Abstraction):
    """RefinedAbstraction extends the interface defined by Abstraction."""

    def operation(self):
        """Performs an operation."""
        return f"RefinedAbstraction: {super().operation()}"


if __name__ == "__main__":
    """Client code that demonstrates the Bridge Design Pattern."""
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()

    abstraction_a = RefinedAbstraction(implementor_a)
    abstraction_b = RefinedAbstraction(implementor_b)

    print(abstraction_a.operation())  # Output: RefinedAbstraction: ConcreteImplementorA operation
    print(abstraction_b.operation())  # Output: RefinedAbstraction: ConcreteImplementorB operation
