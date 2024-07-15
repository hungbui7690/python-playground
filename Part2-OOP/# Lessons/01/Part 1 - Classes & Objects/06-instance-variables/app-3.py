"""
Initializing instance variables
- In practice, you initialize instance variables for all instances of a class in the __init__ method.

"""


# For example, the following redefines the HtmlDocument class that has two instance variables name and contents
class HtmlDocument:
    version = 5
    extension = "html"

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents


# When creating a new instance of the HtmlDocument, you need to pass the corresponding arguments like this:
blank = HtmlDocument("Blank", "")


# Summary
# Instance variables are bound to a specific instance of a class.
# Python stores instance variables in the __dict__ attribute of the instance. Each instance has its own __dict__ attribute and the keys in this __dict__ may be different.
# When you access a variable via the instance, Python finds the variable in the __dict__ attribute of the instance. If it cannot find the variable, it goes up and look it up in the __dict__ attribute of the class.
