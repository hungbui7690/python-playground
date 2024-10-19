"""
Separating an iterator from an iterable


"""


# The following places the ColorIterator class inside the Colors class to encapsulate them into a single class:
class Colors:
    def __init__(self):
        self.rgb = ["red", "green", "blue"]

    def __len__(self):
        return len(self.rgb)

    def __iter__(self):
        return self.ColorIterator(self)

    class ColorIterator:
        def __init__(self, colors):
            self.__colors = colors
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.__colors):
                raise StopIteration

            # return the next color
            color = self.__colors.rgb[self.__index]
            self.__index += 1
            return color


# Summary
# An iterable is an object that implements the __iter__ method which returns an iterator.
# An iterator is an object that implements the __iter__ method which returns itself and the __next__ method which returns the next element.
# Iterators are also iterables.
