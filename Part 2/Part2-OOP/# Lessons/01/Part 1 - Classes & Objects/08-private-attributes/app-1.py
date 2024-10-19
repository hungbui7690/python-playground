"""
PRIVATE ATTRIBUTES

  Introduction to encapsulation in Python

  - Encapsulation is one of the four fundamental concepts in object-oriented programming including abstraction, encapsulation, inheritance, and polymorphism.

  - Encapsulation is the packing of data and functions that work on that data within a single object. By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.

  - A class is an example of encapsulation. A class bundles data and methods into a single unit. And a class provides the access to its attributes via methods.

  - The idea of information hiding is that if you have an attribute that isn’t visible to the outside, you can control the access to its value to make sure your object is always has a valid state.

  - I.E. we use the remote to control TV. We don't know what's going on inside the remote. But we know what happen when we press the buttons on the remote.
    > From this, we can see that all the details are hidden.

"""


# The following defines the Counter class:


class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0


"""
The Counter class has one attribute called current which defaults to zero. And it has three methods:

    increment() increases the value of the current attribute by one.
    value() returns the current value of the current attribute
    reset() sets the value of the current attribute to zero.
"""


# The following creates a new instance of the Counter class and calls the increment() method three times before showing the current value of the counter to the screen:
counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value())  # 3

# It works perfectly fine but has one issue.
# From the outside of the Counter class, you still can access the current attribute and change it to whatever you want. For example:

counter.current = -999
print(counter.value())  # -999


# In this example, we create an instance of the Counter class, call the increment() method 3 times and set the value of the current attribute to an invalid value -999.
# So how do you prevent the current attribute from modifying outside of the Counter class?
# That’s why private attributes come into play.
