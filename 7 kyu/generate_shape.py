""" Build a square - 7 kyu Kata Fundamentals
I will give you an integer. Give me back a shape that is as long and wide as
the integer. The integer will be a whole number between 0 and 50.

Example
n = 3, so I expect a 3x3 square back just like below as a string:

+++
+++
+++
"""

def generateShape(int):
    s = ""
    for i in range(int):
        s += '+' * int + '\n'

    return s[:-1]

print(generateShape(3), '+++\n+++\n+++')
print(generateShape(8), '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++')
