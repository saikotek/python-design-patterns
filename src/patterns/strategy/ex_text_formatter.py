"""
Strategy Pattern Example: Changing text formatting strategies in a document editor.
"""
from typing import Protocol


class TextFormatter(Protocol):
    """Protocol that defines the interface for text formatting strategies."""

    def format(self, text: str) -> str:
        """Formats the given text."""
        ...

class PlainTextFormatter:
    """Concrete strategy for plain text formatting."""

    def format(self, text: str) -> str:
        return text

class HTMLFormatter:
    """Concrete strategy for HTML text formatting."""

    def format(self, text: str) -> str:
        """Formats the text as HTML."""
        return f"<html><body>{text}</body></html>"

class MarkdownFormatter:
    """Concrete strategy for Markdown text formatting."""

    def format(self, text: str) -> str:
        """Formats the text as Markdown."""
        return f"**{text}**"

class Document:
    """Context class that uses a TextFormatter to format and display text."""

    def __init__(self, formatter: TextFormatter) -> None:
        """Initializes the document with a specific text formatter."""
        self._formatter = formatter

    def set_formatter(self, formatter: TextFormatter) -> None:
        """Sets a new text formatter."""
        print(f"Changing formatter to {formatter.__class__.__name__}")
        self._formatter = formatter

    def display(self, text: str) -> None:
        """Formats and displays the text using the current formatter."""
        formatted_text = self._formatter.format(text)
        print(formatted_text)


# Usage
if __name__ == "__main__":
    doc = Document(PlainTextFormatter())
    doc.display("Hello, World!")

    doc.set_formatter(HTMLFormatter())
    doc.display("Hello, World!")

    doc.set_formatter(MarkdownFormatter())
    doc.display("Hello, World!")
