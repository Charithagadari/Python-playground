"""Scenario: You need to build a function separate_types(*args) that takes a mix of different data types.
Goal: Process the input positional arguments and return two separate lists:
    one containing only integers/floats, 
    and one containing only strings.
Core Concept: Iterating over *args and checking types using isinstance()."""

def separate_types(*args):
    numbers = []
    strings = []
    for _ in args:
        if isinstance(_, str):
            strings.append(_)
        elif isinstance(_, (int, float)):
            numbers.append(_)
    return (numbers, strings)

print(separate_types(1, 3, 4, "3"))