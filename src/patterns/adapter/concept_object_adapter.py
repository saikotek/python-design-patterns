"""Object Adapter Pattern

Intent: Converts the interface of a class into another interface that the clients
expect. Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
Object adapter uses composition to adapt one interface to another.
"""

from typing import Protocol


class Target(Protocol):
    """Protocol declaring domain-specific interface used by the client code."""

    def request(self, input_str) -> str:
        ...

class ConcreteTarget(Target):
    """Example of a class that follows the Target interface."""

    def request(self, input_str) -> str:
        # add numbers separated by , and return the sum
        return f"Result: {sum(map(int, input_str.split(',')))}"

class Adaptee:
    """Defines an existing interface that needs adapting."""

    def specific_request(self, a: int, b: int) -> str:
        return f"Result: {a + b}"

class Adapter(Target):
    """Adapter makes the Adaptee's interface compatible with the Target's interface
    via composition.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self, input_str) -> str:
        # Parse the input string to extract two integers
        try:
            a, b = map(int, input_str.split(","))
            # Use the Adaptee's specific_request method
            return self.adaptee.specific_request(a, b)
        except ValueError:
            return "Invalid input. Please provide two integers separated by a comma."


def client_code(target: Target, input_str) -> None:
    """The client code supports all classes that follow the Target interface."""
    print(target.request(input_str))


if __name__ == "__main__":
    target = ConcreteTarget()
    client_code(target, "3,5")  # Valid input
    # Adaptee is not compatible with the Target interface
    adaptee = Adaptee()
    # client_code(adaptee, "3,5")  # This will raise an error

    # So lets use the Adapter and pass the Adaptee instance
    adapter = Adapter(adaptee=adaptee)
    client_code(adapter, "3,5")  # Valid input
