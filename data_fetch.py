# data_fetch.py

import requests
import pandas as pd
from config import TWELVE_DATA_API_KEY

def get_chfjpy_price():
    url = f"https://api.twelvedata.com/price?symbol=CHF/JPY&apikey={TWELVE_DATA_API_KEY}"
    res = requests.get(url).json()
    return float(res['price'])

def get_ohlc_data(interval='1min', outputsize=50):
    url = f"https://api.twelvedata.com/time_series?symbol=CHF/JPY&interval={interval}&outputsize={outputsize}&apikey={TWELVE_DATA_API_KEY}"
    res = requests.get(url).json()
    
    values = res.get('values', [])
    df = pd.DataFrame(values)
    
    if df.empty:
        return None
    
    df = df.rename(columns={
        'datetime': 'timestamp',
        'open': 'open',
        'high': 'high',
        'low': 'low',
        'close': 'close'
    })
    
    df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
    df = df.sort_values(by='timestamp')
    df.reset_index(drop=True, inplace=True)
    
    return df
