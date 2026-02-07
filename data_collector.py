import yfinance as yf
import pandas as pd
import numpy as np

# Function to collect historical XAUUSD data

def collect_xauusd_data(start_date, end_date):
    # Collect the data
    data = yf.download('XAUUSD=X', start=start_date, end=end_date)
    return data

# Function to clean the data

def clean_data(data):
    # Drop rows with NaN values
    data = data.dropna()
    return data

# Function to add technical indicators

def add_technical_indicators(data):
    # Simple Moving Average (SMA)
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    # Exponential Moving Average (EMA)
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    # Add more indicators as needed here
    return data

# Main execution block
if __name__ == '__main__':
    start_date = '2008-01-01'
    end_date = '2026-01-31'
    xauusd_data = collect_xauusd_data(start_date, end_date)
    cleaned_data = clean_data(xauusd_data)
    final_data = add_technical_indicators(cleaned_data)
    # Save to CSV
    final_data.to_csv('xauusd_data.csv')
    print('Data collection and processing complete, saved to xauusd_data.csv')
