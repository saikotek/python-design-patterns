"""
Strategy Pattern

Intent: Lets you define a family of algorithms, put each of them into a separate
class, and make their objects interchangeable.
"""
from typing import Protocol


class Strategy(Protocol):
    """Strategy interface that declares the operation common to all supported algorithms."""

    def algorithm_interface(self) -> None:
        """Performs the algorithmic operation."""
        ...

class ConcreteStrategyA:
    """ConcreteStrategyA implements the algorithm using the Strategy interface."""

    def algorithm_interface(self) -> None:
        print("Algorithm implemented by ConcreteStrategyA")

class ConcreteStrategyB:
    """ConcreteStrategyB implements the algorithm using the Strategy interface."""

    def algorithm_interface(self) -> None:
        print("Algorithm implemented by ConcreteStrategyB")

class Context:
    """Context maintains a reference to a Strategy object and calls its algorithm_interface method.

    Attributes:
        strategy (Strategy): The current strategy used by the context.
    """

    def __init__(self, strategy: Strategy) -> None:
        """Initializes the context with a specific strategy.

        Args:
            strategy (Strategy): The initial strategy to be used by the context.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """Gets the current strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Sets a new strategy."""
        self._strategy = strategy

    def context_interface(self) -> None:
        """Calls the algorithm_interface method of the current strategy."""
        self._strategy.algorithm_interface()


# Usage example
if __name__ == "__main__":
    # Create context with ConcreteStrategyA
    context = Context(ConcreteStrategyA())
    context.context_interface()  # Output: Algorithm implemented by ConcreteStrategyA

    # Change strategy to ConcreteStrategyB
    context.strategy = ConcreteStrategyB()
    context.context_interface()  # Output: Algorithm implemented by ConcreteStrategyB
