import pandas as pd
from data import load_data  

def calculate_metrics(data):
    
    mean_viewing_duration = data['viewing_duration'].mean()
    median_likes = data['likes'].median()
    mean_comments = data['comments'].mean()
    median_shares = data['shares'].median()


    # Display the metrics
    print("Metrics:")
    print("Mean Viewing Duration:", mean_viewing_duration)
    print("Median Likes:", median_likes)
    print("Mean Comments:", mean_comments)
    print("Median Shares:", median_shares)

if __name__ == "__main__":

    file_path = "C:/Users/user/Downloads/MOCK_DATA.csv"  
    data = load_data(file_path)


    #calling the calculate_metrics function
    calculate_metrics(data)
