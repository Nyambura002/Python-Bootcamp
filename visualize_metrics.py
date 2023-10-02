import pandas as pd
from data import load_data

def preprocess_data(data):
    data['viewing_duration'] = pd.to_datetime(data['viewing_duration'], format='%I:%M %p')

    # Extracting hour and minute for analysis
    data['viewing_hour'] = data['viewing_duration'].dt.hour
    data['viewing_minute'] = data['viewing_duration'].dt.minute

    return data

def visualize_metrics(data):
    # Visualize the metrics
    print("Mean Viewing Hour:", data['viewing_hour'].mean())
    print("Mean Viewing Minute:", data['viewing_minute'].mean())
    print("Median Likes:", data['likes'].median())
    print("Mean Comments:", data['comments'].mean())
    print("Median Shares:", data['shares'].median())

if __name__ == "__main__":
    file_path = "C:/Users/user/Downloads/MOCK_DATA.csv"
    data = load_data(file_path)
    
    # Preprocess the data
    data = preprocess_data(data)
    
    # Call the visualize_metrics function
    visualize_metrics(data)
