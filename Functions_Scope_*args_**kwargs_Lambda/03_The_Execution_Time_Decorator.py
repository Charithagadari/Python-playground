"""
    Scenario: You want to measure how long different functions take to run in a 
    production app without manually writing timing code inside every single function.
    Goal: Write a decorator function @time_logger that wraps any target function. 
    The decorator must intercept all inputs, call the function, 
    log how long it took to run, and return the function's original output.
    Core Concept: Passing *args and **kwargs down to an underlying function inside a
    wrapper to preserve its original behavior perfectly.
"""

