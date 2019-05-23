""" Find the unique number - 6 kyu Kata Fundamentals
There is an array with some numbers. All numbers are equal except for one. Try
to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
Find the unique number (this kata)
Find the unique string
Find The Unique
"""

def find_uniq(arr):
    numbers = {}

    for i in arr:
        if i in numbers:
            numbers[i] += 1
        else:
            numbers[i] = 1

    # return the lowest value
    return min(numbers, key=numbers.get)

# Tests
print(find_uniq([ 1, 1, 1, 2, 1, 1 ])) # 2
print(find_uniq([ 0, 0, 0.55, 0, 0 ])) # 0.55
print(find_uniq([ 3, 10, 3, 3, 3 ])) # 10
