"""
Define static method

- A static method is not bound to a class or any instances of the class.

- In Python, you use static methods to group logically related functions in a class.

- To define a static method, you use the @staticmethod decorator.

## static method is like util

@@  @staticmethod

"""


# For example, the following defines a class TemperatureConverter that has two static methods that convert from celsius to Fahrenheit and vice versa:
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


# To call a static method, you use the ClassName.static_method_name() syntax. For example:
f = TemperatureConverter.celsius_to_fahrenheit(30)
print(f)  # 86


# For static methods, we don't need to pass instance (self) or class (cls) as the 1st argument of static method.
