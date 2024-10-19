import matplotlib.pyplot as plt

def visualize_data(df):
    """
    Visualize the cleaned SQL DataFrame.

    Parameters:
    df (DataFrame): DataFrame containing the cleaned data.
    """
    df['SomeMetric'].plot(kind='line')  # Example metric
    plt.title('Some Metric Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig('image/data_visualization.png')
    plt.show()
