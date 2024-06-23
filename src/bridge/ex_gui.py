"""
Bridge Design Pattern

Example: Tkinter GUI application.

The script defines:
- Theme (Implementor interface)
- LightTheme and DarkTheme (Concrete Implementors)
- Application (Abstraction interface)
- SimpleApplication and AdvancedApplication (Refined Abstractions)
"""
from typing import Protocol
import tkinter as tk
from tkinter import ttk


class Theme(Protocol):
    """Implementor Interface using Protocol."""

    def apply_theme(self, root: tk.Tk) -> None:
        ...

class LightTheme:
    """Concrete Implementor A: Light Theme."""

    def apply_theme(self, root: tk.Tk) -> None:
        style = ttk.Style(root)
        style.theme_use('default')  # Using the default 'light' theme

class DarkTheme:
    """Concrete Implementor B: Dark Theme."""

    def apply_theme(self, root: tk.Tk) -> None:
        style = ttk.Style(root)
        style.theme_use('clam')  # Using an alternative 'dark' theme

class Application(Protocol):
    """Abstraction using Protocol."""

    def __init__(self, theme: Theme) -> None:
        ...

    def render(self) -> None:
        ...

class SimpleApplication:
    """Refined Abstraction A: Simple Application."""

    def __init__(self, theme: Theme) -> None:
        """
        Initializes the SimpleApplication with a given theme.
        """
        self._theme = theme
        self._root = tk.Tk()

    def render(self) -> None:
        self._theme.apply_theme(self._root)
        self._root.title("Simple Application")
        ttk.Label(self._root, text="Welcome to the Simple App!").pack(pady=20)
        ttk.Button(self._root, text="Close", command=self._root.quit).pack(pady=10)
        self._root.mainloop()


class AdvancedApplication:
    """Refined Abstraction B: Advanced Application."""

    def __init__(self, theme: Theme) -> None:
        """
        Initializes the AdvancedApplication with a given theme.
        """
        self._theme = theme
        self._root = tk.Tk()

    def render(self) -> None:
        self._theme.apply_theme(self._root)
        self._root.title("Advanced Application")
        ttk.Label(self._root, text="Welcome to the Advanced App!").pack(pady=20)
        ttk.Entry(self._root).pack(pady=10)
        ttk.Button(self._root, text="Submit").pack(pady=10)
        ttk.Button(self._root, text="Close", command=self._root.quit).pack(pady=10)
        self._root.mainloop()


if __name__ == "__main__":
    """
    Client code to select the type of application and theme, and render the application.
    """
    # Select the type of application and theme
    theme = LightTheme()  # or DarkTheme()
    application = SimpleApplication(theme)  # or AdvancedApplication(theme)

    application.render()
