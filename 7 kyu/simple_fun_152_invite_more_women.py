""" Simple Fun #152: Invite More Women? - 7 kyu Kata Puzzles
King Arthur and his knights are having a New Years party. Last year Lancelot
was jealous of Arthur, because Arthur had a date and Lancelot did not, and
they started a duel.

To prevent this from happening again, Arthur wants to make sure that there are
at least as many women as men at this year's party. He gave you a list of
integers of all the party goers.

Arthur needs you to return true if he needs to invite more women or false if
he is all set.

Input/Output
[input] integer array L ($a in PHP)

An array (guaranteed non-associative in PHP) representing the genders of the
attendees, where
-1 represents women and
1 represents men.

2 <= L.length <= 50

[output] a boolean value

true if Arthur need to invite more women, false otherwise.
"""
from collections import Counter

def invite_more_women(arr):
    if len(arr) < 2:
        return False
    else:
        count = Counter(arr)
        return True if count[1] > count[-1] else False



print(invite_more_women([1, -1, 1]) == True)
print(invite_more_women([-1, -1, -1]) == False)
print(invite_more_women([1, -1]) == False)
print(invite_more_women([1, 1, 1]) == True)
print(invite_more_women([]) == False)
