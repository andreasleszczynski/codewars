"""Third Angle of a Triangle - 8 kyu Kata Fundamentals
You are given two angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
"""

def other_angle(a, b):
    return 180-a-b


print(other_angle(30, 60) == 90)
print(other_angle(60, 60) == 60)
print(other_angle(43, 78) == 59)
print(other_angle(10, 20) == 150)
