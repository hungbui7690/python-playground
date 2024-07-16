"""
Get the values of class variables


@@ getattr(HtmlDocument, "version")
@@ getattr(HtmlDocument, "media_type", "text/html")

"""


class HtmlDocument:
    extension = "html"
    version = "5"


# To get the values of class variables, you use the dot notation (.). For example:
print(HtmlDocument.extension)  # html
print(HtmlDocument.version)  # 5


# If you access a class variable that doesn’t exist, you’ll get an AttributeError exception. For example:
# print(HtmlDocument.media_type)
# AttributeError: type object 'HtmlDocument' has no attribute 'media_type'


# Another way to get the value of a class variable is to use the getattr() function. The getattr() function accepts an object and a variable name. It returns the value of the class variable. For example:
extension = getattr(HtmlDocument, "extension")
version = getattr(HtmlDocument, "version")
print(extension)  # html
print(version)  # 5


# If the class variable doesn’t exist, you’ll also get an AttributeError exception. To avoid the exception, you can specify a default value if the class variable doesn’t exist like this:
media_type = getattr(HtmlDocument, "media_type", "text/html")
print(media_type)  # text/html
