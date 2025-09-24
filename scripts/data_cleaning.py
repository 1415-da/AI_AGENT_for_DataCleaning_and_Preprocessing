import pandas as pd

def clean_data(df):
    """
    Performs basic data cleaning on a pandas DataFrame.
    - Handles missing values (fills numerical with median, categorical with mode).
    - Removes duplicate rows.
    """
    if df is None:
        print("No DataFrame provided for cleaning.")
        return None

    # Handle missing numerical values with median
    for col in df.select_dtypes(include=['number']).columns:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
            print(f"Filled missing numerical values in column '{col}' with median: {median_val}")

    # Handle missing categorical values with mode
    for col in df.select_dtypes(include=['object', 'category']).columns:
        if df[col].isnull().any():
            mode_val = df[col].mode()[0] # .mode() can return multiple values, take the first
            df[col].fillna(mode_val, inplace=True)
            print(f"Filled missing categorical values in column '{col}' with mode: {mode_val}")

    # Remove duplicate rows
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    rows_after_deduplication = df.shape[0]
    if initial_rows > rows_after_deduplication:
        print(f"Removed {initial_rows - rows_after_deduplication} duplicate rows.")
    else:
        print("No duplicate rows found.")

    print("Data cleaning complete.")
    return df
