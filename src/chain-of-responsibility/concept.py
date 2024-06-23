"""
Chain of Responsibility Design Pattern

Intent: Allows an object to pass a request along a chain of handlers. 
Each handler in the chain decides either to process the request or
to pass it along the chain to the next handler.
"""
from __future__ import annotations
from abc import ABC
from typing import Optional

class Handler(ABC):
    """Handler defines an interface for handling requests and optionally
    sets a successor."""

    def __init__(self):
        self.successor: Optional[Handler] = None

    def set_successor(self, successor: Handler) -> None:
        """
        Sets the successor handler.

        Args:
            successor (Handler): The next handler in the chain.
        """
        self.successor = successor

    def handle_request(self, request: int) -> None:
        """
        Handles the request or passes it to the successor.

        Args:
            request (int): The request to be handled.
        """
        if self.successor:
            self.successor.handle_request(request)


class ConcreteHandler1(Handler):
    """ConcreteHandler1 handles requests it is responsible for, otherwise
    passes them to the successor."""

    def handle_request(self, request: int) -> None:
        """
        Handles the request or passes it to the successor.

        Args:
            request (int): The request to be handled.
        """
        if 0 <= request < 10:
            print(f"ConcreteHandler1 handled request {request}")
        else:
            super().handle_request(request)


class ConcreteHandler2(Handler):
    """ConcreteHandler2 handles requests it is responsible for, otherwise 
    passes them to the successor."""

    def handle_request(self, request: int) -> None:
        """
        Handles the request or passes it to the successor.

        Args:
            request (int): The request to be handled.
        """
        if 10 <= request < 20:
            print(f"ConcreteHandler2 handled request {request}")
        else:
            super().handle_request(request)


class ConcreteHandler3(Handler):
    """ConcreteHandler3 handles requests it is responsible for, otherwise
    passes them to the successor."""

    def handle_request(self, request: int) -> None:
        """
        Handles the request or passes it to the successor.

        Args:
            request (int): The request to be handled.
        """
        if 20 <= request < 30:
            print(f"ConcreteHandler3 handled request {request}")
        else:
            super().handle_request(request)


if __name__ == "__main__":
    """Client code that demonstrates the Chain of Responsibility Design Pattern."""
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.set_successor(handler2)
    handler2.set_successor(handler3)

    # Generate and process requests
    requests = [2, 5, 14, 22, 18, 27, 3, 20, 25]
    for request in requests:
        handler1.handle_request(request)
