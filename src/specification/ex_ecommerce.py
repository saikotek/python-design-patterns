"""Specification Pattern Example (E-commerce)

In this example, we create a list of products and then filter them based
on a combined specification of price range and category.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    category: str

class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item: Product) -> bool:
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)

class PriceSpecification(Specification):
    def __init__(self, min_price: float, max_price: float):
        self.min_price = min_price
        self.max_price = max_price

    def is_satisfied(self, item: Product) -> bool:
        return self.min_price <= item.price <= self.max_price

class CategorySpecification(Specification):
    def __init__(self, category: str):
        self.category = category

    def is_satisfied(self, item: Product) -> bool:
        return item.category == self.category

class AndSpecification(Specification):
    def __init__(self, *specifications):
        self.specifications = specifications

    def is_satisfied(self, item: Product) -> bool:
        return all(spec.is_satisfied(item) for spec in self.specifications)

class OrSpecification(Specification):
    def __init__(self, *specifications):
        self.specifications = specifications

    def is_satisfied(self, item: Product) -> bool:
        return any(spec.is_satisfied(item) for spec in self.specifications)

class ProductFilter:
    def filter(self, products, spec):
        return [product for product in products if spec.is_satisfied(product)]


# Usage example
if __name__ == "__main__":
    products = [
        Product("Laptop", 1200, "Electronics"),
        Product("Smartphone", 800, "Electronics"),
        Product("Desk", 350, "Furniture"),
        Product("Chair", 150, "Furniture"),
        Product("Tablet", 600, "Electronics"),
    ]

    # Specifications
    price_500_1000 = PriceSpecification(500, 1000)
    price_under_400 = PriceSpecification(0, 400)
    category_electronics = CategorySpecification("Electronics")
    category_furniture = CategorySpecification("Furniture")

    # Combined specifications
    electronics_500_1000 = price_500_1000 & category_electronics
    budget_items = price_under_400 | category_furniture

    product_filter = ProductFilter()

    print("Electronics between $500 and $1000:")
    for product in product_filter.filter(products, electronics_500_1000):
        print(f"- {product.name}: ${product.price}")

    print("\nBudget items (under $400 or Furniture):")
    for product in product_filter.filter(products, budget_items):
        print(f"- {product.name}: ${product.price} ({product.category})")