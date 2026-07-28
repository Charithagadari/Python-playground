""" 
Scenario: You are writing an internal API tool that generates mock SQL WHERE clauses based on filter parameters passed by front-end engineers.
Goal: Create a function build_query(table_name, **filters) that accepts a mandatory string for the table name, followed by any number of keyword filter arguments. 
It should return a formatted string.
Example Output: build_query("users", status="active", role="admin") 
should return:"SELECT * FROM users WHERE status = 'active' AND role = 'admin';
"Core Concept: Mixing fixed parameters with **kwargs and transforming dictionary key-values into strings.
"""
def build_query(**kwargs):
    if not kwargs:
        return "Nothing to query"
    table_name = kwargs.pop("table_name")
    print("SELECT * FROM", table_name, "WHERE", end=" ")
    for key, values in kwargs.items():
        print(key, "=", values, end=" ")
        if key != list(kwargs.keys())[-1]:
            print("AND", end=" ")

build_query(table_name="users", status = "active", role ="admin")        