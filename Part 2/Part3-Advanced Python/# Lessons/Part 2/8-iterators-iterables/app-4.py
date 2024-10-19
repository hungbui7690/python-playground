"""
Separating an iterator from an iterable

- Let’s separate the color iterator from its iterable like what Python does with the list iterator and list.

"""


# The following defines the Colors class:
class Colors:
    def __init__(self):
        self.rgb = ["red", "green", "blue"]

    def __len__(self):
        return len(self.rgb)


# The following defines the ColorIterator class:
class ColorIterator:
    def __init__(self, colors):
        self.__colors = colors
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__colors):
            raise StopIteration

        color = self.__colors.rgb[self.__index]
        self.__index += 1
        return color


"""
How it works.

    The __init__ method accepts an iterable which is an instance of the Colors class.
    The __iter__ method returns the iterator itself.
    The __next__ method returns the next element from the Colors object.
"""


# The following shows how to use the ColorIterator to iterate over the Colors object:
colors = Colors()
color_iterator = ColorIterator(colors)

for color in color_iterator:
    print(color)
# red
# green
# blue


"""
To iterate the Colors object again, you just need to create a new instance of the ColorIterator.

There’s one problem!

When you want to iterate the Colors object, you need to manually create a new ColorIterator object. And you also need to remember the iterator name ColorIterator.

It would be great if you can automate this.
"""
