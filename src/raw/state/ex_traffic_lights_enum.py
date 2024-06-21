# Enum-based state machine implementation
# Sometimes using state design pattern is an overkill.
# In such cases, you can use a simple enum-based state machine.

# The state machine for the traffic light cycles through 3 states: RED, GREEN, and YELLOW.

from enum import Enum, auto
from typing import Dict, Callable

class TrafficLightState(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()

# The transitions between states and the actions performed in each state
# are managed by a TrafficLightStateMachine class.
class TrafficLightStateMachine:
    def __init__(self) -> None:
        self.state = TrafficLightState.RED

        # Define state transitions: each state points to the function for the next state.
        self.transitions: Dict[TrafficLightState, Callable[[], None]] = {
            TrafficLightState.RED: self.to_green,
            TrafficLightState.GREself.to_yellow,
            TrafficLightState.YELLOW: self.to_red
        }
        # Define actions for each state
        self.actions: Dict[TrafficLightState, Callable[[], None]] = {
            TrafficLightState.RED: self.red_action,
            TrafficLightState.GREself.green_action,
            TrafficLightState.YELLOW: self.yellow_action
        }

    def to_red(self) -> None:
        print("Transitioning to RED")
        self.state = TrafficLightState.RED

    def to_green(self) -> None:
        print("Transitioning to GREEN")
        self.state = TrafficLightState.GREEN

    def to_yellow(self) -> None:
        print("Transitioning to YELLOW")
        self.state = TrafficLightState.YELLOW

    def red_action(self) -> None:
        print("Stop! The light is RED")

    def green_action(self) -> None:
        print("Go! The light is GREEN")

    def yellow_action(self) -> None:
        print("Caution! The light is YELLOW")

    def transition(self) -> None:
        self.transitions[self.state]()

    def perform_action(self) -> None:
        self.actions[self.state]()


# Usage example
if __name__ == "__main__":
    traffic_light = TrafficLightStateMachine()

    # Simulate traffic light changes
    for _ in range(5):  # Cycle through the states multiple times
        traffic_light.perform_action()
        traffic_light.transition()
