"""Strategy Design Pattern

Example: Changing payment strategies for an online store.
"""

from typing import Protocol

class PaymentStrategy(Protocol):
    """Protocol that defines the interface for payment strategies."""

    def pay(self, amount: float) -> None:
        ...

class CreditCardPayment:
    """Concrete strategy for payment using Credit Card."""

    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using Credit Card.")

class PayPalPayment:
    """Concrete strategy for payment using PayPal."""

    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using PayPal.")

class CryptoPayment:
    """Concrete strategy for payment using Cryptocurrency."""

    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using Cryptocurrency.")

class PaymentContext:
    """Context class that uses a PaymentStrategy to perform payments."""

    def __init__(self, strategy: PaymentStrategy) -> None:
        """Initializes the context with a specific payment strategy."""
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        print(f"Changing payment strategy to {strategy.__class__.__name__}")
        self._strategy = strategy

    def execute_payment(self, amount: float) -> None:
        """Executes the payment using the current strategy."""
        self._strategy.pay(amount)


# Usage
if __name__ == "__main__":
    context = PaymentContext(CreditCardPayment())
    context.execute_payment(100.0)

    context.set_strategy(PayPalPayment())
    context.execute_payment(200.0)
