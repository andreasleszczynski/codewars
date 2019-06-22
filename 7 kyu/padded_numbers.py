""" Substituting Variables Into Strings: Padded Numbers - 7 kyu Kata Fundamentals
Complete the solution so that it returns a formatted string.
The return value should equal "Value is VALUE" where value is a 5 digit
padded number.

Example:
solution(5)  # should return "Value is 00005"
"""

def solution(value):
    return "Value is {:05d}".format(value)



print(solution(0) == 'Value is 00000')
print(solution(5) == 'Value is 00005')
print(solution(109) == 'Value is 00109')
print(solution(1204) == 'Value is 01204')
