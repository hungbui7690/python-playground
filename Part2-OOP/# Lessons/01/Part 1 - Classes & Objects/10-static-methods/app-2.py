"""
STATIC METHODS

"""


# The following defines a class called TemperatureConverter that has static methods for converting temperatures between Celsius, Fahrenheit, and Kelvin:


class TemperatureConverter:
    KEVIN = ("K",)
    FAHRENHEIT = "F"
    CELSIUS = "C"

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5 * (f + 459.67) / 9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9 * k / 5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ""
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = "°F"
        elif unit == TemperatureConverter.CELSIUS:
            symbol = "°C"
        elif unit == TemperatureConverter.KEVIN:
            symbol = "°K"

        return f"{value}{symbol}"


# And to call the TemperatureConverter class, you use the following:
f = TemperatureConverter.celsius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))  # 95.0°F


# Summary
# Use static methods to define utility methods or group a logically related functions into a class.
# Use the @staticmethod decorator to define a static method.
