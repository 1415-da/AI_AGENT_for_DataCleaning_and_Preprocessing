import pandas as pd

def ingest_data(file_path):
    """
    Ingests data from a specified file path into a pandas DataFrame.
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
        print(f"Successfully ingested data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
        return None
