"""
Introduction the Python reduce() function

- Python offers a function called reduce() that allows you to reduce a list in a more concise way.

- Here is the syntax of the reduce() function:

      reduce(fn,list)

- The reduce() function applies the fn function of two arguments cumulatively to the items of the list, from left to right, to reduce the list into a single value.

- Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module.

- To use the reduce() function, you need to import it from the functools module using the following statement at the top of the file:

      from functools import reduce

- Note that you’ll learn more about modules and how to use them in the later tutorial.

"""

# The following illustrates how to use the reduce() function to calculate the sum of elements of the scores list:

from functools import reduce


def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)  # 365


# As you can see clearly from the output, the reduce() function cumulatively adds two elements of the list from left to right and reduces the whole list into a single value.
# To make the code more concise, you can use a lambda expression instead of defining the sum() function:

total = reduce(lambda a, b: a + b, scores)

print(total)  # 365
