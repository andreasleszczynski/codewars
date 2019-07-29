""" Simple remove duplicates - 7 kyu Kata Fundamentals
In this Kata, you will remove the left-most duplicates from a list of
integers and return the result.

# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1
solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]
More examples can be found in the test cases.

Good luck!
"""

def solve(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]



print(solve([3,4,4,3,6,3]) == [4,6,3])
print(solve([1,2,1,2,1,2,3]) == [1,2,3])
print(solve([1,2,3,4]) == [1,2,3,4])
print(solve([1,1,4,5,1,2,1]) == [4,5,2,1])
