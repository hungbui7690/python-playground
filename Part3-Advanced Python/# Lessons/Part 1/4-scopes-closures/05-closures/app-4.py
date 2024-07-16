"""
Returning an inner function


"""


# If you display the memory address of the string object in the say function and closure, you should see that they reference the same object in the memory:


def say():
    greeting = "Hello"
    print(hex(id(greeting)))

    def display():
        print(hex(id(greeting)))
        print(greeting)

    return display


fn = say()
fn()
# 0x176c07b5170
# 0x176c07b5170
# Hello


"""
When you access the value of the greeting variable, Python will technically “double-hop” to get the string value.

This explains why when the say() function was out of scope, you still can access the string object referenced by the greeting variable.

Based on this mechanism, you can think of a closure as a function and an extended scope that contains free variables.
"""
