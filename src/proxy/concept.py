"""
Proxy Pattern

A proxy is a class that functions as an interface to something else, such as a network connection, 
a large object in memory, a file, or another object. It acts as a wrapper that the client calls to
access the real object behind the scenes. The proxy can simply forward requests to the real object
or provide additional functionality, such as caching or checking preconditions. For the client, 
using a proxy is similar to using the real object because both implement the same interface.
"""

from typing import Protocol

class Subject(Protocol):
    """Subject protocol that defines the common interface for RealSubject and Proxy."""

    def request(self) -> None:
        ...

class RealSubject(Subject):
    """RealSubject class that implements the actual business logic."""

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """Proxy class that acts as a RealSubject.

    Attributes:
        _real_subject (RealSubject): The real subject being proxied.

    Methods:
        request() -> None:
            Controls access to the RealSubject's request method.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        """Initializes the Proxy with a RealSubject.

        Args:
            real_subject (RealSubject): The real subject being proxied.
        """
        self._real_subject = real_subject

    def request(self) -> None:
        """We can implement additional functionality here before or after forwarding the request to the RealSubject."""
        print("Logic before forwarding the request to the RealSubject.")
        self._real_subject.request()
        print("Logic after forwarding the request to the RealSubject.")


# Example usage
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print("Client: Executing the client code with a proxy:")
    proxy.request()
