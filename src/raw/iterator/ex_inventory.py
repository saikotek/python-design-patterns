"""
Iterator Design Pattern

Example: Inventory Traversal
"""
from typing import Iterator, List
import random


class InventoryIterator(Iterator[str]):
    """Iterator for traversing the inventory in normal order."""

    def __init__(self, items: List[str]) -> None:
        """
        Initializes the iterator with a list of items.

        Args:
            items (List[str]): The list of items to iterate over.
        """
        self.items = items
        self.index = 0

    def __next__(self) -> str:
        """
        Returns the next item in the inventory.
        """
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

class ReverseInventoryIterator(Iterator[str]):
    """Iterator for traversing the inventory in reverse order."""

    def __init__(self, items: List[str]) -> None:
        """
        Initializes the iterator with a list of items.

        Args:
            items (List[str]): The list of items to iterate over.
        """
        self.items = items
        self.index = len(items) - 1

    def __next__(self) -> str:
        """
        Returns the next item in the inventory in reverse order.
        """
        if self.index >= 0:
            item = self.items[self.index]
            self.index -= 1
            return item
        else:
            raise StopIteration

class RandomOrderInventoryIterator(Iterator[str]):
    """Iterator for traversing the inventory in random order."""

    def __init__(self, items: List[str]) -> None:
        """
        Initializes the iterator with a list of items and shuffles them.

        Args:
            items (List[str]): The list of items to iterate over.
        """
        self.items = items[:]
        random.shuffle(self.items)
        self.index = 0

    def __next__(self) -> str:
        """
        Returns the next item in the inventory in random order.
        """
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

class InventoryIterable:
    """Iterable collection of inventory items."""

    def __init__(self, items: List[str]) -> None:
        """
        Initializes the iterable with a list of items.

        Args:
            items (List[str]): The list of items in the inventory.
        """
        self.items = items

    def __iter__(self) -> InventoryIterator:
        """
        Returns an iterator for traversing the inventory in normal order.
        """
        return InventoryIterator(self.items)

    def reverse_iterator(self) -> ReverseInventoryIterator:
        """
        Returns an iterator for traversing the inventory in reverse order.
        """
        return ReverseInventoryIterator(self.items)

    def random_order_iterator(self) -> RandomOrderInventoryIterator:
        """
        Returns an iterator for traversing the inventory in random order.

        Returns:
            RandomOrderInventoryIterator: An iterator for the inventory in random order.
        """
        return RandomOrderInventoryIterator(self.items)


# Client code
def client_code(iterator: Iterator[str]) -> None:
    """
    Iterates over and prints items using the provided iterator.

    Args:
        iterator (Iterator[str]): The iterator to use for traversing the items.
    """
    for item in iterator:
        print(item)


# Usage
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
inventory_iterable = InventoryIterable(items)

print("Normal Order:")
client_code(iter(inventory_iterable))

print("\nReverse Order:")
client_code(inventory_iterable.reverse_iterator())

print("\nRandom Order:")
client_code(inventory_iterable.random_order_iterator())
