from abc import ABC, abstractmethod

# Abstract document class
class Document(ABC):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @abstractmethod
    def clone(self): # like ICloneable in C#
        pass

    def display(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}\n")

# Report class (a specific type of document)
class Report(Document):
    def __init__(self, title: str, content: str, author: str):
        super().__init__(title, content)
        self.author = author

    def clone(self):
        # Create a new instance with the same attributes
        return Report(self.title, self.content, self.author)

    def display(self):
        print(f"Report by {self.author}")
        super().display()

# Invoice class (another type of document)
class Invoice(Document):
    def __init__(self, title: str, content: str, customer: str, total: float):
        super().__init__(title, content)
        self.customer = customer
        self.total = total

    def clone(self):
        # Create a new instance with the same attributes
        return Invoice(self.title, self.content, self.customer, self.total)

    def display(self):
        print(f"Invoice for {self.customer}")
        print(f"Total amount: ${self.total:.2f}")
        super().display()

# Example usage
# Create a report template
report_template = Report("Monthly Report", "This is the main report content.", "Alice")
# Clone the report template and customize it
custom_report = report_template.clone()
custom_report.title = "Monthly Report - April"
custom_report.content = "April report content with new data."

# Create an invoice template
invoice_template = Invoice("Invoice Template", "Details of services provided.", "ACME Corp", 0.0)
# Clone the invoice template and customize it
custom_invoice = invoice_template.clone()
custom_invoice.title = "Invoice #1234"
custom_invoice.customer = "Global Industries"
custom_invoice.total = 1500.75

# Display the documents
print("Template Documents:")
report_template.display()
invoice_template.display()

print("Customized Documents:")
custom_report.display()
custom_invoice.display()
