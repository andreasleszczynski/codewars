"""Your task is to write function findSum. - 7 kyu Fundamentals

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)"""

def find(n):
    new_sum = 0
    for i in range(n+1):
        if (i % 3 == 0) or (i % 5 == 0):
            new_sum += i

    return new_sum



print(find(5)) # 8)
print(find(10)) # 33)
