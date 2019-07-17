""" Fake Binary - 8 kyu Kata Fundamentals
Given a string of digits, you should replace any digit below 5 with '0' and
any digit 5 and above with '1'. Return the resulting string.
"""
def fake_bin(x):
    return ''.join(['0' if int(n) < 5 else '1' for n in x])



tests = [
    # [expected, input]
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

for exp, inp in tests:
    print(fake_bin(inp) == exp)