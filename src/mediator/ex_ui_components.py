"""
Mediator Pattern Example: UI Components

In this example, the Mediator coordinates communication between UI components
such as buttons and text fields. E.g. when a button is clicked, the mediator is
notified and can respond by updating the text field.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol


class Mediator(Protocol):
    """Mediator interface for handling communication between components."""

    @abstractmethod
    def notify(self, sender: Component, event: str) -> None:
        ...

class Component(ABC):
    """Abstract Component class that has a reference to the mediator."""

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Button(Component):
    """Concrete Button component that triggers events."""

    def trigger(self) -> None:
        """
        Triggers the button click event and notifies the mediator.
        """
        if self.mediator:
            self.mediator.notify(self, "button_clicked")

class TextField(Component):
    """Concrete TextField component that holds and changes text."""

    def __init__(self, mediator: Mediator = None) -> None:
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text: str) -> None:
        """
        Sets the text of the text field and notifies the mediator.
        """
        self.text = text
        if self.mediator:
            self.mediator.notify(self, "text_changed")

class Dialog(Mediator):
    """Concrete Mediator class that coordinates communication between components."""

    def __init__(self) -> None:
        """Initializes the dialog with a button and a text field."""
        self.button = Button(self)
        self.text_field = TextField(self)

    def notify(self, sender: Component, event: str) -> None:
        """
        Handles notifications from components and coordinates responses.
        """
        if event == "button_clicked":
            self.handle_button_click()
        elif event == "text_changed":
            self.handle_text_change()

    def handle_button_click(self) -> None:
        """Handles the button click event."""
        print(f"Button clicked, text field says: {self.text_field.text}")

    def handle_text_change(self) -> None:
        """Handles the text change event."""
        print(f"Text field changed, new text: {self.text_field.text}")


if __name__ == "__main__":
    # Usage
    dialog = Dialog()
    dialog.text_field.set_text("Hello World")
    dialog.button.trigger()
    dialog.text_field.set_text("Goodbye World")
    dialog.button.trigger()
