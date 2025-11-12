import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def save_results_to_db(df: pd.DataFrame):
    """
    Loads cleaned F1 race results into a MySQL database.
    """
    print("Loading clean data into MySQL database...")

    # Database connection parameters
    user = "rayen"
    password = 'password'
    host = "127.0.0.1"
    database = "f1etl"

    # Create SQLAlchemy engine for MySQL
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

    # Save DataFrame to SQL table
    df.to_sql("raceResults", con=engine, if_exists="replace", index=False)

    print("Data successfully loaded into MySQL table 'raceResults'.")
