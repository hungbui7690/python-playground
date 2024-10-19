"""
Lambda Expressions

"""

# Python lambda in a loop
# See the following example:
callables = []
for i in (1, 2, 3):
    callables.append(lambda: i)

for f in callables:
    print(f())

"""
    How it works.

        First, define a list with the name callables.
        Second, iterate from 1 to 3, create a new lambda expression in each iteration, and add it to the callables list.
        Third, loop over the callables and call each function.


    The expected output will be:

        1
        2
        3

    However, the program shows the following output:

        3
        3
        3

    The problem is that all the there lambda expressions reference the i variable, not the current value of i. When you call the lambda expressions, the value of the variable i is 3.
"""

# To fix this, you need to bind the i variable to each lambda expression at the time the lambda expression is created. One way to do it is to use the default argument:
callables = []
for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
# In this example, the value of a is evaluated at the time the lambda expression is created. Therefore, the program returns the expected output.


"""
    Summary

        Use Python lambda expressions to create anonymous functions, which are functions without names.
        A lambda expression accepts one or more arguments, contains an expression, and returns the result of that expression.
        Use lambda expressions to pass anonymous functions to a function and return a function from another function.

"""
