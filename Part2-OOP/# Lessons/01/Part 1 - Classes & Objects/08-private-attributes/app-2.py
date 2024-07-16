"""
PRIVATE ATTRIBUTES
- Private attributes can be only accessible from the methods of the class. In other words, they cannot be accessible from outside of the class.

- Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class.

- By convention, you can define a private attribute by prefixing a single underscore (_):

    ~~ _attribute

- This means that the _attribute should not be manipulated and may have a breaking change in the future.

## We still can access to _attribute from outside of class. It just the convention between devs. It states that this attribute is private and doesn't allow to modify

"""


# The following redefines the Counter class with the "current" as a "private attribute" by convention:


class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0


counter = Counter()

# We still can access this "private" attribute from outside of the class
print(counter._current)  # 0
