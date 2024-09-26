"""Enum-based State Machine Example: Traffic Lights

Intent: Sometimes using the state design pattern is an overkill. 
In such cases, you can use a simple enum-based state machine.

Example: The state machine for the traffic light cycles through 3 states: RED, GREEN, and YELLOW.
"""
from enum import Enum, auto
from typing import Dict, Callable


class TrafficLightState(Enum):
    """Enum representing the states of a traffic light."""
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

class TrafficLightStateMachine:
    """A state machine for a traffic light, cycling through RED, GREEN, and YELLOW states."""

    def __init__(self, init_state: TrafficLightState) -> None:
        """Initializes the state machine with the init_state
        and sets up transitions and actions tables."""
        self.state = init_state

        self.transitions: Dict[TrafficLightState, Callable[[], None]] = {
            TrafficLightState.RED: self.to_green,
            TrafficLightState.GREEN: self.to_yellow,
            TrafficLightState.YELLOW: self.to_red
        }
        self.actions: Dict[TrafficLightState, Callable[[], None]] = {
            TrafficLightState.RED: self.red_action,
            TrafficLightState.GREEN: self.green_action,
            TrafficLightState.YELLOW: self.yellow_action
        }

    def to_red(self) -> None:
        """Transitions the state machine to the RED state."""
        print("Transitioning to RED")
        self.state = TrafficLightState.RED

    def to_green(self) -> None:
        """Transitions the state machine to the GREEN state."""
        print("Transitioning to GREEN")
        self.state = TrafficLightState.GREEN

    def to_yellow(self) -> None:
        """Transitions the state machine to the YELLOW state."""
        print("Transitioning to YELLOW")
        self.state = TrafficLightState.YELLOW

    def red_action(self) -> None:
        """Performs the action associated with the RED state."""
        print("Stop! The light is RED")

    def green_action(self) -> None:
        """Performs the action associated with the GREEN state."""
        print("Go! The light is GREEN")

    def yellow_action(self) -> None:
        """Performs the action associated with the YELLOW state."""
        print("Caution! The light is YELLOW")

    def transition(self) -> None:
        """Transitions the state machine to the next state."""
        self.transitions[self.state]()

    def perform_action(self) -> None:
        """Performs the action associated with the current state."""
        self.actions[self.state]()


# Usage example
if __name__ == "__main__":
    traffic_light = TrafficLightStateMachine(TrafficLightState.RED)

    # Simulate traffic light changes
    for _ in range(5):  # Cycle through the states multiple times
        traffic_light.perform_action()
        traffic_light.transition()
