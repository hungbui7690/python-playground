"""
Class variable storage

@@ from pprint import pprint

@@ pprint(HtmlDocument.__dict__)

"""

from pprint import pprint


class HtmlDocument:
    extension = "html"
    version = "5"


HtmlDocument.media_type = "text/html"


# 1. Python stores class variables in the __dict__ attribute. The __dict__ is a mapping proxy, which is a dictionary. For example:
pprint(HtmlDocument.__dict__)


"""
mappingproxy({'__dict__': <attribute '__dict__' of 'HtmlDocument' objects>,
            '__doc__': None,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'HtmlDocument' objects>,
            'extension': 'html',
            'media_type': 'text/html',
            'version': '5'})

As clearly shown in the output, the __dict__ has three class variables: extension, media_type, and version besides other predefined class variables.
"""


# 2. Python does not allow you to change the __dict__ directly. For example, the following will result in an error:
# HtmlDocument.__dict__["released"] = 2008
# TypeError: 'mappingproxy' object does not support item assignment


# 3. However, you can use the setattr() function or dot notation to indirectly change the __dict__ attribute.
# Also, the key of the __dict__ are strings that will help Python speeds up the variable lookup.
# Although Python allows you to access class variables through the __dict__ dictionary, it’s not a good practice. Also, it won’t work in some situations. For example:
print(HtmlDocument.__dict__["extension"])  # BAD CODE
