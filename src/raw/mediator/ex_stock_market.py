# Mediator Design Pattern real-world example
# Stock market

from abc import ABC, abstractmethod
from dataclasses import dataclass
import enum

# event type
class EventType(enum.Enum):
    TRADE = 1
    QUOTE = 2

# Mediator base class
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: "Component", event: EventType, *args):
        pass

# Component base class which has a reference to the mediator
class Component(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = Mediator

###
### Concrete component classes
###

# Trader class can place an offer to an instrument
class Trader(Component):
    def __init__(self, mediator, name):
        super().__init__(mediator)
        self.name = name
    
    def trade(self, instrument, price, amount):
        self.mediator.notify(self, EventType.TRADE, instrument, price, amount)

@dataclass
class Offer:
    trader: Trader
    price: float
    amount: int

# Instrument class accepts offers and can be quoted
class Instrument(Component):
    offers: Offer = []
    
    def __init__(self, mediator, name):
        super().__init__(mediator)
        self.name = name
        self.offers = []
    
    def add_offer(self, trader, price, amount):
        self.offers.append(Offer(trader, price, amount))
        print(f"Instrument {self.name} received an offer from {trader.name} to trade {amount} at {price}")
    
    def quote(self):
        return self.mediator.notify(self, EventType.QUOTE, self.name, self.offers)

# Analyst class can analyze the market by quoting instruments
class Analyst(Component):
    def __init__(self, mediator, name):
        super().__init__(mediator)
        self.name = name
    
    def analyze(self, instrument):
        offers = self.mediator.notify(self, EventType.QUOTE, instrument)
        print(f"Analyst {self.name} analyzed {instrument} and found {len(offers)} offers")

# Marketplace class is the mediator
class Marketplace(Mediator):
    def __init__(self):
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
        component.mediator = self
    
    def notify(self, sender: Component, event: EventType, *args):
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