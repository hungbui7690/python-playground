"""

- To do that, you define an interface and make the App dependent on it instead of FXConverter class. And then you change the FXConverter to comply with the interface.

+-----------+    +------------------+
| App       |    |CurrencyConverter |
+-----------+  > +------------------+
| + start() |    | + convert()      |
+-----------+    +------------------+
                    ^
              +------------+
              |FXConverter |
              +------------+
              | + convert()|
              +------------+




"""

from abc import ABC


# First, define an abstract class CurrencyConverter that acts as an interface. The CurrencyConverter class has the convert() method that all of its subclasses must implement:
class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


# Second, redefine the FXConverter class so that it inherits from the CurrencyConverter class and implement the convert() method:
class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using FX API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 2


# Third, add the __init__ method to the App class and initialize the CurrencyConverter‘s object:
class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert("EUR", "USD", 100)


# Now, the App class depends on the CurrencyConverter interface, not the FXConverter class.
# The following creates an instance of the FXConverter and pass it to the App:
if __name__ == "__main__":
    converter = FXConverter()
    app = App(converter)
    app.start()
# Converting currency using FX API
# 100 EUR = 120.0 USD
