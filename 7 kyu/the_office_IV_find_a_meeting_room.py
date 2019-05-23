""" The Office IV - Find a Meeting Room - 7 kyu Kata Fundamentals
Your job at E-Corp is both boring and difficult. It isn't made any easier by
the fact that everyone constantly wants to have a meeting with you, and that
the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room.
Your job? Find the first empty one and return its index (N.B. There may be more
than one empty room in some test cases).

'X' --> busy 'O' --> empty

If all rooms are busy, return 'None available!'.
"""
def meeting_room(arr):
    return 'None available!' if not ('O' in rooms) else rooms.index('O')



print(meeting(['X', 'O', 'X'])) # 1
print(meeting(['O','X','X','X','X'])) # 0
print(meeting(['X','X','O','X','X'])) # 2
print(meeting(['X'])) # 'None available!'
