def integrate_data(df1, df2, key):
    """
    Integrate two DataFrames based on a key.

    Parameters:
    df1 (DataFrame): First DataFrame.
    df2 (DataFrame): Second DataFrame.
    key (str): Key column to join on.

    Returns:
    DataFrame: Integrated DataFrame.
    """
    return pd.merge(df1, df2, on=key, how='inner')
