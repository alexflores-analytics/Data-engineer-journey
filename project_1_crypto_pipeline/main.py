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

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None

def transform_data(data):
    if not data:
        print("No data to transform.")
        return None

    df = pd.DataFrame(data)

    if df.empty:
        print("DataFrame is empty.")
        return None
    
    required_columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]

    missing_cols = [col for col in required_columns if col not in df.columns]

    if missing_cols:
        print(f"Missing columns: {missing_cols}")
        return None

    df = df[required_columns]

    return df

def load_data(df):
    if df is None:
        print("No data to load.")
        return

    try:
        df.to_csv("data/crypto_data.csv", index=False)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    data = extract_data()
    df = transform_data(data)
    load_data(df)

if __name__ == "__main__":
    main()
