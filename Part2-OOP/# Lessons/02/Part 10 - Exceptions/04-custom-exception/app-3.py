"""
Define the fahrenheit_to_celsius function


"""


class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f"The {self.f} is not in a valid range {self.min_f, self.max_f}"


# The following defines the fahrenheit_to_celsius function that accepts a temperature in Fahrenheit and returns a temperature in Celcius:
# The fahrenheit_to_celsius function raises the FahrenheitError exception if the input temperature is not in the valid range. Otherwise, it converts the temperature from Fahrenheit to Celcius.
def fahrenheit_to_celsius(f: float) -> float:
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)

    return (f - 32) * 5 / 9


# The following main program uses the fahrenheit_to_celsius function and the FahrenheitError custom exception class:
if __name__ == "__main__":
    # First, prompt users for a temperature in Fahrenheit.
    f = input("Enter a temperature in Fahrenheit:")
    try:
        # Second, convert the input value into a float. If the float() cannot convert the input value, the program will raise a ValueError exception. In this case, it displays the error message from the ValueError exception:
        f = float(f)
    except ValueError as ex:
        print(ex)
    else:
        # Third, convert the temperature to Celsius by calling the fahrenheit_to_celsius function and print the error message if the input value is not a valid Fahrenheit value:
        try:
            c = fahrenheit_to_celsius(float(f))
        except FahrenheitError as ex:
            print(ex)
        else:
            print(f"{f} Fahrenheit = {c:.4f} Celsius")


# Summary
# Subclass the Exception class or one of its subclasses to define a custom exception class.
# Create a exception class hierarchy to make the exception classes more organized and catch exceptions at multiple levels.
