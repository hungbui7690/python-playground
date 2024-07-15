"""
CLASS VARIABLES


Introduction to the Python class variables

- Everything in Python is an object including a class. In other words, a class is an object in Python.

"""


# When you define a class using the class keyword, Python creates an object with the name the same as the class’s name. For example:
class HtmlDocument:
    # Both extension and version are the class variables of the HtmlDocument class. They’re bound to the HtmlDocument class.
    extension = "html"
    version = "5"


# This example defines the HtmlDocument class and the HtmlDocument object. The HtmlDocument object has the __name__ property:
print(__name__)  # __main__
print(HtmlDocument.__name__)  # HtmlDocument


# And the HTMLDocument has the type of type:
print(type(HtmlDocument))  # <class 'type'>


# It’s also an instance of the type class:
print(isinstance(HtmlDocument, type))  # True


# Class variables are bound to the class. They’re shared by all instances of that class.
