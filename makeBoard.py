import pandas as pd
import requests

# Function to extract two columns from CSV and post to online leaderboard
def extract_and_post(csv_path, column1, column2, leaderboard_url):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Extract specified columns
    selected_columns = df[[column1, column2]]

    # Convert DataFrame to a list of dictionaries
    data_to_post = selected_columns.to_dict(orient='records')

    # Post data to online leaderboard
    response = requests.post(leaderboard_url, json=data_to_post)

    # Print the response
    print(response.text)

# Example usage
csv_path = 'your_csv_file.csv'
column1 = 'column_name1'
column2 = 'column_name2'
leaderboard_url = 'https://keepthescore.com/online-leaderboard-maker/'

extract_and_post(csv_path, column1, column2, leaderboard_url)
