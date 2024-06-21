"""
Decorator Design Pattern

Example: Document Processor with Spell Check and Grammar Check Decorators
"""

from typing import Protocol


class Processable(Protocol):
    def process(self, text: str) -> str:
        ...

class DocumentProcessor(Processable):
    """Document processor base class."""

    def process(self, text):
        return f"Processing document: {text}"

class SpellCheckDecorator(DocumentProcessor):
    """Spell check decorator for document processing."""

    def __init__(self, processor):
        self._processor = processor

    def process(self, text):
        spell_checked_text = f"SpellChecked({text})"
        return self._processor.process(spell_checked_text)

class GrammarCheckDecorator(DocumentProcessor):
    """Grammar check decorator for document processing."""

    def __init__(self, processor):
        self._processor = processor

    def process(self, text):
        grammar_checked_text = f"GrammarChecked({text})"
        return self._processor.process(grammar_checked_text)

def client_code(processor: Processable):
    """Client code is not aware whether it works with base processor
    or with decorated one."""
    print(processor.process("This is a test document."))


if __name__ == "__main__":
    # Client code
    processor = DocumentProcessor()
    enhanced_processor = GrammarCheckDecorator(SpellCheckDecorator(processor))
    print("Lets give to client a simple document processor:")
    client_code(processor)
    print("\nLets give to client an enhanced document processor:")
    client_code(enhanced_processor)