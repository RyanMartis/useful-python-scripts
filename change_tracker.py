import os
import yfinance as yf
import pendulum
import matplotlib.pyplot as plt

stock_info = yf.Ticker('TSLA').info
market_price = stock_info['regularMarketPrice']
previous_close_price = stock_info['regularMarketPreviousClose']
price_history = yf.Ticker('TSLA').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)

time_series = list(price_history['Open'])
dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]

plt.style.use('dark_background')
plt.plot(dt_list, time_series, linewidth=2)


#print('TSLA market_price ', market_price )
#print('TSLA previous close price', previous_close_price )



# path = '/home/ryan/'

# files = os.listdir(path)

# for file in files:
#    print(file)

# get data from somewhere