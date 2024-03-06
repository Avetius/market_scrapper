import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from mplfinance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime

# Provided data
values = [306849.2511, 61033.25, 33830.0676, 993587.7247999999, 66157.2068, 178455.7194,
          168662.105, 15569.448, 580298.4762, 189993.87, 340879.41370000003, 741899.136,
          153014.7181, 2346740.5535999998, 1243239.4880000001, 40431.9825, 808474.506,
          125485.71175, 94345.04612, 947327.0132, 2075756.8260000001, 171243.08370000002,
          560192.5119, 577139322.4025]

timestamps = [1705116342059, 1705116342044, 1705116342013, 1705116342006, 1705116342005,
              1705116341991, 1705116341984, 1705116341977, 1705116341963, 1705116341930,
              1705116341929, 1705116341924, 1705116341923, 1705116341901, 1705116341893,
              1705116341891, 1705116341889, 1705116341846, 1705116341843, 1705116341839,
              1705116341831, 1705116341828, 1705116341806, 1705116341801]

# Convert timestamps to datetime objects
dates = [datetime.utcfromtimestamp(ts / 1000) for ts in timestamps]

# Prepare the data for candlestick chart
ohlc = list(zip(mdates.date2num(dates), values))

fig, ax = plt.subplots()

# Plot candlestick chart
candlestick_ohlc(ax, ohlc, width=0.6, colorup='g', colordown='r')

# Format x-axis to display dates nicely
ax.xaxis_date()
ax.xaxis.set_major_locator(WeekdayLocator(MONDAY))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

plt.title('Candlestick Chart')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()