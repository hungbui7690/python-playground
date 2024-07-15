"""
Overriding attributes

"""

# The following shows how to implement the Parser and UkParser classes by overriding attributes:
import re


class Parser:
    phone_pattern = r"\d{3}-\d{3}-\d{4}"

    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(self.phone_pattern, self.text)
        if match:
            return match.group(0)
        return None

    def parse(self):
        return {"email": self.email(), "phone": self.phone()}


class UkParser(Parser):
    phone_pattern = r"(\+\d{1}-\d{3}-\d{3}-\d{4})"


if __name__ == "__main__":
    s = "Contact us via 408-205-5663 or email@test.com"
    parser = Parser(s)
    print(parser.parse())

    s2 = "Contact me via +1-650-453-3456 or email@test.co.uk"
    parser = UkParser(s2)
    print(parser.parse())


# In this example, the Parser has a class variable phone_pattern. The phone() method in the Parser class uses the phone_pattern to extract a phone number.
# The UkParser child class redefines (or overrides) the phone_pattern class attribute.
# If you call the parse() method from the UkParser‘s instance, the parse() method calls the phone() method that uses the phone_pattern defined in the UkParser class.


# Summary
# Method overriding allows a child class to provide a specific implementation of a method that is already provided by one of its parent class.
