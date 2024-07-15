"""
Instance Variables
- In Python, class variables are bound to a class while instance variables are bound to a specific instance of a class. The instance variables are also called instance attributes.

"""


# The following defines a HtmlDocument class with two class variables:

from pprint import pprint


class HtmlDocument:
    version = 5
    extension = "html"


pprint(HtmlDocument.__dict__)

"""
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
            '__doc__': None,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
            'extension': 'html',
            'version': 5})

The HtmlDocument class has two class variables: extension and version. Python stores these two variables in the __dict__ attribute.

When you access the class variables via the class, Python looks them up in the __dict__ of the class.

"""

print(HtmlDocument.extension)  # html
print(HtmlDocument.version)  # 5
