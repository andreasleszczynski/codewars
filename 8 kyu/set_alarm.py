""" L1: Set Alarm - 8 kyu Kata Fundamentals

Write a function named setAlarm which receives two parameters. The first
parameter, employed, is true whenever you are employed and the second
parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation
(because these are the circumstances under which you need to set an alarm).
It should return false otherwise.

Examples:
setAlarm(true, true) -> false
setAlarm(false, true) -> false
setAlarm(false, false) -> false
setAlarm(true, false) -> true
"""
def set_alarm(employed, vacation):
    return True if employed and not vacation else False
    # return employed and not vacation

print(set_alarm(True, True) == False) # "Fails when input is True, True"
print(set_alarm(False, True) == False) # "Fails when input is False, True"
print(set_alarm(False, False) == False) # "Fails when input is False, False"
print(set_alarm(True, False) == True) # "Fails when input is True, False"
