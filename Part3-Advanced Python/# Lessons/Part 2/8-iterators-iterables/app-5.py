"""
Separating an iterator from an iterable
- When you want to iterate the Colors object, you need to manually create a new ColorIterator object. And you also need to remember the iterator name ColorIterator.

- It would be great if you can automate this. To do it, you can make the Colors class iterable by implementing the __iter__ method

"""


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


class Colors:
    def __init__(self):
        self.rgb = ["red", "green", "blue"]

    def __len__(self):
        return len(self.rgb)

    # The __iter__ method returns a new instance of the ColorIterator class.
    def __iter__(self):
        return ColorIterator(self)


# Now, you can iterate the Colors object without explicitly creating the ColorIterator object:
colors = Colors()

for color in colors:
    print(color)
# red
# green
# blue


# Internally, the for loop calls the __iter__ method of the colors object to get the iterator and uses this iterator to iterate over the elements of the colors object.
