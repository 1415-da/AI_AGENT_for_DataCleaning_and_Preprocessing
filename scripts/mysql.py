from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

class MySQLConnector:
    def __init__(self, db_connection_str):
        self.db_connection_str = db_connection_str
        self.engine = None

    def connect(self):
        """
        Establishes a connection to the MySQL database.
        """
        try:
            self.engine = create_engine(self.db_connection_str)
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Successfully connected to the MySQL database.")
            return True
        except SQLAlchemyError as e:
            print(f"Error connecting to the database: {e}")
            self.engine = None
            return False

    def save_data(self, df: pd.DataFrame, table_name: str, if_exists: str = 'replace'):
        """
        Saves a pandas DataFrame to a specified MySQL table.
        'if_exists' can be 'fail', 'replace', or 'append'.
        """
        if self.engine is None:
            print("Database engine not initialized. Call connect() first.")
            return False
        try:
            df.to_sql(name=table_name, con=self.engine, if_exists=if_exists, index=False)
            print(f"Successfully saved data to table '{table_name}'.")
            return True
        except SQLAlchemyError as e:
            print(f"Error saving data to table {table_name}: {e}")
            return False

    def read_data(self, table_name: str):
        """
        Reads data from a specified MySQL table into a pandas DataFrame.
        """
        if self.engine is None:
            print("Database engine not initialized. Call connect() first.")
            return None
        try:
            df = pd.read_sql_table(table_name, con=self.engine)
            print(f"Successfully read data from table '{table_name}'.")
            return df
        except SQLAlchemyError as e:
            print(f"Error reading data from table {table_name}: {e}")
            return None

    def table_exists(self, table_name: str) -> bool:
        """
        Checks if a given table exists in the connected database.
        """
        if self.engine is None:
            print("Database engine not initialized. Call connect() first.")
            return False
        try:
            inspector = inspect(self.engine)
            return inspector.has_table(table_name)
        except SQLAlchemyError as e:
            print(f"Error checking for table {table_name}: {e}")
            return False

# Example Usage (for testing purposes)
if __name__ == "__main__":
    # Replace with your actual database connection string
    # Example: "mysql+mysqlconnector://user:password@host/dbname"
    # For this example, we'll use a placeholder. To run, you'd need a running MySQL instance.
    DB_CONNECTION_STRING = "mysql+mysqlconnector://user:password@localhost/test_db"

    db_connector = MySQLConnector(DB_CONNECTION_STRING)
    if db_connector.connect():
        # Create a dummy DataFrame to save
        data = {'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}
        df_test = pd.DataFrame(data)
        table_name = "test_table"

        # Save data
        db_connector.save_data(df_test, table_name)

        # Read data
        df_read = db_connector.read_data(table_name)
        if df_read is not None:
            print("\nData read from DB:")
            print(df_read)

        # Check if table exists
        print(f"Does table '{table_name}' exist? {db_connector.table_exists(table_name)}")

        # Example of appending data
        data_append = {'col1': [4], 'col2': ['D']}
        df_append = pd.DataFrame(data_append)
        db_connector.save_data(df_append, table_name, if_exists='append')

        df_read_appended = db_connector.read_data(table_name)
        if df_read_appended is not None:
            print("\nData after append:")
            print(df_read_appended)
    else:
        print("Failed to connect to MySQL, skipping database operations.")
