def print_list_in_rows(lst, row_length):
    """
    Prints the elements of a list in rows of a specified length.

    Args:
        lst (list): The list of elements to be printed.
        row_length (int): The number of elements to be printed in each row.

    Returns:
        None
    """
    for i in range(0, len(lst), row_length):
        print(", ".join(map(str, lst[i:i+row_length])))