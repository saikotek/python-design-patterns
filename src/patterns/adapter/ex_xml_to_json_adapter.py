"""Object Adapter Pattern Example: XML to JSON Adapter

Adapts the XML data processor to work with the new JSON analytics system.
"""
import json
import xml.etree.ElementTree as ET


class XMLDataProcessor:
    """
    Legacy XML data processor that we want to integrate with the new JSON analytics system.
    """

    def parse_xml(self, xml_data: str) -> dict:
        """
        Parses the XML string into a Python dictionary.
        """
        root = ET.fromstring(xml_data)

        return {
            "name": root.find("name").text,
            "age": int(root.find("age").text)
        }

    def process(self, data: dict) -> None:
        """
        Processes the parsed data (simulation).
        """
        print(f"Processing data: {data}")

class JSONAnalyticsSystem:
    """
    New data analytics system works only with JSON data.
    We want to adapt the XML data processor to work with this interface.
    """

    def analyze(self, json_data: str) -> None:
        """
        Analyzes the JSON data.

        Args:
            json_data (str): The JSON data to be analyzed.
        """
        print(f"Analyzing JSON data: {json_data}")


class XMLToJSONAdapter(JSONAnalyticsSystem):
    """
    Adapter class inheriting from JSONAnalyticsSystem.
    """

    def __init__(self, xml_processor: XMLDataProcessor) -> None:
        """
        Initializes the adapter with an instance of XMLDataProcessor.
        """
        self.xml_processor = xml_processor

    def analyze(self, xml_data: str) -> None:
        """
        Parses XML data and adapts it for analysis by the JSON system.
        """
        # Parse the XML data to a Python dictionary
        parsed_data = self.xml_processor.parse_xml(xml_data)

        # Convert the parsed dictionary to a JSON string
        json_data = json.dumps(parsed_data)

        # Use the new JSON analytics system's analyze method
        super().analyze(json_data)


# Example usage
if __name__ == "__main__":
    xml_data = "<person><name>John Doe</name><age>30</age></person>"

    # Using the legacy XML processor directly
    xml_processor = XMLDataProcessor()
    xml_processor.process(xml_processor.parse_xml(xml_data))

    # Using the adapter to integrate the XML processor with the JSON analytics system
    adapter = XMLToJSONAdapter(xml_processor)
    adapter.analyze(xml_data)
