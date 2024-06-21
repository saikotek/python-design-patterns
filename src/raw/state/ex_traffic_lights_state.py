# Class-based state machine implementation using the state design pattern
# The state machine for the traffic light cycles through 3 states: RED, GREEN, and YELLOW. 

from typing import Protocol

# Protocol that defines the interface for all state classes
class TrafficLightState(Protocol):
    def transition(self, context: 'TrafficLightContext') -> None:
        pass

    def perform_action(self) -> None:
        pass

# Concrete state class representing the RED light state
class RedState:
    def transition(self, context: 'TrafficLightContext') -> None:
        print("Transitioning to GREEN")
        context.state = GreenState()

    def perform_action(self) -> None:
        print("Stop! The light is RED")

# Concrete state class representing the GREEN light state
class GreenState:
    def transition(self, context: 'TrafficLightContext') -> None:
        print("Transitioning to YELLOW")
        context.state = YellowState()

    def perform_action(self) -> None:
        print("Go! The light is GREEN")

# Concrete state class representing the YELLOW light state
class YellowState:
    def transition(self, context: 'TrafficLightContext') -> None:
        print("Transitioning to RED")
        context.state = RedState()

    def perform_action(self) -> None:
        print("Caution! The light is YELLOW")

# Context class that maintains a reference to the current state
class TrafficLightContext:
    def __init__(self) -> None:
        # Initialize the traffic light to the RED state
        self.state: TrafficLightState = RedState()

    def transition(self) -> None:
        # Delegate the transition to the current state
        self.state.transition(self)

    def perform_action(self) -> None:
        # Delegate the action to the current state
        self.state.perform_action()

# Usage example
if __name__ == "__main__":
    traffic_light = TrafficLightContext()

    # Simulate traffic light changes
    for _ in range(5):  # Cycle through the states multiple times
        traffic_light.perform_action()  # Perform action of the current state
        traffic_light.transition()      # Transition to the next state
