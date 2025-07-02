import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta



def get_stock_candles(symbol, start_date, end_date):
    # Fetch data with auto_adjust=True to avoid MultiIndex
    data = yf.download(symbol, start=start_date, end=end_date, auto_adjust=True)
    
    if data.empty:
        raise Exception(f"No price data for {symbol}")
    
    # Reset index to make date a regular column
    data = data.reset_index()
    
    # Standardize column names
    data = data.rename(columns={
        "Date": "date",
        "Adj Close": "adj_close",
        "Close": "close",
        "High": "high",
        "Low": "low",
        "Open": "open",
        "Volume": "volume"
    })
    
    # Ensure date is in proper format
    data['date'] = pd.to_datetime(data['date']).dt.date
    
    return data
