"""Template Method Pattern Example: Data processing pipeline
"""
from abc import ABC


class DataPipelineTemplate(ABC):
    """Template class that defines a structure for data processing pipelines."""

    def fetch_data(self) -> None:
        """Fetches data from a source."""
        ...

    def transform_data(self) -> None:
        """Transforms the fetched data."""
        ...

    def save_data(self) -> None:
        """Saves the transformed data."""
        ...

    def process(self) -> None:
        """Processes the data by fetching, transforming, and saving it."""
        self.fetch_data()
        self.transform_data()
        self.save_data()

class CSVDataPipeline(DataPipelineTemplate):
    """Concrete implementation of DataPipeline for handling CSV data."""

    def fetch_data(self) -> None:
        print("Fetching data from CSV file")
        # with open("data.csv") as file:
        #    data = file.read()
        # return data

    def transform_data(self) -> None:
        print("Transforming CSV data")
        # return data.upper()

    def save_data(self) -> None:
        print("Saving transformed data to CSV file")
        # with open("transformed_data.csv", "w") as file:
        #     file.write(data)
        # print("Data saved to database")

class APIDataPipeline(DataPipelineTemplate):
    """Concrete implementation of DataPipeline using data from API."""

    def fetch_data(self) -> None:
        """Fetches data from an API."""
        print("Fetching data from API")
        # response = requests.get("https://api.example.com/data")
        # return response.json()

    def transform_data(self) -> None:
        """Transforms the fetched API data."""
        print("Transforming API data")

    def save_data(self) -> None:
        """Saves the transformed API data to a database."""
        print("Saving transformed data to API endpoint")


def client_code(pipeline: DataPipelineTemplate) -> None:
    pipeline.process()


if __name__ == "__main__":
    csv_pipeline = CSVDataPipeline()
    api_pipeline = APIDataPipeline()

    print("Running CSV pipeline:")
    client_code(csv_pipeline)
    print("\nRunning API pipeline:")
    client_code(api_pipeline)
