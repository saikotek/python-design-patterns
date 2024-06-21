"""
Decorator Design Pattern

Intent: Allows behavior to be added to an individual object, dynamically, 
without affecting the behavior of other instances of the same class.

This is the classic implementation of the Decorator Design Pattern.
"""
from typing import Protocol


class Component(Protocol):
    """Component declares the interface for objects that can have responsibilities added to them dynamically."""

    def operation(self) -> str:
        """Performs an operation."""
        pass


class ConcreteComponent(Component):
    """ConcreteComponent defines an object to which additional responsibilities can be attached."""

    def operation(self) -> str:
        """Performs an operation."""
        return "ConcreteComponent"


class Decorator(Component):
    """Decorator maintains a reference to a Component object and defines an interface that conforms to Component's interface."""

    def __init__(self, component: Component) -> None:
        """
        Initializes the decorator with a component.

        Args:
            component (Component): The component to be decorated.
        """
        self._component = component

    def operation(self) -> str:
        """Performs an operation by delegating to the wrapped component."""
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """ConcreteDecoratorA adds responsibilities to the component."""

    def operation(self) -> str:
        """Performs an operation and adds additional behavior."""
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    """ConcreteDecoratorB adds responsibilities to the component."""

    def operation(self) -> str:
        """Performs an operation and adds additional behavior."""
        return f"ConcreteDecoratorB({self._component.operation()})"


if __name__ == "__main__":
    """Client code that demonstrates the Decorator Design Pattern."""
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    print(f"Result: {simple.operation()}\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    print(f"Result: {decorator2.operation()}")
