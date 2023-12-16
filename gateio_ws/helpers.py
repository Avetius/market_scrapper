from datetime import datetime

def convert_unix_timestamp_to_utc(timestamp):
    # Converting to a human-readable date and time
    date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return date_time

# Example usage
timestamp_example = 1545405058
converted_date_time = convert_unix_timestamp_to_utc(timestamp_example)
print(converted_date_time)


def convert_to_unix_timestamp(input_date_time):
    # Check if the input is a datetime object
    if isinstance(input_date_time, datetime):
        timestamp = datetime.timestamp(input_date_time)
    # Check if the input is a string
    elif isinstance(input_date_time, str):
        try:
            date_time_obj = datetime.strptime(input_date_time, '%Y-%m-%d %H:%M:%S')
            timestamp = datetime.timestamp(date_time_obj)
        except ValueError:
            return "Invalid date-time string format. Please use 'YYYY-MM-DD HH:MM:SS'."
    else:
        return "Invalid input type. Please provide a datetime object or a string."

    return int(timestamp)


# Example usage
date_time_example = '2023-12-10 15:10:58'
date_time_example2 = datetime.now()
date_time_example3 = str(datetime.now()).split('.')[0]
converted_timestamp = convert_to_unix_timestamp(date_time_example2)
print(converted_timestamp)
print(date_time_example3)