"""Leap Years - 7 kyu Kata Fundamentals
In this kata you should simply determine, whether a given year is a leap year
or not. In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are not leap years
but years divisible by 400 are leap years
Additional Notes:

Only valid years (positive integers) will be tested, so you don't have to validate them
Examples can be found in the test fixture."""


def isLeapYear(year):
    return False if year % 4 != 0 else True if year % 100 != 0 else False if year % 400 != 0 else True



print(isLeapYear(1984)) # True, 'Year 1984 was a leap year!'
print(isLeapYear(2000)) # True, 'Year 2000 was a leap year!'
print(isLeapYear(1234)) # False, 'Year 1234 was NOT a leap year!'
print(isLeapYear(1100)) # False, 'Year 1100 was NOT a leap year!'

