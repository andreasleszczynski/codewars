""" Correct the mistakes of the character recognition software - 8 kyu Kata Fundamentals

Character recognition software is widely used to digitise printed texts.
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are
digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle
the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.
"""
def correct(string):
    new_string = ""
    for letter in string:
        if letter == "0":
            new_string = new_string[:] + "O"
        elif letter == "1":
            new_string = new_string[:] + "I"
        elif letter == "5":
            new_string = new_string[:] + "S"
        else:
            new_string = new_string[:] + letter
    return new_string


print(correct("L0ND0N")) # "LONDON"
print(correct("DUBL1N")) # "DUBLIN"
print(correct("51NGAP0RE")) # "SINGAPORE"
print(correct("BUDAPE5T")) # "BUDAPEST"
print(correct("PAR15")) # "PARIS"
