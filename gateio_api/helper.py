def list_to_string(lst, delimiter=','):
    """
    Convert a list to a string, with elements separated by a delimiter.
    
    :param lst: The list to convert.
    :param delimiter: The delimiter to use for separating list items.
    :return: A string representation of the list.
    """
    return delimiter.join(str(item) for item in lst)

def string_to_list(string, delimiter=','):
    """
    Convert a string to a list, splitting the string by a delimiter.
    
    :param string: The string to convert.
    :param delimiter: The delimiter used in the string.
    :return: A list of items.
    """
    return string.split(delimiter)

if __name__ == '__main__':
    # Example Usage
    my_list = ['apple', 'banana', 'cherry']
    list_string = list_to_string(my_list)
    print("List to String:", list_string)

    reverted_list = string_to_list(list_string)
    print("String to List:", reverted_list)