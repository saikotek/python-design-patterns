from typing import Protocol

class DataPipeline(Protocol):
    def fetch_data(self) -> None:
        ...

    def transform_data(self) -> None:
        ...

    def save_data(self) -> None:
        ...

    def process(self) -> None:
        self.fetch_data()
        self.transform_data()
        self.save_data()

class CSVDataPipeline(DataPipeline):
    def fetch_data(self) -> None:
        print("Fetching data from CSV file")
        # with open("data.csv") as file:
        #    data = file.read()
        # return data

    def transform_data(self) -> None:
        print("Transforming CSV data")
        # return data.upper()
        
    def save_data(self) -> None:
        print("Saving transformed data to database")
        # with open("transformed_data.csv", "w") as file:
        #     file.write(data)
        # print("Data saved to database")
        
class APIDataPipeline(DataPipeline):
    def fetch_data(self) -> None:
        print("Fetching data from API")
        # response = requests.get("https://api.example.com/data")
        # return response.json()
        
    def transform_data(self) -> None:
        print("Transforming API data")
        # return data["results"].upper()
        
    def save_data(self) -> None:
        print("Saving transformed data to database")
        # with open("transformed_data.csv", "w") as file:
        #     file.write(data)
        # print("Data saved to database")
        
# Client code is not aware of the concrete classes 
def run_pipeline(pipeline: DataPipeline) -> None:
    print("Running data pipeline...")
    pipeline.process()
    print("Data pipeline completed.")
    
# Usage
csv_pipeline = CSVDataPipeline()
api_pipeline = APIDataPipeline()

print("Running CSV pipeline:")
run_pipeline(csv_pipeline)
print("\nRunning API pipeline:")
run_pipeline(api_pipeline)
