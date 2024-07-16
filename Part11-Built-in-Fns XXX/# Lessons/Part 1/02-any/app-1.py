"""
ANY
- The any() function accepts an iterable and returns true if any element of the iterable is true:

    any(iterable)

- If the iterable is empty, the any() function returns false.

"""


# Technically, the any() function is equivalent to the following:
def any(iterable):
    for elem in iterable:
        if elem:
            return True
    return False


# By using the any() function, you can avoid for loops and make your code more concise.
# Note that if you want to check if all elements of an iterable are true, you can use the all() function.


# 1) Simple any() function examples
# The following example uses the any() function the checks if a list has any number that is not zero:
scores = [0, 4, 1, 2]
print(any(scores))  # True
# Since all non-zero numbers evaluate to true and the scores contain the none zero numbers, the result is true.


# The following example uses the any() function to check if a list contains at least one non-empty string:
names = ["", "", "Jane"]
print(any(names))  # True
# Because the list contains a non-empty string, the any() function returns true.


# The following example uses the any() function to check if the list contains any truthy value:
items = ["", False, 0, ()]
print(any(items))  # False
# Because all the elements of the items are falsy, the any() function returns false.
