"""
Memento Pattern

Intent: Memento pattern allows an object to capture its internal state without exposing its internal structure.
State of a target object (Originator) is saved in a Memento object and can be restored later (undo mechanism).
The Caretaker object is responsible for keeping track of the Memento objects.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Protocol


class Memento(Protocol):
    """Interface for Memento"""

    def get_state(self) -> str:
        """Returns the saved state"""
        ...


class Originator:
    """The Originator creates a Memento containing a snapshot of its current state."""

    def __init__(self) -> None:
        """Initializes the Originator with an empty state."""
        self._state: str = ''

    def set_state(self, state: str) -> None:
        """
        Sets the state of the Originator.
        """
        self._state = state
        print(f"Originator: Setting state to {state}")

    def save_to_memento(self) -> Memento:
        """
        Saves the current state to a memento.
        """
        print(f"Originator: Saving to Memento with state {self._state}")
        return self._ConcreteMemento(self._state)

    def restore_from_memento(self, memento: Memento) -> None:
        """
        Restores the state from a memento.
        """
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")

    @dataclass(frozen=True)
    class _ConcreteMemento(Memento):
        """Concrete implementation of Memento that stores the state of the Originator.
        It is encapsulated within the Originator class, as it is tightly coupled to the Originator
        and Caretracker should not care about the internal structure of the Memento.

        ConcreteMemento is immutable (frozen=True) dataclass to prevent modification of the saved state.
        """
        _state: str

        def get_state(self) -> str:
            """Returns the saved state."""
            return self._state

class Caretaker:
    """The Caretaker is responsible for keeping track of the Originator's mementos."""

    def __init__(self) -> None:
        """Initializes the Caretaker with an empty list of mementos."""
        self._mementos: deque[Memento] = []
        self._originator: Originator = Originator()

    def backup(self) -> None:
        """Saves the Originator's current state to a memento."""
        print("Caretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save_to_memento())

    def undo(self) -> None:
        """Restores the Originator's state to the last saved memento."""
        if not self._mementos:
            print("Caretaker: No mementos to restore.")
            return

        memento = self._mementos.pop()
        print("Caretaker: Restoring state to previous memento...")
        self._originator.restore_from_memento(memento)

    def show_history(self) -> None:
        """Prints the list of saved mementos' states."""
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_state())

    def set_originator_state(self, state: str) -> None:
        """
        Sets the state of the Originator.
        """
        self._originator.set_state(state)


# Example usage
if __name__ == "__main__":
    caretaker = Caretaker()
    caretaker.set_originator_state("State1")
    caretaker.backup()
    caretaker.set_originator_state("State2")
    caretaker.backup()
    caretaker.set_originator_state("State3")
    caretaker.undo()
    caretaker.show_history()
