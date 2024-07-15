"""
Using the * operator on the right hand side


"""

# Python allows you to use the * operator on the right-hand side. Suppose that you have two tuples:

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)


# The following example uses the * operator to unpack those tuples and merge them into a single tuple:

numbers = (*odd_numbers, *even_numbers)
print(numbers)  # (1, 3, 5, 2, 4, 6)


"""
    Summary

        Python uses the commas (,) to define a tuple, not parentheses.
        Unpacking tuples means assigning individual elements of a tuple to multiple variables.
        Use the * operator to assign remaining elements of an unpacking assignment into a list and assign it to a variable.

"""
