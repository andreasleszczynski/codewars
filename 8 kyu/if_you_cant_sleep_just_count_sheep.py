""" If you can't sleep, just count sheep!! - 8 kyu Kata Fundamentals
If you can't sleep, just count sheep!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur:
"1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no
negative integers.
"""
def count_sheep(n):
    count = ""
    for i in range(n):
        count += str(i+1) + " sheep..."
    return count

print(count_sheep(1)) # "1 sheep..."
print(count_sheep(2)) # "1 sheep...2 sheep..."
print(count_sheep(3)) # "1 sheep...2 sheep...3 sheep..."
