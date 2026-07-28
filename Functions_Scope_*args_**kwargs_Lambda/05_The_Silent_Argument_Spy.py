""" 
You want to write a decorator that monitors function calls, 
but the functions it wraps have completely different signatures 
(some take integers, some take keywords).
Goal: Create a decorator named @spy_logger. 
It must intercept whatever positional or keyword arguments
are passed into the target function, print them out using a 
standard string template, execute the function, and return the function's output.
"""

def spy_logger(func):
    def wrapper(*args,**kwargs):
        print( f"args of {func.__name__} : {args} and {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper        
@spy_logger
def target(price,tax=0.3):
    return price+tax

@spy_logger
def print_mess(*args, **kwargs):
    return f"message is {args} and {kwargs}"
print(target(100,tax=34)) 
print(print_mess("Hello" , "I", "am" ,"practicing" ,key1 = "decorators", key2 = "**args" , key3 = "**kwargs"))