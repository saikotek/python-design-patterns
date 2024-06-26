"""
Prototype Pattern Example: Document Cloning
"""
from abc import ABC
import copy
from typing import Dict, Any


class Report(ABC):
    """Report class, a specific type of document.

    Attributes:
        title (str): The title of the report.
        content (Dict[str, Any]): The content of the report.
        author (str): The author of the report.
    """

    def __init__(self, title: str, content: Dict[str, Any], author: str):
        """Initializes the Report with a title, content, and author.

        Args:
            title (str): The title of the report.
            content (Dict[str, Any]): The content of the report.
            author (str): The author of the report.
        """
        self.title = title
        self.content = content
        self.author = author

    def __copy__(self):
        """Creates a shallow copy of the Report."""
        return Report(self.title, self.content.copy(), self.author)

    def __deepcopy__(self, memo):
        """Creates a deep copy of the Report."""
        return Report(copy.deepcopy(self.title, memo),
                      copy.deepcopy(self.content, memo),
                      copy.deepcopy(self.author, memo))

    def __str__(self):
        return f"Report: {self.title} by {self.author}" + \
            f"\nContent: {self.content}"


# Example usage
if __name__ == "__main__":
    # Create a report template
    report_template = Report(
        "Monthly Report",
        {
            "data": [1, 2, 3],
            "details": {"section": "A", "value": 42}
        },
        "Alice"
    )
    # Clone the report template and customize it
    custom_report = copy.deepcopy(report_template)
    custom_report.title = "Monthly Report - April"
    custom_report.content["data"].append(4)
    custom_report.content["details"]["section"] = "B"

    # Display the documents
    print("Template Document:", report_template)
    print("Customized Documents:", custom_report)

    # Display template document again
    print("Template Document:", report_template)
