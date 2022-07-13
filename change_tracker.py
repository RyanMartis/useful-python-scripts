import os
import yfinance as yf
import pendulum
import matplotlib.pyplot as plt
import matplotlib.axis as axis
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from pprint import pprint
from datetime import datetime
# needed for animated charts
import matplotlib.animation as animation
from matplotlib import style

# Get stock data from API
tsla_stock_info = yf.Ticker('TSLA').info
tsla_market_price = tsla_stock_info['regularMarketPrice']
tsla_previous_close_price = tsla_stock_info['regularMarketPreviousClose']
tsla_price_history = yf.Ticker('TSLA').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)

# matplotlib style spec
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# I need to pull a backlog of data (i.e. ticker.history(period, interval, actions...)
# example pprint(yf.Ticker('TSLA').history(period='1d', interval='5m')) 
# from this I can use the date and corresponding "close" price? 
# every minute, we query again (not sure what the rate limit is here)

# while looping, I'd need to get the "current price" and then a date (can likely set this to current date/time).
# This might make sense to have a final list of dictionary elements (price and date)
# then have pandas datafram and then plot this

# Let's print this live list of data out every minute and see how it looks. 
# once the data is good and updating as expected, animated graphs should work too

# Get stock data from API
tm_stock_info = yf.Ticker('TM').info
tm_market_price = tm_stock_info['regularMarketPrice']
tm_previous_close_price = tm_stock_info['regularMarketPreviousClose']
tm_price_history = yf.Ticker('TM').history(period='2y', # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                   interval='1wk', # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                   actions=False)
# create list for plotting
tsla_time_series = list(tsla_price_history['Open'])
tm_time_series = list(tm_price_history['Open'])

# not the most readable imo
# dt_list = [pendulum.parse(str(dt)).date() for dt in list(price_history.index)]

dt_list = []

for dt in list(tsla_price_history.index):
    MD_date = '{:%b-%d-%Y}'.format(datetime.strptime(str(dt.date()), '%Y-%m-%d'))
    dt_list.append(MD_date)

figure, axis = plt.subplots(2)

plt.style.use('dark_background')
ax = plt.gca()
#print(ax)
#print(axis[0])
axis[0].xaxis.set_major_locator(ticker.AutoLocator())#MonthLocator(interval=1))#ticker.AutoLocator())
axis[0].plot(dt_list, tsla_time_series, linewidth=2, color='black')
axis[0].set_facecolor('darkslategrey')
axis[0].set_title("TSLA")
figure.patch.set_facecolor('darkslategrey')

axis[1].xaxis.set_major_locator(ticker.AutoLocator())
axis[1].plot(dt_list, tm_time_series, linewidth=2, color='black')
axis[1].set_facecolor('darkslategrey')
axis[1].set_title("TM")
# doesnt seem to work... x axis still has all the intervals as ticks
#plt.locator_params(nbins=10)
plt.show()

#print('TSLA market_price ', market_price )
#print('TSLA previous close price', previous_close_price )



# path = '/home/ryan/'

# files = os.listdir(path)

# for file in files:
#    print(file)

# get data from somewhere
