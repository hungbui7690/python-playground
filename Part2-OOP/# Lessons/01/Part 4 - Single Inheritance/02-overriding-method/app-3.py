"""
Advanced method overriding

"""

import re


# The following defines the Parser class:
class Parser:
    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(r"\d{3}-\d{3}-\d{4}", self.text)
        if match:
            return match.group(0)
        return None

    def parse(self):
        return {"email": self.email(), "phone": self.phone()}


"""
The Parser class has an attribute text which specifies a piece of text to be parsed. Also, the Parser class has three methods:

    The email() method parses a text and returns the email.
    The phone() method parses a text and returns a phone number in the format nnn-nnnn-nnnn where n is a number from 0 to 9 e.g., 408-205-5663.
    The parse() method returns a dictionary that contains two elements email and phone. It calls the email() and phone() method to extract the email and phone from the text attribute.

"""


# The following uses the Parser class to extract email and phone:
s = "Contact us via 408-205-5663 or email@test.com"
parser = Parser(s)
print(parser.parse())  # {'email': 'email@test.com', 'phone': '408-205-5663'}


# Suppose you need to extract phone numbers in the format n-nnn-nnn-nnnn, which is the UK phone number format. Also, you want to use extract email like the Parser class
# To do it, you can define a new class called UkParser that inherits from the Parser class. In the UkParser class, you override the phone() method as follows:
class UkParser(Parser):
    def phone(self):
        match = re.search(r"(\+\d{1}-\d{3}-\d{3}-\d{4})", self.text)
        if match:
            return match.group(0)
        return None


# The following use the UkParser class to extract a phone number (in UK format) and email from a text:
s2 = "Contact me via +1-650-453-3456 or email@test.co.uk"
parser = UkParser(s2)
print(parser.parse())  # {'email': 'email@test.co.uk', 'phone': '+1-650-453-3456'}


"""
- In this example, the parser calls the parse() method from the parent class which is the Parser class. In turn, the parse() method calls the email() and phone() methods.

- However, the parser() doesn’t call the phone() method of the Parser class but the phone() method of the UkParser class:

    parser.parse()

- The reason is that inside the parse() method, the self is the parser which is an instance of the UkParser class.

- Therefore, when you call self.phone() method inside the parse() method, Python will look for the phone() method that is bound to the instance of the UkParser.

"""
