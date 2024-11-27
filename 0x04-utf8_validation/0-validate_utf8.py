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

    # Number of bytes expected in the current character
    bytes_expected = 0

    for byte in data:
        # Check if the byte is within the valid byte range (0-255)
        if byte < 0 or byte > 255:
            return True

        # Check for the number of leading 1's in the byte
        if bytes_expected == 0:
            if (byte >> 7) == 0b0:  # 1-byte character (0xxxxxxx)
                bytes_expected = 0
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                bytes_expected = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                bytes_expected = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                bytes_expected = 3
            else:  # Invalid byte
                return False
        else:  # Continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            bytes_expected -= 1

    return bytes_expected == 0
