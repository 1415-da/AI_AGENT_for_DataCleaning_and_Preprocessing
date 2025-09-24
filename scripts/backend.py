from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scripts.ai_agent import AIAgent
from scripts.data_ingestion import ingest_data
from scripts.data_cleaning import clean_data
from scripts.preprocessing import preprocess_data
import pandas as pd

app = FastAPI()
agent = AIAgent()

class FilePath(BaseModel):
    file_path: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Backend API for Data Preprocessing and Analysis."}

@app.post("/run-pipeline")
async def run_pipeline(filepath_data: FilePath):
    """
    Runs the data ingestion, cleaning, and preprocessing pipeline using the AI Agent.
    Expects a JSON body with {"file_path": "path/to/your/file.csv"}.
    """
    print(f"Backend: Running data pipeline for {filepath_data.file_path}")
    result = agent.run_data_pipeline(filepath_data.file_path)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.post("/analyze-data")
async def analyze_data(filepath_data: FilePath):
    """
    Analyzes data after running the pipeline. This endpoint first runs the pipeline 
    and then performs analysis on the processed data.
    Expects a JSON body with {"file_path": "path/to/your/file.csv"}.
    """
    print(f"Backend: Analyzing data from {filepath_data.file_path}")
    
    df = ingest_data(filepath_data.file_path)
    if df is None:
        raise HTTPException(status_code=400, detail="Failed to ingest data for analysis.")
    
    df_cleaned = clean_data(df.copy())
    if df_cleaned is None:
        raise HTTPException(status_code=400, detail="Failed to clean data for analysis.")
    
    df_processed = preprocess_data(df_cleaned.copy())
    if df_processed is None:
        raise HTTPException(status_code=400, detail="Failed to preprocess data for analysis.")

    analysis_result = agent.analyze_data(df_processed)
    if analysis_result["status"] == "error":
        raise HTTPException(status_code=400, detail=analysis_result["message"])
    return analysis_result
