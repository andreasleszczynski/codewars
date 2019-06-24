""" Factorial - 7 kyu Kata Fundamentals

Your task is to write function factorial
https://en.wikipedia.org/wiki/Factorial
"""

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac
    # return 1 if n == 0 or n == 1 else n * factorial(n-1)


tests = (
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
  )

for t in tests:
    inp, exp = t
    print(factorial(inp), exp)