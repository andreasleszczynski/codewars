""" count vowels in a string - 7 kyu Kata Fundamentals
Write a function count_vowels to count the number of vowels in a given string.

Notes:
Return nil or None for non-string inputs.
Return 0 if the parameter is omitted.
Examples:
count_vowels("abcdefg") => 2
count_vowels("aAbcdeEfg") => 4

count_vowels(12) => None
"""
def count_vowels(s = ''):
    if type(s) is str:
        vowels = "aeiou"
        number_of_vowels = 0
        for letter in s:
            if letter.lower() in vowels:
                number_of_vowels +=1
        return number_of_vowels
    return None

print(count_vowels("abcdefg")) # 2
print(count_vowels("aAbcdeEfg")) # => 4
