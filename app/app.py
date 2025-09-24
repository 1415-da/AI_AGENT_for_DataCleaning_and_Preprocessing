import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

from scripts.data_ingestion import ingest_data
from scripts.data_cleaning import clean_data
from scripts.preprocessing import preprocess_data

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(layout="wide", page_title="Data Preprocessing App")

st.title("AI-Powered Data Preprocessing and Cleaning")

st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    st.sidebar.success("File successfully uploaded!")

    # Ingestion
    st.header("1. Data Ingestion")
    df = ingest_data(uploaded_file)

    if df is not None:
        st.session_state['original_df'] = df
        st.subheader("Original Data Head")
        st.dataframe(df.head())

        # Add a button to trigger cleaning
        if st.button("Clean Data"):
            st.session_state['cleaned_df'] = clean_data(st.session_state['original_df'].copy())
            if st.session_state['cleaned_df'] is not None:
                st.header("2. Data Cleaning")
                st.subheader("Cleaned Data Head")
                st.dataframe(st.session_state['cleaned_df'].head())
                st.success("Data cleaning completed!")
            else:
                st.error("Data cleaning failed.")

        if 'cleaned_df' in st.session_state and st.session_state['cleaned_df'] is not None:
            # Preprocessing
            st.header("3. Data Preprocessing")
            st.info("Applying preprocessing: One-Hot Encoding for categorical features and StandardScaler for numerical features.")
            df_processed = preprocess_data(st.session_state['cleaned_df'].copy())

            if df_processed is not None:
                st.subheader("Processed Data Head")
                st.dataframe(df_processed.head())
                st.success("Data pipeline executed successfully!")
            else:
                st.error("Data preprocessing failed.")
        elif 'original_df' in st.session_state and st.session_state['original_df'] is not None:
            st.info("Click 'Clean Data' to proceed with cleaning and preprocessing.")

    else:
        st.error("Data ingestion failed.")

else:
    st.info("Please upload a file to start the data preprocessing pipeline.")
    st.markdown("**Note:** Ensure your `.env` file contains your `GEMINI_API_KEY` if you plan to extend functionality with AI models.")
