"""
Instance Variables
- In Python, class variables are bound to a class while instance variables are bound to a specific instance of a class. The instance variables are also called instance attributes.

"""


# The following defines a HtmlDocument class with two class variables:

from pprint import pprint


class HtmlDocument:
    version = 5
    extension = "html"


# The following creates a new instance of the HtmlDocument class:
home = HtmlDocument()

# The home is an instance of the HtmlDocument class. It has its own __dict__ attribute:
# The home.__dict__ is now empty:
pprint(home.__dict__)  # {}
# The home.__dict__ stores the instance variables of the home object like the HtmlDocument.__dict__ stores the class variables of the HtmlDocument class.


# Unlike the __dict__ attribute of a class, the type of the __dict__ attribute of an instance is a dictionary. For example:
print(type(home.__dict__))  # <class 'dict'>


# Since a dictionary is mutable, you can mutate it e.g., adding a new element to the dictionary.
# Python allows you to access the class variables from an instance of a class. For example:
print(home.extension)  # html
print(home.version)  # 5
# In this case, Python looks up the variables extension and version in home.__dict__ first. If it doesn’t find them there, it’ll go up to the class and look up in the HtmlDocument.__dict__.
# However, if Python can find the variables in the __dict__ of the instance, it won’t look further in the __dict__ of the class.


# The following defines the version variable in the home object:
home.version = 6

# Python adds the version variable to the __dict__ attribute of the home object:
# The __dict__ now contains one instance variable:
print(home.__dict__)  # {'version': 6}


# If you access the version attribute of the home object, Python will return the value of the version in the home.__dict__ dictionary:
print(home.version)  # 6


# If you change the class variables, these changes also reflect in the instances of the class:
HtmlDocument.media_type = "text/html"
print(home.media_type)  # text/html
