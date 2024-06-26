"""
Iterator Pattern

Intent: Lets you traverse elements of a collection without exposing its
underlying representation (list, stack, tree, etc.).
"""
from __future__ import annotations
from typing import List, Any, Protocol
from collections.abc import Iterable, Iterator
from typing import Any

"""
To create an iterator in Python, there are two abstract classes from the
built-in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in the iterator.
"""

class Aggregate(Protocol):
    """Aggregate declares an interface for creating an Iterator object."""

    def create_iterator(self) -> Iterator[Any]:
        """Creates an iterator for the aggregate."""
        pass

class ConcreteAggregate(Iterable):
    """ConcreteAggregate implements the Iterator creation interface to return an instance of the proper ConcreteIterator."""

    def __init__(self, items: List[Any]) -> None:
        """
        Initializes the aggregate with a list of items.

        Args:
            items (List[Any]): The list of items to be iterated over.
        """
        self._items = items

    def __iter__(self) -> Iterator[Any]:
        """
        Returns an iterator for the aggregate.

        Returns:
            Iterator[Any]: An iterator for the aggregate.
        """
        return ConcreteIterator(self)

    def get_items(self) -> List[Any]:
        """
        Returns the list of items in the aggregate.

        Returns:
            List[Any]: The list of items in the aggregate.
        """
        return self._items

class ConcreteIterator(Iterator):
    """ConcreteIterator implements the Iterator interface and keeps track of the current position in the traversal of the aggregate."""

    def __init__(self, aggregate: ConcreteAggregate) -> None:
        """
        Initializes the iterator with an aggregate.

        Args:
            aggregate (ConcreteAggregate): The aggregate to iterate over.
        """
        self._aggregate = aggregate
        self._index = 0

    def __next__(self) -> Any:
        """
        Returns the next item in the aggregate.

        Returns:
            Any: The next item in the aggregate.

        Raises:
            StopIteration: If there are no more items to return.
        """
        try:
            value = self._aggregate.get_items()[self._index]
        except IndexError:
            raise StopIteration()
        self._index += 1
        return value

    def __iter__(self) -> Iterator[Any]:
        """
        Returns the iterator itself.

        Returns:
            Iterator[Any]: The iterator itself.
        """
        return self


if __name__ == "__main__":
    """Client code that demonstrates the Iterator Design Pattern."""
    items = ["Item1", "Item2", "Item3", "Item4"]
    aggregate = ConcreteAggregate(items)

    print("Iterating over the aggregate:")
    for item in aggregate:
        print(item)
