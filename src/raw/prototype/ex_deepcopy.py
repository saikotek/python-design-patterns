from abc import ABC, abstractmethod
import copy

# Abstract base class for all prototypes
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete implementation of a prototype (a Report)
class Report(Prototype):
    """Concrete Prototype class representing a report."""
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def clone(self):
        """Create a deep copy of this report."""
        return copy.deepcopy(self)

    def __str__(self):
        return (f"Report Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content: {self.content}\n")

# Registry class for managing report templates
class ReportRegistry:
    """Registry containing predefined report templates."""
    def __init__(self):
        self._templates = {}

    def add_template(self, name, report):
        """Add a report template to the registry."""
        self._templates[name] = report

    def get_template(self, name):
        """Retrieve and clone a report template by name."""
        template = self._templates.get(name)
        return template.clone() if template else None

# Example usage
if __name__ == "__main__":
    # Create a registry instance
    registry = ReportRegistry()

    # Add report templates to the registry
    marketing_template = Report("Marketing Analysis", "Detailed analysis of Q1 results.", "Jane Doe")
    financial_template = Report("Financial Overview", "Annual financial summary.", "John Smith")
    registry.add_template("marketing", marketing_template)
    registry.add_template("financial", financial_template)

    # Clone and modify a marketing report
    cloned_report = registry.get_template("marketing")
    cloned_report.author = "Emily Clarke"  # Change the author
    cloned_report.title = "Q2 Marketing Analysis"
    print(cloned_report)

    # Clone and modify a financial report
    cloned_report2 = registry.get_template("financial")
    cloned_report2.content = "Summary of Q2 performance."
    print("\n" + str(cloned_report2))
