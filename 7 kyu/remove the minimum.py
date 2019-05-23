""" Remove the minimum - 7 kyu Kata Fundamentals
The museum of incredible dull things
The museum of incredible dull things wants to get rid of some exhibitions.
Miriam, the interior architect, comes up with a plan to remove the most boring
 exhibitions. She gives them a rating, and then removes the one with the lowest
  rating.

However, just as she finished rating all exhibitions, she's off to an important
 fair, so she asks you to write a program that tells her the ratings of the
  items after one removed the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the
original array/list. If there are multiple elements with the same value, remove
the one with a lower index. If you get an empty array/list, return an empty
array/list.

Don't change the order of the elements that are left.

Examples
remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]
"""

def remove_smallest(numbers):
    # copy the input list
    new_list = numbers[:]
    # check if new_list is empty
    if new_list:
        # remove the smallest item from the list
        new_list.remove(min(new_list))

    return new_list




print(remove_smallest([1, 2, 3, 4, 5])) # [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
print(remove_smallest([5, 3, 2, 1, 4])) # [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
print(remove_smallest([1, 2, 3, 1, 1])) # [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
print(remove_smallest([])) # [], "Wrong result for []")
