"""

- In the future, you can support another currency converter API by subclassing the CurrencyConverter class. For example, the following defines the AlphaConverter class that inherits from the CurrencyConverter.

+-----------+    +------------------+
| App       |    |CurrencyConverter |
+-----------+  > +------------------+
| + start() |    | + convert()      |
+-----------+    +------------------+
                    ^             ^
              +------------+ +--------------+
              |FXConverter | |AlphaConverter|
              +------------+ +--------------+
              | + convert()| | + convert()  |
              +------------+ +--------------|
"""

from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using FX API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 2


# AlphaConverter class that inherits from the CurrencyConverter.
class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print("Converting currency using Alpha API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.15


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert("EUR", "USD", 100)


# Since the AlphaConvert class inherits from the CurrencyConverter class, you can use its object in the App class without changing the App class:
if __name__ == "__main__":
    converter = AlphaConverter()
    app = App(converter)
    app.start()
# Converting currency using Alpha API
# 100 EUR = 120.0 USD


# Summary
# Use the dependency inversion principle to make your code more robust by making the high-level module dependent on the abstraction, not the concrete implementation.
