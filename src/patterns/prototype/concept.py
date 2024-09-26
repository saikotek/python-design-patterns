"""Prototype Pattern

Intent: Allows cloning objects without coupling to their specific classes.

In Python, the `copy` module provides functions for shallow and deep copying of objects.
__copy__():
    Creates a shallow clone of the object.
__deepcopy__():
    Creates a deep clone of the object.

Shallow clone copies the object itself, but not its nested objects.
Deep clone copies the object and all its nested objects recursively.
    
Thanks to duck typing, we can simply implement these methods in our classes to make them cloneable,
so there is no need for formal interfaces or abstract classes.
But if you want to be sure that your class is cloneable in a correct way, you can use Protocols.
"""
from __future__ import annotations
from typing import Any, Dict, List
import copy


class MyClass:
    """An example class that we want to clone.

    Attributes:
        integer (int): An example integer field.
        string (str): An example string field.
        nested_list (List[int]): An example nested list field.
    """

    def __init__(self, integer: int, string: str, nested_list: List[int]) -> None:
        self.string = string
        self.integer = integer
        self.nested_list = nested_list

    def __copy__(self) -> MyClass:
        """Creates a shallow clone of the object."""
        return MyClass(self.integer, self.string, self.nested_list)

    def __deepcopy__(self, memo: Dict[int, Any]) -> MyClass:
        """Creates a deep clone of the object.

        Args:
            memo (Dict[int, Any]): Dictionary for tracking already copied objects.

        Returns:
            MyClass: A new instance with the same field values.
        """
        return MyClass(copy.deepcopy(self.integer, memo),
                       copy.deepcopy(self.string, memo),
                       copy.deepcopy(self.nested_list, memo))

    def __str__(self) -> str:
        return f"MyClass({self.integer}, {self.string}, {self.nested_list})"


# Usage example
if __name__ == "__main__":
    cloneable = MyClass(42, "prototype", [1, 2, 3])

    shallow_clone = copy.copy(cloneable)
    print(f"Before modification: original: {cloneable}, Shallow Clone: {shallow_clone}")
    shallow_clone.integer = 100
    shallow_clone.string = "shallow"
    shallow_clone.nested_list.append(4)
    print(f"After modification: original: {cloneable}, Shallow Clone: {shallow_clone}")

    cloneable2 = MyClass(42, "prototype", [1, 2, 3])
    deep_clone = copy.deepcopy(cloneable)

    print(f"Before modification: original: {cloneable2}, Deep Clone: {deep_clone}")
    deep_clone.integer = 100
    deep_clone.string = "deep"
    deep_clone.nested_list.append(4)
    print(f"After modification: original: {cloneable2}, Deep Clone: {deep_clone}")
