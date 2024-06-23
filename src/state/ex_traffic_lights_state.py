"""State Design Pattern

Class-based state machine implementation using the state design pattern.

Example: The state machine for the traffic light cycles through 3 states: RED, GREEN, and YELLOW.
"""
from __future__ import annotations
from typing import Protocol

class TrafficLightState(Protocol):
    """Protocol that defines the interface for all state classes."""

    def transition(self, context: TrafficLightContext) -> None:
        """Transitions to the next state."""
        ...

    def perform_action(self) -> None:
        """Performs the action associated with the current state."""
        ...

class RedState:
    """Concrete state class representing the RED light state."""

    def transition(self, context: TrafficLightContext) -> None:
        print("Transitioning to GREEN")
        context.state = GreenState()

    def perform_action(self) -> None:
        print("Stop! The light is RED")

class GreenState:
    """Concrete state class representing the GREEN light state."""

    def transition(self, context: TrafficLightContext) -> None:
        print("Transitioning to YELLOW")
        context.state = YellowState()

    def perform_action(self) -> None:
        print("Go! The light is GREEN")

class YellowState:
    """Concrete state class representing the YELLOW light state."""

    def transition(self, context: TrafficLightContext) -> None:
        print("Transitioning to RED")
        context.state = RedState()

    def perform_action(self) -> None:
        print("Caution! The light is YELLOW")

class TrafficLightContext:
    """Context class that maintains a reference to the current state."""

    def __init__(self) -> None:
        """Initializes the traffic light to the RED state."""
        self.state: TrafficLightState = RedState()

    def transition(self) -> None:
        """Delegates the transition to the current state."""
        self.state.transition(self)

    def perform_action(self) -> None:
        """Delegates the action to the current state."""
        self.state.perform_action()


# Usage example
if __name__ == "__main__":
    traffic_light = TrafficLightContext()

    # Simulate traffic light changes
    for _ in range(5):  # Cycle through the states multiple times
        traffic_light.perform_action()  # Perform action of the current state
        traffic_light.transition()      # Transition to the next state
