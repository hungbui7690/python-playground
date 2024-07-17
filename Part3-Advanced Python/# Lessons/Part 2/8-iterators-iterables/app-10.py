"""
The second form of the Python iter() function

- The following shows the second form of the iter() function:

        iter(callable, sentinel)

- The iter(callable,sentinel) will call a callable when the next() method is called.

- It’ll return the value returned by the callable or raise the StopIteration exception if the result is equal to the sentinel value.

"""


# First, define a function that returns closure:
def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


# The counter() function returns a closure. And the closure returns a new integer starting from one when it’s called.


# Second, use the counter() function to show the numbers from 1 to 3:
cnt = counter()

while True:
    current = cnt()
    print(current)
    if current == 3:
        break
# 1
# 2
# 3
# To make it more generic, you can use an iterator instead.
