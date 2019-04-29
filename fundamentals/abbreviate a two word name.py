""" Abbreviate a Two Word Name - 8 kyu Fundamentals
Write a function to convert a name into initials. This kata strictly takes
two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F"""


def abbrevName(name):
    return (name[0] + "." + name[name.find(" ")+1]).upper()


print(abbrevName("Sam Harris")) # "S.H"
print(abbrevName("Patrick Feenan")) # "P.F"
print(abbrevName("Evan Cole")) # "E.C")
print(abbrevName("P Favuzzi")) # "P.F"
print(abbrevName("David Mendieta")) # "D.M");
