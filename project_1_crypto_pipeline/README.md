# Crypto Data ETL Pipeline

This project implements a simple ETL pipeline that extracts 
cryptocurrency market data from the CoinGecko API, transforms the dataset using pandas, and saves it as a structured CSV file.

## Technologies Used

- Python
- Pandas
- Requests
- CSV storage

## How to Run

Install dependencies:
pip install pandas requests

Run the pipeline:
python main.py

## Pipeline Architecture
CoinGecko API
      ↓
Extract (requests)
      ↓
Transform (pandas + validation)
      ↓
Load (CSV storage)

The pipeline follows a simple ETL architecture. Data is extracted from the CoinGecko public API, transformed using pandas with basic data validation, and loaded into a CSV dataset for further analysis.

