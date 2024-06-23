"""
Template Method Design Pattern

Intent: Defines the skeleton of an algorithm in a superclass but allows subclasses
to override specific steps of the algorithm without changing its structure.
"""
from abc import ABC, abstractmethod


class BaseTemplateClass(ABC):
    """Base template class that defines a template method and primitive operations."""

    def template_method(self) -> None:
        """Template method defining the skeleton of an algorithm."""
        self.primitive_operation1()
        self.primitive_operation2()
        self.hook()

    @abstractmethod
    def primitive_operation1(self) -> None:
        """Primitive operation 1 that must be implemented by subclasses."""
        pass

    @abstractmethod
    def primitive_operation2(self) -> None:
        """Primitive operation 2 that must be implemented by subclasses."""
        pass

    def hook(self) -> None:
        """Hook method that can be overridden by subclasses."""
        pass

class ConcreteClassA(BaseTemplateClass):
    """Concrete class that implements the primitive operations to carry out subclass-specific steps of the algorithm."""

    def primitive_operation1(self) -> None:
        print("ConcreteClassA: Performing primitive operation 1")

    def primitive_operation2(self) -> None:
        print("ConcreteClassA: Performing primitive operation 2")

    def hook(self) -> None:
        print("ConcreteClassA: Optional hook")

class ConcreteClassB(BaseTemplateClass):
    """Concrete class that implements the primitive operations to carry out subclass-specific steps of the algorithm."""

    def primitive_operation1(self) -> None:
        print("ConcreteClassB: Performing primitive operation 1")

    def primitive_operation2(self) -> None:
        print("ConcreteClassB: Performing primitive operation 2")

    # not mandatory to implement hook
    # def hook(self) -> None:
    #     print("ConcreteClassB: Optional hook")


def client_code(template: BaseTemplateClass) -> None:
    """Client code that uses the template class 
    does not know about concrete implementation."""
    template.template_method()


# Usage example
if __name__ == "__main__":
    concrete_class_a = ConcreteClassA()
    concrete_class_b = ConcreteClassB()

    print("ConcreteClassA execution:")
    client_code(concrete_class_a)

    print("\nConcreteClassB execution:")
    client_code(concrete_class_b)