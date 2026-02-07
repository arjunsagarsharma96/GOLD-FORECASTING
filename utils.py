# utils.py

"""
Utility functions for XAUUSD forecasting analysis.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def prepare_data(data, target_column):
    """
    Prepare data for modeling by splitting into features and target.
    
    Parameters:
        data (pd.DataFrame): The input data containing features and target.
        target_column (str): The name of the target column in the DataFrame.
    
    Returns:
        X (pd.DataFrame): Features.
        y (pd.Series): Target variable.
    """
    X = data.drop(columns=[target_column])
    y = data[target_column]
    return X, y


def plot_forecasting_results(y_true, y_pred):
    """
    Plot the actual vs predicted values.
    
    Parameters:
        y_true (pd.Series): Actual values.
        y_pred (pd.Series): Predicted values from the model.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(y_true.index, y_true, label='Actual', color='blue')
    plt.plot(y_pred.index, y_pred, label='Predicted', color='orange')
    plt.title('XAUUSD Forecasting Results')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()