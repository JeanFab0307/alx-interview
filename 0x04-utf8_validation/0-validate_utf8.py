#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if byte >> 7 == 0:       # 1-byte character (0xxxxxxx)
                num_bytes = 0
            elif byte >> 5 == 0b110:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False
        else:
            # Continuation byte check (should be 10xxxxxx)
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
