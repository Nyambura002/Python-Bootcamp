import pandas as pd

def load_data(file_path):
    # Load the data from the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    # Load the data
    file_path = ("C:/Users/user/Downloads/MOCK_DATA.csv")
    
    data = load_data(file_path)
    
    print("Data loaded successfully:")
    
    print(data.head())

