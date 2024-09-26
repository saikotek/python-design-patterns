"""
Facade Pattern

Intent: Provides a simplified interface to a library, a framework, or any other
complex set of classes.
"""
from __future__ import annotations


class SubsystemA:
    """SubsystemA is a part of the complex system."""

    def operation_a1(self) -> str:
        """Performs operation A1."""
        return "SubsystemA: Operation A1"

    def operation_a2(self) -> str:
        """Performs operation A2."""
        return "SubsystemA: Operation A2"


class SubsystemB:
    """SubsystemB is another part of the complex system."""

    def operation_b1(self) -> str:
        """Performs operation B1."""
        return "SubsystemB: Operation B1"

    def operation_b2(self) -> str:
        """Performs operation B2."""
        return "SubsystemB: Operation B2"


class SubsystemC:
    """SubsystemC is yet another part of the complex system."""

    def operation_c1(self) -> str:
        """Performs operation C1."""
        return "SubsystemC: Operation C1"

    def operation_c2(self) -> str:
        """Performs operation C2."""
        return "SubsystemC: Operation C2"


class Facade:
    """Facade provides a simplified interface to the complex subsystems."""

    def __init__(self) -> None:
        """Initializes the facade with the subsystems."""
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation(self) -> str:
        """Performs a high-level operation that uses the subsystems."""
        results = [
            self._subsystem_a.operation_a1(),
            self._subsystem_a.operation_a2(),
            self._subsystem_b.operation_b1(),
            self._subsystem_b.operation_b2(),
            self._subsystem_c.operation_c1(),
            self._subsystem_c.operation_c2(),
        ]
        return "\n".join(results)


if __name__ == "__main__":
    """Client code that demonstrates the Facade Design Pattern."""
    facade = Facade()
    print("Client: Using the facade to perform operations:")
    print(facade.operation())
