""" Beginner - Reduce but Grow 8 kyu Kata Fundamentals
Given a non-empty array of integers, return the result of multiplying the
values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""
import numpy as np

def grow(arr):
    prod = 1
    for x in arr:
        prod *= x
    return prod




print(grow([1, 2, 3])) # 6
print(grow([4, 1, 1, 1, 4])) # 16
print(grow([2, 2, 2, 2, 2, 2])) # 64