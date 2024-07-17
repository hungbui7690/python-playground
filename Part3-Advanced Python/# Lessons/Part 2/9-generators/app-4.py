"""
Using Python generators to create iterators


"""


# The following rewrites the Squares iterator as a generator function:
def squares(length):
    for n in range(length):
        yield n**2


# As you can see, it’s much shorter and more expressive. The usage of the squares generator function is similar to the iterator above:
length = 5
square = squares(length)
for s in square:
    print(s)
# 0
# 1
# 4
# 9
# 16


# Summary
# Python generators are functions that contain at least one yield statement.
# A generator function returns a generator object.
# A generator object is an iterator. Therefore, it becomes exhausted once there’s no remaining item to return.
