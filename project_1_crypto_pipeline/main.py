import requests
import pandas as pd

def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error fetching data")
        return None

    return response.json()

def transform_data(data):
    if not data:
    print("No data to transform.")
    return None

    df = pd.DataFrame(data)

    if df.empty:
        print("DataFrame is empty.")
        return None
    
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]]
    return df

def load_data(df):
    if df is None:
    print("No data to load.")
    return

    df.to_csv("data/crypto_data.csv", index=False)
    print("Data saved successfully.")

def main():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

if __name__ == "__main__":
    main()
