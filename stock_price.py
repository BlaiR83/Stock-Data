import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#---株価データの取得---#
ticker = 'AAPL'
stock_data = yf.download(ticker, start='2022-01-01', end='2024-07-31', progress=True)

#---株価データの基本統計量を表示---#
print('基本統計量：')
print(stock_data.describe())

#---終値のプロット(終値を基に株価のパフォーマンスや傾向を評価するため重要)---#
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')

#---移動平均線の追加---#
#５０日移動平均線
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
#２００日移動平均線
stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

plt.plot(stock_data.index, stock_data['MA50'], label='50-Day MA', color='orange')
plt.plot(stock_data.index, stock_data['MA200'], label='200-Day MA', color='green')

#---ボリンジャーバンドの計算---#
#２０日移動平均線 ボリンジャーバンドの中央線として利用
stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()
plt.plot(stock_data.index, stock_data['MA20'], label='20-Day MA', color='purple')
#２０日標準偏差
stock_data['stddev'] = stock_data['Close'].rolling(window=20).std()
#上部バンド
stock_data['Upper Band'] = stock_data['MA20'] + (2*stock_data['stddev'])
plt.plot(stock_data.index, stock_data['Upper Band'], label='Upper Band', color='red')
#下部バンド
stock_data['Lower Band'] = stock_data['MA20'] - (2*stock_data['stddev'])
plt.plot(stock_data.index, stock_data['Lower Band'], label='Lower Band', color='red')

plt.title('Apple Stock Closing Price with Moving Averages and Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price(USD)')
plt.legend()
plt.grid()
plt.show()