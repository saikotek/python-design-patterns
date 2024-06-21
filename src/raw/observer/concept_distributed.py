# The distributed observer pattern allows components to act as both publishers and subscribers. 
# Each component can dynamically subscribe to events published by other components and publish
# its own events to notify subscribers. This pattern eliminates the need for a central mediator,
# enabling a decentralized and flexible communication network.

from typing import List, Dict, Any, Protocol

# Define the Observer protocol
class Observer(Protocol):
    def update(self, event: str, *args: Any, **kwargs: Any) -> None:
        pass

# Component class acting both as a publisher and subscriber
class Component:
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
    # Create components
    component1 = Component("Component 1")
    component2 = Component("Component 2")
    component3 = Component("Component 3")

    # Subscribe components to each other's events
    component1.subscribe("event_x", component2)
    component2.subscribe("event_y", component1)
    component3.subscribe("event_x", component1)
    component3.subscribe("event_y", component2)

    # Publish events
    component1.publish("event_x", "Data for event_x from Component 1")
    component2.publish("event_y", "Data for event_y from Component 2")
    component3.publish("event_x", "Data for event_x from Component 3")
    component3.publish("event_y", "Data for event_y from Component 3")
