import pandas as pd
import matplotlib.pyplot as plt

def plot_most_watched_shows(data):
    """
    Plot the most watched shows.
    
    Parameters:
    - data: pd.DataFrame, preprocessed Netflix data
    """
    # Example implementation: counting most watched shows
    most_watched = data['Title'].value_counts().head(10)
    
    plt.figure(figsize=(10, 5))
    most_watched.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Most Watched Shows')
    plt.xlabel('Show Title')
    plt.ylabel('Watch Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('results/most_watched_shows.png')
    plt.close()
