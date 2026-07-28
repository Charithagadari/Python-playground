"""Scenario: You need to build a function separate_types(*args) that takes a mix of different data types.
Goal: Process the input positional arguments and return two separate lists:
    one containing only integers/floats, 
    and one containing only strings.
Core Concept: Iterating over *args and checking types using isinstance()."""

def separate_types(*args):
    list1 = []
    list2 = []
    for _ in args:
        if isinstance(_, str):
            list2.append(_)
        elif isinstance(_, (int, float)):
            list1.append(_)
    print(list1)
    print(list2)

separate_types(1, 3, 4, "3")