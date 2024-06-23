"""
Flyweight Design Pattern

Intent: Lets you minimize memory usage by sharing
some common state between multiple objects instead
of keeping all of the data in each object.
"""
from typing import Dict, Protocol


class Flyweight(Protocol):
    """Flyweight declares an interface through which flyweights can receive and act on extrinsic state."""

    def operation(self, extrinsic_state: str) -> str:
        """
        Performs an operation using extrinsic state.

        Args:
            extrinsic_state (str): The extrinsic state passed to the flyweight.
        """
        pass

class ConcreteFlyweight:
    """ConcreteFlyweight implements the Flyweight interface and stores intrinsic state."""

    def __init__(self, intrinsic_state: str) -> None:
        """
        Initializes the flyweight with intrinsic state.

        Args:
            intrinsic_state (str): The intrinsic state stored in the flyweight.
        """
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> str:
        """
        Performs an operation using both intrinsic and extrinsic state.

        Args:
            extrinsic_state (str): The extrinsic state passed to the flyweight.

        Returns:
            str: A string representation of the operation result.
        """
        return f"ConcreteFlyweight: Intrinsic state = {self._intrinsic_state}, Extrinsic state = {extrinsic_state}"

class FlyweightFactory:
    """FlyweightFactory creates and manages flyweight objects."""

    def __init__(self) -> None:
        """Initializes the flyweight factory with an empty pool of flyweights."""
        self._flyweights: Dict[str, Flyweight] = {}

    def get_flyweight(self, key: str) -> Flyweight:
        """
        Returns an existing flyweight with the given key or creates a new one if it doesn't exist.

        Args:
            key (str): The key identifying the flyweight.

        Returns:
            Flyweight: The flyweight associated with the key.
        """
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight(key)
            print(f"FlyweightFactory: Created new flyweight for key '{key}'")
        else:
            print(f"FlyweightFactory: Reusing existing flyweight for key '{key}'")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        """Lists all flyweights managed by the factory."""
        print(f"FlyweightFactory: I have {len(self._flyweights)} flyweights:")
        for key in self._flyweights:
            print(f"  Key: {key}")


if __name__ == "__main__":
    """Client code that demonstrates the Flyweight Design Pattern."""
    factory = FlyweightFactory()

    flyweight1 = factory.get_flyweight("State1")
    print(flyweight1.operation("Context1"))

    flyweight2 = factory.get_flyweight("State2")
    print(flyweight2.operation("Context2"))

    flyweight3 = factory.get_flyweight("State1")
    print(flyweight3.operation("Context3"))

    factory.list_flyweights()
