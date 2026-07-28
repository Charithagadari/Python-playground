"""
Scenario: You want to make sure an internal application function always prints a
clean section separator before and after it runs so logs are readable.
Goal: Create a decorator named @box_wrapper. 
When applied to any function that prints text, 
it should print a line of hyphens --------- before and after that function executes. 
"""
def box_wrapper(say_hello):
    def wrapper ():
        print ("--------------------------")
        say_hello()
        print ("--------------------------")
    return wrapper 
@box_wrapper        
def say_hello():
    print("hello")       

say_hello()     