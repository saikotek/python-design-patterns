"""
State Design Pattern

Intent: Lets an object alter its behavior when its internal state changes. It
appears as if the object changed its class. This is close concept to finite state machines.
"""
from __future__ import annotations
from typing import Protocol


class Context:
    """Context maintains an instance of a State that defines the current state.

    Attributes:
        state (State): The current state of the context.
    """

    def __init__(self, state: State) -> None:
        """Initializes the Context with an initial state.

        Args:
            state (State): The initial state of the context.
        """
        self._state = state
        self._state.context = self

    @property
    def state(self) -> State:
        """Gets the current state of the context.

        Returns:
            State: The current state of the context.
        """
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        """Sets a new state for the context.

        Args:
            state (State): The new state to be set.
        """
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request(self) -> None:
        """Triggers a request, which delegates the behavior to the current state."""
        self._state.handle()

class State(Protocol):
    """State interface declares a method for handling requests."""

    context: Context

    def handle(self) -> None:
        """Handles the request according to the current state."""
        ...

class ConcreteStateA:
    """ConcreteStateA implements the behavior associated with a state.

    Attributes:
        context (Context): The context associated with this state.
    """

    context: Context

    def handle(self) -> None:
        """Handles the request and transitions to ConcreteStateB."""
        print("ConcreteStateA handles the request and transitions to ConcreteStateB.")
        self.context.state = ConcreteStateB()

class ConcreteStateB:
    """ConcreteStateB implements the behavior associated with a state.

    Attributes:
        context (Context): The context associated with this state.
    """

    context: Context

    def handle(self) -> None:
        """Handles the request and transitions to ConcreteStateA."""
        print("ConcreteStateB handles the request and transitions to ConcreteStateA.")
        self.context.state = ConcreteStateA()


# Example usage:
if __name__ == "__main__":
    initial_state = ConcreteStateA()
    context = Context(initial_state)

    context.request()  # ConcreteStateA handles the request and transitions to ConcreteStateB.
    context.request()  # ConcreteStateB handles the request and transitions to ConcreteStateA.
