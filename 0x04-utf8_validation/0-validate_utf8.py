#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    data: List of integers representing a sequence of bytes.

    Returns:
    True if the data represents valid UTF-8 encoding, else False.
    """
    i = 0
    while i < len(data):
        byte = data[i]
        if byte < 0 or byte > 255:
            return False

        num_bytes = 0

        if (byte >> 7) == 0:
            num_bytes = 1  # 0xxxxxxx
        elif (byte >> 5) == 0b110:
            num_bytes = 2  # 110xxxxx
        elif (byte >> 4) == 0b1110:
            num_bytes = 3  # 1110xxxx
        elif (byte >> 3) == 0b11110:
            num_bytes = 4  # 11110xxx
        else:
            return False  # Invalid start byte

        # Check if we have enough bytes left for the sequence
        if i + num_bytes > len(data):
            return False

        # Check continuation bytes (all must start with 10xxxxxx)
        for j in range(1, num_bytes):
            if (data[i + j] >> 6) != 0b10:
                return False

        # Move to the next byte after the valid sequence
        i += num_bytes

    return True
