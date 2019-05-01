""" Find the odd int 6 kyu Fundamentals
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
def find_it(seq):
    numbers = {}
    for element in seq:
        if element in numbers:
            numbers[element] += 1
        else:
            numbers[element] = 1

    for key, value in numbers.items():
        if value % 2 != 0:
            return key

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) # 5
