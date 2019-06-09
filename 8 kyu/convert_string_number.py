""" Convert a String to a Number! - 8 kyu Kata Fundamentals
We need a function that can transform a string into a number. What ways of
achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly
valid representation of an integral number.

Examples
stringToNumber("1234") == 1234
stringToNumber("605" ) == 605
stringToNumber("1405") == 1405
stringToNumber("-7"  ) == -7
"""

def string_to_number(s):
    return int(s)



print(string_to_number("1234"), 1234)
print(string_to_number("605"), 605)
print(string_to_number("1405"), 1405)
print(string_to_number("1234"), 1234)
