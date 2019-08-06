""" Form The Largest - 7 kyu Kata Fundamentals
Given a number, Return_The Maximum number_ could be formed from the digits
of the number given.

Notes
Only Positve numbers passed to the function, numbers Contain digits [1:9]
inclusive

Digit Duplications could occur, so also consider it when forming the Largest.

Input >> Output Examples:
maxNumber (213) ==> return (321)
Explanation:
As 321 is _The Maximum number_ could be formed from the digits of the number
*213***.

maxNumber (7389) ==> return (9873)
Explanation:
As 9873 is _The Maximum number_ could be formed from the digits of the number
*7389***.

maxNumber (63729) ==> return (97632)
Explanation:
As 97632 is _The Maximum number_ could be formed from the digits of the number
*63729***.

maxNumber (566797) ==> return (977665)
Explanation:
As 977665 is _The Maximum number_ could be formed from the digits of the
number *566797***.

Note: Digit duplications are considered when forming the largest.

maxNumber (17693284) ==> return (98764321)
Explanation:
As 98764321 is _The Maximum number_ could be formed from the digits of the
number *17693284***.
"""
def max_number(n):
    max_number = list(str(n))
    max_number.sort(reverse=True, key=int)
    return int(''.join(max_number))


print(max_number(213) == 321)
print(max_number(7389) == 9873)
print(max_number(63792) == 97632)
print(max_number(566797) == 977665)
print(max_number(1000000) == 1000000)
