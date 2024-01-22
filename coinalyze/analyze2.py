import psycopg2
from psycopg2 import sql
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime

import os

load_dotenv()
host = os.getenv("POSTGRES_HOST")
user = os.getenv("POSTGRES_USER")
database_name = os.getenv("POSTGRES_DB")
password = os.getenv("POSTGRES_PASSWORD")

def update_to_datetime(timestamp_in_milliseconds = 1705050113170):
    # Replace 'timestamp_in_milliseconds' with your actual timestamp
    timestamp_in_milliseconds = 1705050113170

    # Convert milliseconds to seconds
    timestamp_in_seconds = timestamp_in_milliseconds / 1000

    # Convert to a datetime object
    datetime_object = datetime.utcfromtimestamp(timestamp_in_seconds)

    # Format the datetime object as a string
    formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')

    print(formatted_time)
    return formatted_time

def datetime_to_update(time_string = '2023-01-01 00:00:00'):
    # Convert the time string to a datetime object
    datetime_object = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

    # Convert the datetime object to a Unix timestamp in milliseconds
    timestamp_in_milliseconds = int(datetime_object.timestamp() * 1000)

    print(timestamp_in_milliseconds)
    return timestamp_in_milliseconds



# Replace these with your TimescaleDB connection details
db_params = {
    'host': host,
    'database': database_name,
    'user': user,
    'password': password
}

# Connect to the TimescaleDB database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Replace 'your_table' with your actual table name
table_name = 'gateio_oi'

# Replace 'symbol_column', 'update_column', and 'value_column' with your actual column names
symbol_column = 'symbol'
update_column = 'update'
value_column = 'value'

# Specify the symbol and time range
symbol_value = 'ASTRA'
start_time = '1705050043635'
end_time = '1705116342059'

# Query to select 'value' where 'symbol' is 'ASTRA' and 'update' is within the specified time range
query = sql.SQL("SELECT {} FROM {} WHERE {} = %s AND {} BETWEEN %s AND %s ORDER BY {};").format(
    sql.Identifier(value_column),
    sql.Identifier(table_name),
    sql.Identifier(symbol_column),
    sql.Identifier(update_column),
    sql.Identifier(update_column)
)

# Execute the query
cursor.execute(query, (symbol_value, start_time, end_time))

# Fetch the data
data = cursor.fetchall()

# Close the database connection
cursor.close()
conn.close()
    
def detectOI(sym):

  url = 'https://api.coinalyze.net/v1/open-interest-history?symbols='+sym+'&from='+str(before)+'&to='+str(now)+'&interval=15min&convert_to_usd=false&api_key='+api

  print(url)

  df = requests.get(url).json()
  dumps = json.dumps(df)
  loads = json.loads(dumps)

  if len(loads) > 0:
    ticker = loads[0]['symbol']

    df = pd.DataFrame(loads[0]['history'])

    # Convert unix timestamps to datetime
    df['datetime'] = pd.to_datetime(df['t'], unit='s')

    # Calculate percentage change
    df['change'] = (df['h'] - df['l']) / df['l'] * 100

    # Check if change exceeds 10%
    mask = df['change'] > 5

    # Perform action on subset where true
    df.loc[mask, 'alert'] = 1

    # Get starting o/h/l/c values
    start_o = df['o'].iloc[0]
    start_h = df['h'].iloc[0]
    start_l = df['l'].iloc[0]
    start_c = df['c'].iloc[0]

    # Calculate min value
    min_value = min(start_o, start_h, start_l, start_c)

    # Normalize columns
    df['open'] = (df['o'] - min_value) / min_value
    df['high'] = (df['h'] - min_value) / min_value
    df['low'] = (df['l'] - min_value) / min_value
    df['close'] = (df['c'] - min_value) / min_value

    # Create a candlestick chart using plotly
    candlestick = go.Candlestick(x=df['datetime'], open=df["open"], high=df["high"], low=df["low"], close=df["close"])

    # Create a layout object
    layout = go.Layout(title=ticker, yaxis_title="OI (%)", xaxis_rangeslider_visible=False)

    # Create a Figure object
    fig = go.Figure(data=[candlestick], layout=layout)

    # Show the chart
    fig.update_yaxes(tickformat='.2%')

    # Add spike annotations
    fig.add_trace(go.Scatter(
      x = df[df['alert']==1]['datetime'],
      y = df[df['alert']==1]['high'],
      mode = 'markers',
      marker = dict(color='black',size=10)
    ))
    fig.show()

  else:
    print('JSON is empty')

##################################################################