import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(df):
    """
    Performs basic data preprocessing on a pandas DataFrame.
    - Identifies categorical and numerical features.
    - Applies One-Hot Encoding to categorical features.
    - Applies StandardScaler to numerical features.
    """
    if df is None:
        print("No DataFrame provided for preprocessing.")
        return None

    # Identify categorical and numerical columns
    categorical_features = df.select_dtypes(include=['object', 'category']).columns
    numerical_features = df.select_dtypes(include=['number']).columns

    # Create preprocessing pipelines for numerical and categorical features
    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    # Create a column transformer to apply different transformations to different columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Create a pipeline that first preprocesses and then can be extended for modeling
    try:
        # Fit and transform the data
        # For simplicity, we'll return a DataFrame from the transformed array.
        # In a real scenario, this would likely be part of a larger ML pipeline.
        processed_array = preprocessor.fit_transform(df)

        # Get feature names after one-hot encoding
        new_feature_names = []
        for col in numerical_features:
            new_feature_names.append(col)
        if len(categorical_features) > 0: # Only add if there are categorical features
            new_feature_names.extend(preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features))

        processed_df = pd.DataFrame(processed_array, columns=new_feature_names, index=df.index)
        print("Data preprocessing complete.")
        return processed_df
    except Exception as e:
        print(f"An error occurred during data preprocessing: {e}")
        return None
