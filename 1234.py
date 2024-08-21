import yfinance as yf

# Download data for a specific stock
data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')
data.to_csv('AAPL_data.csv')