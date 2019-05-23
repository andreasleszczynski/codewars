""" Find numbers which are divisible by given number - 8 kyu Kata Algorithms
Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
"""
def divisible_by(numbers, divisor):
    divisible_numbers =[]
    for n in numbers:
        if n % divisor == 0:
            divisible_numbers.append(n)
    return divisible_numbers



print(divisible_by([1,2,3,4,5,6], 2)) #  [2,4,6]
print(divisible_by([1,2,3,4,5,6], 3)) #  [3,6]
print(divisible_by([0,1,2,3,4,5,6], 4)) # [0,4]
print(divisible_by([0], 4)) # [0]
print(divisible_by([1,3,5], 2)) # []
