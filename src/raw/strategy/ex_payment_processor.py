from typing import Protocol

class PaymentStrategy(Protocol):
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment:
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using Credit Card.")

class PayPalPayment:
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using PayPal.")

class CryptoPayment:
    def pay(self, amount: float) -> None:
        print(f"Paying {amount} using Cryptocurrency.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def execute_payment(self, amount: float) -> None:
        self._strategy.pay(amount)

# Usage
context = PaymentContext(CreditCardPayment())
context.execute_payment(100.0)

context.set_strategy(PayPalPayment())
context.execute_payment(200.0)
