"""
Python custom exception example
- Suppose you need to develop a program that converts a temperature from Fahrenheit to Celsius.

- The minimum and maximum values of a temperature in Fahrenheit are 32 and 212. If users enter a value that is not in this range, you want to raise a custom exception e.g., FahrenheitError.

\\\\\\\\\\\\\\\\\\\\\

Define the FahrenheitError custom exception class

"""


# The following defines the FahrenheitError exception class:
class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The {self.f} is not in a valid range {self.min_f, self.max_f}"


"""
How it works.

- First, define the FahrenheitError class that inherits from the Exception class.
- Second, add two class attributes min_f and max_f that represent the minimum and maximum Fahrenheit values.
- Third, define the __init__ method that accepts a Fahrenheit value (f) and a number of position arguments (*args). In the __init__ method, call the __init__ method of the base class. Also, assign the f argument to the f instance attribute.
- Finally, override the __str__ method to return a custom string representation of the class instance.
"""
