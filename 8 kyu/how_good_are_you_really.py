"""How good are you really? - 8 kyu Kata Fundamentals
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the
average student in your class.
You got an array with your colleges' points. Now calculate the average to
your points!

Return True if you're better, else False!

Note:
Your points are not included in the array of your classes points. For
calculating the average point you may add your point to the given array!
"""
def better_than_average(class_points, your_points):
    return True if (sum(class_points) + your_points) / (len(class_points)+1) < your_points else False




print(better_than_average([2, 3], 5) == True)
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) == True)
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69) == True)
