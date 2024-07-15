"""
Callable class attributes

- Class attributes can be any object such as a function.

"""

from pprint import pprint


class HtmlDocument:
    extension = "html"
    version = "5"

    def render():
        print("Rendering the Html doc...")


# When you add a function to a class, the function becomes a class attribute. Since a function is callable, the class attribute is called a callable class attribute. For example:
pprint(HtmlDocument.__dict__)


"""
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
            '__doc__': None,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
            'extension': 'html',
            'render': <function HtmlDocument.render at 0x0000017DB7918FE0>,
            'version': '5'})

In this example, the render is a class attribute of the HtmlDocument class. Its value is a function.
"""


# Summary
# A class is an object which is an instance of the type class.
# Class variables are attributes of the class object.
# Use dot notation or getattr() function to get the value of a class attribute.
# Use dot notation or setattr() function to set the value of a class attribute.
# Python is a dynamic language. Therefore, you can assign a class variable to a class at runtime.
# Python stores class variables in the __dict__ attribute. The __dict__ attribute is a dictionary.
