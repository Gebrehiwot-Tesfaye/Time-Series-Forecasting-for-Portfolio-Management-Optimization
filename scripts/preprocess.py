
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/raw')
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/processed')
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

ASSETS = ['TSLA', 'BND', 'SPY']

def preprocess(asset):
    file_path = os.path.join(RAW_DATA_DIR, f'{asset}.csv')
    df = pd.read_csv(file_path)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        df = df.reset_index().rename(columns={'index': 'Date'})
        df['Date'] = pd.to_datetime(df['Date'])

    # Sort and set index
    df = df.sort_values('Date').reset_index(drop=True)

    # Handle missing values
    df = df.fillna(method='ffill').fillna(method='bfill')

    # Feature engineering
    df['Return'] = df['Adj Close'].pct_change()
    df['LogReturn'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))
    df['Volatility'] = df['Return'].rolling(window=21).std()
    df['RollingMean'] = df['Adj Close'].rolling(window=21).mean()
    df['RollingStd'] = df['Adj Close'].rolling(window=21).std()

    # Outlier detection (z-score)
    df['z_score'] = (df['Return'] - df['Return'].mean()) / df['Return'].std()

    # Normalization (for ML)
    scaler = StandardScaler()
    scaled_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df[[f'{col}_scaled' for col in scaled_cols]] = scaler.fit_transform(df[scaled_cols])

    # Drop initial rows with NaN after rolling
    df = df.dropna().reset_index(drop=True)

    # Save processed data
    df.to_csv(os.path.join(PROCESSED_DATA_DIR, f'{asset}_processed.csv'), index=False)
    print(f"Processed {asset}.")

    # Print basic stats
    print(df.describe())

if __name__ == '__main__':
    for asset in ASSETS:
        preprocess(asset)
