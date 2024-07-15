"""
Recursive Functions
- A recursive function is a function that calls itself until it doesn’t.
- Also, a recursive function needs to have a condition to stop calling itself. So you need to add an if statement like this:

    def fn():
        # ...
        if condition:
            # stop calling itself
        else:
            fn()
        # ...

- Typically, you use a recursive function to divide a big problem that’s difficult to solve into smaller problems that are easier to solve.
- In programming, you’ll often find the recursive functions used in data structures and algorithms like trees, graphs, and binary searches.

"""


# 1) A simple recursive function example in Python
# Suppose you need to develop a countdown function that counts down from a specified number to zero.
def count_down(start):
    """Count down from a number"""
    print(start)


# If you call the count_down() function now:
count_down(3)
# …it’ll show only the number 3.

"""
    To show the numbers 3, 2, and 1, you need to:

        First, call the count_down(3) to show the number 3.
        Second, call the count_down(2) to show the number 2.
        Finally, call the count_down(1) to show the number 1.

    In order to do so, inside the count_down() function, you’ll need to define a logic to call the function count_down() with argument 2, and 1.

    To do it, you need to make the count_down() function recursive.
"""


# ///////////////////////
# The following defines a recursive count_down() function and calls it by passing the number 3:
# def count_downX(start):
#     """Count down from a number"""
#     print(start)
#     count_downX(start - 1)

# count_downX(3) # RecursionError: maximum recursion depth exceeded while calling a Python object


# ///////////////////////
# The reason is that the count_down() calls itself indefinitely until the system stops it.
# Since you need to stop counting down the number reaches zero. To do so, you add a condition like this:
def count_down(start):
    """Count down from a number"""
    print(start)

    # call the count_down if the next
    # number is greater than 0

    if start - 1 > 0:
        count_down(start - 1)


count_down(3)
# In this example, the count_down() function only calls itself when the next number is greater than zero. In other words, if the next number is zero, it stops calling itself.
