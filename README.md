# XAUUSD Forecasting Project

## Description
The XAUUSD forecasting project aims to predict the future prices of Gold (XAU) against the US Dollar (USD). Utilizes historical data and machine learning models to provide insights into potential price movements.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/arjunsagarsharma96/GOLD-FORECASTING.git
   ```
2. Navigate to the project directory:
   ```bash
   cd GOLD-FORECASTING
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guide
1. Prepare your data by placing the historical XAUUSD data in the appropriate directory.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to view the forecasting results.

## Model Details
- **Model Type**: Random Forest Regressor
- **Features Used**: Previous prices, volume, and other technical indicators
- **Evaluation Metric**: Mean Absolute Error (MAE)