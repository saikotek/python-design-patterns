"""
Command Pattern Example: Text Editor with Undo Functionality
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    """
    Abstract base class for commands.

    Attributes:
        editor (Editor): The editor instance the command operates on.
        backup (str): Backup of the editor's text.
    """

    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    def save_backup(self):
        """Saves a backup of the current editor text."""
        self.backup = self.editor.text

    def undo(self):
        """Restores the editor text from the backup."""
        self.editor.text = self.backup

    @abstractmethod
    def execute(self):
        """Executes the command."""
        pass


class CopyCommand(Command):
    """
    Command to copy text to the clipboard.
    """

    def __init__(self, editor, clipboard):
        super().__init__(editor)
        self.clipboard = clipboard

    def execute(self):
        """Copies the selected text to the clipboard."""
        print("Executing CopyCommand")
        self.clipboard.content = self.editor.get_selection()
        return False

class CutCommand(Command):
    """
    Command to cut text to the clipboard.
    """

    def __init__(self, editor, clipboard):
        super().__init__(editor)
        self.clipboard = clipboard

    def execute(self):
        """Cuts the selected text to the clipboard and deletes it from the editor."""
        print("Executing CutCommand")
        self.save_backup()
        self.clipboard.content = self.editor.get_selection()
        self.editor.delete_selection()
        return True

class PasteCommand(Command):
    """
    Command to paste text from the clipboard.
    """

    def __init__(self, editor, clipboard):
        super().__init__(editor)
        self.clipboard = clipboard

    def execute(self):
        """Pastes the text from the clipboard into the editor."""
        print("Executing PasteCommand")
        self.save_backup()
        self.editor.replace_selection(self.clipboard.content)
        return True

class UndoCommand(Command):
    """Command to undo the last operation."""

    def execute(self):
        """Undoes the last operation by restoring the editor text from the backup."""
        print("Executing UndoCommand")
        self.undo()
        return False

class CommandHistory:
    """Class to maintain a history of executed commands."""

    def __init__(self):
        self.history: List[Command] = []

    def push(self, command: Command):
        """
        Pushes a command onto the history stack.
        """
        self.history.append(command)

    def pop(self):
        """
        Pops a command from the history stack.
        """
        if self.history:
            return self.history.pop()
        return None

class Clipboard:
    """Class to represent a clipboard for storing text."""

    def __init__(self):
        self.content = ""

class Editor:
    """Class to represent an editor for editing text."""

    def __init__(self):
        self.text = ""

    def get_selection(self):
        """
        Gets the selected text in the editor.
        """
        return self.text

    def delete_selection(self):
        """Deletes the selected text in the editor."""
        self.text = ""

    def replace_selection(self, text):
        """
        Replaces the selected text in the editor with the given text.
        """
        self.text = text

class Application:
    """Class to represent the application containing the editors and command history."""

    def __init__(self):
        self.editors: List[Editor] = []
        self.active_editor: Editor | None = None
        self.clipboard = Clipboard()
        self.history = CommandHistory()

    def create_ui(self):
        """Creates the user interface and initializes the active editor."""
        self.active_editor = Editor()
        self.editors.append(self.active_editor)

    def execute_command(self, command: Command):
        """
        Executes a command and pushes it onto the history stack if it modifies the editor.
        """
        if command.execute():
            self.history.push(command)

    def undo(self):
        """Undoes the last command in the history stack."""
        command = self.history.pop()
        if command:
            command.undo()


if __name__ == "__main__":
    """Example usage of the command pattern with an editor application."""

    app = Application()
    app.create_ui()

    # Create commands
    copy_cmd = CopyCommand(app.active_editor, app.clipboard)
    cut_cmd = CutCommand(app.active_editor, app.clipboard)
    paste_cmd = PasteCommand(app.active_editor, app.clipboard)
    undo_cmd = UndoCommand(app.active_editor)

    # Execute commands
    app.active_editor.text = "Hello, World!"
    app.execute_command(copy_cmd)
    app.execute_command(cut_cmd)
    print("Current text in editor:", app.active_editor.text)
    app.execute_command(paste_cmd)
    print("Current text in editor:", app.active_editor.text)
    app.execute_command(undo_cmd)
    print("Current text in editor:", app.active_editor.text)
