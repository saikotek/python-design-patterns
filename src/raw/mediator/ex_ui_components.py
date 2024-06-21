# Mediator Design Pattern real-world example
# UI components

from abc import ABC, abstractmethod

# Abstract Mediator class
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Abstract Component class
class Component(ABC):
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

# Concrete components
class Button(Component):
    def trigger(self):
        if self.mediator:
            self.mediator.notify(self, "button_clicked")

class TextField(Component):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text):
        self.text = text
        if self.mediator:
            self.mediator.notify(self, "text_changed")

# Concrete Mediator class
class Dialog(Mediator):
    def __init__(self):
        self.button = Button(self)
        self.text_field = TextField(self)

    def notify(self, sender, event):
        if event == "button_clicked":
            self.handle_button_click()
        elif event == "text_changed":
            self.handle_text_change()

    def handle_button_click(self):
        print(f"Button clicked, text field says: {self.text_field.text}")

    def handle_text_change(self):
        print(f"Text field changed, new text: {self.text_field.text}")


if __name__ == "__main__":
    # Usage
    dialog = Dialog()
    dialog.text_field.set_text("Hello World")
    dialog.button.trigger()
    dialog.text_field.set_text("Goodbye World")
    dialog.button.trigger()
