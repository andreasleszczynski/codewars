﻿""" You're a square! - 7 kyu Kata Fundamentals
A square of squares
You like building blocks. You especially like building blocks that are squares.
And what you even like more, is to arrange them into a square of square
building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up
with an ordinary rectangle! Those blasted things! If you just had a way to
know, whether you're currently working in vain… Wait! That's it! You just have
to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the
square of an integer; in other words, it is the product of some integer with
itself.

The tests will always use some integral number, so don't worry about that in
dynamic typed languages.

Examples
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true
isSquare(26) returns  false
"""
import math

def is_square(n):
    return math.sqrt(n).is_integer() if n >= 0 else False


print(is_square(-1) == False, "-1: Negative numbers cannot be square numbers")
print(is_square( 0) == True, "0 is a square number")
print(is_square( 3) == False, "3 is not a square number")
print(is_square(25) == True, "25 is a square number")
print(is_square( 4) == True, "4 is a square number")
print(is_square(26) == False, "26 is not a square number")

