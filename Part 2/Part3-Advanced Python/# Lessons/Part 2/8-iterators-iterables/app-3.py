"""
Python Iterator and Iterable

"""


# The following defines the Colors class:


class Colors:
    def __init__(self):
        self.rgb = ["red", "green", "blue"]
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.rgb):
            raise StopIteration

        # return the next color
        color = self.rgb[self.__index]
        self.__index += 1
        return color


"""
In this example, the Colors class plays two roles: iterable and iterator.

The Colors class is an iterator because it implements both __iter__ and __next__ method. The __iter__ method returns the object itself. And the __next__ method returns the next item from a list.

The Colors class is also an iterable because it implements the __iter__ method that returns an object itself, which is an iterator.
"""


# The following creates a new instance of the Colors class and iterates over its elements using a for loop:
colors = Colors()


for color in colors:
    print(color)
# red
# green
# blue


# Once you complete iterating, the colors object becomes useless. If you attempt to iterate it again, you’ll get a StopIteration exception:
# next(colors)  # StopIteration


# If you use the for loop, you’ll get nothing back. The iterator is empty:
print("Run Again...")
for color in colors:
    print(color)

# To iterate again, you need to create a new colors object with the rgb attribute. This is inefficient
