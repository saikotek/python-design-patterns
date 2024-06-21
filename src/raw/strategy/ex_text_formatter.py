from typing import Protocol

class TextFormatter(Protocol):
    def format(self, text: str) -> str:
        pass

class PlainTextFormatter:
    def format(self, text: str) -> str:
        return text

class HTMLFormatter:
    def format(self, text: str) -> str:
        return f"<html><body>{text}</body></html>"

class MarkdownFormatter:
    def format(self, text: str) -> str:
        return f"**{text}**"

class Document:
    def __init__(self, formatter: TextFormatter) -> None:
        self._formatter = formatter

    def set_formatter(self, formatter: TextFormatter) -> None:
        self._formatter = formatter

    def display(self, text: str) -> None:
        formatted_text = self._formatter.format(text)
        print(formatted_text)

# Usage
doc = Document(PlainTextFormatter())
doc.display("Hello, World!")

doc.set_formatter(HTMLFormatter())
doc.display("Hello, World!")

doc.set_formatter(MarkdownFormatter())
doc.display("Hello, World!")
