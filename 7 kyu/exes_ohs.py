""" Exes and Ohs - 7 kyu Kata Fundamentals
Check to see if a string has the same amount of 'x's and 'o's. The method
must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
def xo(s):
    x, X, o, O = s.count('x'), s.count('X'), s.count('o'), s.count('O')
    return x + X == o + O


print(xo('xo'), 'True expected')
print(xo('xo0'), 'True expected')
print(xo('xxxoo'), 'False expected')
