"""
The evaluation order of expressions in Python f-strings

"""

# Python evaluates the expressions in an f-string in the left-to-right order. This is obvious if the expressions have side effects like the following example:


def inc(numbers, value):
    numbers[0] += value
    return numbers[0]


numbers = [0]

s = f"{inc(numbers,1)},{inc(numbers,2)}"
print(s)  #  1,3
# In this example, the following function call increases the first number in the numbers list by one:
#       inc(numbers,1)
# After this call, the numbers[0] is one. And the second call increases the first number in the numbers list by 2, which results in 3.
