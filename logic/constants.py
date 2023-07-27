"""
File stores constants that are used by the cipher.py file.
To extend range of ascii values accepted by the logic:
    1) add another range in ASCII_RANGES
    2) add its length to ASCII_RANGES_LENGTHS with the key corresponding to 1)
"""

ASCII_RANGES = {1: [48, 57], 2: [65, 90], 3: [97, 122]}
ASCII_RANGES_LENGTHS = {1: 10, 2: 26, 3: 26}
