"""
Builder Pattern Example: Fluent Builder for building computer with different specifications.
"""
from abc import ABC


class Computer(ABC):
    """Product class representing a computer."""

    def __init__(self):
        """Initializes a new Computer instance with an empty specifications dictionary."""
        self.specifications = {}

    def __str__(self):
        """Returns a string representation of the computer specifications."""
        specs = "\n".join(f"{key}: {value}" for key, value in self.specifications.items())
        return f"Computer Specifications:\n{specs}"

class ComputerBuilder:
    """Fluent builder class for constructing Computer objects."""

    def __init__(self):
        """Initializes a new ComputerBuilder instance with a blank Computer object."""
        self.computer = Computer()

    def with_cpu(self, cpu: str):
        self.computer.specifications['CPU'] = cpu
        return self

    def with_ram(self, ram: str):
        self.computer.specifications['RAM'] = ram
        return self

    def with_storage(self, storage: str):
        self.computer.specifications['Storage'] = storage
        return self

    def with_graphics_card(self, graphics_card: str):
        self.computer.specifications['Graphics Card'] = graphics_card
        return self

    def build(self):
        """
        Finalizes the construction of the computer.

        Returns:
            Computer: The constructed Computer object.
        """
        return self.computer


if __name__ == "__main__":
    # Build a gaming computer using fluent builder
    gaming_computer = (
        ComputerBuilder()
        .with_cpu("AMD Ryzen 9 5950X")
        .with_ram("32GB DDR4")
        .with_storage("1TB NVMe SSD")
        .with_graphics_card("NVIDIA GeForce RTX 3080")
        .build()
    )
    print(gaming_computer)

    # Build an office computer using fluent builder
    office_computer = (
        ComputerBuilder()
        .with_cpu("Intel Core i5-11400")
        .with_ram("16GB DDR4")
        .with_storage("512GB SSD")
        .with_graphics_card("Integrated Graphics")
        .build()
    )
    print("\n" + str(office_computer))
