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

    # Initialize the number of continuation bytes
    continuation_bytes = 0

    # Iterate over the bytes in the data array
    for byte in data:

        # Create a mask to check if the most
        # significant bit of the byte is set
        mask = 1 << 7

        # If the number of continuation bytes is zero,
        # then the byte must be a start byte
        if not continuation_bytes:

            # Keep shifting the mask to the right until we
            # find the most significant bit that is set
            while byte & mask:
                continuation_bytes += 1
                mask >>= 1

            # If the number of continuation bytes is still zero,
            # then the byte is not a valid start byte
            if not continuation_bytes:
                continue

            # If the number of continuation bytes is 1 or greater than 4,
            # then the byte is not a valid start byte
            if continuation_bytes == 1 or continuation_bytes > 4:
                return False

        # Otherwise, the byte must be a continuation byte
        else:

            # If the most significant two bits of the byte are not set to 10,
            # then the byte is not a valid continuation byte
            if byte >> 6 != 0b10:
                return False

        # Decrement the number of continuation bytes
        continuation_bytes -= 1

    # If the number of continuation bytes is not zero,
    # then the byte array is not a valid UTF-8 encoding
    return continuation_bytes == 0
