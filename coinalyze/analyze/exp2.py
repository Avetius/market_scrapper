from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as datetime
import numpy as np
quotes = np.array(...)
fig, ax = plt.subplots()
candlestick2_ohlc(ax,quotes['open'],quotes['high'],quotes['low'],quotes['close'],width=0.6)
xdate = [datetime.datetime.fromtimestamp(i) for i in quotes['time']]
ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
def mydate(x,pos):
    try:
        return xdate[int(x)]
    except IndexError:
        return ''
ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
fig.autofmt_xdate()
fig.tight_layout()
plt.show()