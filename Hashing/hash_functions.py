"""hash functions"""


def mod(number, cell_number):
    """
    number (int|float): key to be hashed
    cell_number (int): hash value. The number of cells available in our hash table in this case (24)

    search - O(1)
    """

    return number % cell_number


print(mod(400, 24))  # means 400 goes into cell 16


def mod_ascii(string, cell_number):
    total = 0

    for char in string:
        total += ord(char)

    return total % cell_number


print(mod_ascii("boy", 24))  # means 400 goes into cell 16
