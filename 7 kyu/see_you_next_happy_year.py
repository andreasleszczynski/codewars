""" See You Next Happy Year - 7 kyu Kata Fundamentals
You're saying good-bye your best friend, See you next happy year.

Happy Year is the year with only distinct digits, (e.g) 2018

Task
Given a year, find The next happy year or the closest year you'll see your
best friend.

Notes
Year Of Course always Positive.
Have no fear, it is guaranteed that the answer exists.
It's not necessary that the year passed to the function is Happy one.
Input Year with in range (1000  ≤  y  ≤  9000)
Input >> Output Examples:
nextHappyYear (7712) ==> return (7801)
Explanation:
As the Next closest year with only distinct digits is 7801.

nextHappyYear (8989) ==> return (9012)
Explanation:
As the Next closest year with only distinct digits is 9012.

nextHappyYear (1001) ==> return (1023)
Explanation:
As the Next closest year with only distinct digits is 1023.
"""
def next_happy_year(year):
    while True:
        year += 1
        if len(set(str(year))) == 4:
            return year

print(next_happy_year(1001) == 1023)
print(next_happy_year(1123) == 1203)
print(next_happy_year(2001) == 2013)
print(next_happy_year(2334) == 2340)
print(next_happy_year(3331) == 3401)
print(next_happy_year(1987) == 2013)
print(next_happy_year(5555) == 5601)
print(next_happy_year(7712) == 7801)
print(next_happy_year(8088) == 8091)
print(next_happy_year(8999) == 9012)