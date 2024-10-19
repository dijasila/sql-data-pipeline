def clean_data(df):
    """
    Clean the SQL DataFrame for analysis.

    Parameters:
    df (DataFrame): Input DataFrame.

    Returns:
    DataFrame: A cleaned DataFrame.
    """
    # Example cleaning: handle missing values and remove duplicates
    df = df.fillna(method='ffill')  # Forward fill
    df = df.drop_duplicates()
    return df
