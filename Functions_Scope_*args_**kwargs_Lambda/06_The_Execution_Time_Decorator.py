"""
    Scenario: You want to measure how long different functions take to run in a 
    production app without manually writing timing code inside every single function.
    Goal: Write a decorator function @time_logger that wraps any target function. 
    The decorator must intercept all inputs, call the function, 
    log how long it took to run, and return the function's original output.
    Core Concept: Passing *args and **kwargs down to an underlying function inside a
    wrapper to preserve its original behavior perfectly.
"""
import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        stop = time.time()
        return f"{func.__name__} : {stop-start:.10f}"
    return wrapper

@time_logger
def addition(*args):
    total = 0
    for num in args :
        total = total + num
    return total  
@time_logger
def multiplication(*args):
    total = 1
    for num in args :
        total = total * num
    return total  

number = [2,4,2,2]
print(addition(*number))
print(multiplication(*number))
        