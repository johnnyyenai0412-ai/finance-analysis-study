import pandas as pd
import yfinance as yf # 這是一個專門抓取 Yahoo Finance 數據的工具

# 設定你想觀察的股票代號
stocks = ['NVDA', 'TSLL', 'SOXL', 'QQQM']

# 抓取最新的市場數據
print("正在從 Yahoo Finance 抓取數據...")
data = yf.download(stocks, period="1d")

# 印出目前的收盤價
print("\n--- 最新收盤價 ---")
print(data['Close'])