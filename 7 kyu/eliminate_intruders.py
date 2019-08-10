""" Eliminate the intruders! Bit manipulation - 7 kyu Kata Fundamentals
You are given a string representing a number in binary. Your task is to delete
all the unset bits in this string and return the corresponding number
(after keeping only the '1's).

In practice, you should implement this function:

def eliminate_unset_bits(number):
Examples
eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
eliminate_unset_bits("111") ->  7
eliminate_unset_bits("1000000") -> 1
eliminate_unset_bits("000") -> 0
"""
def eliminate_unset_bits(number):
    return int("".join(["1" if x == "1" else "" for x in number]), 2) if "1" in number else 0


print(eliminate_unset_bits("11010101010101"), 255)
print(eliminate_unset_bits("111"), 7)
print(eliminate_unset_bits("1000000"), 1)
print(eliminate_unset_bits("000"), 0)