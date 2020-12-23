
#!/user/bin/python shi-bang
# import requests
# import bs4
# import lxml
import random
import numpy as np
import pandas as pd
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import time
from datetime import datetime
import matplotlib.pyplot as plt
# from matplotlib import style
import yfinance as yf


# date range
start_date = '2000-01-01'
end_date = str(datetime.now().strftime('%Y-%m-%d'))

print(end_date)

# select stocks
dictionary = {}
tickers = ['CBA.AX', 'WBC.AX', 'NAB.AX', 'ANZ.AX', 'TLS.AX', 'CSL.AX']
for t in tickers:
    ticker = yf.Ticker(t)
    dictionary[t] = ticker.info

asx = yf.download(tickers, start=start_date, end=end_date)

# save dataframes to spreadsheet


df1 = pd.DataFrame(asx)

df2 = pd.DataFrame(dictionary)



"""
df1.to_excel('/Users/jforbes84/PycharmProjects/Cash Flow/stockYF.xlsx')

writer = pd.ExcelWriter('/Users/jforbes84/PycharmProjects/Cash Flow/stockYF.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='portfolio')
df2.to_excel(writer, sheet_name='stockInfo')
writer.save()
"""

# 5 day trading volume / income / dividends from graphs

# save to dataframe - ok

# research stock KPI's

# ML pricing

# schedule auto update to sheet

# surface in tableau

"""

stock = 'CBA.AX'

def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }

def clean_data(stock_data, col):
    weekdays = pd.date_range(start=start_date, end=end_date)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def create_plot(stock_data, ticker):
    stats = get_stats(stock_data)
    # plt.style.use('dark_background')
    plt.subplots(figsize=(12,8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label='20 day rolling mean')
    plt.plot(stats['long_rolling'], label='200 day rolling mean')
    plt.xlabel('Date')
    plt.ylabel('Adj Close (p)')
    plt.legend()
    plt.title('Stock Price over Time')
    # plt.show()

def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker,
                                     'yahoo',
                                     start_date,
                                     end_date)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plot(adj_close, ticker)
        
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))
        
get_data(stock)


"""
