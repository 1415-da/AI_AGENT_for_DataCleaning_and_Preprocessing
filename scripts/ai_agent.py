from scripts.data_ingestion import ingest_data
from scripts.data_cleaning import clean_data
from scripts.preprocessing import preprocess_data
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class AIAgent:
    def __init__(self, gemini_api_key: str = None):
        self.gemini_api_key = gemini_api_key
        print("AI Agent initialized.")

    def run_data_pipeline(self, file_path):
        print(f"AI Agent starting data pipeline for {file_path}...")

        df = ingest_data(file_path)
        if df is None:
            return {"status": "error", "message": "Data ingestion failed."}

        df_cleaned = clean_data(df.copy())
        if df_cleaned is None:
            return {"status": "error", "message": "Data cleaning failed."}

        df_processed = preprocess_data(df_cleaned.copy())
        if df_processed is None:
            return {"status": "error", "message": "Data preprocessing failed."}

        print("AI Agent successfully completed the data pipeline.")
        return {"status": "success", "message": "Data pipeline executed successfully.", "processed_data_head": df_processed.head().to_dict()}

    def analyze_data(self, df):
        if df is None:
            return {"status": "error", "message": "No DataFrame to analyze."}
        
        analysis_results = {
            "columns": df.columns.tolist(),
            "data_types": df.dtypes.astype(str).to_dict(),
            "shape": df.shape,
            "description": df.describe().to_dict()
        }
        print("Data analysis complete.")
        return {"status": "success", "analysis": analysis_results}

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Placeholder for the API key - replace with your actual key or environment variable
    # For a real application, consider using environment variables for sensitive data
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    agent = AIAgent(gemini_api_key=GEMINI_API_KEY)
    test_file_path = 'data/sample_data.csv' # Make sure this file exists for testing
    result = agent.run_data_pipeline(test_file_path)
    print("\nPipeline Result:", result)

    if result["status"] == "success":
        # To analyze, we need the actual processed DataFrame, not just the head dict
        # For this example, we'll re-run parts of the pipeline to get the df_processed
        df = ingest_data(test_file_path)
        df_cleaned = clean_data(df.copy())
        df_processed = preprocess_data(df_cleaned.copy())
        
        analysis = agent.analyze_data(df_processed)
        print("\nAnalysis Result:", analysis)
