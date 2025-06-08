import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_data(symbol, days=30):
    end = datetime.now()
    start = end - timedelta(days=days)
    data = yf.download(symbol, start=start, end=end)
    return data.reset_index()