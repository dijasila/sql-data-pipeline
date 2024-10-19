import pandas as pd
from sqlalchemy import create_engine

def read_sql_data(connection_string, query):
    """
    Read data from a SQL database.

    Parameters:
    connection_string (str): SQL Alchemy connection string.
    query (str): SQL query to execute.

    Returns:
    DataFrame: A pandas DataFrame containing the queried data.
    """
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
    return df
