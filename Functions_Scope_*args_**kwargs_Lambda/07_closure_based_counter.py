def outer_func():
    count = 0 
    def inner_func():
        nonlocal count
        count+=1
        return count
    return inner_func

counter = outer_func()
print(counter())
print(counter())
print(counter())
print(counter())