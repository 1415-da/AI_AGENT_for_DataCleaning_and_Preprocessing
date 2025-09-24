from data_ingestion import ingest_data
from data_cleaning import clean_data
from preprocessing import preprocess_data
import pandas as pd

def main():
    print("Starting data pipeline...")

    # Step 1: Data Ingestion
    file_path = 'data/sample_data.csv'  # Adjust this path as needed
    df = ingest_data(file_path)

    if df is not None:
        print("\n--- Original Data Head ---")
        print(df.head())

        # Step 2: Data Cleaning
        df_cleaned = clean_data(df.copy()) # Use a copy to avoid modifying original df

        if df_cleaned is not None:
            print("\n--- Cleaned Data Head ---")
            print(df_cleaned.head())

            # Step 3: Data Preprocessing
            df_processed = preprocess_data(df_cleaned.copy()) # Use a copy

            if df_processed is not None:
                print("\n--- Processed Data Head ---")
                print(df_processed.head())
                print("Data pipeline finished successfully!")
            else:
                print("Data preprocessing failed.")
        else:
            print("Data cleaning failed.")
    else:
        print("Data ingestion failed. Cannot proceed.")

if __name__ == "__main__":
    main()
