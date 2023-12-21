from datetime import datetime

def convert_unix_timestamp_to_utc(timestamp):
    # Converting to a human-readable date and time
    date_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return date_time


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


def list_to_string(lst, delimiter=','):
    """
    Convert a list to a string, with elements separated by a delimiter.
    
    :param lst: The list to convert.
    :param delimiter: The delimiter to use for separating list items.
    :return: A string representation of the list.
    """
    return delimiter.join(str(item) for item in lst)


def string_to_list(inputstr='', delimiter=','):
    """
    Convert a string to a list, splitting the string by a delimiter.
    
    :param string: The string to convert.
    :param delimiter: The delimiter used in the string.
    :return: A list of items.
    """
    newList = inputstr.split(delimiter)
    print(newList)
    return newList


if __name__ == '__main__':
    # Example usage
    date_time_example = '2023-12-10 15:10:58'
    date_time_example2 = datetime.now()
    date_time_example3 = str(datetime.now()).split('.')[0]
    converted_timestamp = convert_to_unix_timestamp(date_time_example2)
    print(converted_timestamp)
    print(date_time_example3)
    # Example usage
    timestamp_example = 1545405058
    converted_date_time = convert_unix_timestamp_to_utc(timestamp_example)
    print(converted_date_time)