"""
Observer Design Pattern

Intent: Defines a one-to-many relation between objects so that when one object (the subject)
changes state, all its dependents (observers) are notified.
 
Observers are also called Subscribers.
Subject is also called Publisher.
"""
from __future__ import annotations
from typing import List, Protocol


class Observer(Protocol):
    """Interface for an Observer which will be updated by Subject."""

    def update(self, subject: Subject) -> None:
        """Receive update from subject.

        Args:
            subject (Subject): The subject being observed.
        """
        ...

class Subject:
    """Class that maintains a list of observers and notifies them of any changes."""

    def __init__(self) -> None:
        """Initialize the subject with an empty list of observers."""
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Attach an observer to the subject."""
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detach an observer from the subject."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Notify all observers about an event."""
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    """Concrete implementation of Subject that maintains a state."""

    def __init__(self) -> None:
        """Initialize the subject and its state."""
        super().__init__()
        self._state: int = 0

    @property
    def state(self) -> int:
        """Get the state of the subject."""
        return self._state

    @state.setter
    def state(self, value: int) -> None:
        """Set the state of the subject and notify observers."""
        print(f"{type(self).__name__} state changed to {value}")
        self._state = value
        self.notify()

class ConcreteObserver(Observer):
    """Concrete implementation of Observer that reacts to updates from Subject."""

    def __init__(self, name: str) -> None:
        """Initialize the observer with a name."""
        self.name = name

    def update(self, subject: Subject) -> None:
        """Update the observer's state to match the subject's state."""
        if isinstance(subject, ConcreteSubject):
            print(f"{self.name} notified with new state: {subject.state}")


# Example usage:
if __name__ == "__main__":
    subject = ConcreteSubject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.attach(observer1)
    subject.attach(observer2)

    subject.state = 10  # This should notify all observers and update their state
    subject.state = 20  # This should notify all observers and update their state
