# The distributed observer pattern allows components to act as both publishers and subscribers. 
# In a smart home automation system, various devices need to interact based on different events.

from typing import List, Dict, Any, Protocol

# Define the Observer protocol
class Observer(Protocol):
    def update(self, event: str, *args: Any, **kwargs: Any) -> None:
        pass

# Device class acting both as a publisher and subscriber
class Device:
    def __init__(self, name: str) -> None:
        self.name = name
        self._subscribers: Dict[str, List[Observer]] = {}

    def subscribe(self, event: str, observer: Observer) -> None:
        if event not in self._subscribers:
            self._subscribers[event] = []
        self._subscribers[event].append(observer)

    def unsubscribe(self, event: str, observer: Observer) -> None:
        if event in self._subscribers:
            try:
                self._subscribers[event].remove(observer)
            except ValueError:
                pass

    def publish(self, event: str, *args: Any, **kwargs: Any) -> None:
        if event in self._subscribers:
            for subscriber in self._subscribers[event]:
                subscriber.update(event, *args, **kwargs)

    def update(self, event: str, *args: Any, **kwargs: Any) -> None:
        print(f"{self.name} received {event}: {args} {kwargs}")

# Usage example
if __name__ == "__main__":
    # Create devices
    light = Device("Smart Light")
    thermostat = Device("Thermostat")
    camera = Device("Security Camera")
    door_lock = Device("Door Lock")
    motion_sensor = Device("Motion Sensor")
    doorbell = Device("Doorbell")
    window_sensor = Device("Window Sensor")

    # Subscribe devices to events
    motion_sensor.subscribe("motion_detected", light)
    motion_sensor.subscribe("motion_detected", camera)
    doorbell.subscribe("button_pressed", camera)
    doorbell.subscribe("button_pressed", door_lock)
    window_sensor.subscribe("window_opened", thermostat)
    window_sensor.subscribe("window_closed", thermostat)

    # Publish events
    motion_sensor.publish("motion_detected", "Motion detected in the living room")
    doorbell.publish("button_pressed", "Doorbell pressed")
    window_sensor.publish("window_opened", "Window opened in the bedroom")
    window_sensor.publish("window_closed", "Window closed in the bedroom")
