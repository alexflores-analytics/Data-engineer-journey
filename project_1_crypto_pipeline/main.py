import requests
import pandas as pd

# Step 1: Extract data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params)
data = response.json()

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Select relevant columns
df = df[[
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume"
]]

# Step 4: Save to CSV
df.to_csv("data/crypto_data.csv", index=False)

print("Data pipeline executed successfully.")
