"""
Builder Pattern Example: Computer Builder with concrete builder classes for gaming
and office computers.
"""
from typing import Protocol

class Computer:
    """Class representing the final product (a computer)"""

    def __init__(self):
        self.specifications = {}

    def __str__(self) -> str:
        specs = "\n".join(f"{key}: {value}" for key, value in self.specifications.items())
        return f"Computer Specifications:\n{specs}"

class ComputerBuilder(Protocol):
    """
    Protocol defining the blueprint for a ComputerBuilder.

    Attributes:
        computer (Computer): Instance variable to hold the computer being built.
    """
    computer: Computer

    def build_cpu(self) -> None:
        ...

    def build_ram(self) -> None:
        ...

    def build_storage(self) -> None:
        ...

    def build_graphics_card(self) -> None:
        ...

    def get_computer(self) -> Computer:
        ...

class GamingComputerBuilder(ComputerBuilder):
    """Concrete builder class for constructing a gaming computer"""

    def __init__(self):
        self.computer = Computer()

    def build_cpu(self) -> None:
        self.computer.specifications['CPU'] = "AMD Ryzen 9 5950X"

    def build_ram(self) -> None:
        self.computer.specifications['RAM'] = "32GB DDR4"

    def build_storage(self) -> None:
        self.computer.specifications['Storage'] = "1TB NVMe SSD"

    def build_graphics_card(self) -> None:
        self.computer.specifications['Graphics Card'] = "NVIDIA GeForce RTX 3080"

    def get_computer(self) -> Computer:
        return self.computer

class OfficeComputerBuilder(ComputerBuilder):
    """Concrete builder class for constructing an office computer"""

    def __init__(self):
        self.computer = Computer()

    def build_cpu(self) -> None:
        self.computer.specifications['CPU'] = "Intel Core i5-11400"

    def build_ram(self) -> None:
        self.computer.specifications['RAM'] = "16GB DDR4"

    def build_storage(self) -> None:
        self.computer.specifications['Storage'] = "512GB SSD"

    def build_graphics_card(self) -> None:
        self.computer.specifications['Graphics Card'] = "Integrated Graphics"

    def get_computer(self) -> Computer:
        return self.computer

class ComputerDirector:
    """Director class to construct the computer using a builder"""

    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_computer(self) -> Computer:
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_graphics_card()
        return self.builder.get_computer()


if __name__ == "__main__":
    # Construct a gaming computer
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    gaming_computer = director.construct_computer()
    print(gaming_computer)

    # Construct an office computer
    office_builder = OfficeComputerBuilder()
    director = ComputerDirector(office_builder)
    office_computer = director.construct_computer()
    print("\n" + str(office_computer))
