"""
Composite Design Pattern

Intent: Lets you compose objects into tree-like structures and allows clients 
to treat individual objects and compositions of objects uniformly. 
In other words, whether dealing with a single object or a group
of objects (composite), clients can use them interchangeably.
"""
from __future__ import annotations
from typing import List, Protocol

class Component(Protocol):
    """Component declares the interface common to both leaf and composite objects."""

    def operation(self) -> str:
        """Performs an operation."""
        ...


class Leaf(Component):
    """Leaf represents leaf objects in the composition. A leaf has no children."""

    def operation(self) -> str:
        """Performs an operation."""
        return "Leaf"


class Composite(Component):
    """Composite represents complex components that may have children."""

    def __init__(self):
        self._children: List[Component] = []

    def operation(self) -> str:
        """Performs an operation and traverses children to perform their operations."""
        results = [child.operation() for child in self._children]
        return f"Composite({'+'.join(results)})"

    def add(self, component: Component) -> None:
        """Adds a component to the composite."""
        self._children.append(component)

    def remove(self, component: Component) -> None:
        """Removes a component from the composite."""
        self._children.remove(component)

    def get_child(self, index: int) -> Component:
        """Gets a child component."""
        return self._children[index]


if __name__ == "__main__":
    """Client code that demonstrates the Composite Design Pattern."""
    # Create leaf components
    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()

    # Create a composite component and add leafs to it
    composite1 = Composite()
    composite1.add(leaf1)
    composite1.add(leaf2)

    # Create another composite component and add a leaf and the first composite to it
    composite2 = Composite()
    composite2.add(leaf3)
    composite2.add(composite1)

    # Perform the operation on the composite structure
    print(composite2.operation())  # Output: Composite(Leaf+Composite(Leaf+Leaf))
