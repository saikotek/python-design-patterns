"""Visitor Pattern

Intent: Lets you separate algorithms from the objects on which they operate.
This is achieved by creating a separate object (a visitor) that performs the
required operation on the object it visits. 

It uses something called "double dispatch" to call the appropriate method on 
the visitor based on the type of the object being visited.
"""
from __future__ import annotations
from typing import Protocol, List


class Visitor(Protocol):
    """Visitor interface that declares a visit operation for each type of ConcreteComponent."""

    def visit_concrete_component_a(self, component: ConcreteComponentA) -> None:
        """Visit operation for ConcreteComponentA."""
        ...

    def visit_concrete_component_b(self, component: ConcreteComponentB) -> None:
        """Visit operation for ConcreteComponentB."""
        ...

class Component(Protocol):
    """Component interface that declares an accept method to accept a visitor."""

    def accept(self, visitor: Visitor) -> None:
        ...

class ConcreteComponentA:
    """ConcreteComponentA implements the Component interface and accepts a visitor."""

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    def operation_a(self) -> str:
        """A specific operation for ConcreteComponentA."""
        return "ConcreteComponentA operation"

class ConcreteComponentB:
    """ConcreteComponentB implements the Component interface and accepts a visitor."""

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_b(self)

    def operation_b(self) -> str:
        """A specific operation for ConcreteComponentB."""
        return "ConcreteComponentB operation"

class ConcreteVisitor1:
    """ConcreteVisitor1 implements the Visitor interface."""

    def visit_concrete_component_a(self, component: ConcreteComponentA) -> None:
        """Visit operation for ConcreteComponentA."""
        print(f"ConcreteVisitor1: {component.operation_a()}")

    def visit_concrete_component_b(self, component: ConcreteComponentB) -> None:
        """Visit operation for ConcreteComponentB."""
        print(f"ConcreteVisitor1: {component.operation_b()}")

class ConcreteVisitor2:
    """ConcreteVisitor2 implements the Visitor interface."""

    def visit_concrete_component_a(self, component: ConcreteComponentA) -> None:
        """Visit operation for ConcreteComponentA."""
        print(f"ConcreteVisitor2: {component.operation_a()}")

    def visit_concrete_component_b(self, component: ConcreteComponentB) -> None:
        """Visit operation for ConcreteComponentB."""
        print(f"ConcreteVisitor2: {component.operation_b()}")

class ObjectStructure:
    """ObjectStructure can store a collection of components and allow visitors to visit them."""

    def __init__(self) -> None:
        """Initializes the object structure with an empty list of components."""
        self._components: List[Component] = []

    def attach(self, component: Component) -> None:
        """Adds a component to the object structure."""
        self._components.append(component)

    def detach(self, component: Component) -> None:
        """Removes a component from the object structure."""
        self._components.remove(component)

    def accept(self, visitor: Visitor) -> None:
        """Accepts a visitor and triggers the visitor's visit operation on each component."""
        for component in self._components:
            component.accept(visitor)


# Usage
if __name__ == "__main__":
    object_structure = ObjectStructure()
    object_structure.attach(ConcreteComponentA())
    object_structure.attach(ConcreteComponentB())

    print("ConcreteVisitor1:")
    object_structure.accept(ConcreteVisitor1())

    print("ConcreteVisitor2:")
    object_structure.accept(ConcreteVisitor2())
