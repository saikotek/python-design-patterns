"""Specification Design Pattern

Intent: Allows to create complex filtering logic by combining simple rules.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List

class Specification(ABC):
    """Abstract base class for all specifications."""

    @abstractmethod
    def is_satisfied_by(self, candidate: Any) -> bool:
        """Check if the candidate satisfies this specification."""
        pass

    def __and__(self, other: Specification) -> AndSpecification:
        """Combine specifications using AND logic."""
        return AndSpecification(self, other)

    def __or__(self, other: Specification) -> OrSpecification:
        """Combine specifications using OR logic."""
        return OrSpecification(self, other)

    def __invert__(self) -> NotSpecification:
        """Negate this specification."""
        return NotSpecification(self)


class AndSpecification(Specification):
    """Combines two specifications using AND logic."""

    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: Any) -> bool:
        """Check if candidate satisfies both specifications."""
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)


class OrSpecification(Specification):
    """Combines two specifications using OR logic."""

    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: Any) -> bool:
        """Check if candidate satisfies either specification."""
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)


class NotSpecification(Specification):
    """Negates a specification."""

    def __init__(self, spec: Specification):
        self.spec = spec

    def is_satisfied_by(self, candidate: Any) -> bool:
        """Check if candidate does not satisfy the specification."""
        return not self.spec.is_satisfied_by(candidate)


class SubstringSpecification(Specification):
    """Check if a string contains a given substring."""

    def __init__(self, substring: str):
        self.substring = substring

    def is_satisfied_by(self, candidate: str) -> bool:
        return self.substring in candidate


def filter_items(items: List[Any], spec: Specification) -> List[Any]:
    """Filter a list of items using a given specification."""
    return [item for item in items if spec.is_satisfied_by(item)]


# Example usage
if __name__ == "__main__":
    spec_a = SubstringSpecification("apple")
    spec_b = SubstringSpecification("orange")
    spec_c = SubstringSpecification("excluded_apple")

    # Create composite specification using operator overloading
    composite_spec = (spec_a | spec_b) & ~spec_c

    # Use the specification to filter items
    items = ["apple", "apple2", "orange", "orange2", "excluded_apple", "excluded_orange"]
    filtered_items = filter_items(items, composite_spec)
    print(f"Filtered items: {filtered_items}")