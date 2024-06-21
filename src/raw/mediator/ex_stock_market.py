"""
Mediator Design Pattern

Example: Stock Market
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
import enum
from typing import List


class EventType(enum.Enum):
    """EventType enum represents types of events in the stock market."""
    TRADE = 1
    QUOTE = 2

class Mediator(ABC):
    """Mediator base class for handling communication between components."""

    @abstractmethod
    def notify(self, sender: Component, event: EventType, *args) -> None:
        """
        Notifies the mediator about an event.

        Args:
            sender (Component): The component that sent the event.
            event (EventType): The type of event.
            *args: Additional arguments for the event.
        """
        pass

class Component(ABC):
    """Component base class which has a reference to the mediator."""

    def __init__(self, mediator: Mediator) -> None:
        self.mediator = mediator

class Trader(Component):
    """Trader class can place an offer to an instrument."""

    def __init__(self, mediator: Mediator, name: str) -> None:
        super().__init__(mediator)
        self.name = name

    def trade(self, instrument: str, price: float, amount: int) -> None:
        """
        Sends a trade offer to the mediator.

        Args:
            instrument (str): The instrument to trade.
            price (float): The price of the instrument.
            amount (int): The amount of the instrument to trade.
        """
        self.mediator.notify(self, EventType.TRADE, instrument, price, amount)

@dataclass
class Offer:
    """Offer class represents a trade offer."""
    trader: Trader
    price: float
    amount: int

class Instrument(Component):
    """Instrument class represents market instrument. It accepts offers and can be quoted."""

    offers: List[Offer] = []

    def __init__(self, mediator: Mediator, name: str) -> None:
        """
        Initializes the instrument with a mediator and a name.

        Args:
            mediator (Mediator): The mediator instance.
            name (str): The name of the instrument.
        """
        super().__init__(mediator)
        self.name = name
        self.offers = []

    def add_offer(self, trader: Trader, price: float, amount: int) -> None:
        """
        Adds an offer to the instrument.

        Args:
            trader (Trader): The trader making the offer.
            price (float): The price of the offer.
            amount (int): The amount of the offer.
        """
        self.offers.append(Offer(trader, price, amount))
        print(f"Instrument {self.name} received an offer from {
              trader.name} to trade {amount} at {price}")

    def quote(self) -> List[Offer]:
        """
        Requests a quote from the mediator.

        Returns:
            List[Offer]: A list of offers for the instrument.
        """
        return self.mediator.notify(self, EventType.QUOTE, self.name, self.offers)

class Analyst(Component):
    """Analyst class can analyze the market by quoting instruments."""

    def __init__(self, mediator: Mediator, name: str) -> None:
        super().__init__(mediator)
        self.name = name

    def analyze(self, instrument: str) -> None:
        """
        Analyzes the market by requesting a quote for an instrument.

        Args:
            instrument (str): The instrument to analyze.
        """
        offers = self.mediator.notify(self, EventType.QUOTE, instrument)
        print(f"Analyst {self.name} analyzed {instrument} and found {len(offers)} offers")

class Marketplace(Mediator):
    """Marketplace class is the mediator for the stock market."""

    def __init__(self) -> None:
        """Initializes the marketplace with an empty list of components."""
        self.components = []

    def add_component(self, component: Component) -> None:
        """
        Adds a component to the marketplace.
        """
        self.components.append(component)
        component.mediator = self

    def notify(self, sender: Component, event: EventType, *args) -> None:
        """
        Handles notifications from components and coordinates responses.

        Args:
            sender (Component): The component that sent the notification.
            event (EventType): The type of event.
            *args: Additional arguments for the event.
        """
        if event == EventType.TRADE:
            instrument, price, amount = args
            print(f"Trader {sender.name} wants to trade {amount} of {instrument} at {price}")
            for component in self.components:
                if isinstance(component, Instrument) and component.name == instrument:
                    component.add_offer(sender, price, amount)
                    break
        elif event == EventType.QUOTE:
            instrument = args[0]
            print(f"Analyst {sender.name} wants to quote {instrument} instrument")
            for component in self.components:
                if isinstance(component, Instrument) and component.name == instrument:
                    return component.offers


if __name__ == "__main__":
    marketplace = Marketplace()
    trader1 = Trader(marketplace, "Bob")
    trader2 = Trader(marketplace, "Alice")
    instrument1 = Instrument(marketplace, "USD")
    instrument2 = Instrument(marketplace, "EUR")
    analyst = Analyst(marketplace, "Mark")

    marketplace.add_component(trader1)
    marketplace.add_component(trader2)
    marketplace.add_component(instrument1)
    marketplace.add_component(instrument2)
    marketplace.add_component(analyst)

    # traders place offers to USD instrument
    trader1.trade("USD", 100, 10)
    trader2.trade("USD", 150, 15)
    analyst.analyze("USD")

    # traders place offers to EUR instrument
    trader1.trade("EUR", 300, 15)
    trader2.trade("EUR", 500, 20)
    analyst.analyze("EUR")
