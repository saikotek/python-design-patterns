# This script demonstrates the use of the Observer design pattern with Python's Protocol type.
# Protocols in Python allow for structural subtyping (duck typing), enabling type checking based on
# the presence of methods and properties rather than explicit inheritance.

from abc import ABC, abstractmethod
from typing import List, Protocol

# Define the Observer protocol, specifying that any observer must implement the update method.
class Observer(Protocol):
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        pass

# Define the abstract base class for the Subject.
class Subject(ABC):
    def __init__(self) -> None:
        # Initialize the list of observers.
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        # Attach an observer to the subject if not already attached.
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # Detach an observer from the subject.
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        # Notify all observers about the state change.
        for observer in self._observers:
            observer.update(self)

# Concrete implementation of the Subject, representing a Stock.
class Stock(Subject):
    def __init__(self, price: float) -> None:
        super().__init__()
        self._price = price
    
    def attach(self, observer: Observer) -> None:
        super().attach(observer)
        print(f"{observer} attached to the stock.")
        
    def detach(self, observer: Observer) -> None:
        super().detach(observer)
        print(f"{observer} detached from the stock.")
    
    @property
    def price(self) -> float:
        # Get the current price of the stock.
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        print(f"Setting new price: {value}")
        # Set a new price for the stock and notify observers.
        self._price = value
        self.notify()

# Concrete implementation of the Observer, representing a Client.
class Client(Observer):
    def __init__(self, name: str) -> None:
        self._name = name
    
    def __str__(self):
        return self._name
    
    def update(self, subject: Subject) -> None:
        # Handle the update notification from the subject.
        if isinstance(subject, Stock):
            print(f'{self._name} notified. New stock price: {subject.price}')

# Usage example
if __name__ == "__main__":
    # Create a Stock subject and two Client observers.
    stock = Stock(100.0)
    client1 = Client("Client 1")
    client2 = Client("Client 2")

    # Attach the clients to the stock.
    stock.attach(client1)
    stock.attach(client2)

    # Change the stock price, notifying both clients.
    stock.price = 105.0
    stock.price = 110.0

    # Detach one client and change the stock price again.
    stock.detach(client1)
    stock.price = 95.0  # Only client2 is notified
