""" Count Odd Numbers below n - 8 kyu Kata Puzzles

Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
Expect large Inputs!
"""
def oddCount(n):
    return n // 2

print(oddCount(7)) # //=> 3, i.e [1, 3, 5]
print(oddCount(15)) # //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
print(oddCount(20)) # -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(oddCount(15023)) # 7511
