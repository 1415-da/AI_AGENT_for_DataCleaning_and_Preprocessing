# AI_AGENT_for_DataCleaning_and_Preprocessing

This project provides an AI-powered data preprocessing and cleaning application. Users can upload CSV or Excel files, trigger a data cleaning process, and then view the cleaned and preprocessed data.

## Features

- **Data Ingestion:** Upload CSV and Excel files.
- **Data Cleaning:** Automated handling of missing values (median for numerical, mode for categorical) and removal of duplicate rows.
- **Data Preprocessing:** One-Hot Encoding for categorical features and StandardScaler for numerical features.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd AI_AGENT_for_DataCleaning_and_Preprocessing
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    . venv/Scripts/activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the project root and add your `GEMINI_API_KEY` (if you plan to extend functionality with AI models):
    ```
    GEMINI_API_KEY="your_gemini_api_key"
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app/app.py
    ```

2.  **Upload Data:** In the sidebar, choose a CSV or Excel file to upload.

3.  **Clean Data:** Click the "Clean Data" button to initiate the cleaning process.

4.  **View Results:** The original, cleaned, and preprocessed data will be displayed on the page.