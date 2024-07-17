"""
Using Python generators to create iterators


"""


# The following example defines an iterator that returns a square number of an integer.
class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current**2

        self.current += 1

        if self.current > self.length:
            raise StopIteration

        return result


# And you can use the Squares iterator to generate the square numbers of the first 5 integers from 0 to 5:
length = 5
square = Squares(length)
for s in square:
    print(s)
# 0
# 1
# 4
# 9
# 16


# This code works as we expected. But it has one issue that there’s a lot of boilerplate.
# And as you might guess, you use a generator function to build that iterator.
