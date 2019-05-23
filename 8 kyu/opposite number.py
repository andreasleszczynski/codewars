""" Opposite number - 8 kyu Kata Fundamentals
Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34"""

def opposite(number):
    return number*-1 if number != 0 else number


print(opposite(1)) # -1
