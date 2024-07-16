"""
Set values for class variables

@@ setattr(HtmlDocument, "version", 10)

"""


class HtmlDocument:
    extension = "html"
    version = "5"


# To set a value for a class variable, you use the dot notation:
HtmlDocument.version = 10


# or you can use the setattr() built-in function:
setattr(HtmlDocument, "version", 10)
print("version:     ", HtmlDocument.version)


# Since Python is a dynamic language, you can add a class variable to a class at runtime after you have created it. For example, the following adds the media_type class variable to the HtmlDocument class:
HtmlDocument.media_type = "text/html"
print("media_type:  ", HtmlDocument.media_type)


# Similarly, you can use the setattr() function:
setattr(HtmlDocument, "tags", "1.0.1")
print("tags:        ", HtmlDocument.tags)
