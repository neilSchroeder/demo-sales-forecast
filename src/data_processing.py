"""
Data processing utilities for sales forecasting.
"""

import pandas as pd
import numpy as np
from typing import Tuple


def load_sales_data(filepath: str) -> pd.DataFrame:
    """
    Load sales data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        DataFrame with parsed dates
    """
    df = pd.read_csv(filepath, parse_dates=['Order_Date'])
    return df


def prepare_time_series(df: pd.DataFrame, 
                        date_col: str = 'Order_Date',
                        value_col: str = 'Sales',
                        freq: str = 'D') -> pd.DataFrame:
    """
    Prepare time series data by aggregating to specified frequency.
    
    Args:
        df: Input DataFrame
        date_col: Name of date column
        value_col: Name of value column to aggregate
        freq: Frequency for resampling ('D', 'W', 'M')
        
    Returns:
        DataFrame with date index and aggregated values
    """
    ts_df = df.groupby(pd.Grouper(key=date_col, freq=freq))[value_col].sum().reset_index()
    ts_df.columns = ['ds', 'y']  # Prophet format
    return ts_df


def calculate_metrics(actual: np.ndarray, predicted: np.ndarray) -> dict:
    """
    Calculate forecasting accuracy metrics.
    
    Args:
        actual: Array of actual values
        predicted: Array of predicted values
        
    Returns:
        Dictionary with MAE, RMSE, MAPE
    """
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'MAPE': mape
    }


def split_train_test(df: pd.DataFrame, 
                     test_size: int = 30) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split time series data into train and test sets.
    
    Args:
        df: Input DataFrame
        test_size: Number of periods for test set
        
    Returns:
        Tuple of (train_df, test_df)
    """
    train = df.iloc[:-test_size]
    test = df.iloc[-test_size:]
    return train, test


def detect_outliers(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    Detect outliers using z-score method.
    
    Args:
        series: Input time series
        threshold: Z-score threshold
        
    Returns:
        Boolean series indicating outliers
    """
    z_scores = np.abs((series - series.mean()) / series.std())
    return z_scores > threshold
