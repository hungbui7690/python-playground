"""
Delete class variables

@@ delattr(HtmlDocument, "media_type")
@@ del HtmlDocument.version


"""


class HtmlDocument:
    extension = "html"
    version = "5"
    media_type = "text/html"


# To delete a class variable at runtime, you use the delattr() function:
delattr(HtmlDocument, "media_type")


# Or you can use the del keyword:
del HtmlDocument.version
