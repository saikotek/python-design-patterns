"""
Command Design Pattern

Intent: Turns a request into a stand-alone object which allows 
parameterization of clients with different requests, queuing of requests,
and support for undoable operations.
"""
from __future__ import annotations
from typing import Protocol, List

class Command(Protocol):
    """Command declares an interface for executing an operation."""

    def execute(self) -> None:
        """Executes the command."""
        ...


class ConcreteCommand(Command):
    """ConcreteCommand implements the Command interface to perform an operation by invoking a receiver."""

    def __init__(self, receiver: Receiver, action: str):
        """
        Initializes the command with a receiver and an action.

        Args:
            receiver (Receiver): The receiver of the command.
            action (str): The action to perform.
        """
        self.receiver = receiver
        self.action = action

    def execute(self) -> None:
        """Executes the command by invoking the receiver's action."""
        if self.action == 'action1':
            self.receiver.action1()
        elif self.action == 'action2':
            self.receiver.action2()


class Receiver:
    """Receiver knows how to perform the operations associated with carrying out a request."""

    def action1(self) -> None:
        """Performs action1."""
        print("Receiver: Executing action1")

    def action2(self) -> None:
        """Performs action2."""
        print("Receiver: Executing action2")


class Invoker:
    """Invoker asks the command to carry out the request."""

    def __init__(self):
        self.commands: List[Command] = []

    def store_command(self, command: Command) -> None:
        """
        Stores the command to be executed later.

        Args:
            command (Command): The command to store.
        """
        self.commands.append(command)

    def execute_commands(self) -> None:
        """Executes all stored commands."""
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    """Client code that demonstrates the Command Design Pattern."""
    receiver = Receiver()

    command1 = ConcreteCommand(receiver, 'action1')
    command2 = ConcreteCommand(receiver, 'action2')

    invoker = Invoker()
    invoker.store_command(command1)
    invoker.store_command(command2)

    invoker.execute_commands()
