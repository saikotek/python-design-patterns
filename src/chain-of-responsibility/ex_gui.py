"""
Chain of Responsibility Pattern Example: GUI Components with Contextual Help
"""
from __future__ import annotations
from typing import Optional, Protocol


class ComponentWithContextualHelp(Protocol):
    """Protocol for components with contextual help."""

    def show_help(self):
        ...

class Component(ComponentWithContextualHelp):
    """Base component class implementing contextual help."""

    def __init__(self, tooltip_text: Optional[str] = None):
        """
        Initializes a new Component with optional tooltip text.
        """
        self.container: Container = None
        self.tooltip_text: Optional[str] = tooltip_text

    def set_container(self, container: Container):
        """
        Sets the container of the component.
        """
        self.container = container

    def show_help(self):
        if self.tooltip_text:
            print(f"Tooltip: {self.tooltip_text}")
        elif self.container:
            self.container.show_help()

class Container(Component):
    """Container class for holding child components."""

    def __init__(self, tooltip_text: Optional[str] = None):
        """
        Initializes a new Container with optional tooltip text.
        """
        super().__init__(tooltip_text)
        self.children = []

    def add(self, child):
        """
        Adds a child component to the container.
        """
        self.children.append(child)
        child.set_container(self)

    def show_help(self):
        if self.tooltip_text:
            print(f"Tooltip: {self.tooltip_text}")
        elif self.container:
            self.container.show_help()
        else:
            print("No help available")

class Button(Component):
    """Button class implementing contextual help."""

    def show_help(self):
        super().show_help()

class Panel(Container):
    """Panel class implementing contextual help with optional modal help text."""

    def __init__(self, tooltip_text: Optional[str] = None,
                 modal_help_text: Optional[str] = None):
        """
        Initializes a new Panel with optional tooltip and modal help text.
        """
        super().__init__(tooltip_text)
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text:
            print(f"Modal Help: {self.modal_help_text}")
        else:
            super().show_help()

class Dialog(Container):
    """Dialog class implementing contextual help with optional wiki page URL."""

    def __init__(self, tooltip_text=None, wiki_page_url=None):
        """
        Initializes a new Dialog with optional tooltip text and wiki page URL.
        """
        super().__init__(tooltip_text)
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        if self.wiki_page_url:
            print(f"Opening wiki page: {self.wiki_page_url}")
        else:
            super().show_help()


def client_code(component: ComponentWithContextualHelp):
    """
    Client code to trigger help for a component.

    Args:
        component (Component): The component to trigger help for.
    """
    print(f"Client: I've got a {component.__class__.__name__}")
    component.show_help()


if __name__ == "__main__":
    # Create components
    button1 = Button(tooltip_text="Button 1 Help")
    button2 = Button(tooltip_text="Button 2 Help")

    # Create containers
    panel = Panel(modal_help_text="Panel Help")
    dialog = Dialog(wiki_page_url="http://help.example.com")

    # Build the hierarchy
    panel.add(button1)
    dialog.add(panel)
    dialog.add(button2)

    # Trigger help
    client_code(button1)  # Should show "Button 1 Help"
    client_code(panel)    # Should show "Panel Help"
    client_code(dialog)   # Should open the wiki page

    # No help available
    button_no_tooltip = Button()
    panel_no_tooltip = Panel()
    panel_no_tooltip.add(button_no_tooltip)
    client_code(button_no_tooltip)
