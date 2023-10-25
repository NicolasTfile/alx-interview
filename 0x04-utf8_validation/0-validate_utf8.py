#!/usr/bin/python3
"""
UTF-8 Validation for data sets
"""


def validUTF8(data) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data: A list of integers representing the data set

    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """

    # Check if the data set is empty
    if not data:
        return False

    # Initialize a variable to track the number of continuation bytes
    continuation_bytes = 0

    # Iterate over the data set
    for byte in data:
        # Check if the byte is a start byte
        if byte & 0b10000000 == 0:
            # If the byte is a start byte,
            # reset the number of continuation bytes
            continuation_bytes = 0

        # Check if the byte is a continuation byte
        elif byte & 0b11000000 == 0b10000000:
            # If the byte is a continuation byte,
            # increment the number of continuation bytes
            continuation_bytes += 1

            # Check if the number of continuation bytes exceeds 4
            if continuation_bytes > 4:
                return False

        else:
            # If the byte is not a start byte or a continuation byte,
            # the data set is not a valid UTF-8 encoding
            return False

    # If the data set ends with a continuation byte,
    # the data set is not a valid UTF-8 encoding
    if continuation_bytes > 0:
        return False

    # Otherwise, the data set is a valid UTF-8 encoding
    return True
