"""
Abstract Factory Design Pattern
Example: GUI Factory

This module demonstrates the Abstract Factory design pattern by creating
families of related UI elements without specifying their concrete classes.
"""
from typing import Protocol


class Button(Protocol):
    """Product interface for buttons."""

    def click(self) -> None:
        ...


class TextBox(Protocol):
    """Product interface for text boxes."""

    def render(self) -> None:
        ...


class UIFactory(Protocol):
    """Abstract factory interface for creating related UI elements."""

    def create_button(self) -> Button:
        ...

    def create_textbox(self) -> TextBox:
        ...


class WindowsButton:
    """Concrete Windows-style button."""

    def click(self) -> None:
        print("Windows button clicked!")


class WindowsTextBox:
    """Concrete Windows-style text box."""

    def render(self) -> None:
        print("Rendering a Windows-style text box.")


class MacButton:
    """Concrete Mac-style button."""

    def click(self) -> None:
        print("Mac button clicked!")


class MacTextBox:
    """Concrete Mac-style text box."""

    def render(self) -> None:
        print("Rendering a Mac-style text box.")


class WindowsFactory:
    """Concrete factory for Windows-style UI elements."""

    def create_button(self) -> Button:
        return WindowsButton()

    def create_textbox(self) -> TextBox:
        return WindowsTextBox()


class MacFactory:
    """Concrete factory for Mac-style UI elements."""

    def create_button(self) -> Button:
        return MacButton()

    def create_textbox(self) -> TextBox:
        return MacTextBox()


def display_ui_elements(factory: UIFactory) -> None:
    """Client function to display UI elements.

    Args:
        factory (UIFactory): The abstract factory used to create UI elements.
    """
    button = factory.create_button()
    textbox = factory.create_textbox()

    button.click()
    textbox.render()


if __name__ == "__main__":
    # Example usage: switch between Windows and Mac factories
    print("Using Windows Factory:")
    windows_factory = WindowsFactory()
    display_ui_elements(windows_factory)

    print("\nUsing Mac Factory:")
    mac_factory = MacFactory()
    display_ui_elements(mac_factory)
