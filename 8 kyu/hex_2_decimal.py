""" Hex to Decimal - 8 kyu Kata Fundamentals
Complete the function which converts hex number (given as a string) to a
decimal number.
"""
def hex_to_dec(s):
    return int(s, 16)


print(hex_to_dec("1") == 1)
print(hex_to_dec("a") == 10)
print(hex_to_dec("10") == 16)
