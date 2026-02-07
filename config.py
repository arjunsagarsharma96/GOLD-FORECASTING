# Configuration file for XAUUSD forecasting models

# Date ranges
START_DATE = "2020-01-01"
END_DATE = "2026-01-01"

# Model parameters
MODEL_TYPE = "ARIMA"  # Options: ARIMA, LSTM, etc.
P = 5    # Order of the autoregressive part
D = 1    # Degree of differencing
Q = 0    # Order of the moving average part
TRAINING_RATIO = 0.8

# Visualization settings
PLOT_STYLE = "seaborn"  # Options: seaborn, ggplot, etc.
SHOW_GRID = True
SAVE_PLOTS = True
