"""How many arguments - 7 kyu Kata Fundamentals

Create a function args_count, that returns the count of passed arguments

args_count(1, 2, 3) -> 3
args_count(1, 2, 3, 10) -> 4
"""

# Create a function args_count, that returns count of passed arguments
def args_count(*args, **kwargs):
    return len(args) + len(kwargs)


print(args_count(100), 1)
print(args_count(100, 2, 3), 3)
print(args_count(32, a1=12), 2)
print(args_count(), 0)
