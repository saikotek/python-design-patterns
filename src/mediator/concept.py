from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol, List

class Mediator(Protocol):
    """Mediator defines an interface for communicating with Colleague objects."""

    def notify(self, sender: Colleague, event: str) -> None:
        """
        Notifies the mediator about an event.

        Args:
            sender (Colleague): The colleague that sent the event.
            event (str): The event that occurred.
        """
        pass

class Colleague(ABC):
    """Colleague defines the interface for colleague objects."""

    def __init__(self, mediator: Mediator) -> None:
        """
        Initializes the colleague with a mediator.

        Args:
            mediator (Mediator): The mediator instance.
        """
        self._mediator = mediator

    @abstractmethod
    def react(self, sender: Colleague) -> None:
        """
        Reacts to an event.

        Args:
            sender (Colleague): The colleague that sent the event.
        """

        pass

class ConcreteColleague1(Colleague):
    """ConcreteColleague1 implements the Colleague interface."""

    def do_something(self) -> None:
        """Performs an action and notifies the mediator."""
        print("ConcreteColleague1 does something.")
        self._mediator.notify(self, "ConcreteColleague1 did something")

    def react(self, sender: Colleague) -> None:
        """Reacts to an event."""
        print(f"ConcreteColleague1 reacts to an event from {type(sender).__name__}.")

class ConcreteColleague2(Colleague):
    """ConcreteColleague2 implements the Colleague interface."""

    def do_something_else(self) -> None:
        """Performs another action and notifies the mediator."""
        print("ConcreteColleague2 does something else.")
        self._mediator.notify(self, "ConcreteColleague2 did something else")

    def react(self, sender) -> None:
        """Reacts to an event."""
        print(f"ConcreteColleague2 reacts to an event from {type(sender).__name__}.")

class ConcreteMediator(Mediator):
    """ConcreteMediator implements the Mediator interface and coordinates communication between Colleagues."""

    def __init__(self) -> None:
        """Initializes the mediator with empty lists of colleagues."""
        self._colleagues: List[Colleague] = []

    def add_colleague(self, colleague: Colleague) -> None:
        """
        Adds a colleague to the mediator's list.

        Args:
            colleague (Colleague): The colleague to add.
        """
        self._colleagues.append(colleague)

    def notify(self, sender: Colleague, event: str) -> None:
        """
        Notifies the mediator about an event and coordinates the response.

        Args:
            sender (Colleague): The colleague that sent the event.
            event (str): The event that occurred.
        """
        print(f"Mediator received event: '{event}' from {type(sender).__name__}")
        if event == "ConcreteColleague1 did something":
            self._mediate(sender, "ConcreteColleague2 reacts to an event")
        elif event == "ConcreteColleague2 did something else":
            self._mediate(sender, "ConcreteColleague1 reacts to an event")

    def _mediate(self, sender: Colleague, action: str) -> None:
        """
        Mediates communication between colleagues without causing an infinite loop.

        Args:
            sender (Colleague): The colleague that initiated the action.
            action (str): The action to perform.
        """
        for colleague in self._colleagues:
            if colleague is not sender:
                if action == "ConcreteColleague2 reacts to an event" and isinstance(colleague, ConcreteColleague2):
                    colleague.react(sender)
                elif action == "ConcreteColleague1 reacts to an event" and isinstance(colleague, ConcreteColleague1):
                    colleague.react(sender)


if __name__ == "__main__":
    """Client code that demonstrates the Mediator Design Pattern."""
    mediator = ConcreteMediator()

    colleague1 = ConcreteColleague1(mediator)
    colleague2 = ConcreteColleague2(mediator)

    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)

    colleague1.do_something()
    print()
    colleague2.do_something_else()
