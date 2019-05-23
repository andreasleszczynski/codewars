""" Sum of the first nth term of Series - 7 kyu Fundamentals
Task:
Your task is to write a function which returns the sum of following series
upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:
series_sum(1) => 1 = "1.00"
series_sum(2) => 1 + 1/4 = "1.25"
series_sum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
"""

def series_sum(n):
    new_sum, i = 0.00, 1
    while i <= n:
        new_sum += 1/(1+3*(i-1))
        i += 1

    return '%.2f' % round(new_sum, 2)


print((series_sum(1), "1.00"))
print((series_sum(2), "1.25"))
print((series_sum(3), "1.39"))
print((series_sum(0), "0.00"))
