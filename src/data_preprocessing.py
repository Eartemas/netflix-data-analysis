import pandas as pd

def load_data(filepath):
    """
    Load Netflix data from a CSV file.
    
    Parameters:
    - filepath: str, path to the CSV file
    
    Returns:
    - pd.DataFrame, loaded Netflix data
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess Netflix data.
    
    Parameters:
    - data: pd.DataFrame, Netflix data
    
    Returns:
    - pd.DataFrame, preprocessed Netflix data
    """
    # Example preprocessing: renaming columns, converting types, etc.
    data.columns = [col.strip() for col in data.columns]
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data.dropna(subset=['Date'], inplace=True)
    return data
