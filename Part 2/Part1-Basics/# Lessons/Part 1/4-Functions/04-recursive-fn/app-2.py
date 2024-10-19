"""
Recursive Functions

"""


# //////////////////////////
# 2) Using a recursive function to calculate the sum of a sequence
# Suppose that you need to calculate a sum of a sequence e.g., from 1 to 100. A simple way to do this is to use a for loop with the range() function:
def sum(n):
    total = 0
    for index in range(n + 1):
        total += index

    return total


result = sum(100)
print(result)  # 5050

"""
    To apply the recursion technique, you can calculate the sum of the sequence from 1 to n as follows:

        sum(n) = n + sum(n-1)
        sum(n-1) = n-1 + sum(n-2)
        …
        sum(0) = 0

    The sum() function keeps calling itself as long as its argument is greater than zero.

"""


# //////////////////////////
# The following defines the recursive version of the sum() function:
def sumX(n):
    if n > 0:
        return n + sum(n - 1)
    return 0


result = sumX(100)
print(result)


# //////////////////////////
# As you can see, the recursive function is much shorter and more readable.
# If you use the ternary operator, the sum() will be even more concise:
def sum(n):
    return n + sum(n - 1) if n > 0 else 0


result = sum(100)
print(result)
